from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np

import time
import os

import sys
from spice.spice import Spice

# 1. parse sentence using SPICE and save the parsed information into json file (adapted from create coco_sg.py)
data_path = './data/caption_sentences.txt'
sent_list = [item for item in open(data_path, 'r')]

gts = {}
res = {}
img_ids = []
for img_id, this_sent in enumerate(sent_list):
    gts[img_id] = []
    gts[img_id].append(this_sent)
    res[img_id] = []
    res[img_id].append('place holder')
    img_ids.append(img_id)

scorer = Spice()
score, scores = scorer.compute_score(gts, res)

# 2. extract the parsed triplets from json file (adapted from process_spice_sg.py)
from nltk.stem import WordNetLemmatizer
from functools import partial

def change_word(lem, word_ori):
    """
    Lemmatizer a word, like change 'holding' to 'hold' or
    'cats' to 'cat'
    """
    word_ori = word_ori.lower()
    word_change = lem.lemmatize(word_ori)
    if word_change == word_ori:
        word_change = lem.lemmatize(word_ori,'v')
    return word_change

lem = WordNetLemmatizer()
lemmatizer = partial(change_word, lem)

json_file_path = './spice/sg.json'
sg_json = json.load(open(json_file_path))
all_triplets = []
all_node_attr = []
t = 0
for img_id in img_ids: # per image
    t += 1
    if t % 1000 == 0:
        print("processing {0} data".format(t))
        
    sg_temp = sg_json[str(img_id)]
    rela = sg_temp['rela']
    sbj = sg_temp['subject']
    obj = sg_temp['object']
    attr = sg_temp['attribute']

    # per triplet
    this_triplet = []
    for i in range(len(rela)):
        rela_temp = rela[i].strip().lower()
        sbj_temp = sbj[i].strip().lower()
        obj_temp = obj[i].strip().lower()

        rela_temp = lemmatizer(rela_temp)
        sbj_temp = lemmatizer(sbj_temp)
        obj_temp = lemmatizer(obj_temp)
        
        this_triplet.append([sbj_temp, rela_temp, obj_temp])
    all_triplets.append(this_triplet)
    
    # per node / attribute
    this_node_attr = []
    for i in range(len(attr)):
        node_temp = attr[i][5:].strip()
        node_temp = lemmatizer(node_temp)
        this_node_attr.append(attr[i][:5] + node_temp)  # the first 5 chars are either 'node:' or 'attr:'
    all_node_attr.append(this_node_attr)


# 3. write the extracted into txt file, with each line corresponding to 1 sentence
with open('extracted_triplets.txt', 'w') as f:
    for sen_i, triplets in enumerate(all_triplets): # per sentence
        for trip_i, trip in enumerate(triplets): # per triplet
            if trip_i == 0:
                f.write(trip[0] + ',' + trip[1] + ',' + trip[2])
            else:
                f.write(';' + trip[0] + ',' + trip[1] + ',' + trip[2])
        f.write('\n')




