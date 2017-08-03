from flask import Blueprint, render_template, request
from app.welcome.controllers import *

welcome_blueprint = Blueprint(
        'main',
        __name__,
        template_folder='templates'
    )


@welcome_blueprint.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = parseApplicationRequest(request)


    return render_template('index.html')