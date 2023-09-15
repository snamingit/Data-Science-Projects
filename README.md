# Data-Science-Projects

This repository includes the following data science projects:

1. Predicting Age-Related Conditions
   Goal: To predict whether the variable 'Class' will have a value of:
      1 :  a person will have any age-related diseases or
      0:  a person will NOT have any age-related diseases

    Description of Datasets: The training dataset was provided by InVitro Cell Research, LLC (ICR). It comprised of 1 ID column (dropped at the onset), and  56 features which are all health characteristics related to age-linked diseases (all but 1 is numerical).  The features are anonymized which limits the use of domain expertise to analyze the data. The training           dataset is small with 617 rows. There was a supplemental dataset that contained the date the training records were collected. The real test dataset was hidden but it was mentioned that that the training dataset was collected prior to the collection of the test dataset. I then created a variable named 'time' to represent the data collection timing. In total, 
       there are 57 readily-available features.

    Models Considered: Logistic Regression, SVM, KNN, Random Forest, CatBoost, XGBoost, LightGBM, TabPFN

    Best Model: TabPFN (based on balanced log-loss score)
