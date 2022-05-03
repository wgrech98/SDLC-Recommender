import pandas as pd
import pickle


class Test():

    def __init__(self, test):
        """
        Set initial variables
        """
        self.remaining_examples = None

        self.cols = ['methodology', 'requirements_volatility',
                     'requirements_clarity', 'development_time', 'project_size', 'team_size',
                     'product_complexity', 'testing_intensity', 'risk_analysis', 'user_participation',
                     'team_expertise', 'development_expertise', 'documentation_needed', 'funding_available', 'delivery_speed', 'task_visualisation', 'prototyping']

        self.f_names = ['requirements_volatility',
                        'requirements_clarity', 'development_time', 'project_size', 'team_size',
                        'product_complexity', 'testing_intensity', 'risk_analysis', 'user_participation',
                        'team_expertise', 'development_expertise', 'documentation_needed', 'funding_available', 'delivery_speed', 'task_visualisation', 'prototyping']

        self.num_cols = [6, 8, 9, 10, 11, 12, 13,
                         14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

        self.num_cols1 = [24, 26, 27, 28, 29, 30, 31,
                          32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

        self.dataset = None

        self.predicted_methodology = None

        self.covered_rule = None

        self.test = test

        self.x_test = None

        self.train = None

        self.min_significance = 0.5

        self.max_star_size = 5

        self.filename = "rules.pkl"

    def read_csv(self):
        """ 
        Function to split the CSV file into two dataframes, one for records representing the first methodology that participants
        rated while the second represents the records for those participant who responded to use a second methodology.
        The two dataframes are then merged together and the final dataframe is returned.
        """

        csv_path = 'survey_dataset.csv'
        df = pd.read_csv(csv_path, names=self.cols,
                         usecols=self.num_cols, header=0)
        df1 = pd.read_csv(csv_path, names=self.cols,
                          usecols=self.num_cols1, header=0)

        # Deleting rows with null values
        df = df.dropna()
        df1 = df1.dropna()

        # Merging the two datasets
        self.dataset = df.append(df1, ignore_index=True)

    def test_model(self):
        """
        Test rule list returned by fit_CN2_Model function on test data(or manually supplied data)
        returns the predicted methodology and the rule that was triggered.
        """
        self.read_csv()
        open_file = open(self.filename, "rb")
        rules = pickle.load(open_file)

        remaining_examples = self.test
        remaining_examples = pd.DataFrame(
            remaining_examples, columns=self.f_names)

        for rule in rules:
            rule_coverage_indexes, rule_coverage_dataframe = self.complex_coverage(
                rule[0], remaining_examples)
            # check for zero coverage due to noise(lense data too small)
            if len(rule_coverage_dataframe) != 0:
                self.predicted_methodology = rule[1]
                # list_of_row_dicts.append(row_dictionary)
                self.covered_rule = rule[0]

                remaining_examples = remaining_examples.drop(
                    rule_coverage_indexes)

        return self.predicted_methodology, self.covered_rule

    def complex_coverage(self, passed_complex, data_set):
        """ Returns set of instances of the data 
            which complex(rule) covers as a dataframe.
        """

        rule = self.build_rule(passed_complex)
        if rule == False:
            return [], []

        mask = data_set.isin(rule).all(axis=1)
        rule_coverage_indexes = data_set[mask].index.values
        rule_coverage_dataframe = data_set[mask]

        return rule_coverage_indexes, rule_coverage_dataframe

    def build_rule(self, passed_complex):
        """
        build a rule in dict format where target attributes have a single value and non-target attributes
        have a list of all possible values. Checks if there are repetitions in the attributes used, if so
        it returns False
        """
        atts_used_in_rule = []
        for selector in passed_complex:
            atts_used_in_rule.append(selector[0])
        set_of_atts_used_in_rule = set(atts_used_in_rule)

        # Checks if there are repetitions in the attributes used
        if len(set_of_atts_used_in_rule) < len(atts_used_in_rule):
            return False

        rule = {}
        attributes = self.dataset.columns.values.tolist()
        for att in attributes:
            rule[att] = list(set(self.dataset[att]))

        for att_val_pair in passed_complex:
            att = att_val_pair[0]
            val = att_val_pair[1]
            rule[att] = [val]

        return rule
