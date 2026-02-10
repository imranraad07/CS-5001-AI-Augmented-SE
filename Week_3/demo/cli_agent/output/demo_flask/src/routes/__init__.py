from flask import Blueprint

main = Blueprint("main", __name__)

from src.routes import views
