from django.views.generic.base import TemplateView
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.models import *
from home import matrix as mt
from inspect import getmembers, isroutine
from django.db import models
import simplejson
import json
import numpy as np
from home.tables import TableView


def responsetoJson(response):
    return json.loads(response.content.decode('utf-8'))

def http400(message):
    context = {'status': '400', 'reason': message}
    response = HttpResponse(json.dumps(context), content_type='application/json')
    response.status_code = 400
    return response


names = ['est','AdicaoArestaBroom','AdicaoArestaDoubleBroom','broom45','broom89']
classes = [Est,Adicaoarestabroom,Adicaoarestadoublebroom,Broom45,Broom89]

def createNamesClasses():
    modeltypes = [models.IntegerField(db_column='N', blank=True, null=True),
            models.DecimalField(db_column='GEhe2', max_digits=13, decimal_places=12, blank=True, null=True),
            models.CharField(max_length=255)]
    pythontypes = ['int','float','str']

    def conv(name,tipo):
        modeltypes = [models.IntegerField(db_column=name, blank=True, null=True),
        models.DecimalField(db_column=name, max_digits=13, decimal_places=12, blank=True, null=True),
        models.CharField(db_column=name, max_length=255)]
        pythontypes = ['int','float','str']
        convers = dict((jt,it) for it,jt in zip(modeltypes,pythontypes))
        return convers[tipo]


    tables = Tables.objects.all()
    for table in tables:
        name = table.name
        names.append(name)
        f = table.file
        #print('#3#',f,'#4#')
        f = json.loads(f)
        #print("#1#",f,"#2#")

        class Meta:
            db_table = name
            managed = False

        d = {'__module__': __name__, 'Meta': Meta}
        for column, tipo in f.items():
            d[column] = conv(column,tipo)
        classe = type(name, (models.Model,), d)
        classes.append(classe)


createNamesClasses()
dicNames = dict(zip(names,classes))

t = TableView(dicNames)
tNames, tTables, tCSV = t.asNameElement()

def getTablesNames(request):
    return JsonResponse(names, safe=False)

class HomeView(TemplateView):
    template_name = 'index.html'

def arvores(request):
    try:
        init = int(request.GET.get('init',0))
        qt = int(request.GET.get('qt',30))
    except:
        return http400('invalid parameters')
    
    fields = {}
    for field, tipo in zip(['alfa','diametro','arestas','n'],[float,int,int,int]):
        for it, jt in zip(['g','l'],['min','max']):
            stformat = '{}{}'.format(field,jt)
            if stformat in request.GET:
                try:
                    fields['{}__{}te'.format(field,it)] = tipo(request.GET[stformat])
                except:
                    return http400('invalid parameters')

    if 'tipo' in request.GET and request.GET['tipo'] in ('1','2'):
        try:
            fields['tipo'] = int(request.GET['tipo'])
        except:
            return http400('invalid parameters')

    arvores = Arvore.objects.filter(**fields).all()
    size = arvores.count()
    arvores = arvores[init:init+qt]
    data = serializers.serialize('python',arvores,fields=('n','alfa','diametro','arestas','tipo','identificacao'))
    data = {'size': size, 'arvores': [it['fields'] for it in data]}
    output = json.dumps(data)
    return HttpResponse(output, content_type='application/json')


def matrix(request):
    try:
        mat = request.POST['matrix']
        mat = np.matrix(mat)
        if mat.shape[0] != mat.shape[1]:
            return http400('wrong size')
    except:
        return http400('invalid format')

    v = mt.matFunc(mat)
    return JsonResponse({'eigenvalue': str(v)})

def matrices(request):
    try:
        matricesStr = request.POST['matrices']
        matrices = matricesStr.split('\n')
        vMatrices = []
        for it in matrices:
            matrix = np.matrix(it)
            if matrix.shape[0] != matrix.shape[1]:
                raise 'wrong size'
            vMatrices.append(matrix)
    except:
        return http400('invalid format')
    
    vEigenValue = []
    for it in matrices:
        vEigenValue.append(mt.matFunc(it))

    return JsonResponse({'eigenvalues': str(vEigenValue)})

def adjacentMatrix(request):
    try:
        n = request.GET['n']
        identificacao = request.GET['identificacao']
    except:
        return http400('invalid format')

    try:
        n = int(n)
        identificacao = int(identificacao)
    except:
        return http400('invalid format')
    try:
        st = ""
        with open('home/matrices/metarvore{}'.format(n)) as f:
            linePosition = (identificacao-1)*(n+2)+2
            qt = 0
            for i, line in enumerate(f):
                if i >= linePosition+n:
                    break
                if i >= linePosition:
                    try:
                        qt += 1
                        term = [int(it) for it in line.split()]
                        if len(term) != n:
                            raise 'exception'
                        st += line
                    except:
                        return http400('invalid identification')
            if qt != n:
                return http400('invalid identification')


        return JsonResponse({'matrix': st})
    except:
        return http400('invalid n')

def getImageTree(request):
    jsonObject = responsetoJson(response)
