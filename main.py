import sys
sys.path.insert(0, './user_role_mgmt')
from accounts import Role,User
from operations import *
from configuration import input_params,output_params
import ast
import json
import os

# Setting working directory 
###########################################################################################################
working_dir = os.getcwd()
os.chdir(working_dir)
os.system('color FF')

INPUT_PARAMS = input_params(working_dir)
OUTPUT_PARAMS = output_params(working_dir)

###########################################################################################################
# Users & Roles INPUT files are processed here and made available as list of dictionary objects to apply 
# operations such as, filter, add role, remove role, add user, remove user, and finally dump the final 
# list of flatted users ( includes user with role details), or to dump individual user list or role list 
# in JSON format to OUTPUT directory
#
#  Python Objects : 
#       role_list  :  contains list of roles provided in the INPUT file
#       user_list contains list of users in the INPUT file.
###########################################################################################################
role_list = getRoleFromFile(INPUT_PARAMS.role_input_file)
user_list = getUserFromFile(INPUT_PARAMS.user_input_file)
flattenUserRole(user_list,role_list)

# Main function definition
def main():
    while(True):
        clear()
        choice_list()
        get_choise = input("Enter choice(1-6) : ")
        if get_choise == '1':
            dispResult(role_list)
            hitContine()

        elif get_choise == '2':
            dispResult(user_list)
            hitContine()

        elif get_choise == '3':
            role_id = int(input('Enter Role_ID to get subordinates defined under Role ID : '))
            linespacing()
            print("Subordinates who are defined under Role ID = "+str(role_id))
            outputResult(role_id,user_list)
            hitContine()

        elif get_choise == '4':
            roleId = int(input('Enter Role_ID : '))
            roleName = str(input('Enter Role Name : '))
            parentId = int(input('Enter Parent : '))
            role = Role(roleId,roleName,parentId)
            addRoleToList(role,role_list)
            dumpListsToFile(role_list,INPUT_PARAMS.role_input_file)
            print("Role Id "+str(roleId)+" added")
            hitContine()

        elif get_choise == '5':
            userId = int(input('Enter User_ID : '))
            userName = str(input('Enter User Name : '))
            roleID = int(input('Enter Role ID : '))
            user = User(userId,userName,roleID)
            addUserToList(user,user_list,role_list)
            dumpListsToFile(user_list,INPUT_PARAMS.user_input_file)
            print("User Id "+str(userId)+" added ")
            hitContine()

        elif get_choise == '6': 
            role_id = None
            role_id = int(input('Enter Role_ID to be removed : '))
            removeRole(role_id,role_list) 
            print("Role Id : "+str(role_id)+" deleted ")

        elif get_choise == '7':
            user_id = None
            user_id = int(input('Enter User_ID to be removed : '))
            removeUser(user_id,user_list)
            print("User Id : "+str(user_id)+" deleted ")

        elif get_choise == '8':
            dispResult(flattenUserRole(user_list,role_list))
            hitContine()

        elif get_choise == '9':
            role_id = int(input('Enter Role_ID to get all subordinates defined for this Role ID: '))
            linespacing()
            print("Subordinates who are defined under Role ID = "+str(role_id))
            outputResult(role_id,flattenUserRole(user_list,role_list))
            hitContine()

        elif get_choise == '10':
            role_id = int(input('Enter Role_ID to get all users belongs to that Role : '))
            linespacing()
            print("Users who belongs to a Role ID = "+str(role_id))
            outputUserList_forRoleId(role_id,flattenUserRole(user_list,role_list))
            hitContine()

        elif get_choise == '11':
            parent_id = int(input('Enter Parent ID to get all users belongs to that Parent_Id : '))
            linespacing()
            print(" Users belongs to a particular Parent Id = "+str(parent_id))
            outputUserList_forParentId(parent_id,flattenUserRole(user_list,role_list))
            hitContine()

        elif get_choise == '12':
            parent_id = int(input('Enter Role_ID to all users belongs to that Role : '))
            linespacing()
            print("Roles belongs to a particular Parent ID = "+str(parent_id))
            outputRolesList_forParentId(parent_id,role_list)
            hitContine()

        elif get_choise == '14':
            dumpListsToFile(role_list,INPUT_PARAMS.role_input_file)
            dumpListsToFile(user_list,INPUT_PARAMS.user_input_file)
            dumpListsToFile(flattenUserRole(user_list,role_list),OUTPUT_PARAMS.combined_user_role__output_filename)
            break

        else:
            print('Invalid input')
            hitContine()

# Execution Starts here            
if __name__ == '__main__':
    main()
    


