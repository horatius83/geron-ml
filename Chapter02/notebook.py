# %%
import os
import tarfile
import urllib

DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
HOUSING_PATH = 'datasets/housing'
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + '/housing.tgz'

def fetch_housing(housing_url: str = HOUSING_URL, housing_path: str = HOUSING_PATH):
    housing_path_tokens = housing_path.split('/')
    safe_housing_path = os.path.join(*housing_path_tokens)
    if not os.path.isdir(safe_housing_path):
        os.makedirs(safe_housing_path)
    tgz_path_tokens = housing_path_tokens +  ["housing.tgz"]
    tgz_path = os.path.join(*tgz_path_tokens)
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

# %%
fetch_housing()
# %%
import pandas as pd

def load_housing_data(housing_path: str =HOUSING_PATH):
    list_tokens = housing_path.split('/') + ['housing.csv']
    csv_path = os.path.join(*list_tokens)
    return pd.read_csv(csv_path)

# %%
housing = load_housing_data()
housing.head()
# %%
housing.info()

# %%
housing['ocean_proximity'].value_counts()
# %%
housing.describe()
# %%
import matplotlib.pyplot as plt

housing.hist(bins=50, figsize=(20,15))
plt.show()
# %%
