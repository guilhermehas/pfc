'use strict';

var app = angular.module("tableController", ['nvd3']);

app.controller('alltablesController', function($scope, $http, $routeParams, $httpParamSerializer){
    $scope.page = 1
    $scope.params = {};
    $scope.changeTable = function(){
        $scope.params.page = $scope.page;

        $http.get('tables/'+$routeParams.name+'/table', {params: $scope.params})
        .then(function(response) {
            $scope.table = response.data.vector;
            $scope.qt = response.data.qt;
            $scope.page = parseInt(response.data.page);
        });
    };

    $scope.downloadCSV = function(){
        $http({
            url: 'tables/'+$routeParams.name+'/csv',
            method: "GET",
            params: $scope.param
        }).success(function (data, status, headers, config) {
            var blob = new Blob([data], {type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"});
            var objectUrl = URL.createObjectURL(blob);
            window.open(objectUrl);
        });
    };

    $scope.download = function(){
        var url = 'tables/'+$routeParams.name+'/csv';
        var paramSer = $httpParamSerializer($scope.param);
        return url+paramSer;
    }


    var getFields = function(){
        $http.get('tables/'+$routeParams.name+'/names')
        .then(function(response) {
            $scope.fields = response.data;
            console.log($scope.fields);
        });
        
    };

    getFields();
    $scope.changeTable();

    $scope.preview = function(){
        if($scope.page > 1){
            $scope.page -= 1;
            $scope.changeTable();
        }
    }

    $scope.advance = function(){
        $scope.page += 1
        $scope.changeTable();
    }
});
