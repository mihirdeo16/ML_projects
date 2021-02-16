#!flask/bin/python

import os
from flask import Flask
from flask import request
import pandas as pd
import numpy as np
import config
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)


def preprocessed_data(data):
    data['listed_in'] = [re.sub(r'[^\w\s]', '', t) for t in data['listed_in']]
    data['description'] = [re.sub(r'[^\w\s]', '', t)
                           for t in data['description']]

    data['listed_in'] = [t.lower() for t in data['listed_in']]
    data['description'] = [t.lower() for t in data['description']]
    data["combined"] = data['listed_in'] + '  ' + \
        data['title'] + ' ' + data['description']
    data.drop(["description", "listed_in", "type"], axis=1, inplace=True)
    return data


df = pd.read_csv(config.TRAINING_FILE)
df = preprocessed_data(df)

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(df["combined"])
cosine_similarities = linear_kernel(matrix, matrix)
movie_title = df['title']
indices = pd.Series(df.index, index=df['title'])


def content_recommender(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return list(movie_title.loc[movie_indices])[0]


# print(content_recommender("Transformers: Robots in Disguise"))

@app.route('/isAlive')
def index():
    return "true"


@app.route('/prediction/', methods=['GET'])
def get_prediction():
    feature = str(request.args.get('f'))
    # d = dict
    d = str(content_recommender(feature))
    return d


if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80, host='0.0.0.0')
