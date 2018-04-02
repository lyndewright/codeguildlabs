#version 2

import random

eyes = [':' ,';' , '8']
nose = ['>' , '0' , '.']
mouth = [')' ,'(' ,'P']

while True:
    for i in range(5):
        print(random.choice(eyes), random.choice(nose),random.choice(mouth))
    quit()
