from flask import Blueprint
from flask_restful import Api

main = Blueprint('main', __name__)
api = Api(main)

from flask_restful.representations.json import output_json
output_json.func_globals['settings'] = {'ensure_ascii': False, 'encoding': 'utf8'}

from . import views, errors, views_api
