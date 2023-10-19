import numpy as np
import pandas as pd
import json
import csv

# Take the incoming JSON data and write it to a pandas dataframe
# example JSON data: {"data": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25 }]}
def process_data(json_data):
    # Load the JSON data into a dictionary
    data_dict = json.loads(json_data)
    
    # Extract the data array from the dictionary
    data_array = data_dict['data']
    
    # Convert the data array to a pandas dataframe
    df = pd.DataFrame(data_array)
    
    return df

