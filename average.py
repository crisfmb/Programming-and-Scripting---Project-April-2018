#Cristina borges, 03/04/2018
#average of width and length of sepal and petal of each class.

'''using matplotlib a library which produces publication quality figures in a variety of hardcopy 
formats and interactive environments across platforms'''

import matplotlib.pyplot as plt # import matplolib e usa alias plt
import os # is a call in the operating system, used to clear a screen terminal


def average(class_name, column_name): #calculates the past average as a parameter
    iris_data_set = open("iris-data-set.csv", "r")

    values = [] # array where is filled with all values ​​to calculate the average

    '''
    separates the columns, all in lower using comma. If it is sepal lenght fill in the values ​​with cols [0]
and if it is width cols [1] and so on
    '''
    for line in iris_data_set: 
        cols = line.split(",")
        if cols[4].lower().rstrip("\n") == class_name.lower():
            if column_name.lower() == "sepal_length":
                values.append(float(cols[0]))
            elif column_name.lower() == "sepal_width":
                values.append(float(cols[1]))
            elif column_name.lower() == "petal_length":
                values.append(float(cols[2]))
            elif column_name.lower() == "petal_width":
                values.append(float(cols[3]))

    iris_data_set.close() # Close dataset. Calculates the sum of the columns (sum) and divides by the size of the array (len) and makes the average

    return sum(values) / len(values)
    #calculate the sepal length average and show the bar chart, change average sepal length, sepal width, petal length etc...
def sepal_length():
    plt.bar(["iris-setosa", "iris-versicolor", "iris-virginica"], [average("iris-setosa", "sepal_length"),
                                                                   average("iris-versicolor", "sepal_length"), average("iris-virginica", "sepal_length")])
    plt.ylabel("cm")
    plt.xlabel("Sepal length average comparison")
    plt.show()

def sepal_width():
    plt.bar(["iris-setosa", "iris-versicolor", "iris-virginica"], [average("iris-setosa", "sepal_width"),
                                                                   average("iris-versicolor", "sepal_width"), average("iris-virginica", "sepal_width")])
    plt.ylabel("cm")
    plt.xlabel("Sepal width average comparison")
    plt.show()

def petal_length():
    plt.bar(["iris-setosa", "iris-versicolor", "iris-virginica"], [average("iris-setosa", "petal_length"),
                                                                   average("iris-versicolor", "petal_length"), average("iris-virginica", "petal_length")])
    plt.ylabel("cm")
    plt.xlabel("Petal length average comparison")
    plt.show()

def petal_width():
    plt.bar(["iris-setosa", "iris-versicolor", "iris-virginica"], [average("iris-setosa", "petal_width"),
                                                                   average("iris-versicolor", "petal_width"), average("iris-virginica", "petal_width")])
    plt.ylabel("cm")
    plt.xlabel("Petal width average comparison")
    plt.show()
option = 0
while option != 9:#Loop..choose an option to show the comparatives 
    os.system("cls") # executes command at the prompt, executes cls to clear the terminal
    print("[1] Sepal length average comparison")
    print("[2] Sepal width average comparison")
    print("[3] Petal length average comparison")
    print("[4] Petal width average comparison")
    print("[9] Exit")
    option = int(input("Choose an option and hit ENTER: "))
    #I use eval instead if. Do the same. He has a dictionary return a string to refer to te number and eval execute comand 
    eval({1:"sepal_length()", 2:"sepal_width()", 3:"petal_length()", 4:"petal_width()"}.get(option,"os.system('cls')"))