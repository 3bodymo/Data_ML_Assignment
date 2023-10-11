# DNA Engineering - ML Assignment

This repository contains the code and documentation for the Streamlit dashboard assignment. In this project, I was tasked with refactoring and enhancing a Streamlit dashboard that includes Exploratory Data Analysis, Training a machine learning model, and Inference (prediction).

## Project Setup

Before starting the tasks, I encountered an issue with the backend where the `main.py` file was not in the correct place. I resolved this problem by moving `main.py` to the project's root directory.

Before run my project, ensure you have the following packages installed:

- [WordCloud](https://pypi.org/project/wordcloud/)
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)

## Task 1 - Code Refactoring

I refactored the codebase following clean code guidelines. The main improvements are as follows:

- Split the monolithic `dashboard.py` script into three separate files, one for each section (EDA, Training, Inference). These components are now located in the `components` directory.
- Reformat the code for readability and maintainability.

Additionally, I sought out and addressed any other code anomalies throughout the entire project to improve the codebase further.

**For example**, there was an error in the display of the title of the confusion matrix; it was a fixed title for `Naive Bayes`, and I made it dynamic, and it changed based on the model that the user chose.

## Task 2 - Exploratory Data Analysis

I conducted Exploratory Data Analysis and added it to the first section of the Streamlit dashboard. The EDA included the following steps:

- Displayed a random sample of the dataset.
- Provided a count of labels for both raw and processed data.
- Showed summary statistics for the data.
- Implemented a user-friendly interface for selecting labels and specifying the number of words to visualize cloud data.

I used Streamlit widgets to display pandas dataframes, charts, and interactive components to enhance the user experience.

## Task 3 - Training

I aimed to beat the baseline pipeline. Here are the key steps I took:

- Preprocessed the data by removing unimportant characters and stop words.
- Balanced the dataset using RandomOverSampler.
- Created a selection box in the Streamlit web app, allowing users to choose the model they wanted to train.

I trained various models and here are the results:

| Model         | Accuracy | F1 Score |
| ------------- | -------- | -------- |
| Random Forest | 0.9594   | 0.9595   |
| XGBC          | 0.9574   | 0.9571   |
| Naive Bayes   | 0.9128   | 0.911    |
| SVC           | 0.9128   | 0.9115   |
| Decision Tree | 0.9594   | 0.9602   |
| KNN           | 0.8945   | 0.8946   |

The user can select the desired model for training, providing flexibility and insight into model performance.

## Task 4 - Inference

I enhanced the Inference section of the dashboard by:

**1. Saving Predictions:**
I implemented an endpoint, `api/save`, accessible through the dashboard, to save prediction results into an SQLite table. The results include resume and prediction.

**2. Displaying Predictions:**
After each inference, I added a feature to display the prediction results, allowing users to review old predictions conveniently.

## Task 5 - Unit Testing

As part of this project, I ensured that the code is thoroughly tested using unit tests.

I specifically wrote two unit tests for the following API endpoints:

**1. `api/inference`:**
The test checks the functionality of the inference endpoint.

**2. `api/save`:**
The test verifies the correctness of the save endpoint, ensuring that predictions are correctly saved to the SQLite table and retrieval to the user.

## Additional Notes

Feel free to explore the code and the Streamlit dashboard to interact with the components and see the results of each task.

If you have any questions or need further clarification, please don't hesitate to reach out.
