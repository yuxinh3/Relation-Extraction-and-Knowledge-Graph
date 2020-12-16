import numpy as np
np.random.seed(2020)
import ipdb

# given the predictions and labels, compute the F1 score in between
prediction_file = './predicted_triplets_news_spacy.txt'
label_file = './news_sentences-label.txt'
num_test = 80
eval_ind = list(np.arange(100)[:num_test]) #sorted(list(np.random.permutation(np.arange(100))[:num_test]))

# read predictions and labels txt files into lists
pred_lst = []
label_lst = []

for i, line in enumerate(open(prediction_file)):
    line = line.strip()
    line = line.replace('\'','')
    if ',' in line:
        trip_lst = line.split(';')
        this_pred = [trip.split(',') for trip in trip_lst]
    else: # no triplets extracted
        this_pred = []
    pred_lst.append(this_pred)

for i, line in enumerate(open(label_file)):
    line = line.strip()
    line = line.replace('\'','')
    if ',' in line:
        trip_lst = line.split(';')
        this_pred = [trip.split(',') for trip in trip_lst]
    else: # no triplets extracted
        this_pred = []
    label_lst.append(this_pred)

# only select num_test samples for evaluation, the rest are used for visualization
vis_pred_lst = [pred_lst[i] for i in range(len(pred_lst)) if i not in eval_ind]
pred_lst = [pred_lst[i] for i in range(len(pred_lst)) if i in eval_ind]
vis_label_lst = [label_lst[i] for i in range(len(label_lst)) if i not in eval_ind]
label_lst = [label_lst[i] for i in range(len(label_lst)) if i in eval_ind]

# compare the predicted triplets and labeled triplets, and calculate single F1 score over all samples
############### Note that: #matched predicted triplets isn't necessarily equals to #labeled triplets hit ###############
def change_word(lem, word_ori):
    """
    From SGAE repo
    Lemmatizer a word, like change 'holding' to 'hold' or
    'cats' to 'cat'
    """
    word_ori = word_ori.lower()
    word_change = lem.lemmatize(word_ori)
    if word_change == word_ori:
        word_change = lem.lemmatize(word_ori,'v')
    return word_change

def trip_list_lemma(trip_list, lemmatizer):
    """
    Input a list of triplets. Lemmatization on each single word. Return the list after lemmatization.
    """
    trip_list_l = []
    for trip in trip_list:
        lemma_trip = []
        for wd in trip:
            if len(wd.split()) == 1: # single word
                lemma_wd = lemmatizer(wd)
            else: # multiple words with spaces
                after_process = [lemmatizer(each_w) for each_w in wd.split()]
                lemma_wd = ''
                for l_wd in after_process:
                    lemma_wd = lemma_wd + l_wd + ' '
                lemma_wd = lemma_wd.strip()
            lemma_trip.append(lemma_wd)
        trip_list_l.append(lemma_trip)
    return trip_list_l

def wd_list_match(list1, list2):
    # match each word between 2 lists by direct string matching
    num_match = len([wdd for wd in list1 for wdd in list2 if wdd in wd or wd in wdd])
    if num_match != 0:
        return True
    else:
        return False

def triplet_match(pred_trip, label_trip, lemmatizer):
    """
    Input 2 lists of triplets
    Return a 2-D binary matrix beween these triplets
    exactly match: the lemma can be matched exactly
    loose match: the lemma can be matched partly; since the words are parsed from a sentence, it's highly likely a correct match
    """
    pred_label_mtx = np.zeros((len(pred_trip), len(label_trip)))
    # lemmatization on each single word
    pred_trip_l = trip_list_lemma(pred_trip, lemmatizer) #[[lemmatizer(wd) for wd in trip] for trip in pred_trip] #
    label_trip_l = trip_list_lemma(label_trip, lemmatizer) #[[lemmatizer(wd) for wd in trip] for trip in label_trip] #

    # match each entity
    for i, this_pred_trip in enumerate(pred_trip_l): # per predicted triplet
        for j, this_label_trip in enumerate(label_trip_l): # per label triplet
            # exactly match
            if this_pred_trip[0] == this_label_trip[0] and \
               this_pred_trip[1] == this_label_trip[1] and \
               this_pred_trip[2] == this_label_trip[2]:
               pred_label_mtx[i,j] = 1
               # print('exact match:')
               # print('prediction:',pred_trip[i])
               # print('label:',label_trip[j])
            # loose match
            else:
                pred_subj_wd = this_pred_trip[0].split()
                label_subj_wd = this_label_trip[0].split()
                pred_rel_wd = this_pred_trip[1].split()
                label_rel_wd = this_label_trip[1].split()
                pred_obj_wd = this_pred_trip[2].split()
                label_obj_wd = this_label_trip[2].split()
                if wd_list_match(pred_subj_wd, label_subj_wd) and \
                    wd_list_match(pred_rel_wd, label_rel_wd) and \
                    wd_list_match(pred_obj_wd, label_obj_wd):
                    pred_label_mtx[i,j] = 1
                    # print('loose match:')
                    # print('prediction:',pred_trip_l[i])
                    # print('label:',label_trip_l[j])

    not_match_ind = (np.max(pred_label_mtx, axis=0) == 0).nonzero()[0]
    if not_match_ind.shape[0] > 0:
        print("all predications and not-matched labels:")
        print('prediction:',pred_trip_l)
        print('label:',[item for i, item in enumerate(label_trip_l) if i in not_match_ind])
        pass

    return pred_label_mtx

# init lemmatizer from NLTK WordNet
from nltk.stem import WordNetLemmatizer
from functools import partial
lem = WordNetLemmatizer()
lemmatizer = partial(change_word, lem)

# evaluate performance
num_matched_pred = []
num_matched_label = []
num_pred_lst = []  
num_label_lst = [] 
for sample_i, (pred, label) in enumerate(zip(pred_lst, label_lst)): # per sentence
    print(sample_i)
    if len(pred) != 0 and len(label) != 0:
        mat = triplet_match(pred, label, lemmatizer)  # return a 2-D binary numpy matrix shaped [num_pred, num_gt]
        num_matched_pred.append(np.max(mat, axis=1).nonzero()[0].shape[0])
        num_matched_label.append(np.max(mat, axis=0).nonzero()[0].shape[0])
        num_pred_lst.append(mat.shape[0])
        num_label_lst.append(mat.shape[1])
    elif len(pred) != 0 and len(label) == 0: # label is empty
        num_matched_pred.append(0)
        num_matched_label.append(0)
        num_pred_lst.append(len(pred))
        num_label_lst.append(0)
    elif len(pred) == 0 and len(label) != 0: # prediction is empty
        num_matched_pred.append(0)
        num_matched_label.append(0)
        num_pred_lst.append(0)
        num_label_lst.append(len(label))
    else:
        pass

precision = np.sum(num_matched_pred) / float(np.sum(num_pred_lst))
recall = np.sum(num_matched_label) / float(np.sum(num_label_lst))
f1_score = 2 * (precision * recall) / (precision + recall)

print('precision is {}%'.format(precision*100))
print('recall is {}%'.format(recall*100))
print('f1_score is {}%'.format(f1_score*100))




