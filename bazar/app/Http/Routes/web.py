from flask import Blueprint
web = Blueprint('web', __name__)

### Register Controller
from bazar.app.Http.Controllers import WebController
## Home
@web.route("/", methods=['GET'])
def home():
    return WebController.index()

def init_app(app):
    app.register_blueprint(web)