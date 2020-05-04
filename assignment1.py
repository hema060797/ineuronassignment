#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('succesfuuly installed')


# In[4]:


nl=[]

for i in range(2000,3200):
    if(i%7==0)and(i%5!=0):
        nl.append(str(i))
print (','.join(nl))


# In[5]:


firstname=input('enter your first name')
lastname=input('enter your last name')
print (lastname + " " + firstname)




# In[1]:


import math
pi = math.pi
#Converting Diameter into radius

r = float(12/2)
V = (float(4/3)*(pi)*(r)**3)
print(V)

#or
import math
pi = math.pi
#Converting Diameter into radius

r = float(12)
V = (float(4/3)*(pi)*(r)**3)
print(V)


# In[ ]:





# In[8]:


values = input('Input some comma seprated numbers :')
list = values.split(",")
print('List : ',list)


# In[38]:



def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end="")
           print("\r")
      for i in range(n, 0 , -1):
          for j in range(0, i - 1):
               print("* ", end="")
          print("\r")
 
pattern(5)


# In[10]:


word=input('enter the word that you want to reverse:')
print(word[::-1])


# In[11]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:





# In[ ]:





# In[ ]:




