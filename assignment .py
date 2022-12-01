#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().set_next_input('1. Write a Python Program to Find LCM');get_ipython().run_line_magic('pinfo', 'LCM')


# In[16]:


def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to Find HCF');get_ipython().run_line_magic('pinfo', 'HCF')


# In[2]:


def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal');get_ipython().run_line_magic('pinfo', 'Hexadecimal')


# In[15]:



dec = 34

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program To Find ASCII value of a character');get_ipython().run_line_magic('pinfo', 'character')


# In[19]:


c = 'r'
print("The ASCII value of '" + c + "' is", ord(c))


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations');get_ipython().run_line_magic('pinfo', 'operations')


# In[ ]:



def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
    
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

