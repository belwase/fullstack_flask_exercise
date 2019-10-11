from flask import render_template, request, redirect
from app import app, db
from app.models import Employee

@app.route('/')
@app.route('/index')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)