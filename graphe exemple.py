
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt


# graphe nombre de jours survecu en fonction de la capadap 

# In[12]:

name = ['entre 0 et 2', 'entre 2 et 4', 'entre 4 et 6', 'entre 6 et 8']
data = [25, 25, 25, 25]

explode=(0.02, 0.02, 0.02, 0.02)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=False)
plt.axis('equal')
plt.title("nombre de jours survécu avec une capadap de 0.25")
plt.show()


# In[15]:

name = ['entre 0 et 2', 'entre 2 et 4', 'entre 4 et 6', 'entre 6 et 8']
data = [25, 25, 25, 25]

explode=(0.02, 0.02, 0.02, 0.02)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=False)
plt.axis('equal')
plt.title("nombre de jours survécu avec une capadap de 0.5")
plt.show()


# In[17]:

name = ['entre 0 et 2', 'entre 2 et 4', 'entre 4 et 6', 'entre 6 et 8']
data = [25, 25, 25, 25]

explode=(0.02, 0.02, 0.02, 0.02)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=False)
plt.axis('equal')
plt.title("nombre de jours survécu avec une capadap de 0.75")
plt.show()

graphe indicateur  en fonction du jour
# In[ ]:




# In[61]:

plt.grid(True)
plt.plot([0,2,4,6,8,10,12,14,16,18,20], [1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0,0,0],"b--", linewidth=2,)
plt.plot([0,2,4,6,8,10,12,14,16,18,20], [1,1,1,1,1,1,1,1,1,1,1],"g--", linewidth=2)
plt.xlabel('Jours')
plt.annotate('mort', xy=(16,0), xytext=(18, 0.2), 
arrowprops={'facecolor':'yellow', 'shrink':-0.02} )
#plt.ylabel('Sante')
plt.axis([0, 20, 0, 2])
plt.show()


# In[ ]:




# In[ ]:



