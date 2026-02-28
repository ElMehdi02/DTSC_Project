# Entity Resolution Project  
### Data Science Course – Duquesne University  
**Instructor: Dr. Arthur Sugden**

---

## Overview

This repository was created as part of a Data Science course at **Duquesne University** taught by **Dr. Arthur Sugden**. Throughout the course, we explored practical and interesting topics in data science, including machine learning models, bias in data, feature engineering, blocking strategies, and classification systems.

This project focuses on **Entity Resolution**, which is the task of determining whether two records refer to the same real-world person. The purpose of this repository is to demonstrate the complete workflow of working with a dataset — from data simulation to feature engineering, model training, and evaluation.

This repository is intended to showcase both understanding of course concepts and clean project structure.

---

## Project Objective

The main goals of this project are:

- Simulate realistic entity resolution training data  
- Engineer meaningful comparison features  
- Train a supervised machine learning model  
- Evaluate model performance  
- Clearly document the entire process  

The project reflects the material covered in class and demonstrates applied understanding of core data science techniques.

---

## What is Entity Resolution?

Entity Resolution (ER) is the process of identifying and matching records that refer to the same entity across datasets.

In this project, we simulate two phonebooks containing:

- Forename  
- Surname  
- Address  
- Phone number  

The task is to determine whether two records from different phonebooks represent the same person.

---

## Methodology

### 1. Data Simulation

Because labeled entity resolution datasets are not always available, training data is generated through simulation.

- Matching pairs are created by copying records and introducing small typographical errors.
- Non-matching pairs are created by randomly sampling different individuals from separate phonebooks.

This allows us to construct a supervised classification problem.

---

### 2. Feature Engineering

Raw text fields cannot be directly used by machine learning models. Therefore, comparison features are created, such as:

- Exact match indicators  
- Prefix similarity  
- String similarity scores  
- Set-based overlap (when applicable)  

These features convert text fields into numerical representations suitable for classification models.

---

### 3. Model Training

A binary classification model is trained to predict:

- **1 → Match (same person)**  
- **0 → Non-match (different people)**  

The model is evaluated using accuracy and other performance metrics.

---

## Blocking Strategy

Comparing every record in phonebook 1 to every record in phonebook 2 would be computationally expensive. To reduce unnecessary comparisons, a simple blocking strategy can be used, such as grouping records by surname or zip code before performing detailed comparisons.

Blocking significantly improves scalability for larger datasets.

---

## Learning Outcomes

Through this project, I strengthened my understanding of:

- Supervised machine learning  
- Feature engineering  
- String similarity techniques  
- Dataset simulation  
- Model evaluation  
- Clean repository structure and documentation  

This project represents applied learning from the Data Science course at Duquesne University.

---

## Conclusion

This repository demonstrates the complete process of building an entity resolution system from scratch. It reflects both conceptual understanding and practical implementation of the topics covered in class under the instruction of Dr. Arthur Sugden.

The goal of this repository is to showcase coding ability, organization, and understanding of real-world data science workflows.