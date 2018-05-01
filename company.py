import pandas as pd
from tabulate import tabulate
__author__ = "Chloe Kim (minkyun3) and Phoebe Wu (zhuoxuew)"
__email__ = "minkyun3@andrew.cmu.edu | zhuoxuew@andrew.cmu.edu"
__copyright__ = "Copyright 2018, The Job Seekers"
__license__ = "GPL"
__version__ = "1.0.1"
"""
This application is to guide developers to grow up as a good engineer.
You can see our project here: https://github.com/phoebeWzx/Python-Group-12
"""
data = {
    'file_names': ['Amazon_dataset.csv', 'Google_dataset.csv'],
    'old_column_names': ['TEMP', 'DEWP', 'HUMI', 'PRES', 'season', 'precipitation']
}

def main():
    print("===== WELCOME TO THE GUIDE FOR DEVELOPERS =====")
    print("Hi, we are here to help you. Know yourself and become a competitive developer!")

    # Get user information
    name = input("Enter your name: ") # Get user name from the user
    age = input("Enter your age: ") # Get age from the user
    begin = input("Enter your age when began coding: ") # Get age begin from the user
    degree = input("Enter your highest degree: ") # Get highest degree from the user
    major = input("Is your major related to computer science? (y/n): ") # Get major from the user
    # Print user information to check
    data = [[name, age, begin, degree, major]]
    headers = ['Name', 'Age', 'First Coding Age', 'Highest Degree', 'Related Major?']
    print(tabulate(data, headers=headers, tablefmt='orgtbl', numalign="decimal", stralign="right", floatfmt=".2f"))
    correct = input("Information is correct? (y/n): ")
if __name__ == "__main__":
    main()