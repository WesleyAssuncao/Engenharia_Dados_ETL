#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Importando as blibliotecas
import pandas as pd 
from pathlib import Path
filename = r'COTAHIST_A2020.TXT'
filename = Path(filename)


# In[8]:


# Importando os dados - Arquivo posicional usar o metódo de read FTWF
# Esse metódo recebe alguns parâmetros (Nome arquivo; Posições das colunas; Nome das colunas)


#Criando uma lista e armazendo as posições das colunas e nome das colunas
colspecs = [(2,10),
            (10,12),
            (12,24),
            (27,39),
            (56,69),
            (69,82),
            (82,95),
            (108,121), 
            (152,170), 
            (170,188)
]

names = ['data_pregao', 'codbdi', 'sigla_acao','nome_acao', 'preco_abertura', 'preco_maximo',
         'preco_minimo','preco_fechamento', 'qtd_negocios', 'volume_negocios']

# Criando o Data Frame 
df = pd.read_fwf(filename, colspecs = colspecs, names = names, skiprows =1)
df


# In[19]:


# 1° Transformação: Filtrando o Lote padrão igual a 2 e tirando o camó codbdi
df = df [df['codbdi']== 2]
df = df.drop(['codbdi'], 1)
df


# In[20]:


# 2° Transformação: Ajuste campo de data 
df['data_pregao'] = pd.to_datetime(df['data_pregao'], format ='%Y%m%d')
df                                    
                                 


# In[21]:


# 3° Transformação: Ajuste dos campos númericos  

df['preco_abertura'] = (df['preco_abertura'] /100).astype(float)
df['preco_maximo'] = (df['preco_maximo'] /100).astype(float)                                                          
df['preco_minimo'] = (df['preco_minimo'] /100).astype(float)                                                         
df['preco_fechamento'] = (df['preco_fechamento'] /100).astype(float)   
df
                                                          
                                                          
                                                          


# In[10]:


df.dtypes


# In[11]:


# 4° Transformação: Ajuste dos campos para o tipo inteiro

df['qtd_negocios'] = (df['qtd_negocios'] /100).astype(int)                                                         
df['volume_negocios'] = (df['volume_negocios'] /100).astype(int)   
df
                


# In[12]:


df.dtypes


# In[17]:


# Salvando os dados em Excel

write = pd.ExcelWriter('C:/Users/wesle/Documents/Python Scripts/Engenharia_Dados/saida.xlsx')
df.to_excel(write, 'dados', index=False)
write.save()


# In[ ]:




