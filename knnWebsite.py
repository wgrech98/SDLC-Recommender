import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from IPython.display import HTML


class KNN_RMS():

    def __init__(self, test):
        """
        constructor: partitions data into train and test sets, sets the minimum accepted significance value
        and maximum star size which limits the number of complexes considered for specialisation.
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
        csv_path = 'survey_dataset.csv'
        df = pd.read_csv(csv_path, names=self.cols,
                         usecols=self.num_cols, header=0)
        df1 = pd.read_csv(csv_path, names=self.cols,
                          usecols=self.num_cols1, header=0)
        df = df.dropna()
        df1 = df1.dropna()
        self.dataset = df.append(df1, ignore_index=True)

        return self.dataset

    def convert_to_vectors(self, df):
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

        # project_type = {'Application (everything else)': 1,'System (sits between the hardware and the application software e.g. OSs)': 2,
        #                 'Utility (performs specific tasks to keep the computer running e.g. antivirus)':3}
        requirements_volatility = {'Changing': 1, 'Fixed': 2}
        requirements_clarity = {
            'unknown/defined later in the lifecycle': 1, 'understandable/early defined': 2}
        development_time = {'Intensive': 1, 'Non-Intensive': 2}
        project_size = {'Small': 1, 'Medium': 2, 'Large': 3}
        team_size = {'Small (1-5)': 1, 'Medium (6-15)': 2, 'Large (16....)': 3}
        product_complexity = {'Simple': 1, 'Complex': 2}
        testing_intensity = {
            'After each cycle (Intensive testing)': 1, 'After development is done (Non-intensive testing)': 2}

        # df.project_type = [project_type[item] for item in df.project_type]
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

        # le = preprocessing.LabelEncoder()
        # df['risk_analysis'] = le.fit_transform(df['risk_analysis'])
        # df['user_participation'] = le.fit_transform(df['user_participation'])
        # df['team_expertise'] = le.fit_transform(df['team_expertise'])
        # df['development_expertise'] = le.fit_transform(
        #     df['development_expertise'])
        # df['documentation_needed'] = le.fit_transform(
        #     df['documentation_needed'])
        # df['funding_available'] = le.fit_transform(df['funding_available'])
        # df['delivery_speed'] = le.fit_transform(df['delivery_speed'])
        # df['task_visualisation'] = le.fit_transform(df['task_visualisation'])
        # df['prototyping'] = le.fit_transform(df['prototyping'])
        # df['requirements_volatility'] = le.fit_transform(
        #     df['requirements_volatility'])
        # df['requirements_clarity'] = le.fit_transform(
        #     df['requirements_clarity'])
        # df['development_time'] = le.fit_transform(df['development_time'])
        # df['project_size'] = le.fit_transform(df['project_size'])
        # df['team_size'] = le.fit_transform(df['team_size'])
        # df['product_complexity'] = le.fit_transform(df['product_complexity'])
        # df['testing_intensity'] = le.fit_transform(df['testing_intensity'])

        return df

    def perform_KNN(self):
        self.read_csv()
        cl_dataset = self.convert_to_vectors(self.dataset)
        X = cl_dataset.drop('methodology', axis=1)
        y = cl_dataset[['methodology']]
        self.model = KNeighborsClassifier(n_neighbors=1)
        self.model.fit(X, y)

        X_test = self.test

        X_test = pd.DataFrame(X_test, columns=self.f_names)

        X_test = self.convert_to_vectors(X_test)

        y_predict = self.model.predict(X_test)

        distances, indices = self.model.kneighbors(
            X_test, n_neighbors=103, return_distance=True)

        names_similar = pd.Series(indices.flatten()).map(
            self.dataset.reset_index()['methodology'])

        result = pd.DataFrame({'Eucilidean Distance': distances.flatten(
        ), 'Methodology': names_similar}).drop_duplicates('Methodology')

        html = HTML(result.to_html(index=False, col_space=80))

        return y_predict[0], html
