'use strict';

angular.module('services', ['ngResource'])
	.factory('Employee', ['$resource', function($resource) {
		return $resource('/api/employee/:employeeId',
			{},
			{
				get: {
					method: 'GET',
					params: { employee_id: '@_id' },
					isArray: false,
					headers: {'Content-Type': 'application/vnd.api+json',
								'Accept': 'application/vnd.api+json'}
				}
			}
		);	
	}])
	.factory('Team', ['$resource', function($resource) {
		return $resource('/api/team/:teamId',
			{},
			{
				get: {
					method: 'GET',
					params: { team_id: '@_id' },
					isArray: false,
					headers: {'Content-Type': 'application/vnd.api+json',
								'Accept': 'application/vnd.api+json'}
				}
			}
		);	
	}]);