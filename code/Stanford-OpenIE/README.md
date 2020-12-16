# Stanford Open information extraction (open IE)

## Introduction
**Stanford Open information extraction (open IE)** is a tool that can be used to extract triples (Subject, Relation, Object) from input sentences, when the schema of the relations does not need to be specified in advance. For example, Barack Obama was born in Hawaii would create a triple (``Barack Obama``; ``was born in``; ``Hawaii``). Also,it only supports English.  

This tool is written by Gabor Angeli and Melvin Johnson Premkumar and originally coded in JAVA 8+, but in our project we will use a python wrapper written by [Phillip Peremy](https://github.com/philipperemy/Stanford-OpenIE-Python). 

More information: [here](https://nlp.stanford.edu/software/openie.html)

## Method (Pipeline)
1. Input sentence
2. split it into several clauses
3. Implement Natural Logic to capture basic form of the clauses
4. Model parse triplets from clauses generated in third step

###  Details to the 2nd step:

First, the system traverses through a dependency tree generated from the sentence. Then, this system will recurse on the dependency arcs, (1) yielding clauses if it finds one, (2) otherwise it continues to search until there are no dependencies to search. 
###  Details to the 4th step:
Having the generated and shortened clauses, the system parses them into triplets by using ``6`` dependency patterns. If there are substructures that relation extraction is still possible, then Stanford openIE implements nominal relations (``5`` dependecy and ``3`` TokensRegex surface form patterns).

## Usage
1. install the Stanford CoreNLP package to your directory
2. input sentences one by one
3. annotator will output object(s) ``triple`` with attributes ``subject``, ``relation``, and ``object``.
4. Iterate through 300 sentences and get a dataframe of all sentence triples with one line representing one sentence. 

## Source of 100 sentences
 <em>Percy Jackson and the Lightning Thief</em>, Chapter 1 & 2

[link](https://getfreestorybooks.weebly.com/uploads/1/0/7/7/107718885/riordan_rick-percy_jackson-_the_complete_series.pdf)