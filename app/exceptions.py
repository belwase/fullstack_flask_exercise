# -*- coding: utf-8 -*-
'''
Wrapper classes to return JSON exception, not HTML exception as werkzeug does.
'''
from flask import jsonify
from werkzeug import exceptions
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException




class JSONHTTPException(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def std_handler(self, error):
        response = jsonify(message=error.message)
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response


    def init_app(self, app):
        self.app = app
        self.register(HTTPException)
        for code, v in default_exceptions.iteritems():
            self.register(code)

    def register(self, exception_or_code, handler=None):
        self.app.errorhandler(exception_or_code)(handler or self.std_handler)

class BadRequest(JSONHTTPException, exceptions.BadRequest):
    pass


class Forbidden(JSONHTTPException, exceptions.Forbidden):
    pass        