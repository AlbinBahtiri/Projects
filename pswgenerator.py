

import random

password_length=10
char="abcdeFGHJKL12345!@#@#$%"
password=""
for i in range(password_length):
    password=password+random.choice(char)
print(password)





