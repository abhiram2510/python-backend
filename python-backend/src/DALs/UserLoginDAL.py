from EMConnectionManager import connection
from src.models import UserLogin
cursor = connection.cursor()

class UserLoginDAL:
    async def login(userLogin:UserLogin):
        query = ("select emp_id from userlogin where username=%s and pass=%s")
        values= (userLogin.username,userLogin.password)
        cursor.execute(query,values)
        empid= cursor.fetchall()
        return empid[0]
    

        
        

