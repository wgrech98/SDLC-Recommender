# A NOVEL RECOMMENDER SYSTEM TO DETERMINE THE OPTIMAL SOFTWARE DEVELOPMENT LIFECYCLE MODEL IN SOFTWARE PROJECTS 
This is a readme file for the implementation of the Recommender System (RMS) for my dissertation project

## Background & Objectives
Software Development Lifecycle (SDLC) methodologies provide the software development community with a structural framework to develop software products in an efficient and qualitative manner. Several recommender tools have been developed to facilitate the SDLC selection process; however, literature evidenced that the existing solutions in the market lack transparency when considering the algorithmic process of how the recommender tools arrive to a recommendation. This dissertation addresses the issue by developing a knowledge-based recommender system (RMS) that predicts the ideal SDLC methodology for different project scenarios. Explainable Artificial Intelligence techniques were utilised to facilitate user understanding of the predictions and the algorithmic process of the RMS.
 
## Dataset
The dataset is composed of the characteristics related to the choice of a SDLC methodology. Overall, the dataset  amounted to 143 records.

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


# KNN Algorithm 
In KNN, the trained data is compared with test data and distances are calculated using Euclidean distance. It then classifies an instance by finding its nearest neighbors and recommend the top n nearest neighbor SDLC Methodologies. The algorithm runs the ‘KNeighborsClassifier'() with the cross validation technqiue. The predictions are returned with the accuracy achieved for each fold. To run the algorithm:


# Decision Tree Algorithm 
Decision Trees (DTs) are another important rule-based technique represented portrayed as a tree structure. The algorithm splits the dataset into smaller classes according to the most important predictor in the predictor space with an if-then rule set. When running the decision tree algorithm, The algorithm runs the ‘DecisionTreeClassifier() with the cross validation technqiue. The predictions are returned with the accuracy achieved for each fold. A decision tree graph is also returned to the user. To run the algorithm:

# The Recommender System
The Web aplication was implemented with the use of python Flask, HTML scripting language, CSS, and Javascript.

Once the application is running, The home page will appear as below.

To run the RMS:
1. Download the entire repository 
2. Unzip all files
3. run app.py on port 5000 
