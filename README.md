#  Titanic Survival Prediction using Linear Regression

##  Project Overview

This project demonstrates the implementation of **Linear Regression** using the Titanic dataset. The goal is to predict whether a passenger survived or not based on features like age, class, fare, and gender.

---

##  Objective

* Implement **Simple & Multiple Linear Regression**
* Understand model training and evaluation
* Interpret model results

---

##  Tools & Technologies

* Python 
* Pandas 
* Scikit-learn 
* Matplotlib 

---

##  Dataset

* Dataset used: Titanic Dataset
* Features used:

  * Pclass (Passenger Class)
  * Age
  * Fare
  * Sex
* Target:

  * Survived (0 = No, 1 = Yes)

---

##  Steps Performed

1. Imported required libraries
2. Loaded dataset using Pandas
3. Handled missing values (Age column)
4. Converted categorical data (Sex → numeric)
5. Split dataset into training and testing sets
6. Trained Linear Regression model
7. Predicted results
8. Evaluated model using:

   * MAE (Mean Absolute Error)
   * MSE (Mean Squared Error)
   * R² Score
9. Visualized results

---

##  Model Performance

* MAE: 0.2878
* MSE: 0.1372
* R² Score: 0.434

 The model shows moderate performance. Since this is a classification problem, Linear Regression is not the ideal choice, but it helps understand regression concepts.

---

##  Output Visualization

* Scatter plot of Actual vs Predicted values

---

##  Key Learnings

* Basics of Linear Regression
* Data preprocessing techniques
* Model evaluation metrics
* Importance of choosing the right model

---

##  Limitations

* Linear Regression is not ideal for classification problems
* Better results can be achieved using Logistic Regression

---

##  Future Improvements

* Implement Logistic Regression
* Perform feature engineering
* Improve accuracy using advanced models

---

##  How to Run

1. Clone the repository
2. Install required libraries:

   ```bash
   pip install pandas scikit-learn matplotlib
   ```
3. Run the Python file:

   ```bash
   python task3.py
   ```

---

##  Conclusion

This project successfully demonstrates how Linear Regression works and how it can be applied to real-world datasets for prediction and analysis.

---

##  Author

Vasu Jain
