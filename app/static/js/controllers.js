'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}


function EmployeeController($scope, Employee){
	self.employees = [];
	var query = Employee.get({employee_id: ''});
    query.$promise.then(function (result) {
		angular.forEach(result['data'], function(d, akey) {
			this.push({id: d['id'], name: d['name']});
		}, self.employees);
		$scope.employees = self.employees;
    });

}

function TeamController($scope, Team){
	self.teams = [];
	var query = Team.get({team_id: ''});
    query.$promise.then(function (result) {
		angular.forEach(result['data'], function(d, akey) {
			this.push({id: d['id'], name: d['name']});
		}, self.teams);
		$scope.teams = self.teams;
    });

}

app.controller("EmployeeController", EmployeeController);
app.controller("TeamController", TeamController);