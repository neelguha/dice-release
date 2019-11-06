# Script for downloading data 
import os 
import urllib.request


data_dir = "./data"


# create local data directory
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

print('Downloading food knowledge graph.. (33 MB)')
url = 'https://storage.googleapis.com/dice-data/food.zip'
urllib.request.urlretrieve(url, os.path.join(data_dir, 'food.zip'))
print('Finished!')
print()

print('Downloading food knowledge graph.. (24 MB)')
url = 'https://storage.googleapis.com/dice-data/uniform.zip'
urllib.request.urlretrieve(url, os.path.join(data_dir, 'uniform.zip'))
print('Finished!')
print()

print('Downloading the popular music knowledge graph.. (247 MB)')
url = 'https://storage.googleapis.com/dice-data/popular.zip'
urllib.request.urlretrieve(url, os.path.join(data_dir, 'popular.zip'))
print('Finished!')
print()