import datetime
import os
import getpass
today = datetime.datetime.now()

today_data_time = today.strftime("%d/%m/%y,%H:%M:%S")
print(today_data_time)
print(getpass.getuser())
PWD = os.getcwd()
users_folder = PWD+'/users/'


def display_names(files_path):
	files_list = os.listdir((files_path))

	for file_name in files_list:
		with open(files_path+file_name, 'r') as file:
			names = file.readlines()
			for name in names:
				print(name, end="")


def gen_uuid(username):
	import random
	uuid = username.split()[0][0].upper()+username.split()[1][0].upper()
	for _ in range(4):
		uuid += str(random.randint(1001,9999))
		uuid += "-"
	return uuid.strip("-")






