#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import glob
import os
import shutil


# In[5]:


source = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/Result/"
dest1 = "//Data/crossdata_prod/apps/PAPricing/CA/"


# In[6]:


files = os.listdir(source)

for f in files:
        shutil.move(source + f, dest1)


# In[ ]:




