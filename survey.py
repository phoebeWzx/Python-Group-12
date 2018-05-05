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

Those are the main features of this application.
Feature 1 - Distribution of Developers in Education & Learning Source
Feature 2 - Distribution of Developers in Employment (Job) and Role (Position)
Feature 3 - Emerging tech skills
Feature 4 - Popular Programming Language
Feature 5 - How does employers measure you?

You can see our project here: https://github.com/phoebeWzx/Python-Group-12
"""
def execute(menu, survey, survey_codebook):
    """ Execute the menu the user chose in the main

    Arguments:
        menu {String} - a number to see the data
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    if (menu == '1'):
        showInfo1(survey, survey_codebook)
    elif (menu == '2'):
        showInfo2(survey, survey_codebook)
    elif (menu == '3'):
        showInfo3(survey, survey_codebook)
    elif (menu == '4'):
        showInfo4(survey, survey_codebook)
    elif (menu == '5'):
        showInfo5(survey, survey_codebook)
    else:
        exit()

def showInfo1(survey, survey_codebook):
    """ Feature 1 - Distribution of Developers in Education
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print('\n1. Distribution of Highest education level')
    education = survey['q4Education'].value_counts()
    print(education) # Print text data

    plt.figure(figsize=(16,4))
    sns.barplot(education.values,education.index,palette='BuPu')
    for i,v in enumerate(education):
        plt.text(1,i,v,fontsize=12,va='center')
    plt.xlabel('count')
    plt.title('Distribution of Highest education level')
    plt.show() # Show the visualized data

    # We also offer free resources to learn to help developers
    additional = input('Do you want to see popular learning sources? (y/n): ')
    if (additional == 'y'):
        showAdditionalInfo1(survey, survey_codebook)
        return
    else:
        return

def showAdditionalInfo1(survey, survey_codebook):
    """ Additional Data for Feature 1 - Popular Free Learning Sources
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print("\n# Popular learning sources")
    cols = survey.columns[survey.columns.str.startswith('q30')]
    learn = pd.DataFrame()

    for i in cols:
        agg = survey[i].value_counts().reset_index(name='count')
        learn = pd.concat([learn,agg])

    learn.sort_values(by='count',ascending=False,inplace=True)
    print(learn) # Print text data

    plt.figure(figsize=(16,10))
    sns.barplot(learn['count'],learn['index'],palette='BuPu')
    for i,v in enumerate(learn['count']):
        plt.text(10,i,v,fontsize=12,va='center')
    plt.xlabel('Count')
    plt.ylabel('')
    plt.title('Source of learning')
    plt.show() # Show the visualized data
    return

def showInfo2(survey, survey_codebook):
    """ Feature 2 - Distribution of Developers in Employment
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print("\n# Distribution of current job")
    job = survey['q8JobLevel'].value_counts()
    print(job) # Print text data

    sns.barplot(x=job.values,y=job.index,palette='BuPu')
    for i,v in enumerate(job.values):
        plt.text(1,i,v,fontsize=12,va='center')
    plt.title('Distribution of current job')
    plt.show() # Show the visualized data

    # We also offer free resources to learn to help developers
    additional = input('Do you want to see distribution of position as well? (y/n): ')
    if (additional == 'y'):
        showAdditionalInfo2(survey, survey_codebook)
        return
    else:
        return

def showAdditionalInfo2(survey, survey_codebook):
    """ Additional Data for Feature 2 - Popular Free Learning Sources
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print("\n# Distribution of current position")
    f, ax = plt.subplots(1,2,figsize=(16,10))
    rolecount = survey['q9CurrentRole'].value_counts()
    print(rolecount) # Print text data
    # Show the visualized data
    sns.barplot(rolecount.values,rolecount.index,palette='BuPu',ax=ax[0],)
    ax[0].set_title('Distribution of current position')
    ax[0].set_xlabel('count')
    for i,v in enumerate(rolecount.values):
        ax[0].text(10,i,v,fontsize='12',va='center')
    return


def showInfo3(survey, survey_codebook):
    """ Feature 3 - Emerging tech skills
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print("\n# Popular emerging technologies")
    survey = survey[survey['CountryNumeric2'] == 'United States']
    tech = survey['q27EmergingTechSkill'].value_counts()
    print(tech) # Print text data

    figure = plt.figure(figsize=(16,10))
    sns.barplot(x=tech.values,y=tech.index,palette='BuPu')
    for i,v in enumerate(tech.values):
        plt.text(10,i,v,fontsize=20,va='center')
    plt.xlabel('Count',fontsize=12)
    plt.title('Emerging Technologies')
    plt.show() # Show the visualized data

def showInfo4(survey, survey_codebook):
    """ Feature 4 - Popular Programming Language
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print("\n# Popular programming languages from employers")
    cols = survey.columns[survey.columns.str.startswith('q25')]
    List = []
    for i in cols:
        list = []
        count = survey[i].count()
        list.append(i[7:])
        list.append(count)
        List.append(list)
    language = pd.DataFrame(data = List, columns = ['index','count'])
    language.sort_values(by='count',ascending=False)
    print(language) # Print text data

    plt.figure(figsize=(16,10))
    sns.barplot(language['count'],language['index'],palette='BuPu')
    for i,v in enumerate(language['count']):
        plt.text(10,i,v,fontsize=12,va='center')
    plt.xlabel('Count')
    plt.ylabel('Language')
    plt.title('Preferred Languages')
    plt.show() # Show the visualized data

def showInfo5(survey, survey_codebook):
    """ Feature 5 - How does employers measure you?
    
    Arguments:
        survey {pandas.core.frame.DataFrame} - the merged survey result
        survey_codebook {pandas.core.frame.DataFrame} - the codebook to analyze
    """
    print("\n# How does employers measure you?")
    survey['q13EmpMeasOtherCodingChallenge'].value_counts()
    cols = survey.columns[survey.columns.str.startswith('q13')]
    measurement = pd.DataFrame()
    for i in cols:
        content = survey[i].value_counts().reset_index(name='count')
        measurement = pd.concat([measurement,content])
    measurement.sort_values(by='count',ascending=False,inplace=True)
    print(measurement) # Print text data

    plt.figure(figsize=(16,10))
    sns.barplot(measurement['count'],measurement['index'],palette='BuPu')
    for i,v in enumerate(measurement['count']):
        plt.text(10,i,v,fontsize=12,va='center')
    plt.xlabel('Count')
    plt.ylabel('')
    plt.title('Popular Measurement')
    plt.show() # Show the visualized data

def main():
    """
    Main function that drives the program
    """
    # Read the data files
    survey = pd.read_csv('input/HackerRank-Developer-Survey-2018-Values.csv', low_memory=False)
    survey_codebook = pd.read_csv('input/HackerRank-Developer-Survey-2018-Codebook.csv')
    survey_codebook = survey_codebook.set_index('Data Field')
    print("============== A Guide for Developers ==============")
    survey.dropna(axis=0,how='all',inplace=True)
    print("\nWe have",survey.shape,"responses in total.")
    menu = 100
    # Show the menu until the user select 0 to exit the program
    while (menu != 0):
        print("\n---------- Information Look-up Table ----------")
        print("0. Exit")
        print("1. Distribution of Highest education level")
        print("2. Distribution of Current employment level")
        print("3. Popular emerging technologies within developers")
        print("4. Popular programming languages from employers")
        print("5. How does employers measure you?")
        menu = input("\nPlease select the number you want to see : ")
        if (menu == '0'):
            exit()
        else:
            execute(menu, survey, survey_codebook)

if __name__ == "__main__":
    main()
