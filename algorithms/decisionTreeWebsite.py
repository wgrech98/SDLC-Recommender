import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import eli5


class D3_Algorithm():

    def __init__(self, test):
        """
        Set initial variables
        """
        self.cols = ['methodology', 'requirements_volatility',
                     'requirements_clarity', 'development_time', 'project_size', 'team_size',
                     'product_complexity', 'testing_intensity', 'risk_analysis', 'user_participation',
                     'team_expertise', 'development_expertise', 'documentation_needed', 'funding_available', 'delivery_speed', 'task_visualisation', 'prototyping']

        self.num_cols = [6, 8, 9, 10, 11, 12, 13,
                         14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

        self.num_cols1 = [24, 26, 27, 28, 29, 30, 31,
                          32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

        self.dataset = None

        self.test = test

        self.f_names = ['requirements_volatility',
                        'requirements_clarity', 'development_time', 'project_size', 'team_size',
                        'product_complexity', 'testing_intensity', 'risk_analysis', 'user_participation',
                        'team_expertise', 'development_expertise', 'documentation_needed', 'funding_available', 'delivery_speed', 'task_visualisation', 'prototyping']

        self.c_names = ['Waterfall', 'Scrum', 'Kanban', 'Hybrid: Scrum and Kanban',
                        'Hybrid: Scrum and Waterfall', 'Spiral', 'RAD']

    def read_csv(self):
        """ 
        Function to split the CSV file into two dataframes, one for records representing the first methodology that participants
        rated while the second represents the records for those participant who responded to use a second methodology.
        The two dataframes are then merged together and the final dataframe is returned.
        """

        csv_path = './dataset/survey_dataset.csv'
        df = pd.read_csv(csv_path, names=self.cols,
                         usecols=self.num_cols, header=0)
        df1 = pd.read_csv(csv_path, names=self.cols,
                          usecols=self.num_cols1, header=0)

        # Deleting rows with null values
        df = df.dropna()
        df1 = df1.dropna()
        self.dataset = df.append(df1, ignore_index=True)

        return self.dataset

    def convert_to_integers(self, df):
        """ 
        Convert characteristics to vectors to enable machine learning processing.

        Returns discrete dataset.
        """

        df['risk_analysis'] = df['risk_analysis'].map(
            dict(Low=1, Medium=2, High=3))
        df['user_participation'] = df['user_participation'].map(
            dict(Low=1, Medium=2, High=3))
        df['team_expertise'] = df['team_expertise'].map(
            dict(Low=1, Medium=2, High=3))
        df['development_expertise'] = df['development_expertise'].map(
            dict(Low=1, Medium=2, High=3))
        df['documentation_needed'] = df['documentation_needed'].map(
            dict(Low=1, Medium=2, High=3))
        df['funding_available'] = df['funding_available'].map(
            dict(Low=1, Medium=2, High=3))
        df['delivery_speed'] = df['delivery_speed'].map(
            dict(Low=1, Medium=2, High=3))
        df['task_visualisation'] = df['task_visualisation'].map(
            dict(Low=1, Medium=2, High=3))
        df['prototyping'] = df['prototyping'].map(
            dict(Low=1, Medium=2, High=3))

        requirements_volatility = {'Changing': 1, 'Fixed': 2}
        requirements_clarity = {
            'unknown/defined later in the lifecycle': 1, 'understandable/early defined': 2}
        development_time = {'Intensive': 1, 'Non-Intensive': 2}
        project_size = {'Small': 1, 'Medium': 2, 'Large': 3}
        team_size = {'Small (1-5)': 1, 'Medium (6-15)': 2, 'Large (16....)': 3}
        product_complexity = {'Simple': 1, 'Complex': 2}
        testing_intensity = {
            'After each cycle (Intensive testing)': 1, 'After development is done (Non-intensive testing)': 2}

        df.requirements_volatility = [
            requirements_volatility[item] for item in df.requirements_volatility]
        df.requirements_clarity = [requirements_clarity[item]
                                   for item in df.requirements_clarity]
        df.development_time = [development_time[item]
                               for item in df.development_time]
        df.project_size = [project_size[item] for item in df.project_size]
        df.team_size = [team_size[item] for item in df.team_size]
        df.product_complexity = [product_complexity[item]
                                 for item in df.product_complexity]
        df.testing_intensity = [testing_intensity[item]
                                for item in df.testing_intensity]

        return df

    def perform_D3(self):
        """
        Function which creates a decision tree model, and generate predictions based on the model.

        Returns the decision tree prediction.
        """

        # Invokes the read csv function
        self.read_csv()

        # Convert string data to discrete variables
        cl_dataset = self.convert_to_integers(self.dataset)

        # Set X and y
        X = cl_dataset.drop('methodology', axis=1)
        y = cl_dataset[['methodology']]

        # Create decision tree model with criterion entropy and max_depth 17 to account for all features
        self.model = DecisionTreeClassifier(
            criterion="entropy", random_state=42, max_depth=17, min_samples_leaf=1)

        # Fit the model
        self.model.fit(X, y)

        X_test = self.test

        # Convert X_test to dataframe to produce prediction
        X_test = pd.DataFrame(X_test, columns=self.f_names)

        # Convert X_test values to discrete
        self.X_test = self.convert_to_integers(X_test)

        y_predict = self.model.predict(self.X_test)

        return y_predict[0]

    def get_explanation(self):
        """ 
        Function which invokes the eli5 library to get insights about the most important features that led to a decision tree prediction.
        Returns explanation.
        """

        exp = eli5.show_prediction(
            self.model, self.X_test, feature_names=self.f_names, top_targets=1, top=8)

        return exp
