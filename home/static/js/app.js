var app = angular.module("myApp", ["ngRoute",'tableController','pascalprecht.translate']);

app.config(function($routeProvider,$interpolateProvider, $translateProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "static/pages/home.html"
    })
    .when("/arvores", {
        templateUrl : "static/pages/arvore.html",
        controller : 'arvorescontroller'
    })
    .when("/tables/:name", {
        templateUrl : "static/pages/content.html",
        controller : 'alltablesController'
    });
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    $translateProvider.useStaticFilesLoader({
        prefix: 'static/data/',
        suffix: '.json'
    });
    $translateProvider.preferredLanguage('pt');
      
});

app.controller('defaultcontroller',function($scope, $http){
    $http.get('tablesnames').then(function(response){
        $scope.tableNames = response.data;
    });

    //$scope.tableNames = ['est','AdicaoArestaBroom','AdicaoArestaDoubleBroom','broom45','broom89'];
});


app.controller('arvorescontroller', function($scope, $http) {
    $scope.page = 0;
    $scope.lenpage = 10;

    var changeTable = function(data){
        if(data == null)
            data = {};
        data.init = $scope.page*$scope.lenpage;
        data.qt = $scope.lenpage;
        $http.get("arvores", {params: data})
        .then(function(response) {
            $scope.size = response.data.size;
            $scope.table = response.data.arvores;
        });
    };

    changeTable();

    $scope.getarvores = function(){
        $scope.page = 0;
        changeTable($scope.arvores);
    };
    
    $scope.preview = function(){
        if($scope.page > 0){
            $scope.page -= 1;
            changeTable($scope.arvores);
        }
    }

    $scope.advance = function(){
        if(($scope.page+1)*$scope.lenpage < $scope.size){
            $scope.page += 1;
            changeTable($scope.arvores);
        }
    }

    $scope.showArvore = function(key,line){
        if(line.ifShow)
            line.ifShow = false;
        else{
            data = {n: line.n, identificacao: line.identificacao}
            $http.get("adjacentMatrix", {params: data} )
            .then(function(response) {
                $scope.table[key].matrix = response.data.matrix;
                var vet = $scope.table[key].matrix.split('\n');
                for(i=0; i<vet.length; i++)
                    vet[i] = vet[i].split(' ');
                //console.log(vet);
                var color = d3.scale.category20();
                $scope.table[key].options = {
                    chart: {
                        type: 'forceDirectedGraph',
                        height: 300,
                         width: (function(){ return nv.utils.windowSize().width/3 })(),
                        color: function(){
                            return color(0)
                        }
            
                    }
                };
                $scope.table[key].data = {'links': new Array()};
                $scope.table[key].data['nodes'] = new Array();
                for(i=0; i<vet.length-1; i++){
                    $scope.table[key].data['nodes'].push({'name': i});
                    for(j=i+1; j<vet.length-1; j++)
                        if(vet[i][j] == '1')
                            $scope.table[key].data['links'].push({'source':i, 'target':j});
                }
                //console.log($scope.table[key].data);
                $scope.table[key].ifShow = true;
            });
        }
    }
    
});
