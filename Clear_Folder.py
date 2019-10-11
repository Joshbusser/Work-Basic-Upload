#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import glob
import os
import shutil


# In[ ]:


source = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/Result/"
dest1 = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/Done/"


# In[ ]:


files = os.listdir(source)

for f in files:
        shutil.move(source + f, dest1)


# In[ ]:


source = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/PA Add On/"
dest1 = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/Done/"


# In[ ]:


files = os.listdir(source)

for f in files:
        shutil.move(source + f, dest1)

