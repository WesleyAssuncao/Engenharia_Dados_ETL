#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from pathlib import Path
filename = r'Teste.xlsx' 
filename = Path(filename)


# In[2]:


base = pd.read_excel(filename)


# In[3]:


base.style


# In[5]:


import matplotlib.pyplot as plt 


# In[6]:


plt.plot(base["Qtd Acessada"])
plt.show()


# In[11]:


plt.hist(base["Qtd Acessada"], bins=10)
plt.show()


# In[15]:





# In[63]:


# Lendo os dados de um Excel

import pandas as pd 
from pathlib import Path
filename = r'Dados.xlsx' 
filename = Path(filename)

base = pd.read_excel(filename)
base.style


# In[64]:


# Gerando gráfico de Barras 

grupos = (base["Modulo"])
valores = (base["Qtd Acessada"])
plt.bar(grupos, valores, color='#FF4500')


# Colocando Legenda, Título
plt.title("Telas mais Acessadas")
plt.show()


# In[55]:


# Gráfico de Pizza 

plt.pie(base["Qtd Acessada"], labels=base["Modulo"], autopct="%1.0f%%")
plt.show()


# In[62]:


# Customizando Gráfico de Pizza 

explode = (0.1, 0, 0, 0)
plt.pie(base["Qtd Acessada"], labels=base["Modulo"], autopct="%1.0f%%", shadow=True, explode=explode)
plt.legend(labels=base["Modulo"], loc=2)
plt.axis('equal')
plt.title("Telas mais Acessadas")
plt.show()


# In[ ]:




