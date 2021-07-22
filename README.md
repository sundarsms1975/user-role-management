User-Role Management Utility
=============================
User-management utility is a Python based package to perform few operations on users list, roles list. This tool provides file based persistent capability(database), therefore adding/removing role/user persisted on disk to keep all changes in tact.

As per the Deputy Task requirement, this utility has been built with the following capabilities.

i. Loading User & Role Lists from Input Files 
ii. Add new User 
iii. Add new Role 
iv. Remove Role 
v. Remove User 
vi. Filter users based on Role Id and Parent ID 
v. Flattened structure of User and Role as single user list with role details added in it.

Note:
=====
In addition to the tasks requirement, built additional capabilities in a modularised fashion, therefore this tool can be extended to build full-fledged solution to facilitate user management.

In addition to the input data (sample Roles, Users), have added additional Roles and Users.
It can be tested by adding or removing Roles and Users, which immediately persisted on input files.

The input are treated DB files to capture changes made to User adn Role definitions.

Installation
=============
This utility is built on python version 3.6 in-built packages, it just needs a python module called "ast", which cleans up JSON file or JSON String.

1. Set a base directory under any drive or filesystem path

2. Download the package into the base directory

Directory Structure
-------------------
├── LICENSE
├── MANIFEST.in
├── README.md
├── data
│   ├── src_data
│   │   ├── roles.json
│   │   └── users.json
│   └── target_data
│       ├── combined_users_role_list.json
│       ├── updated_roles_list.json
│       ├── updated_users_list.json
│       └── users_ent.json
├── main.py
├── pyproject.toml
├── requirements.txt
├── setup.py
└── user_role_mgmt
    ├── __init__.py
    ├── __pycache__
    │   ├── accounts.cpython-39.pyc
    │   ├── configuration.cpython-39.pyc
    │   └── operations.cpython-39.pyc
    ├── accounts.py
    ├── configuration.py
    └── operations.py


3. Install required python modules as shown below

To install ast python package
-----------------------------
python3 -m pip install -r requirements.txt

4. To Start this utility

 $ python3 main.py
 Choose the operation you would like to perform on User & Role List
                1. Load User List from INPUT file 
                2. Load Role List from INPUT file 
                3. Show Subordinates defined under a Role ID
                4. Add a new Role to List 
                5. Add a new User to List 
                6. Remove a role from List 
                7. Remove a user from List 
                8. Show Users with role definition 
                9. Show Subordinates with role details defined under a Role ID  
               10. Show Users belongs to a Role_ID 
               11. Show Users belongs to a Parent_ID
               12. Show Roles belongs to a Particular Parent_ID
               14. Exit 
Enter choice(1-6) : 


Usage
=====
This utility is menu driven program. These menu items are almost self-explanatory. 

To use this utility

 Choose the operation you would like to perform on User & Role List
                1. Load User List from INPUT file 
                2. Load Role List from INPUT file 
                3. Show Subordinates defined under a Role ID
                4. Add a new Role to List 
                5. Add a new User to List 
                6. Remove a role from List 
                7. Remove a user from List 
                8. Show Users with role definition 
                9. Show Subordinates with role details defined under a Role ID  
               10. Show Users belongs to a Role_ID 
               11. Show Users belongs to a Parent_ID
               12. Show Roles belongs to a Particular Parent_ID
               14. Exit 

Enter choice(1-6) : 3
Enter Role_ID to get subordinates defined under Role ID : 5

Subordinates who are defined under Role ID = 5
************************************************************************************************************************
[
  {
    "Id": 8,
    "Name": "Hamish",
    "Role": 7
  },
  {
    "Id": 9,
    "Name": "Michiel Marsdan",
    "Role": 7
  },
  {
    "Id": 10,
    "Name": "Siddharth Sundar",
    "Role": 8
  },
  {
    "Id": 11,
    "Name": "Michal",
    "Role": 8
  }
]
************************************************************************************************************************

Hit Enter to continue  



Additional Notes
================

This utility is built the following industry programming best practices applied.

Programming Features Applied
----------------------------
1. Right data structure for this task

2. Compact codes, most of the repeatable codes are written as functions and are reused in this program

3. Relevant sections of the related components are separated into different modules, which provides clean code base and module de-coupling capability.

3. Avoided unnecessary variables, which consumes memory and becomes inefficient

4. Detailed comments, however comments are the section in most programming code base never touched once deployed or code base increased, therefore used a minimal comments with full name used for variables and functions, so it does not required very detailed comments

5. Avoid abbreviations as much as possible.

6. Used simple functions and argument passig approach, which avoids confusions.


