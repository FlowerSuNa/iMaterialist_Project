
# https://www.kaggle.com/shivamb/imaterialist-fashion-eda-object-detection-colors
# https://www.kaggle.com/djuuuu/imaterialist-object-detection-colors-eda

# Import Library
from IPython.core.display import HTML
from IPython.display import Image
from collections import Counter
import pandas as pd
import json
import requests


from plotly.offline import init_notebook_mode, iplot
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from wordcloud import WordCloud
from plotly import tools
import seaborn as sns
from PIL import Image

import tensorflow as tf
import numpy as np

init_notebook_mode(connected=True)
%matplotlib inline


# Load Data
train = open('train.json').read()
train = json.loads(train)

print(train)    # {url, imageId} , {labelId, imageId}

valid = open('validation.json').read()
valid = json.loads(valid)

print(valid)    # {url, imageId} , {labelId, imageId}

test = open('test.json').read()
test= json.loads(test)

print(test)     # {url, imageId}


#
def get_states(data):
    total_images = len(data['images'])
    
    all_annotations = []
    
    if 'annotations' in data:
        for each in data['annotations']:
            all_annotations.extend(each['labelId'])
    
    total_labels = len(set(all_annotations))
    return total_images, total_labels, all_annotations


total_images, total_labels, train_annotations = get_states(train)
print('Total Image in the train : ', total_images)      # 1,014,544
print('Total Labels in the train : ', total_labels)     # 228


total_images, total_labels, valid_annotations = get_states(valid)
print('Total Image in the valid : ', total_images)      # 9,897
print('Total Labels in the valid : ', total_labels)     # 225


total_images, total_labels, test_annotations = get_states(test)
print('Total Image in the test : ', total_images)       # 39,706
print('Total Labels in the test : ', total_labels)      # 0



train_file = requests.get()


#
train_labels = Counter(train_annotations)

x = list(train_labels.keys())
y = list(train_labels.values())

trace = go.Bar(x=x, y=y, opacity=0.8, name='count', marker=dict(color='rgba(20,20,20,1)'))
layout = dict(width=800, title='Distribution of different labels in the train dataset', 
              legend=dict(orientation='h'))
fig = go.Figure(data=[trace], layout=layout)
iplot(fig)


#
def get_image_url(imgid, data):
    for each in data['images']:
        if each['imageId'] == imgid:
            return each['url']

