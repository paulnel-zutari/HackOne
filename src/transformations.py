import pandas as pdimport reclass Transformations:    def add_count_coloumn(self, data: pd.DataFrame):        """Add count coloumn if not already present"""        if 'Count' not in data.columns:            data['Count'] = 1        return data    def clean_column_headers(self, data: pd.DataFrame):        coloumns = ['Size', 'Count', 'Area', 'Surface Area']        headers = list(data.columns.values)        for header in headers:            search = re.findall(r'\w+', header)            print(header)