# AI & ML Internship Task 1

## Data Cleaning and Preprocessing on Titanic Dataset

---

## Objective

The objective of this task is to perform data cleaning and preprocessing on the Titanic dataset using Python libraries. This process helps prepare raw data for Machine Learning models by handling missing values, encoding categorical data, scaling numerical features, and removing outliers.

---

## Tools and Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Dataset Information

The Titanic dataset contains passenger details such as:

* Passenger ID
* Passenger Class
* Name
* Gender
* Age
* Fare
* Embarked Location
* Survival Status

---

## Steps Performed

### 1. Dataset Loading

* Loaded the Titanic dataset using Pandas.

### 2. Data Inspection

* Displayed the first few rows of the dataset.
* Checked dataset structure and information.

### 3. Missing Value Handling

* Filled missing values in the `Age` column using median.
* Filled missing values in the `Embarked` column using mode.
* Removed the `Cabin` column because it contained too many missing values.

### 4. Encoding Categorical Features

* Converted categorical columns such as `Sex` and `Embarked` into numerical values using Label Encoding.

### 5. Feature Scaling

* Standardized numerical columns like `Age` and `Fare` using StandardScaler.

### 6. Outlier Detection

* Used Boxplot visualization to identify outliers in the `Fare` column.

### 7. Outlier Removal

* Removed outliers using the IQR (Interquartile Range) method.

### 8. Saving Processed Data

* Saved the cleaned dataset as `cleaned_titanic.csv`.

---

## Visualizations

The following visualization was created:

* Boxplot for outlier detection

---

## Files Included

* `task1.py` → Main Python source code
* `cleaned_titanic.csv` → Cleaned dataset
* `README.md` → Project documentation
* `requirements.txt` → Required Python libraries
* `dataset/` → Original Titanic dataset
* `screenshots/` → Output screenshots and graphs

---

## Output

* Missing values handled successfully
* Categorical data encoded
* Numerical features standardized
* Outliers detected and removed
* Cleaned dataset generated successfully

---

## Result

Task 1 completed successfully as part of the AI & ML Internship Project.

---

## Internship

AI & ML Internship Project
