'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function PostListController($scope, Post) {
    var self = this;
    self.posts = [];
    var postsQuery = Post.get({postId: ''});
    postsQuery.$promise.then(function (result) {
		angular.forEach(result['data'], function(post, akey) {
			this.push({id: post['id'], title: post['attributes']['title']});
		}, self.posts);
		$scope.posts = self.posts;
    });
}