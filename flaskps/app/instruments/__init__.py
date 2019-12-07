from flask import Blueprint
students = Blueprint('instruments', __name__)
from . import views
