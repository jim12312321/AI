
# coding: utf-8

# In[3]:


from functions import func


# In[4]:


f = open('input.txt','r')
x,y = [],[]
for i in range(2):
    sentence = f.readline()
    if(i==0):
        x=sentence.strip().split(',')
    else:
        y = sentence.strip().split(',')
    


# In[5]:


#暴力法
min_num,min_x,min_y = 10000,10000,10000
for i in range(int(x[0]),int(x[1])+1,1):
    for j in range(int(y[0]),int(y[1]),1):
        if(float(func(float(i),float(j))) < min_num):
            min_num = float(func(float(i),float(j)))
            min_x = i
            min_y = j


# In[6]:


print(min_x)
print(min_y)
print('%.3f'%min_num)


# In[21]:


#模擬退火法
import random
from math import exp
min_t = 0.1 #end temp
t = 1000 # init temp
L = 40 # re
r = 0.95 # de
x_now,y_now = random.randint(int(x[0]),int(x[1])),random.randint(int(y[0]),int(y[1]))
while(t > min_t):
    for k in range(L):
        x_next,y_next = random.randint(int(x[0]),int(x[1])),random.randint(int(y[0]),int(y[1]))
        delta = func(x_next,y_next) - func(x_now,y_now)
        if(delta < 0):
            x_now,y_now = x_next,y_next
        else:
            if(exp(-delta/t) > random.random()):
                x_now,y_now = x_next,y_next
    t *= r   


# In[22]:


print(x_now)
print(y_now)
print('%.3f'%func(x_now,y_now))

