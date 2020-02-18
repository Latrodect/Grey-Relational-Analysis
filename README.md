# Grey-Relational-Analysis
# What will do this program for you
Gray Relational Analysis is a fuzzy system of black, white and gray. Gray values ​​can take values ​​from 0-1. Values ​​between 0-1 allow us to determine the most optimal parameters. It does not need any output variable. Gray Relational Analysis is the name given to the method that is part of the Gray Systems. While applying Gray Relational Analysis, two different types of normalization types can be processed. These normalization methods are Biggest Best (EBEI) and Smallest Best (EKEI). After the decision is made according to the parameter needs, normalization is performed and the absolute value matrix is ​​created. We need a ‘Theta‘ value to subtract the Gray Relational Coefficient matrix from the created Absolute value matrix. Theta value usually takes 0.5. Gray Relational Coefficient is obtained by using this 'Theta' value and absolute value coefficient matrix in the Gray Relational Coefficient formula. The columns of the obtained Gray Relational Coefficient matrix are multiplied by the weights given the sum of one. After all the columns are multiplied, a new column is obtained by adding all the lines. This column obtained is our Gray Relational Degree.
## İncluding-Librarys
	pip install -r requirements.txt
İf you wish the program run correctly you need download the all python librarys.
For including the librarys open your command line and write the given code over the top of this section and make sure the add python to path.
 
## How the program works
First of all you need to know the parameters of program.
All desired parameters are given below, respectively.
- Full path to csv file
	- Give the path of dataset with csv form
	- You will see example of that right below this sentence.
	> C:\Users\hbaha\OneDrive\Masaüstü\Github Projects\Grey-Relational-Analysis\Example.csv
- How many columns will normalizing according to the maximum value
	- Program will normalizing the data with minimum according. 
	- Give the count of the columns with normalizing according to the maximum value.
	-  You will see example of that right below this sentence.
	> 4 or 2
- Chose the which columns are normalizing according to the maximum value.
	- İnput the columns name.
	-  You will see example of that right below this sentence.
	- - Attention! You must give the exacly same column name
	 > Column1
- You need to give correct weight for each columns.
	- The maximum normalization columns you select are added to the bottom of the list.
	- You should pay attention to this when giving your column weights.
	- > 0.1 or 0.8 (Which weight will you use)
	
After this steps program give you xlsx output on the program directory.
You can check the GreyRelationalRanking.xlsx for learning best option for you.
[this is the description](http://www.github.com/Latrodect/Grey-Relational-Analysis)