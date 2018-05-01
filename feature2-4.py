import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns

survey = pd.read_csv('HackerRank-Developer-Survey-2018-Values.csv', low_memory=False)

# Select a subset that only includes student responses
survey = survey[survey['q8Student'] == 'Students']

print("Total number of students surveyed:",len(survey))

# Select a subset of students from the United States only
survey = survey[survey['CountryNumeric2'] == 'United States']


res=survey['q27EmergingTechSkill'].value_counts()

figure = pyplot.figure(figsize=(16,10))
sns.barplot(x=res.values,y=res.index,palette='Wistia')
for i,v in enumerate(res.values):
    pyplot.text(10,i,v,fontsize=20,va='center')
pyplot.xlabel('Count',fontsize=12)
pyplot.title('Emerging Technology')
pyplot.show()


survey['q13EmpMeasOtherCodingChallenge'].value_counts()
cols = survey.columns[survey.columns.str.startswith('q13')]
interview =pd.DataFrame()

for i in cols:
    content = survey[i].value_counts().reset_index(name='count')
    interview = pd.concat([interview,content])

interview.sort_values(by='count',ascending=False,inplace=True)

pyplot.figure(figsize=(16,10))
sns.barplot(interview['count'],interview['index'],palette='terrain')
for i,v in enumerate(interview['count']):
    pyplot.text(10,i,v,fontsize=12,va='center')
    
pyplot.xlabel('Count')
pyplot.ylabel('')
pyplot.title('Interview content')
pyplot.show()


cols = survey.columns[survey.columns.str.startswith('q25')]
List = []
for i in cols:
	list = []
	count = survey[i].count()
	list.append(i[7:])
	list.append(count)
	List.append(list)


language = pd.DataFrame(data = List, columns = ['index','count'])

language.sort_values(by='count',ascending=False,inplace=True)

pyplot.figure(figsize=(16,10))
sns.barplot(language['count'],language['index'],palette='terrain')
for i,v in enumerate(language['count']):
    pyplot.text(10,i,v,fontsize=12,va='center')
    
pyplot.xlabel('Count')
pyplot.ylabel('Language')
pyplot.title('Language Prefer')
pyplot.show()


