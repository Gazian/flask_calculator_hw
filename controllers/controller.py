from flask import render_template
from app import app
from modules.calculator import *

@app.route('/add')
def