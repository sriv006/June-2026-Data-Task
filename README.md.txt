# Student Performance Analysis (Kaggle Dataset)


## What This Code Does
1. **Loads Data:** Uses `pd.read_csv()` to load the Kaggle Student Performance dataset (`StudentsPerformance.csv`).
2. **Cleans Data:** Renames the columns so they are easier to read and work with in the code.
3. **Calculates Stats:** Uses `describe()` to output the minimum, maximum, and average scores across Math, Reading, and Writing.
4. **Visualizes Data:** Creates three easy-to-understand charts:
   - **Scatter Plot:** Compares Math scores to Reading scores to look for a correlation.
   - **Bar Chart:** Shows the average math score of students who took the test prep course versus those who didn't.
   - **Pie Chart:** Displays the gender breakdown of the dataset.

## Key Insights Discovered
* **Skill Correlation:** The scatter plot shows a strong relationship between math and reading. Students who score high in one subject tend to score high in the other.
* **Test Prep Works:** The bar chart reveals that students who completed the test preparation course had a noticeably higher average math score than those who skipped it.
* **Class Demographics:** The pie chart indicates the dataset is very evenly split between male and female students, meaning our insights are not heavily skewed toward one gender.

## How to Run This Code
1. Python installed.
2. The `pandas` and `matplotlib` libraries. 
3. The `StudentsPerformance.csv` file saved in the exact same folder as the Python script.