import json
import ast

class User:
       
    # User object constructor
    def __init__(self,user_id,username,roleId):
        self.user_id = user_id
        self.username = username
        self.roleId = roleId
 
    # Function to get User Object
    def getUser(self):
        return {"Id":self.user_id,"Name":self.username,"Role":self.roleId}
    
    
class Role:
    # Role object constructor
    def __init__(self,role_id,role_name,parent_id):
        self.role_id = role_id
        self.role_name = role_name
        self.parent_id = parent_id

    # Function to get Role Object
    def getRole(self):
        return {"Id":self.role_id,"Name":self.role_name,"Parent":self.parent_id}
 
