import sng_parser
import sys


def get_prediction(sentence):
    # Here we just use the default parser.
    # sng_parser.tprint(sng_parser.parse(sentence), show_entities=False)
    sng_parser.get_triplet(sng_parser.parse(sentence))


def main():
    # get_prediction('The idea seems to be to reduce inflammation')
    file = open("caption_sentences.txt")
    sys.stdout = open('predicted_triplets_caption_spacy_nonedit.txt', 'w')
    for line in file:
        # print(line)
        get_prediction(line)
    sys.stdout.close()


if __name__ == '__main__':
    main()
