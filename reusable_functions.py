import requests, io
import pandas as pd
def csv_factory(url):
    content = requests.get(url).content
    return pd.read_csv(io.StringIO(content.decode('UTF-8')))