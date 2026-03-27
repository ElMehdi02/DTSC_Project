# Entity Resolution Project

## Overview
This project focuses on entity resolution, which is the task of figuring out if two records refer to the same real-world person. The goal is to build a full pipeline starting from raw data all the way to a working model that can decide whether two records match or not.

The project includes data simulation, feature engineering, machine learning, and evaluation. It shows how different concepts like similarity, classification, and data processing come together in one system.

## Project Objective
The main goals of this project are:

- Create realistic training data for entity resolution
- Build meaningful features to compare records
- Train a machine learning model to classify matches
- Evaluate how well the model performs
- Organize everything in a clean and reusable way

## What is Entity Resolution?
Entity resolution is the process of identifying when two records represent the same real-world entity, even if they look different.

For example:

- "Christine D Timko"
- "C. Timko"

These could refer to the same person, but the strings are not identical.

In this project, we simulate two datasets (like phonebooks) with fields such as:

- Forename
- Surname
- Address
- Phone number

The task is to compare records across datasets and decide if they refer to the same person.

## Methodology

### 1. Data Simulation
Since labeled data is not always available, training data is created manually and through simulation.

- Matching pairs are created by copying records and adding small changes (typos, abbreviations, etc.)
- Non-matching pairs are created by pairing different people randomly

This turns the problem into a supervised learning task.

### 2. Feature Engineering
Raw text cannot be used directly by models, so we convert it into features.

Examples of features used:

- Exact match (0 or 1)
- Prefix match (first few characters)
- String similarity scores
- Overlap between values

These features represent how similar two records are.

### 3. Model Training
A classification model is trained to predict:

- `1` → same person
- `0` → different people

The model learns patterns from the features and uses them to make predictions on new data.

## Blocking Strategy
Comparing every record with every other record is too slow when datasets get large.

To fix this, we use blocking:

- Only compare records that share something in common (like surname or zip code)

This reduces the number of comparisons and makes the system faster.

## Machine Learning Concepts Used
This project applies several important machine learning ideas:

- **Features vs labels** → features describe similarity, labels indicate match or not
- **Classification** → predicting whether two records match
- **Training data creation** → simulation, manual labeling, and generated examples
- **Bias** → bad data can affect model performance
- **Evaluation** → checking how accurate the model is

## Entity Resolution with Similarity
A key idea in this project is measuring similarity between records.

Instead of exact matches, we compare:

- Names (string similarity)
- Addresses
- Other attributes

In more advanced approaches, text can also be converted into vectors (embeddings), and similarity is measured using distance between vectors.

## Learning Outcomes
Through this project, I worked on:

- Building a full machine learning pipeline
- Creating and using features from raw data
- Understanding how similarity works in real problems
- Handling large comparisons with blocking
- Training and evaluating models
- Structuring code in a clean and reusable way

## Conclusion
This project shows how to build an entity resolution system from scratch. It combines data processing, feature engineering, and machine learning to solve a real problem: identifying when two records refer to the same person.

The final result is a working system that can take two records and predict whether they match, using learned patterns from data.
