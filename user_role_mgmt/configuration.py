import os

# INPUT parameters to provide source data directory and file names for Role and User
class input_params:
    def __init__(self,current_working_dir):
        self.current_working_dir = current_working_dir
        self.src_data_dir = os.path.abspath(current_working_dir+'/data/src_data')
        self.user_input_file = os.path.abspath(current_working_dir+"/data/src_data/users.json")
        self.role_input_file = os.path.abspath(current_working_dir+"/data/src_data/roles.json")

# OUTPUT parameters to provide source data directory and file names for Role and User
class output_params:
    def __init__(self,current_working_dir):
        self.current_working_dir=current_working_dir
        self.dest_data_dir = os.path.abspath(current_working_dir+'/data/target_data')
        self.combined_user_role__output_filename = os.path.abspath(current_working_dir+"/data/target_data/combined_users_role_list.json")
        
