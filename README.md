# A NOVEL RECOMMENDER SYSTEM TO DETERMINE THE OPTIMAL SOFTWARE DEVELOPMENT LIFECYCLE MODEL IN SOFTWARE PROJECTS

This is a readme file for the implementation of the Recommender System (RMS) for my dissertation project

## Background & Objectives

Software Development Lifecycle (SDLC) methodologies provide the software development community with a structural framework to develop software products in an efficient and qualitative manner. Several recommender tools have been developed to facilitate the SDLC selection process; however, literature evidenced that the existing solutions in the market lack transparency when considering the algorithmic process of how the recommender tools arrive to a recommendation. This dissertation addresses the issue by developing a knowledge-based recommender system (RMS) that predicts the ideal SDLC methodology for different project scenarios. Explainable Artificial Intelligence techniques were utilised to facilitate user understanding of the predictions and the algorithmic process of the RMS.

## Dataset

The dataset is composed of the characteristics related to the choice of a SDLC methodology. Overall, the dataset amounted to 143 records.

## Models

The repository hosts the implementation of a knowledge-based RMS with the use of three python algorithms, namely the KNN algorithm, the decision tree algorithm, and the CN2 algorithm.

Explainable Artificial Intelligence techniques were utilised to facilitate user understanding of the predictions and the algorithmic process of the RMS.

# CN2 Algorithm

The CN2 algorithm is a rule-based technique that supersedes its predecessors, namely the ID3 algorithm, and AQ by accounting for the presence of noise in the domain data.

A rule list produced with the CN2 algorithm follows the following notation:

    if Condition_1 then Class_A
    else if Condition_2 then Class_B
    ...
    else Default_Class.

A prediction is made by checking if any of the rules covers the testing record.

The prediction along with the rule that was triggered for the record entered by the user are displayed to the user in the results page of the RMS.

# KNN Algorithm

In KNN, the trained data is compared with test data and distances are calculated using Euclidean distance. It then classifies an instance by finding its nearest neighbors and recommend the top n nearest neighbor SDLC Methodologies. The algorithm runs the ‘KNeighborsClassifier'() to build a KNN model and produce predictions.

The prediction along with a table representing the methodologies ranked according to Eucilidean distance based on the record entered by the user are displayed to the user in the results page of the RMS.

# Decision Tree Algorithm

Decision Trees are another important rule-based technique represented portrayed as a tree structure. The algorithm splits the dataset into smaller classes according to the most important predictor in the predictor space with an if-then rule set. When running the decision tree algorithm, The algorithm runs the ‘DecisionTreeClassifier()' to build a decision tree model and produce predictions.

The prediction along with a feature contribution table (used the eli5 python package) that displays the features that led to the prediction are displayed to the user in the results page of the RMS.

# The Recommender System

The Web aplication was implemented with the use of python Flask (Python version used: 3.10.1), HTML scripting language, CSS, and Javascript.

To run the RMS:

1. Download the entire repository
2. Unzip all files
3. pip install -r requirements.txt
4. run app.py on port 5000

## Guidance to use the RMS

1. Get to the home page by running the RMS as highlighted in the above section

<p align="center">
  <img src="https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/homepage.png" alt="Size Limit CLI" width="738">
</p>

2. Enter values for each characteristic by clicking on the dropdown arrow and selecting the appropriate value for the software project

<p align="center">
  <img src="https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/dropdown_for_characteristic.png" alt="Size Limit CLI" width="738">
</p>

<!-- ![dropdown values](https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/dropdown_for_characteristic.png) -->

3. Once all values are entered, hit the submit button

4. The results page pops up with a table holding the name of the algorithm in question and the corresponding prediction.

<!-- ![results_table](https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/results_table.png) -->

<p align="center">
  <img src="https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/results_table.png" alt="Size Limit CLI" width="738">
</p>

5. The prediction explanation can be accessed by hovering over the prediction

<p align="center">
  <img src="https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/rule_cn2.png" alt="Size Limit CLI" width="500"  height = 200>
</p>
<p align="center">
  <img src="https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/knn_explanation.png" alt="Size Limit CLI" width="500"  height = 500>
</p>
<p align="center">
  <img src="https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/feature_contribution.png" alt="Size Limit CLI" width="500" height = 500>
</p>

<!-- ![CN2](https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/rule_cn2.png)
![KNN](https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/knn_explanation.png)
![Decision_Tree](https://github.com/wgrech98/SDLC-Recommender/blob/master/Images/feature_contribution.png) -->
