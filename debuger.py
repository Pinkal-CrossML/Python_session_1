#  This file is all about "debugging with pdb module".
import pdb

pdb.set_trace()
name = input("Enter your name :")
age = input("Enter your age   :")  #use int here after debuging

next_age = age + 5
print(f'hello {name} you will be {next_age} in next five years!')


# use l and n to fine the error like this :

# terminal
"""
> /home/user/crossml/python-work/debuger.py(5)<module>()
-> name = input("Enter your name :")
(Pdb) l
  1  	# Todo: This file is all about "debugging with pdb module".
  2  	import pdb
  3  	
  4  	pdb.set_trace()
  5  ->	name = input("Enter your name :")
  6  	age = input("Enter your age   :")
  7  	
  8  	next_age = age + 5
  9  	print(f'hello {name} you will be {next_age} in next five years!')
 10  	
 11  	
(Pdb) n
Enter your name :pinkj
> /home/user/crossml/python-work/debuger.py(6)<module>()
-> age = input("Enter your age   :")
(Pdb) name
'pinkj'
(Pdb) l
  1  	# Todo: This file is all about "debugging with pdb module".
  2  	import pdb
  3  	
  4  	pdb.set_trace()
  5  	name = input("Enter your name :")
  6  ->	age = input("Enter your age   :")
  7  	
  8  	next_age = age + 5
  9  	print(f'hello {name} you will be {next_age} in next five years!')
 10  	
 11  	
(Pdb) n
Enter your age   :5
> /home/user/crossml/python-work/debuger.py(8)<module>()
-> next_age = age + 5
(Pdb) n
TypeError: can only concatenate str (not "int") to str
> /home/user/crossml/python-work/debuger.py(8)<module>()
-> next_age = age + 5
(Pdb) l
  3  	
  4  	pdb.set_trace()
  5  	name = input("Enter your name :")
  6  	age = input("Enter your age   :")
  7  	
  8  ->	next_age = age + 5
  9  	print(f'hello {name} you will be {next_age} in next five years!')
 10  	
 11  	
 12  	
 13  	
(Pdb) n
--Return--
> /home/user/crossml/python-work/debuger.py(8)<module>()->None
-> next_age = age + 5
(Pdb) 
--Call--
Traceback (most recent call last):
  File "/home/user/crossml/python-work/debuger.py", line 8, in <module>
> /usr/lib/python3.9/codecs.py(309)__init__()
-> def __init__(self, errors='strict'):
(Pdb) 
"""









