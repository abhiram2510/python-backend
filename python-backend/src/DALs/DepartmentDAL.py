from EMConnectionManager import connection
from src.models import Department
cursor= connection.cursor()

class DepartmentDAL:
    async def createDepartment(department:Department):
        query=("insert into department(name) values(%s)")
        value=[department.name]
        try:
            cursor.execute(query,value)
            connection.commit()
            return True
        except:
            return False
        
    async def getAllDepartment():
        query=("select * from department")
        cursor.execute(query)
        depDetails = cursor.fetchall()
        return depDetails
    
    
        
