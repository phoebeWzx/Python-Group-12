import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

__author__ = "Chloe Kim (minkyun3) and Phoebe Wu (zhuoxuew)"
__email__ = "minkyun3@andrew.cmu.edu | zhuoxuew@andrew.cmu.edu"
__copyright__ = "Copyright 2018, The Job Seekers"
__license__ = "GPL"
__version__ = "1.0.1"

"""
This application is to guide developers to grow up as a good engineer.
You can see our project here: https://github.com/phoebeWzx/Python-Group-12
"""

survey = pd.read_csv('input/HackerRank-Developer-Survey-2018-Values.csv', low_memory=False)
survey_codebook = pd.read_csv('input/HackerRank-Developer-Survey-2018-Codebook.csv')
survey_codebook = survey_codebook.set_index('Data Field')

print("Processing...")

# Show the total number of responses
survey.dropna(axis=0,how='all',inplace=True)
print("\nWe have ",survey.shape," responses in total.")

# Show the Age Distribution
print("\n# Age Distribution")
count = survey['q2Age'].value_counts()
print(count)
plt.figure(figsize=(12,5))
sns.barplot(count.values,count.index,palette='pink')
for i,v in enumerate(count.values):
    plt.text(0.8,i,v,color='k',fontsize=12)
    
plt.title('Age Distribution')
plt.show()

# Show the Age Begin Coding
print("\n# Distribution of Age begin coding")
count = survey['q1AgeBeginCoding'].value_counts()
print(count)
plt.figure(figsize=(10,6))
sns.barplot(count.values,count.index,palette='terrain')
for i,v in enumerate(count.values):
    plt.text(0.8,i,v,color='k',fontsize=12,va='center')

plt.title('Distribution of Age begin coding')
plt.xlabel('count')
plt.show()

# Show the highest education distribution
print("\n# Distribution of Highest education level")
count = survey['q4Education'].value_counts()
print(count)
plt.figure(figsize=(16,4))
sns.barplot(count.values,count.index,palette='coolwarm')
for i,v in enumerate(count):
    plt.text(1,i,v,fontsize=12,va='center')
plt.xlabel('count')
plt.title('Distribution of Highest education level')
plt.show()

# Show the current employment level
print("\n# Distribution of Current employment level")
count = survey['q8JobLevel'].value_counts()
print(count)
sns.barplot(x=count.values,y=count.index,palette='cool')
for i,v in enumerate(count.values):
    plt.text(1,i,v,fontsize=12,va='center')
plt.title('Distribution of Current employment level')
plt.show()  

