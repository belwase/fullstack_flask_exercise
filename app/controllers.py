from app.base import APIEndpoint, BadRequest
from app.models import Employee

class EmployeeView(APIEndpoint):

    def get(self, employee_id=None):
        if employee_id:
            return Employee.query.get(employee_id=employee_id)
        else:
            return Employee.query.all()

    def post(self):
        
        payload = request.json or {}
        name = payload.get('name')
        if not name:
            raise BadRequest('"name" is required.')

        # emp = Employee(name=name)
        # to do insert employee
        return {}

