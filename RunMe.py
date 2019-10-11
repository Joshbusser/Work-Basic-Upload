#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import glob
import os
import shutil


# In[81]:


path = r'C:/Users/Jbusse/Documents/Python Work/PA Add on JB/PA Add On' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)



PA_add_df = frame


# In[82]:


PA_add_df.head(2)


# In[83]:





sent_info_df = PA_add_df[['PA #','Product Code',' Cost Basis ','Cost','Mark Up ','START DATE','Expire',"BILLBACK"]]

sent_info_df.head()


# In[84]:



value_df = sent_info_df[np.isfinite(PA_add_df['PA #'])]

value_df[' Cost Basis '] = value_df[' Cost Basis '].replace([' INVOICE '], 'FIXED')
value_df[' Cost Basis '] = value_df[' Cost Basis '].replace([' BPL 20 ',' BPL 184 ',' BPL 11 '], 'BPL')
value_df[' Cost Basis '] = value_df[' Cost Basis '].replace([' VRBT '], 'FIXED')

value_df


# In[85]:


value_df['BILLBACK'] = value_df['BILLBACK'].fillna(0)




# In[86]:


value_df['BILLBACK'] = value_df['BILLBACK'].replace('[\$,]','',regex=True).astype(float)

z = value_df['BILLBACK']

value_df['PriceAdjCode1 [10]'] = np.where(z>0, 'VRBT', 'MUP')
value_df["PriceAdjCalc1 [5]"] =  np.where(z>0, 'Amt', 'Amt')
value_df["PriceAdjValue1 [#.#]"] = np.where(z>0, z, value_df['Mark Up '] )
value_df["PriceAdjBasis1[20]"] = np.where(z>0, 'Per Price UOM', 'Per Price UOM' )
value_df["PriceAdjAddorStack1 [10]"] =  np.where(z>0, 'Stacked', 'Stacked')
value_df["PriceAdjType1 [10]"] =  np.where(z>0, 'Charge', '')

value_df['PriceAdjCode2 [10]'] = np.where(z>0, 'MUP', '')
value_df['PriceAdjType1 [10]'] = np.where(z>0, 'Discount', 'Charge')
value_df['PriceAdjType2[10]'] = np.where(z>0, 'Charge', '')
value_df["PriceAdjCalc2 [5]"] =  np.where(z>0, 'Amt', '')
value_df["PriceAdjAddorStack2 [10]"] =  np.where(z>0, 'Stacked', '')
value_df["PriceAdjBasis2[20]"] =  np.where(z>0, 'Per Price UOM', '')
value_df["PriceAdjValue1 [#.#]"] = np.where(z>0, z, value_df['Mark Up '] )
value_df["PriceAdjValue2 [#.#]"] = np.where(z>0, value_df['Mark Up '], '')
value_df["PriceAdjustmentSeq2 [11]"] = ""
value_df


# In[87]:


x = value_df[' Cost Basis ']
value_df["BPL[10]"] = np.where(x.str.contains('BPL'), '20', '')
value_df["BPL[10]"] = np.where(x.str.contains('FIXED'), '20', '')

value_df["CreateDate"] = ""
value_df["Label[5]"] = ""
value_df["ProductDescription [60]"] = ""
value_df["MfgID[20]"] = ""
value_df["Status[10]"] = ""
value_df["ProductUom [2]"] = ""
value_df["Vendor [10]"] = ""
value_df["CS/LB"] = "CS"
value_df["Vendor [10]"] = ""
value_df["FreightOverride [#.#]"] = ""
value_df["FixedBasePricePrintInd [#]"] = "Monthly"
value_df["PriceAdjustmentSeq1 [11]"] = ""


value_df["PriceAdjustmentSeq2 [11]"] = ""


print(value_df["BPL[10]"])


# In[88]:


value_df


# In[89]:


df_2 = value_df.rename(columns={"PA #": "PA [10]",
                                "Product Code":"ProductID [20]", 
                                "START DATE":"EffectiveDate", 
                                "Expire":"InactiveDate",
                                " Cost Basis ":"PricingMethod[10]", 
                                "Cost":"FixedCost[#.#]"})


# In[90]:


df_2


# In[91]:


Upload_df = df_2[['PA [10]',
                  'CreateDate',
                  'EffectiveDate',
                  'InactiveDate',
                  'ProductID [20]',
                  'CS/LB','Label[5]',
                  'ProductDescription [60]',
                  'MfgID[20]','Status[10]',
                  'ProductUom [2]',
                  'PricingMethod[10]',
                  'BPL[10]',
                  'FixedCost[#.#]',
                  'FreightOverride [#.#]',
                  'FixedBasePricePrintInd [#]',
                  'Vendor [10]',
                  'PriceAdjCode1 [10]',
                  'PriceAdjCalc1 [5]',
                  'PriceAdjValue1 [#.#]',
                  'PriceAdjBasis1[20]',
                  'PriceAdjustmentSeq1 [11]',
                  'PriceAdjAddorStack1 [10]',
                  'PriceAdjType1 [10]',
                  'PriceAdjCode2 [10]' ,
                  'PriceAdjCalc2 [5]' ,
                  'PriceAdjValue2 [#.#]',
                  'PriceAdjBasis2[20]' ,
                  'PriceAdjustmentSeq2 [11]' ,
                  'PriceAdjAddorStack2 [10]' ,
                  'PriceAdjType2[10]']]
Upload_df


# In[ ]:





# In[92]:


Upload_df.to_csv("C:/Users/Jbusse/Documents/Python Work/PA Add on JB/Result/Upload_Temp_JB_12.csv", index =False)


# In[13]:


source = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/PA Add On/"
dest1 = "C:/Users/Jbusse/Documents/Python Work/PA Add on JB/Done/"


# In[14]:


files = os.listdir(source)

for f in files:
        shutil.move(source + f, dest1)


# In[ ]:





# In[ ]:




