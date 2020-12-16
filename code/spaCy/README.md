# spaCy relation extraction


## Introduction
**spaCy** is an open-source software library for advanced natural language processing supporting multi-languages. spaCy provides lots of linguistic annotations, including word types, dependencies, and relations between words, so that user could get an overview into a text’s grammatical structure. For example, if you’re analyzing text, spaCy will check whether a noun is the subject of a sentence, or the object – or whether a word is used as a verb, or refers to the noun in specific context.


## Method (Pipeline)
The parsing is performed in three steps:
1. find all the noun chunks as the entities, and resolve the modifiers on them.
2. determine the subject of verbs (including nsubj, acl and pobjpass). 
3. determine all the relations among entities.


### Resources for checking tagging/dependencies in spaCy
- Pos Tagging: [link](https://spacy.io/usage/linguistic-features#pos-tagging)
- Dependency Parse: [link](https://spacy.io/api/annotation#dependency-parsing), [link](https://spacy.io/usage/linguistic-features#dependency-parse)
- Named Entities: [link](https://spacy.io/usage/linguistic-features#named-entities)
- Entity Linking: [link](https://spacy.io/usage/linguistic-features#entity-linking)
- Tokenization: [link](https://spacy.io/usage/linguistic-features#tokenization)
- Merging and Splitting: [link](https://spacy.io/usage/linguistic-features#retokenization)
- Sentence Segmentation: [link](https://spacy.io/usage/linguistic-features#sbd)

### Code Reference
[link](https://github.com/vacancy/SceneGraphParser/tree/04daa9f464355c5e4575cf85020e49fa1abe1df1)

## Usage Example
> A woman is playing the piano in the room.
```
pip install spacy
python -m spacy download en_core_web_sm
import sng_parser
graph = sng_parser.parse('A woman is playing the piano in the room.')
```
The graph is:
```
{'entities': [{'head': 'woman', 
               'lemma_head': 'woman',
               'lemma_span': 'a woman',
               'modifiers': [{'dep': 'det', 'lemma_span': 'a', 'span': 'A'}],
               'span': 'A woman'},
              {'head': 'piano',
               'lemma_head': 'piano',
               'lemma_span': 'the piano',
               'modifiers': [{'dep': 'det',
                              'lemma_span': 'the',
                              'span': 'the'}],
               'span': 'the piano'},
              {'head': 'room',
               'lemma_head': 'room',
               'lemma_span': 'the room',
               'modifiers': [{'dep': 'det',
                              'lemma_span': 'the',
                              'span': 'the'}],
               'span': 'the room'}],
 'relations': [{'object': 1, 'relation': 'playing', 'subject': 0},
               {'object': 2, 'relation': 'in', 'subject': 0}]}
```
```
sng_parser.get_prediction(graph) # get triplets from the sentence
```
```
woman,playing,piano;woman,in,room
```
The generated graph follows the rules:
```
{
  'entities': [  # a list of entities
    {
      'span': "the full span of a noun phrase",
      'lemma_span': "the lemmatized version of the span",
      'head': "the head noun",
      'lemma_head': "the lemmatized version of the head noun",
      'modifiers': [
        {
          'dep': "the dependency type",
          'span': "the span of the modifier",
          'lemma_span': "the lemmatized version of the span"
        },
        # other modifiers...
      ]
    },
    # other entities...
  ],
  
  'relations': [  # a list of relations
    # the subject and object fields are sometimes called "head" and "tail" in relation extraction papers.
    {
      'subject': "the entity id of the subject",
      'object': "the entity id of the object",
      'relation': "the relation"
    }
    # other relations...
  ]
}
```
