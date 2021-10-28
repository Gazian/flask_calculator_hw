from flask import render_template
from app import app
from modules.calculator import *



@app.route('/calculator') 

@app.route('/add/<value_1>/<value_2>')
def add(value_1,value_2):
    return f"The answer is {calc_add_function(int(value_1),int(value_2))}"

@app.route('/subtract/<value_1>/<value_2>')
def subtract(value_1,value_2):
    return f"The answer is {calc_subtract_function(int(value_1),int(value_2))}"

@app.route('/multiply/<value_1>/<value_2>')
def multiply (value_1, value_2):
    return f"The answer is {calc_multiply_function(int(value_1),int(value_2))}"

@app.route('/divide/<value_1>/<value_2>')
def divide (value_1,value_2):
    return f"The answer is {calc_divide_function(int(value_1),int(value_2))}"