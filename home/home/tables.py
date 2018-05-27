from django.views.generic.base import TemplateView
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.models import Arvore, Est
from home import matrix as mt
from inspect import getmembers, isroutine
from django.db import models
import simplejson
import json
import csv


def http400(message):
    context = {'status': '400', 'reason': message}
    response = HttpResponse(json.dumps(context), content_type='application/json')
    response.status_code = 400
    return response

class TableView:
    def __init__(self,nameTable):
        self.nameTable = nameTable

    def getTypes(self,name):
        if name not in self.nameTable:
            return HttpResponse(status=404)
        else:
            class_table = self.nameTable[name]
        members = class_table._meta.get_fields()
        vtypes = ['IntegerField','BigIntegerField','FloatField','CharField','DecimalField']
        types = ['int','int','float','str','float']
        vret = []
        for it in members:
            name = it.name
            tipo = it.get_internal_type()
            #print(name, tipo)
            if tipo in vtypes:
                vret.append( (it.name,types[vtypes.index(tipo)]) )
        return vret

    def asName(self):
        def getNamesTypes(request,name):
            vret = self.getTypes(name)
            output = json.dumps(vret)
            return HttpResponse(output, content_type='application/json')

        return getNamesTypes

    def asElementJsonCSV(self,fileType):
        def getElements(request,name):
            if name not in self.nameTable:
                return HttpResponse(status=404)
            else:
                class_table = self.nameTable[name]

            fields = {}
            vparams = self.getTypes(name)
            for field, tipo in vparams:
                tipo = eval(tipo)
                #print(field,tipo)
                for it, jt in zip(['g','l'],['min','max']):
                    stformat = '{}_{}'.format(field,jt)
                    if stformat in request.GET:
                        try:
                            fields['{}__{}te'.format(field,it)] = tipo(request.GET[stformat])
                        except:
                            return http400('invalid parameters')


            objects = class_table.objects.filter(**fields).all()
            fields = class_table._meta.fields

            if fileType == 'json':
                paginator = Paginator(objects,10)
                page = request.GET.get('page')
                try:
                    objects = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    objects = paginator.page(1)
                    page = 1
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    objects = paginator.page(paginator.num_pages)
                    page = paginator.num_pages

                vret = []

                output = serializers.serialize("json", [q for q in objects.object_list])
                resultx = simplejson.loads(output)
                #print(resultx[0]['fields'])
                vresult = {'page': page, 'qt': len(resultx), 'vector': [q['fields'] for q in resultx]}
                output = json.dumps(vresult)
                return HttpResponse(output, content_type='application/json')
            else:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="table.csv"'

                writer = csv.writer(response)
                row = []
                for field in fields:
                    row.append(field.name)
                writer.writerow(row)

                for obj in objects:
                    row = []
                    for field in fields:
                        row.append(str(getattr(obj, field.name)))
                    writer.writerow(row)

                return response

        
        return getElements
        

    def asElement(self):
        return self.asElementJsonCSV('json')

    def asNameElement(self):
        return (self.asName(),self.asElementJsonCSV('json'),self.asElementJsonCSV('csv'))
