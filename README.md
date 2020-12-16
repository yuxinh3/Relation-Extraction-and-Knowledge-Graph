# STAT 451 Project
This repo is for STAT 451 course project -- knowledge graph construction & sentence triplet extraction.

[Google doc for meeting](https://docs.google.com/document/d/1ct8JyxPd-bLGz95hA_hSOymbX6vF5OCDo_7FzTqo32o/edit?usp=sharing)

[Google slides](https://docs.google.com/presentation/d/13g8NIbUJd10DpsnG6OC40j3V7dr2XYpM/edit#slide=id.p1)

## Folder Struture
1. `code`: stores the code and instructions for each tool.

2. `data`: stores the collected sentences and their triplet annotations.

3. `predictions`: stores the extracted triplets using each tool on each data source, with the same format with triplet annotations.

4. `evaluation`: stores the evaluation code that takes the triplet annotations and predictions as inputs.

5. `visualization`: stores the code and instructions for visualizing the extracted triplets.

6. `slides and reports`: stores the presentation slides and project reports.

## Tool List:
1. spaCy: [scene graph parser with Python and spaCy](https://github.com/vacancy/SceneGraphParser), [tutorial 1](https://www.analyticsvidhya.com/blog/2019/09/introduction-information-extraction-python-spacy/), [tutorial 2]( https://github.com/bdmarius/python-knowledge-graph/)

2. Stanford OpenIE: [tutorial](https://github.com/philipperemy/Stanford-OpenIE-Python)

3. [SPICE](https://arxiv.org/pdf/1607.08822.pdf) that uses [Stanford Scene Graph Parser](https://nlp.stanford.edu/software/scenegraph-parser.shtml)

## Performance (precision / recall / F1 (%)):
Correct prediction: the predicted triplet is correct when its subject, relation, and object words can be matched to one of the labeled triplet at the same time.

Process: apply lemmatization on each single word and return the basic form (lemma) --> match the words using the string of lemma 

(1) Exact matching: the lemma of prediction is exactly the same as the lemma of label
| Methods \ Data Sources | News | Novel | Caption |
| :-----: |:--------:| :-----:| :-----:|
| spaCy | 18.60 / 16.49 / 17.49  | 19.53 / 17.01 / 18.18  | 37.68 / 32.30 / 34.78 |
| OpenIE | 8.02 / 19.59 / 11.38 | 23.81 / 47.62 / 31.75  | 19.87 / 19.25 / 19.56 | 
| SPICE | 13.08 / 14.43 / 13.73  | 1.50 / 1.36 / 1.43     | 34.51 / 30.43 / 32.34 | 


(2) Exact matching + loose matching: the lemma of prediction is exactly the same as the lemma of label, or the lemma of prediction has overlapping strings with the lamma of label
| Methods \ Data Sources | News | Novel | Caption |
| :-----: |:--------:| :-----:| :-----:|
| spaCy | 40.70 / 36.08 / 38.25  | 40.70 / 36.08 / 38.25  | 57.25 / 50.31 / 53.55 |
| OpenIE | 59.49 / 52.58 / 55.82 | 59.49 / 52.58 / 55.82  | 83.33 / 49.07 / 61.77 | 
| SPICE | 28.97 / 29.90 / 29.43  | 26.32 / 22.45 / 24.23  | 52.82 / 47.20 / 49.85 | 
