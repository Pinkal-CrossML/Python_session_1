class UserDetails:
    def __init__(self, user_name):
        self.name  = user_name

    def gen_uuid(self):
        import uuid
        return str(uuid.uuid1())

    def gen_email(self):
        return self.name.split()[0] + self.name.split()[1][0]+'@dummy.com'

users_list_of_names = []

def date_name():
    from datetime import datetime
    import getpass

    time = datetime.now().strftime("%H:%M:%S")
    username = getpass.getuser()
    return (time, username)

def display_usernames():
    import os
    PWD = os.getcwd()
    file_name = input("Enter your folders name : ")
    full_path = PWD+"/"+file_name

    for file_name in os.listdir(full_path):
        # print(file_name)
        with open(full_path +"/"+file_name, 'r') as f:
            user_names = f.readlines()
            # print(user_names)
            for user_name in user_names:
                users_list_of_names.append(user_name.strip())
                print(user_name.rstrip())

def writeToJson():
    writer = open('users.json', 'w')
    import json
    json_object = []
    for user in users_list_of_names:
        u = UserDetails(user)
        json_object.append({\
        u.gen_uuid():{\
        'name':user,\
        'email':u.gen_email()\
        }\
        })
    
    json.dump(json_object, writer, indent = 1)
    # print(json_object)
            
        

time, username = date_name()
print("Time is : ", time)
print("Name is : ", username)
display_usernames()
writeToJson()

