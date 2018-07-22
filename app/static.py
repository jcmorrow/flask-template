from flask import Blueprint, render_template

static = Blueprint('main', __name__)


@static.route('/', methods=['GET'])
def index():
    return render_template('index.html')
