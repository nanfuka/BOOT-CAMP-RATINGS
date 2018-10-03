

class Login():

 #innitialise variable
    def __init__(self,users=[] ):
        self.registred_users = users
        self.lfa_list = []
        self.boot_campers_list = []
        self.lf_list = []
        self.lfa_obj = {}
        self.lf_obj ={}
        self.boot_camper_obj = {}
        self.lf_id = 0
        self.bootcamper_id = 0
        self.lfa_id = 0

    def login_user(self,user_name = input("enter user name"), password = input("enter username") ):
        "  a method to login user  "
        for user in self.registred_users:
             if not user["user_name"] == user_name and user["password"]== password:
                 print("un registered user. please login")
                 return False

             if user["role"] == "LF":
                 self.lf_id =  len(self.lf_list) + 1
                 self.lf_obj = {"user_name" : user_name,
                                 "user_id" : self.lf_id}
                 self.lf_list.append(self.lf_obj)

             if user["role"] == "LFA":
                 self.lfa_id =  len(self.lfa_list) + 1
                 self.lf_obj = {"user_name" : user_name,
                                 "user_id" : self.lf_id}
                 self.lfa_list.append(self.lf_obj)

             if user["role"] == "BT":
                 self.bootcamper_id  =len(self.boot_campers) + 1
                 self.boot_camper_obj = {"user_name" : user_name,
                                 "user_id" : self.lf_id}
                 self.boot_campers_list.append(self.boot_camper_obj)

    def get_boot_campers(self):
        return self.boot_campers_list

    def get_lfs(self):
        return self.lf_list

    def get_lfs(self):
        return self.lfa_list

