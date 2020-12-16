from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np

import time
import os

import sys
from spice.spice import Spice

sent_list = ['a man in tan shirt sitting at a table with food.',\
'a man who is sitting at a table with a plate of food in front of him.',\
'man sitting at a dinner table at an open restaurant.',\
'the man smiles over a table covered with plates of food.',\
'a man sitting at a table with an almost empty plate of food']

gts = {}
res = {}
for img_id, this_sent in enumerate(sent_list):
	gts[img_id] = []
	gts[img_id].append(this_sent)
	res[img_id] = []
	res[img_id].append('place holder')

scorer = Spice()
score, scores = scorer.compute_score(gts, res)

#sys.path.append("coco-caption")
#from pycocotools.coco import COCO
#from pycocoevalcap.spice.spice import Spice

# train_path = '/media/user/4T/download/SGAE-master/coco-caption/annotations/captions_train2014.json'
# val_path = '/media/user/4T/download/SGAE-master/coco-caption/annotations/captions_val2014.json'

# coco_train = COCO(train_path)
# coco_val = COCO(val_path)

# coco_use = coco_val

# image_ids = coco_use.getImgIds()

# gts = {}
# res = {}
# for img_id in image_ids:
# 	gts[img_id] = []
# 	data_temp = coco_use.imgToAnns[img_id]
# 	for dt in data_temp:
# 		gts[img_id].append(dt['caption'])
# 	res[img_id] = []
# 	res[img_id].append(gts[img_id][0])

# scorer = Spice()
# score, scores = scorer.compute_score(gts, res)