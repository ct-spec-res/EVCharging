import pandas as pd
import requests
from io import StringIO
import pyvin


# Load electric vehicle registration into a dataframe
url = "https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/ChargeNY/ny_ev_registrations.csv"# New York State Energy Research and Development Authority(NYSERDA) electric vehicle registration
def url_to_df(url):
    '''
    Input: url that downloads to a csv from online
    Output: dataframe with data url/csv
    '''
    bytes_data = requests.get(url).content# Request data into bytes format
    clean_bytes = str(bytes_data,'utf-8')# Adjust bytes data into utf-8
    data_file = StringIO(clean_bytes)# Read string into a new file
    return pd.read_csv(data_file)# Load data into pandas



df = url_to_df(url)

print(df['VIN Prefix'][1])

single_vin = df['VIN Prefix'][1] + '0000000'

print()

veh = pyvin.VIN(single_vin, error_handling=pyvin.RAISE)

# print(veh.Make, veh.Model, veh.ModelYear)

# print(df.head())



