import pandas as pd
import csv
import numpy as np
import json
from lxml import html
from lxml import objectify
import requests
import time



def save_json(dict):
    jsons = json.dumps(dict)
    f = open("data.json","w")
    f.write(jsons)
    f.close()

# helper function for get requests
def get(url, headers):
    # sleep to add variable pauses in requests
    delay = np.random.randint(60)
    time.sleep(delay)
    #request then convert data into html element
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    return tree

