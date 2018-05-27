import os
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
import MySQLdb
import json
import codecs
from home.models import Tables
import csv

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

def loginView(request):
    form = LoginForm()
    template_name = 'login.html'
    return render(request, template_name, {'form': form})

class LoginError(TemplateView):
    template_name = 'login_error.html'

def loginVerify(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        return redirect('create_table')
    else:
        # No backend authenticated the credentials
        return redirect('login_error')

class TableForm(forms.Form):
    jsonFile = forms.FileField()
    tableFile = forms.FileField()

def createTable(request):
    form = TableForm()
    template_name = 'create_table.html'
    return render(request, template_name, {'form': form})

def table_validate(request):
    form = TableForm(request.POST, request.FILES)
    if form.is_valid():
        jsonFile = request.FILES['jsonFile']
        tableFile = request.FILES['tableFile']


        lines = jsonFile.read()
        #print(type(lines))
        lines = lines.decode("utf-8-sig")
        js = json.loads(lines)
        name = js['name']
        url = settings.CLASS_ROOT+name
        data = js['class']
        f = json.dumps(data, sort_keys=True, indent=4)
        t = Tables(name=name, url=url, file=f)
        t.save()


        db = MySQLdb.connect("localhost","root","12345","mydatabase")
        cursor = db.cursor()
        
        st = '''CREATE TABLE IF NOT EXISTS `{}` (`id` bigint(20) NOT NULL DEFAULT '0','''.format(name)
        for it,jt in data.items():
            tipost = {'int': 'bigint(20)', 'str': 'varchar(63)', 'float': 'double'}
            st += '`{}` {} DEFAULT NULL,'.format(it,tipost[jt])
        st += 'KEY `ix_est_index` (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=latin1;'
        cursor.execute(st)
        db.commit()

        lines = tableFile.read()
        csvf = lines.decode("utf-8").splitlines()
        print(csvf)
        reader = csv.reader(csvf)
        columns = next(reader) 
        print(columns)
        query = 'INSERT INTO `{2}` ({0}) values ({1})'
        query = query.format(', '.join('`{}`'.format(it) for it in columns), ','.join('?' * len(columns)), name)
        for datan in reader:
            assert len(datan) == len(columns)
            assert query.count('?') == len(datan)

            dn = []
            for i, it in enumerate(datan):
                if columns[i] == 'id' or data[columns[i]] != 'str':
                    dn.append(it)
                else:
                    dn.append('\'{}\''.format(it))
            qn = query.replace('?','{}').format(*dn)
            cursor.execute(qn)
        db.commit()

        db.close()

        return redirect('create_table')
