# Notes for SPICE:

## Folders
`data` folder includes the input sentences and labeled triplets. `predictions` folder includes the extracted triplets `extracted_triplets.txt` which are read from the generated json file `sg.json`. `spice` folder stores all the code for SPICE. `edu` folder isn't used in this relation extraction project and the details can be viewed in Code Source below.

## Instruction
0. Environment: python 2.7, refer to SGAE installation for the other dependency.

1. First, run `bash get_stanford_models.sh` to download the Stanford CoreNLP 3.6.0 code and models for SPICE.

2. Second, run `python parse_sentence.py`. It will obtain `spice/sg.json` which contains the parsed subject, relation, object and attributes, read the parsed triplets from `spice/sg.json`, and finally write them into `extracted_triplets.txt` file.

3. Third, each line in `extracted_triplets.txt` file corresponds to one input sentence. If a line is empty, it means there isn't any triplets extracted from the sentence.

## Code Source

1. The code within the `edu` folder is uncompressed from the revised spice-1.0.jar in project [SGAE](https://github.com/yangxuntu/SGAE#generating-scene-graphs). The original coco-caption file [spice-1.0.jar](https://github.com/YiwuZhong/Sub-GC/blob/master/misc/coco-caption/pycocoevalcap/spice/spice-1.0.jar) was revised in SGAE project, by adding functions to export the parsed subject, relation, object and attributes. More details for added functions can be viewed in [commit-'revised spice from SGAE'](https://github.com/YiwuZhong/STAT-451-Project/commit/04cc0bf48895910b6ea268e626e1b3f1d1f0a20c).

2. The above instruction starts from the SGAE code, including `get_stanford_models.sh`, `spice` folder, `create_coco_sg.py`, and `process_spice_sg.py`. `parse_sentence.py` is the main file that was adapted from `create_coco_sg.py` and `process_spice_sg.py`.

3. TODO: whether needs tokenizer as coco-caption?