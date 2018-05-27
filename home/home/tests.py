from django.test import TestCase
from django.test import Client
from home.models import Arvore
import json

def responsetoJson(response):
    return json.loads(response.content.decode('utf-8'))

class QuestionMethodTests(TestCase):

    def setUp(self):
        self.c = Client()
        #Arvore.objects.create(id=1,tipo=2,identificacao=3,alfa=5,diametro=7,arestas=23)

    def testArvore(self):
        response = self.c.get('/arvores')
        jsonObject = responsetoJson(response)
        #print(jsonObject[0]['alfa'])

    def testOK(self):
        mat = '2 0; 0 1'
        response = self.c.post('/matrix', {'matrix': mat})
        self.assertIs(response.status_code,200)
        jsonObject = responsetoJson(response)
        v = jsonObject['eigenvalue']
        v = int(v)
        self.assertIs(v,5)

    def testWrong(self):
        response = self.c.post('/matrix', {'matrix': 'a 2; 3 4'})
        assert response.status_code == 400
        assert responsetoJson(response)['reason'] == 'invalid format'

        response = self.c.post('/matrix', {'matrix': "'a' 2; 3 4"})
        assert response.status_code == 400
        assert responsetoJson(response)['reason'] == 'invalid format'

        response = self.c.post('/matrix', {'mat': '123'})
        assert response.status_code == 400

        response = self.c.post('/matrix', {'matrix': '1 2 3, 4 5 6'})
        assert response.status_code == 400

        response = self.c.post('/matrix', {'matrix': '1 2, 4 5 6'})
        assert response.status_code == 400
    
    def testMatricesOK(self):
        response = self.c.post('/matrices', {'matrices': '1 2; 3 4\n1 0; 0 2'})
        assert response.status_code == 200
        jsonObject = responsetoJson(response)
        v = jsonObject['eigenvalues']
        vet = eval(v)
        assert len(vet) == 2

    def testAdjacentMatrix(self):
        response = self.c.get('/adjacentMatrix', {'n': '11', 'identificacao':
            '1'})
        jsonObject = responsetoJson(response)
        print(jsonObject)
