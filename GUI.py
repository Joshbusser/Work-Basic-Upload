#!/usr/bin/env python
# coding: utf-8

# In[156]:


from tkinter import *
import os
import sys


# In[157]:


root = Tk()
root.title("Hello Josh")


# In[158]:


# theLabel = Label(root, text="This is too easy")


# In[159]:


# theLabel.pack()


# In[160]:


topFrame = Frame(root)


# In[161]:


topFrame.pack()


# In[162]:


bottomFrame = Frame(root)


# In[163]:


bottomFrame.pack(side=BOTTOM)


# In[164]:


def RunFunction():
    os.system('python Runme.py')
def Upload_Path():
    os.system('python Upload_Path.py')
def Upload_Path1():
    os.system('python Upload_Path_CO.py')
def Upload_Path2():
    os.system('python Upload_Path_CA.py')
def Upload_Path3():
    os.system('python Upload_Path_NM.py')
def Clear():
    os.system('python Clear_Folder.py')


# In[165]:


button1 = Button(topFrame, text="Run Me", fg="purple", command= RunFunction, height = 5, width = 40, font= 30, background = "white")
button2 = Button(topFrame, text="Move to Upload AZ", fg="red", command= Upload_Path, height = 5, width = 40, font= 30, background = "white")
button3 = Button(topFrame, text="Move to Upload CO", fg="blue", command= Upload_Path1, height = 5, width = 40, font= 30, background = "white")
button4 = Button(topFrame, text="Move to Upload CA", fg="green", command= Upload_Path2, height = 5, width = 40, font= 30, background = "white")
button5 = Button(topFrame, text="Move to Upload NM", fg="orange", command= Upload_Path3, height = 5, width = 40, font= 30, background = "white")
button6 = Button(topFrame, text="Clear folders", fg="pink", command= Clear, height = 5, width = 40, font= 30, background = "white")


# In[166]:


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()


# In[167]:


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




