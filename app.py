

class RegisterUser():

    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role
        self.users = []

    def register_user(self, username, password, role):
        """A function to operate on registration"""
        username = input("\nEnter username....")
        password = input("\nEnter password....")
        role = input("\nEnter role....")

        if not username:
            print("username not provided")
        if not password:
            print("password not provided")

        for user in self.users:
            if user.username == user['username']:
                return "user already exists"
            new_user = user(username, password, role)
            self.users.append(new_user)
            print('Account created successfully')

"""This displays the menu"""
print('-------welcome------')
print('\n-------Menu---------')
print('\n1. Create New Account')
print('\n2. Login')

choice = input("\nwould you like to login or register....")
if choice == '1':
    code = RegisterUser('username', 'password', 'role')
    code.register_user('username', 'password', 'role')
 



        
   

 
