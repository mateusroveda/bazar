from flask import Blueprint, jsonify, url_for
api = Blueprint('api', __name__)

### Register Controller
from bazar.app.Http.Controllers import ApiController

@api.route('/api', methods=['GET'])
def index():
    return ApiController.index()

def init_app(app):
    app.register_blueprint(api)