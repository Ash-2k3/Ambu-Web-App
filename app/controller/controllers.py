from flask import request
from flask import Blueprint, render_template
import json
import requests


get_index_bp = Blueprint('index', __name__)
get_emergency_page_bp = Blueprint('emergency_page', __name__)

@get_index_bp.route('/')
def index():
           # Render index.html
           return render_template('index.html')

@get_emergency_page_bp.route('/emergency')
def emergency_page():
           # Render e----.html
           return render_template('ambu-emergency-page.html')