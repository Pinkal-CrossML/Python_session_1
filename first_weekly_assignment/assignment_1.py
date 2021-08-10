"""
Problem:
Create a shell script that will unzip the user.zip archive and run python script that
 1. Display Time and Username.
 2. Read each file one by one and display the names of users in each file.
 3. Generate a
    * userId -> random UUID
    * dummy email address based on user name.
 4. store all the data in json file with format:

"""
from datetime import datetime
import getpass
import os


class User_information():
    """
    In this function user_datetime_name(),
    we will Display Time and Username of user.
    """
    def user_datetime_name(self):
        time = datetime.now().time().strftime('%H:%M:%S')
        username = getpass.getuser()
        print(f"Time: {time} ,Username: {username}")

    """
    In this function we display the text file
    and inside data(name) in the form of list 

    """

    def user_name(self):
        path = "/home/user/crossml/first_weekly_assignment/users/"

        file_name = os.listdir(path)
        for file in file_name:
            read_file = open(path + file, 'r')
            read_data = read_file.readlines()
            for name in read_data:
                print(name.strip())
        read_file.close()


user = User_information()
user.user_name()


user = User_information()
user.user_datetime_name()








