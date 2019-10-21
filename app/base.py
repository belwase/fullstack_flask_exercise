from flask import Blueprint, make_response, json, current_app
from flask.views import MethodView
from .exceptions import BadRequest

#api = Blueprint('the_api', __name__)


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def handle_exception(e):
    # handle common exceptions
    if isinstance(e, DuplicateKeyError):
        raise BadRequest(str(e))


def json_converter(f):
    '''Converts `dict`, list or mongo cursor to JSON.
    Creates `~flask.Response` object and sets headers.
    '''
    def decorator(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception as e:
            handle_exception(e)
            raise

        if isinstance(result, dict):
            result = json.dumps(result, cls=JsonEncoder)
        else:
            # unwind cursor
            result = json.dumps(list(result), cls=JsonEncoder)
        response = make_response(result)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    return decorator





class APIEndpoint(MethodView):
    # make converter run after every request handler method returns
    decorators = [json_converter]

    def __init__(self, *args, **kwargs):
        super(APIEndpoint, self).__init__(*args, **kwargs)
        self.logger = current_app.logger