# Programming-and-Scripting---Project-April-2018
Repository for my research and analysis of the Fisher Irish data set. 


## Project Outline 

<img src="https://image.ibb.co/bUxVwx/flower.jpg" alt="flower" border="1" height="200" width="200" align = "left"> <p align="justify">The final assignment for the Programming & Scripting Module is a project based on the Fisher Iris data set. The data set was sourced from the UCI Machine Learning repository*

The project entails researching the data set, writing Python code based on that research and writing concise documentation based on our findings.
	
The Fisher Iris data set was originally compiled in 1936 by Ronald Fisher for his paper "THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS"**.

This data set was most likely selected as it is a real data set rather than a sythetic/simulated data set and relates to a topic that is easily articulated to non-statisticians/biologists.</p>


## Objectives

The project instruction document has given us some well signposted objectives that we should achieve through this project.

<ol type="[1]">
	<li>Research background information about the data set and write a summary about it.</li>
	<li>Keep a list of references you used in completing the project.</li>
	<li>Download the data set and write some Python code to investigate it.</li>
	<li>Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set.A Python 		script will quickly do this for you.</li>
	<li>Write a summary of your investigations.</li>
	<li>Include supporting tables and graphics as you deem necessary.</li>
</ol>

<ol type="[1]">
In addition to the objectives that we are graded on, we should also develop a better understanding of:
<li>The importance of consise and well commented code - this is particularly relevant when carrying out work that is time sensitive as it can significantly spped up the process.</li>
<li>how to develop a clear audit trail that allows other users to follow our thought process and potentially pick up and continue our work if needed.</li>
<li>what tools are best suited to communicate results - text/graphics/tables etc. 
It is vital that my findings can be communicated in a manner that can be adapted depending on my audience (i.e. for a technical or non-technical viewer) as this would reflect real world working conditions.</li>
	</ol>

## Introduction

<p align="justify">The Fisher Iris data set was originally compiled in 1936 by Ronald Fisher for his paper "THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS"**.<br>
<img src="https://image.ibb.co/g0o1mx/gaf4.jpg" alt="gaf4" border="1" height="400" width="480">

The data set itself is relatively small with a total of 150 observations (50 observations for each of 3 different species of Iris, with 4 different measurements taken for each observation). This gives 600 model points with which to work.

The variants of Iris from which measurements were taken are the Iris Selosa, Iris versicolor and Iris virginica.

The 4 measurments taken are sepal length, sepal width, petal length and petal width.

The Iris data set is what is known as a Multivariate data set, that is the data set contains two or more variable quantities. 

When considering a Multivariate data set, it is important to ensure that due consideration is given to potential spurious correlations*** which could give rise to incorrect inferrences about the data set in our analysis.</p><br> 

The columns in this dataset are:

* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species<br>

<img src="https://image.ibb.co/kSQx9H/graf1.jpg" alt="graf1" border="1" height="500" width="580"><br>


## Method

``` python 
import matplotlib.pyplot as plt
import os 
```
<p align="justify">The purpose of this library is to draw the graphics that are printed by the program.
The library allows you to run commands in the operating system. The command is being used in the main menu at the end of the code (os.system) and is exectuing a "cls" from the windows prompt.  The library is also required to execute these commands.</p>

``` python
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
```
<p align="justify">Having given some consideration to the problem and carrying out some research both online and following discussions with former colleagues who have experience of python, I decided that it would be best to split into functions ("Separation of Concerns"). The reason for this was for simplicity and to potentially make the code easier and clearer to read. This should also help any third parties reading the code to understand and edit my work with minimal explanation.</p>
<p>The "Separation of Concerns" method separates the responsibilities of each function from the code rather than putting everything in the same module and getting a large block filled with could be difficult to read/follow "if" statements. Each function uses certain "boxes" and has a particular responsibility in the code. It helps make the code more organized, readable and easy to find something. 
This could have been done in a single statement without functions but would not be very presentable. The performance of the code would not be affected by the method used i.e. it was a purely organizational and stylistic decision. 
When giving consideration to what I could do with the data, I thought it would be interesting and informative to use the data provided to calculate the mean of the measurements taken for each flower class (iris setosa, iris versicolor, iris virginica). </p> 

The system (os) shows:
* the stem width for each flower class
* the mean stem size for each flower class
* the mean size of the petal for each flower class
allowing us to draw comparisons on the three.

The system then asks for a simple mean calculation which is calculated for 4 different measures for each flower class. Th measures being summarised are:
* stem length
* stem width
* petal length
* petal width

<p align="justify">We then use another programming concept which is referred to as "don't repeat yourself". This basically tells you that you don't need to write the same piece of code each time as the method/formula used for the calculation of the mean will be the same for each class. It is more sensible/simple to create a function which does the task for us. This the "average" function which reads in each class and each field you want to average.</p>

``` python
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

```
<p align="justify">For each of these measures, the average function would have to be repeated in the menu. In order to be better organized, I created a function that performs the average function calculation for each field and class i.e. the average function is the average for the field, class and the field that was sent as the default base function. From it a calculation was created for each part of the plant and those others call the average to do their work and they are initialized by the main menu.</p>

``` python
eval({1:"sepal_length()", 2:"sepal_width()", 3:"petal_length()", 4:"petal_width()"}.get(option,"os.system('cls')"))
```
<p align="justify">eval() method runs the python code (which is passed as an argument) within the program. I carefully chose eval() method, it was very difficult to get this part correct as initially I did not have the necessary knowledge but after several attempts, searches online and discussing with colleagues, I believe I was able to correctly execute.</p>
<p>In the inner part of the "eval" function we have a dictionary that has its own index and a string with the EXACT name of the function referring to each menu option:
1 - sepal_length
2 - sepal_width
etc.
The "get" of the dictionary gives it a number and it returns a string/information that is after the ":" i.e. the get passes the key and it returns me a value. In the case of my code, the key is a number and it will return me a string.</p>
	

## Results

## Conclusions

<img src="https://image.ibb.co/hA1LDc/petal_legth_average.jpg" alt="petal_legth_average" border="1" height="400" width="480"><br>
<img src="https://image.ibb.co/mbyp6x/petal_width_average.jpg" alt="petal_width_average" border="1" height="400" width="480"><br>
<img src="https://image.ibb.co/jVgyzH/sepal_lenght_average.jpg" alt="sepal_lenght_average" border="1" height="400" width="480"><br>
<img src="https://image.ibb.co/daLrKH/sepal_width_average.jpg" alt="sepal_width_average" border="1" height="400" width="480"><br>

## Post Project Considerations

## References/Bibliography
<ol type="[1]">
<li>[UCI Machine Learning Repository] (https://archive.ics.uci.edu/ml/datasets/Iris)</li>

<li>[Wiley Online Library] (https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x)</li>

<li>[The Python Tutorial] (https://docs.python.org/3/tutorial/index.html)</li>

<li>[Python packages] (https://pypi.python.org/pypi)</li>

<li>[Docs Python Built-in Functions] (https://docs.python.org/3/library/functions.html)</li>

<li>[Pyplot tutorial] (https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)</li>

<li>[Machine Learning with Iris Dataset] (https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset)</li>

<li> [Your First Machine Learning Project in Python] (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)</li></ol>
