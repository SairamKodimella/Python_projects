import pandas as pd
import requests
import matplotlib as mlt
import seaborn as sns
import json
from datetime import datetime,timedelta

def get_zillow_data(location):

    #Load Json file
    with open(f'C:\vinay\Python\Zillow Analytics\API.json','r')as apifile:
        api_host_key=json.load(apifile)

    url = "https://zillow56.p.rapidapi.com/search"

    querystring = {"location":"houston, tx"}

    response = requests.get(url, headers=api_host_key, params=querystring)

    print(response.json())