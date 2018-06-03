'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarCauchonegroCtrl
 * @description
 * # AgregarCauchonegroCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarCauchonegroCtrl', function ($scope, $http) {
    $scope.title = 'Cauchonegro';
    $scope.message = 'Agregar Cauchonegro';

      $http.get(api_path + 'velocidad?limit=0')
      .then(function(response) {
        $scope.velocidad = response.data;
      });
      $http.get(api_path + 'control?limit=0')
      .then(function(response) {
        $scope.control = response.data;
      });
      $http.get(api_path + 'desc?limit=0')
      .then(function(response) {
        $scope.desc = response.data;
      });

    $scope.add = function(){
      if($scope.CauchoNegro.velocidad == null){
        return;
      }
      if($scope.CauchoNegro.control == null){
        return;
      }
      if($scope.CauchoNegro.desc == null){
        return;
      }
    var data = {
        velocidad: $scope.CauchoNegro.velocidad,
        control: $scope.CauchoNegro.control,
        desc: $scope.CauchoNegro.desc,
    };
    $http.post(api_path + 'CauchoNegro',data);
    window.location.href = '#/CauchoNegro';
  };

  $scope.cancel = function(){
    window.location.href = '#/CauchoNegro';
  };
  });