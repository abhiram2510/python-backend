from fastapi import FastAPI
from sample import showTables
from src.models.UserLogin import UserLogin
from src.DALs.UserLoginDAL import UserLoginDAL
from src.models.Employee import Employee
from src.DALs.EmployeeDAL import EmployeeDAL
from src.models.Department import Department
from src.DALs.DepartmentDAL import DepartmentDAL

app = FastAPI()



@app.get('/')
async def root():
    showTables()
    return {'example':'This is an example','data':0}

@app.post('/api/v1/login')
async def login(item:UserLogin):
    empid= await UserLoginDAL.login(item)
    return {"Employeeid": empid}


@app.post('/api/v1/getEmployees')
async def getEmployee(employee:Employee):
    empdetails= await EmployeeDAL.getEmployee(employee)
    return {"EmployeeDetails":empdetails[0]}


@app.post('/api/v1/getAllEmployees')
async def getAllEmployee():
    empdetails= await EmployeeDAL.getAllEmployees()
    return {"EmployeeDetails":empdetails}

@app.post('/api/v1/createDepartment')
async def createDepartment(department:Department):
    depdetails = await DepartmentDAL.createDepartment(department)
    return {"CreatedSuccessfully?":depdetails}

@app.post('/api/v1/getAllDepartment')
async def getAllDepartment():
    depDetails = await DepartmentDAL.getAllDepartment()
    return {"departmentDetails":depDetails}
