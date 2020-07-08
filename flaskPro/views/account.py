from flask import Blueprint
from flask import render_template
from flask import request

account = Blueprint('account',__name__)


@account.route('/login')
def login():
    return render_template('login.html')