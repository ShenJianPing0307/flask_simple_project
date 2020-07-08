from flask import Blueprint
from flask import render_template
from flask import request


blogs = Blueprint('blogs',__name__)

@blogs.route('/home')
def home():
    return render_template('home.html')