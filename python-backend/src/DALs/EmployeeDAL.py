from EMConnectionManager import connection
from src.models import Employee
cursor =  connection.cursor()

class EmployeeDAL:
    async def getEmployee(employee:Employee):
        query=("select * from employee where first_name=%s")
        value=[employee.first_name]
        cursor.execute(query,value)
        empdetails=cursor.fetchall()
        return empdetails
    
    async def getAllEmployees():
        query=("select * from employee")
        cursor.execute(query)
        empdetails = cursor.fetchall()
        return empdetails
