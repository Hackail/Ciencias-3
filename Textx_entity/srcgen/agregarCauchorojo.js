'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarCauchorojoCtrl
 * @description
 * # AgregarCauchorojoCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarCauchorojoCtrl', function ($scope, $http) {
    $scope.title = 'Cauchorojo';
    $scope.message = 'Agregar Cauchorojo';

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
      if($scope.CauchoRojo.velocidad == null){
        return;
      }
      if($scope.CauchoRojo.control == null){
        return;
      }
      if($scope.CauchoRojo.desc == null){
        return;
      }
    var data = {
        velocidad: $scope.CauchoRojo.velocidad,
        control: $scope.CauchoRojo.control,
        desc: $scope.CauchoRojo.desc,
    };
    $http.post(api_path + 'CauchoRojo',data);
    window.location.href = '#/CauchoRojo';
  };

  $scope.cancel = function(){
    window.location.href = '#/CauchoRojo';
  };
  });