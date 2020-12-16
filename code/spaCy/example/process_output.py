file=open('predicted_triplets_caption_spacy_nonedit.txt','r')
file2=open('predicted_triplets_caption_spacy.txt','w')
sen=file.readlines()
file
for lines in sen:
    print(lines)
    if 'test' in lines:
        file2.write(lines[4:])
    else:
        file2.write(lines[3:])
