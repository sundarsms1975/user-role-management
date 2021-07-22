from accounts import User,Role
import ast
import json
import os
import sys
from copy import deepcopy

# Operation List presented when the main program execution starts
def choice_list():
    print('\n Choose the operation you would like to perform on User & Role List')
    print('                1. Load User List from INPUT file ')
    print('                2. Load Role List from INPUT file ')
    print('                3. Show Subordinates defined under a Role ID')
    print('                4. Add a new Role to List ')
    print('                5. Add a new User to List ')
    print('                6. Remove a role from List ')
    print('                7. Remove a user from List ')
    print('                8. Show Users with role definition ')
    print('                9. Show Subordinates with role details defined under a Role ID  ')
    print('               10. Show Users belongs to a Role_ID ')
    print('               11. Show Users belongs to a Parent_ID')
    print('               12. Show Roles belongs to a Particular Parent_ID')
    print('               14. Exit ')
    print('\n')
# Function loads User list from INPUT FILE and returns a list of dictionary objects
def getUserFromFile(filename):
    try:
        with open(filename) as f:
            s = f.read()
            users = ast.literal_eval(s)
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])

    return users

# Function loads Roles list from INPUT FILE and returns a list of dictionary objects
def getRoleFromFile(filename):
    try:
        with open(filename) as f:
            s = f.read()
            roles = ast.literal_eval(s)
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])

    return roles

# Function to fetch subordinates defined under a particular Role ID
def getSubordinates(roleid,userList):
    filteredUsers = [user for user in userList if int(user["Role"]) > int(roleid) ]
    return filteredUsers

# Function checks whether a Role exist in the current List
def isRoleExist(role_id,roles):
    for r in roles:
        if int(role_id) == int(r["Id"]):
            return True   

# Function checks whether Role to be added exists in the list before adding a Role to the List 
def addRoleToList(role,roleList):
    try:
        if not isRoleExist(role.role_id,roleList):
            roleList.append({"Id":role.role_id,"Name":role.role_name,"Parent":role.parent_id})
            del role
        else:
            print("Role_ID found in the new User object")
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    
    return roleList

# Function checks the role to be deleted before removing it
def removeRole(role_id,roleList):
    if not isRoleExist(role_id,roleList):
        print("Role ID supplied does not exist") 
    try:
        for i in range(len(roleList)):
            if int(roleList[i]["Id"]) == int(role_id):
                del roleList[i]     
                break
    except:
        print("Unexpected error:", sys.exc_info()[0])

# Function checks the role before adding a user to a particular role.
def addUserToList(user,userList,roleList):
    try:
        if isRoleExist(user.roleId,roleList):
            userList.append({"Id":user.user_id,"Name":user.username,"Role":user.roleId})
            del user
        else:
            print("Role_ID not found in the new User object, please add the role and add the user again")
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    
    return userList

# Function checks whether a User exists
def isUserExist(user_id,users):
    for user in users:
        if int(user_id) == int(user["Id"]):
            return True

# Function checks whether the user exits in the list before deleting it           
def removeUser(user_id,userList):
    if not isUserExist(user_id,userList):
        print("User ID supplied does not exist") 
        
    try:
        for i in range(len(userList)):
            if int(userList[i]["Id"]) == int(user_id):
                del userList[i]     
                break
    except:
        print("Unexpected error:", sys.exc_info()[0])

def lineDecorator(ichar):
    print(ichar*120)

#Get subordinates based on role_id
def getSubOrdinates(role_id,users):
    filteredUsers = [user for user in users if int(user["Role"]) > int(role_id) ]
    return filteredUsers


#Get user based on user_id
def getUser(user_id,users):
    filteredUsers = [user for user in users if int(user["Id"]) == int(user_id) ]
    return filteredUsers

# Decorator funtion
def linespacing():
    print("\n")

# Function to flatten User and Role, produces a combined list
# A single list user and role details in one record
def flattenUserRole(userList,roleList):
    userList_c = deepcopy(userList)
    for user in userList_c:
        for role in roleList:
            if user["Role"] == role["Id"]:
                user.update({"role_name":role["Name"],"parent_id":role["Parent"]})
    return userList_c

# Function to output a Role or User List in a nice JSON format
def dispResult(output_list):
    lineDecorator("*")
    print(json.dumps(output_list,indent=2))
    lineDecorator("*")
    #Spacing function as decorator
    linespacing() 

# Function to filter subordinates defined under a particular role.
def outputResult(id,output_list):
    lineDecorator("*")
    print(json.dumps(getSubOrdinates(id,output_list),indent=2))
    lineDecorator("*")
    #Spacing function as decorator
    linespacing() 

# Screen clear function, based on the OS type, it automatically chooses the command
# to clear the screen
def clear():
    _ = os.system('clear' if os.name =='posix' else 'cls')

# Pause function waits until user hits ENTER button to move the main Menu
def hitContine():
    input('Hit Enter to continue')

# Function to update changes back to User and Role definition INPUT files
# Next run of this program of picks up the latest changes as the starting List of Roles
def dumpListsToFile(Lists,filename):
    try:
        with open(filename,'w+') as f:
            json.dump(Lists,f,indent=2)
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])

#Get subordinates based on role_id
def getUserListForRoleId(role_id,users):
    filteredUsers = [user for user in users if int(user["Role"]) == int(role_id) ]
    return filteredUsers

#Get All users belongs to a particular parent_id
def getListForParentID(parent_id,users):
    filteredUsers = [user for user in users if int(user["parent_id"]) == int(parent_id) ]
    return filteredUsers

# Get all roles belongs to a particular parent_id
def getRolesListForParentID(parent_id,roles):
    filteredRoles = [role for role in roles if int(role["Parent"]) == int(parent_id) ]
    return filteredRoles

# The below functions are defined as decorator to output the result.s
def outputUserList_forRoleId(id,output_list):
    lineDecorator("*")
    print(json.dumps(getUserListForRoleId(id,output_list),indent=2))
    lineDecorator("*")
    #Spacing function as decorator
    linespacing() 

def outputUserList_forParentId(id,output_list):
    lineDecorator("*")
    print(json.dumps(getListForParentID(id,output_list),indent=2))
    lineDecorator("*")
    #Spacing function as decorator
    linespacing() 

def outputRolesList_forParentId(parent_id,roles):
    lineDecorator("*")
    print(json.dumps(getRolesListForParentID(parent_id,roles),indent=2))
    lineDecorator("*")
    #Spacing function as decorator
    linespacing() 