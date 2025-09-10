# 🛳️ **Titanic Survival Analysis – Exploratory Data Analysis (EDA)**

## 📑 **Table of Contents**
- [**Project Overview**](#-project-overview)  
- [**Dataset**](#-dataset)  
- [**Steps Performed**](#-steps-performed)  
  - [**Data Preprocessing**](#1-data-preprocessing)  
  - [**Exploratory Data Analysis**](#2-exploratory-data-analysis)  
  - [**Data Visualization**](#3-data-visualization)  
- [**Key Insights**](#-key-insights)  
- [**Sample Visualizations**](#-sample-visualizations)  
- [**Learnings**](#-learnings)  
- [**Tech Stack**](#-tech-stack)  
- [**Future Scope**](#-future-scope)  
- [**License**](#-license)  

---

## 📌 **Project Overview**
This project focuses on performing **Exploratory Data Analysis (EDA)** on the famous **Titanic dataset** to uncover insights about passenger survival.  
The goal is to analyze key factors such as **age, gender, class, family size, and fare**, and understand how they influenced survival chances.  

Through **data cleaning, visualization, and correlation analysis**, this project demonstrates structured EDA practices that are essential in any **Machine Learning workflow**.

---

## 📂 **Dataset**
- **Source:** [Kaggle – Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)  
- **Files Used:** `train.csv`  
- **Size:** `891 rows × 12 columns`  

**Features of Interest:**  
- `Pclass` – Passenger class  
- `Sex` – Gender  
- `Age` – Age of passenger  
- `SibSp` & `Parch` – Family size aboard  
- `Fare` – Ticket fare  
- `Embarked` – Port of embarkation  
- `Survived` – Survival status (**Target variable**)  

---

## 🛠️ **Steps Performed**

### 1. **Data Preprocessing**
- Handled **missing values** (`Age`, `Embarked`, `Cabin`).  
- Converted categorical variables into numerical for analysis.  
- Created new features like **family count** & **age categories**.  

### 2. **Exploratory Data Analysis**
- **Univariate Analysis:** Distribution of survival, age, fare, and classes.  
- **Bivariate Analysis:** Survival rate across gender, class, and embarkation point.  
- **Multivariate Analysis:** Interaction of age, family size, and survival.  
- Correlation analysis with **heatmaps**.  

### 3. **Data Visualization**
- Used **Matplotlib & Seaborn** to create:  
  - Count plots, bar plots, histograms.  
  - Survival rates by passenger attributes.  
  - Heatmaps for correlations.  

---

## 📊 **Key Insights**
- **Gender:** Females had a much higher survival rate than males.  
- **Class:** Passengers in **1st Class** were more likely to survive.  
- **Age:** Children had higher survival chances compared to adults.  
- **Family Size:** Those with small families (1–3 members) had better chances of survival than those alone or with large families.  
- **Fare:** Higher ticket fares correlated with higher survival probability.  

---

## 📸 **Sample Visualizations**
*(Add screenshots of your plots here – survival by gender, class, heatmap, etc.)*  

---

## 💡 **Learnings**
- Practiced **data wrangling** and handling missing values.  
- Gained insights into **feature importance** before ML modeling.  
- Strengthened **data visualization** and storytelling skills.  

---

## ⚙️ **Tech Stack**
- **Python** 🐍  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn  

---

## 🚀 **Future Scope**
- Apply **Machine Learning models** (Logistic Regression, Random Forest) to predict survival.  
- Perform **feature engineering** for better model accuracy.  
- Build an **interactive dashboard** using Plotly or Power BI.  

---

## 📜 **License**
This project is open-source and available under the **MIT License**.  
