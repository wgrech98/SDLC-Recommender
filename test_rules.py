import pandas as pd
import numpy as np
import pickle

class Test():

    def __init__(self, test):
        self.remaining_examples = None
        self.cols = ['methodology', 'requirements_volatility', 
            'requirements_clarity', 'dev_time', 'project_size', 'team_size', 
            'prod_complexity', 'testing_intensity', 'risk_analysis', 'user_participation',
            'team_expertise', 'dev_expertise', 'doc_needed', 'fund_avail', 'delivery_speed','task_visualisation', 'prototyping']

        self.f_names = ['requirements_volatility', 
            'requirements_clarity', 'dev_time', 'project_size', 'team_size', 
            'prod_complexity', 'testing_intensity', 'risk_analysis', 'user_participation',
            'team_expertise', 'dev_expertise', 'doc_needed', 'fund_avail', 'delivery_speed', 'task_visualisation', 'prototyping']
                
        self.num_cols = [6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

        self.num_cols1 = [24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]

        self.dataset = None

        self.test = test

        self.x_test = None

        self.train = None

        #self.train = pd.read_csv(data_csv)
        self.min_significance = 0.5
        self.max_star_size = 5
        self.filename = "rules.pkl"


    def read_csv(self):
        csv_path = 'survey_dataset.csv'
        df = pd.read_csv(csv_path, names = self.cols, usecols=self.num_cols, header = 0)
        df1 = pd.read_csv(csv_path, names = self.cols, usecols= self.num_cols1, header = 0)
        df = df.dropna()
        df1 = df1.dropna()
        self.dataset = df.append(df1, ignore_index = True)
        
        
    def test_model(self):
        """
        Test rule list returned by fit_CN2_Model function on test data(or manually supplied data)
        returns a dataframe that contains the rule, rule acc, num of examples covered.
        Also return general accuracy as average of each rule accuracy
        """
        self.read_csv()
        open_file = open(self.filename, "rb")
        rules = pickle.load(open_file)

        remaining_examples = self.test
        remaining_examples = pd.DataFrame(remaining_examples, columns=self.f_names)


        for rule in rules:
            rule_coverage_indexes,rule_coverage_dataframe = self.complex_coverage(rule[0],remaining_examples)
            #check for zero coverage due to noise(lense data too small)
            if len(rule_coverage_dataframe) != 0:
                row_dictionary = rule[1]
                # list_of_row_dicts.append(row_dictionary)			   

                remaining_examples = remaining_examples.drop(rule_coverage_indexes)

        return row_dictionary


    # def testo(self):
    #     testSet = [['Changing', 'unknown/defined later in the lifecycle', 
    #         'Intensive', 'Medium', 'Small (1-5)', 'Complex', 'After each cycle (Intensive testing)', 'High', 
    #         'High','Low', 'High','Low','Medium','High', 'Low', 'Low']]

    #     self.test = pd.DataFrame(testSet, columns=self.f_names)


    def complex_coverage(self, passed_complex, data_set = 'default'):
        """ Returns set of instances of the data 
            which complex(rule) covers as a dataframe.
        """
        # if type(data_set) == str: 
        #     data_set = self.train
        # coverage = []

        rule = self.build_rule(passed_complex)
        if rule == False:
            return [],[]

        mask = data_set.isin(rule).all(axis=1)
        rule_coverage_indexes = data_set[mask].index.values
        rule_coverage_dataframe = data_set[mask]
    
        # #iterate over dataframe rows
        # for index,row in data_set.iterrows():
        # 	if self.check_rule_datapoint(row, complex):
        # 		coverage.append(index)
        

        #import ipdb;ipdb.set_trace(context=8)
        return rule_coverage_indexes, rule_coverage_dataframe


    def build_rule(self,passed_complex):
        """
        build a rule in dict format where target attributes have a single value and non-target attributes
        have a list of all possible values. Checks if there are repetitions in the attributes used, if so
        it returns False
        """
        atts_used_in_rule = []
        for selector in passed_complex:
            atts_used_in_rule.append(selector[0])
        set_of_atts_used_in_rule = set(atts_used_in_rule)
        
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

