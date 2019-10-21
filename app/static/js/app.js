'use strict';

var app = angular.module('myapp', ['ngRoute', 'services'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: IndexController
		})
		.when('/employees', {
			templateUrl: 'static/partials/employee_list.html',
			controller: EmployeeController
		})
		.when('/teams', {
			templateUrl: 'static/partials/team_list.html',
			controller: TeamController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
		$locationProvider.hashPrefix('');
	}])
;