"""
# Show current role at job
f, ax = plt.subplots(1,2,figsize=(16,10))
rolecount = survey['q9CurrentRole'].value_counts()
sns.barplot(rolecount.values,rolecount.index,palette='hsv',ax=ax[0],)
ax[0].set_title('Current Job Role')
ax[0].set_xlabel('count')
for i,v in enumerate(rolecount.values):
    ax[0].text(10,i,v,fontsize='12',va='center')
    
agg = survey.groupby(['q9CurrentRole','q3Gender'])['q3Gender'].count().reset_index(name='count')
agg = agg.pivot(columns='q3Gender',index='q9CurrentRole',values='count')
sns.heatmap(agg,cmap='Pastel1',annot=True,fmt='.0f',ax=ax[1])
ax[1].set_title('Current role grouped be gender')
ax[1].set_xlabel('Gender')
ax[1].set_ylabel('Current role')
plt.subplots_adjust(wspace=0.7)

# Current industry distribution
f,ax = plt.subplots(1,2,figsize=(16,10))
industry =  survey['q10Industry'].value_counts()
sns.barplot(industry.values,industry.index,ax=ax[0],palette='Pastel1')
for i,v in enumerate(industry.values):
    ax[0].text(10,i,v,fontsize=12,va='center')
ax[0].set_title('Industry distribution')
ax[0].set_xlabel('count')

agg = survey.groupby(['q10Industry','q3Gender'])['q3Gender'].count().reset_index(name='count')
agg =agg.pivot(columns='q3Gender',index='q10Industry',values='count')
sns.heatmap(agg,cmap='Pastel2',ax=ax[1],fmt='.0f',annot=True)
ax[1].set_title('Industry Distribution grouped by gender')
ax[1].set_xlabel('Gender')
ax[1].set_ylabel('Industry')
plt.subplots_adjust(wspace=0.8)

# How employer measure skills

cols = survey.columns[survey.columns.str.startswith('q13')]
#cols
skills = pd.DataFrame()

for i in cols:
    agg = survey[i].value_counts().reset_index(name='count')    
    skills = pd.concat([skills,agg])
    
#print(skills)
skills.sort_values(by='count',ascending=False,inplace=True)

plt.figure(figsize=(16,6))
sns.barplot(skills['count'],skills['index'],palette='spring')

for i,v in enumerate(skills['count']):
    plt.text(1,i,v,fontsize=20,verticalalignment='center')
                     
plt.title('Employers top most ways of mesuring skills')
plt.xlabel('Count')
plt.show()

# Qualification required for the onsite
cols = survey.columns[survey.columns.str.startswith('q20')]
#cols

qual = pd.DataFrame()
for i in cols:
    agg = survey[i].value_counts().reset_index(name='count')
    qual=pd.concat([qual,agg])

qual.sort_values(by='count',ascending=False,inplace=True)
qual

plt.figure(figsize=(16,10))
sns.barplot(qual['count'],qual['index'],palette='hsv')
for i,v in enumerate(qual['count']):
    plt.text(0.5,i,v,fontsize=20,verticalalignment='center')
plt.xlabel('count')
plt.title('Qualifications required for the onsite')
plt.show()

# What Recruiters look for in Software developers
col1 = survey.columns[survey.columns.str.startswith('q21')]
col2 = survey.columns[survey.columns.str.startswith('q22')]
skills = pd.DataFrame()
col1

for i in col1:
    agg = survey[i].value_counts().reset_index(name='count')
    skills = pd.concat([skills,agg],axis=0,ignore_index=True)

lang = pd.DataFrame()
for i in col2:
    agg2 = survey[i].value_counts().reset_index(name='count')
    lang = pd.concat([lang,agg2])
    
lang.sort_values(by='count',ascending=False,inplace=True)

skills.loc[len(skills)]=['Language Proficiency',lang['count'].sum()]
skills.sort_values(by='count',ascending=False,inplace=True)
#skills

f,ax =plt.subplots(1,2,figsize=(15,10))
sns.barplot(skills['count'], skills['index'], palette='GnBu',ax=ax[0])
for i,v in enumerate(skills['count']):
    ax[0].text(100,i,v,fontsize=18,verticalalignment='center')
ax[0].set_xlabel('Count')
ax[0].set_ylabel('Skills')
ax[0].set_title('Desired Skill required')

sns.barplot(lang['count'],lang['index'],palette='YlGn',ax=ax[1])
for i,v in enumerate(lang['count']):
    ax[1].text(100,i,v,fontsize=12)
ax[1].set_xlabel("Count")
ax[1].set_ylabel('Languages')
ax[1].set_title('Language Proficiency')
plt.subplots_adjust(wspace=0.5)
plt.show()

# Which Languages do developers know and will learn?
cols= survey.columns[survey.columns.str.startswith('q25')]
cols = cols.drop('q25LangOther')

f,ax = plt.subplots(4,6,figsize=(16,25))
axs=ax.ravel()

for i,c in enumerate(cols):
    sns.countplot(survey[c],ax=axs[i],palette='pink')
    axs[i].set_ylabel('')
    axs[i].set_xlabel('')
    axs[i].set_title(survey_codebook.loc[c]['Survey Question'])

plt.subplots_adjust(hspace=0.5,wspace=0.5)
plt.suptitle('Programming language know or will learn',fontsize=14)
plt.show()

# Which emerging tech skill are you currently learning or looking to learn in the next year??
res=survey['q27EmergingTechSkill'].value_counts()

fig = plt.figure(figsize=(16,10))
sns.barplot(x=res.values,y=res.index,palette='Wistia')
for i,v in enumerate(res.values):
    plt.text(10,i,v,fontsize=20,va='center')
plt.xlabel('Count',fontsize=12)
plt.title('Emerging Technology')
plt.show()

# Learning Source
cols = survey.columns[survey.columns.str.startswith('q30')]
learn =pd.DataFrame()

for i in cols:
    agg = survey[i].value_counts().reset_index(name='count')
    learn = pd.concat([learn,agg])

learn.sort_values(by='count',ascending=False,inplace=True)
#print(learn)

plt.figure(figsize=(16,10))
sns.barplot(learn['count'],learn['index'],palette='cool')
for i,v in enumerate(learn['count']):
    plt.text(10,i,v,fontsize=12,va='center')
    
plt.xlabel('Count')
plt.ylabel('')
plt.title('Source of learning')
plt.show()
"""