'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarRaquetaCtrl
 * @description
 * # AgregarRaquetaCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarRaquetaCtrl', function ($scope, $http) {
    $scope.title = 'Raqueta';
    $scope.message = 'Agregar Raqueta';

      $http.get(api_path + 'velocidad?limit=0')
      .then(function(response) {
        $scope.velocidad = response.data;
      });
      $http.get(api_path + 'control?limit=0')
      .then(function(response) {
        $scope.control = response.data;
      });
      $http.get(api_path + 'cauchoNegro?limit=0')
      .then(function(response) {
        $scope.cauchoNegro = response.data;
      });
      $http.get(api_path + 'desc?limit=0')
      .then(function(response) {
        $scope.desc = response.data;
      });
      $http.get(api_path + 'cauchoRojo?limit=0')
      .then(function(response) {
        $scope.cauchoRojo = response.data;
      });

    $scope.add = function(){
      if($scope.Raqueta.velocidad == null){
        return;
      }
      if($scope.Raqueta.control == null){
        return;
      }
      if($scope.Raqueta.cauchoNegro == null){
        return;
      }
      if($scope.Raqueta.desc == null){
        return;
      }
      if($scope.Raqueta.cauchoRojo == null){
        return;
      }
    var data = {
        velocidad: $scope.Raqueta.velocidad,
        control: $scope.Raqueta.control,
        cauchoNegro: $scope.Raqueta.cauchoNegro,
        desc: $scope.Raqueta.desc,
        cauchoRojo: $scope.Raqueta.cauchoRojo,
    };
    $http.post(api_path + 'Raqueta',data);
    window.location.href = '#/Raqueta';
  };

  $scope.cancel = function(){
    window.location.href = '#/Raqueta';
  };
  });