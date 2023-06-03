#!/usr/bin/env python
# coding: utf-8
Python Working Directory and File Paths
# In[20]:


# Load in some packages
get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import os 


# In[21]:


os.getcwd() #get your current Directory


# In[22]:


os.chdir('D:\Titanic analysis') # change your current Directory


# In[23]:


os.getcwd()


# In[24]:


os.listdir('D:\Titanic analysis')


# In[25]:


#Read the data 
Titanic_train = pd.read_csv(r'D:\Titanic analysis\titanic.csv')


# In[26]:


Titanic_train.head(6)


# In[29]:


#read excel file
draft = pd.read_excel("D:\data analysis\sqlexceltableau\Bicycle team.xlsx")
#draft = pd.read_excel("D:\sqlexceltableau\Bicycle team.xlsx",
                        #sheet_name = 'Bike')
draft.head(6)


# In[30]:


#Writing Data excel to csv
draft.to_csv("draft_saved.csv")


# In[31]:


os.getcwd()


# In[32]:


os.listdir('D:\\Titanic analysis')


# In[33]:


Titanic_train.shape


# In[34]:


Titanic_train.info()


# In[35]:


Titanic_train.head(10)


# In[36]:


#Distribution of numerical columns summary statistics
Titanic_train.describe()


# In[39]:


#Summary the categorical variables 
categorical = Titanic_train.dtypes[Titanic_train.dtypes == "object"].index
print(categorical)


# In[40]:


Titanic_train[categorical].describe()

VARIABLE DESCRIPTIONS:

Pclass    Passenger Class
             (1 = 1st ; 2 = 2nd; 3 = 3rd)
survival  Survival (0 = No; 1 = Yes)
name      Name
sex       Sex
age       Age
sibsp     Number of Siblings/Spouses Aboard
parch     Number of Parents/Children Aboard
ticket    Ticket Number
fare      Passenger Fare (British pound)
cabin     Cabin
embarked  Port of Embarkation 
          (C = Cherbourg; Q = Queenstown; S = Southampton)
Questions to ask:
Do i need all the variables?
Should i transform any variables?
Are there NA values, outliers or other strange values?
Should i create new variables?
Do i need all the variables
# In[41]:


#Go through each variable and consider whether we should keep it or not in the context of prediction survival:
del Titanic_train["PassengerId"] #Remove PassengerId


# In[42]:


sorted(Titanic_train["Name"])[0:15]


# In[43]:


Titanic_train["Name"].describe()


# In[44]:


del Titanic_train["Ticket"] #remove Ticket

Should i transform any variables?
# In[46]:


#Survived 0 and 1 to Died or Survived
new_survived = pd.Categorical(Titanic_train["Survived"])
new_survived = new_survived.rename_categories(["Died", "Survived"])

new_survived.describe()


# In[48]:


#Pclass 1, 2 ,3...
new_Pclass = pd.Categorical(Titanic_train["Pclass"],
                            ordered=True)

new_Pclass = new_Pclass.rename_categories(["Class1","Class2","Class3"])
new_Pclass.describe()


# In[49]:


Titanic_train["Pclass"] = new_Pclass


# In[51]:


Titanic_train["Cabin"].unique()


# In[56]:


#group cabin by letter 

char_cabin = Titanic_train["Cabin"].astype(str) #Convert data to str
new_Cabin = np.array([cabin[0] for cabin in char_cabin]) #take first letter
new_Cabin = pd.Categorical(new_Cabin)
new_Cabin.describe()


# In[57]:


Titanic_train["Cabin"] = new_Cabin

Are there NA values, outliers or other strange values?
# In[61]:


#get indexis of missing value for Age
missing = np.where(Titanic_train["Age"].isnull() == True)
missing


# In[63]:


#Creating a histogram of the age column to get sense of the distribution of ages

Titanic_train.hist(column='Age',
                   figsize=(9,6),
                   bins=20)


# In[64]:


new_age_var = np.where(Titanic_train["Age"].isnull(), #Logical check
                       28,                            #Value if check is true
                       Titanic_train["Age"])          #Value if check is false

Titanic_train["Age"] = new_age_var


# In[65]:


Titanic_train["Age"].describe()


# In[66]:


Titanic_train.hist(column = 'Age',#Column to plot 
                   figsize=(9,6), #Plot size
                   bins=20)       #Number of histogram bins


# In[68]:


#create new variable:
Titanic_train["Family"] = Titanic_train["SibSp"] + Titanic_train["Parch"]


# In[70]:


#Check who had the most family members on board
most_family = np.where(Titanic_train["Family"] == max(Titanic_train["Family"]))

Titanic_train.loc[most_family]


# In[ ]:





# In[ ]:





# In[ ]:




