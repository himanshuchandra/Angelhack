'use strict';

/**
 * @ngdoc function
 * @name webskeletonApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the webskeletonApp
 */
angular.module('webskeletonApp')
  .controller('AboutCtrl', function ($scope,$window,webindex,requrl,$route) {
    $scope.ready=false;
    $scope.productDisplay=true;
    $scope.done=true;
    $scope.finishText=true;
    $scope.Credits=300;
    $scope.clickButton=true;

    $scope.displayProduct=function(){
      $scope.ready=true;
      $scope.productDisplay=false;
    }

    $scope.typing=function(){
      if($scope.sentiment.length>25){
        $scope.done=false;
      }
      else{
        $scope.done=true;
      }
    }

    $scope.sendToDjango=function(){
      $scope.productDisplay=true;
      $scope.finishText=false;
      $scope.Credits+=100;
    }
  });
