import numpy as np
import random

for i in range(10):
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    ans =  input('"%s"+"%s"=' %(x,y))
    print(1.0*x+1.0*y)
    ans =  input('"%s"x"%s"=' %(x,y))
    print(1.0*x*1.0*y)
    ans =  input('"%s"-"%s"=' %(x,y))
    print(1.0*x-1.0*y)
    ans =  input('"%s":"%s"=' %(x,y))
    print(1.0*x/1.0*y)

