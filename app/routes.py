from flask import render_template, request, redirect, abort
from app import app, db
from app.models import Employee
from app.controllers import EmployeeView

@app.route('/')
@app.route('/index')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

app.add_url_rule('/api/employee', view_func=EmployeeView.as_view('employee'))
app.add_url_rule('/api/employee/<employee_id>', view_func=EmployeeView.as_view('employe_with_id'))

