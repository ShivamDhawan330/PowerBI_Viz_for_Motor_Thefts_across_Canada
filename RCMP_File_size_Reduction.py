#!/usr/bin/env python
# coding: utf-8

# ### Reducing File Size of RCMP Dataset

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


df=pd.read_csv(r'C:\35100184.csv',
              dtype={'REF_DATE': np.int32,
                     'GEO': str,
                     'DGUID': str,
                     'Violations': str,
                     'Statistics': str,
                     'UOM': str,
                     'UOM_ID': np.int32,
                     'SCALAR_FACTOR': str,
                     'SCALAR_ID': np.int32,
                     'VECTOR': str,
                     'COORDINATE': str,
                     'VALUE': np.float64,
                     'STATUS': str,
                     'SYMBOL': str,
                     'TERMINATED': str,
                     'DECIMALS': np.int32}
              )


# In[ ]:


df2 = df.query('REF_DATE>=2011 & VALUE > 0 & Statistics != "Cleared by charge" & Statistics != "Cleared otherwise" & Statistics != "Total cleared" & Statistics != "Cleared otherwise" & Statistics != "Unfounded incidents" & Statistics != "Percent unfounded" & Statistics != "Total, youth not charged" & Statistics != "Rate, youth not charged per 100,000 population aged 12 to 17 years" & Statistics != "Percentage change in rate"')


# In[ ]:


df2[["REF_DATE","GEO", "Violations", "Statistics", "UOM", "VALUE"]].to_csv('35100184-Reduced.csv', index=False, encoding='utf-8')


# In[ ]:





# In[ ]:





# In[ ]:




