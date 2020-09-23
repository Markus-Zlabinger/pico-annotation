# Annotation of Participants, Interventions, and Outcomes
This repository contains the code and the annotation interfaces for our experiments on data annotation of Participants, Interventions, and Outcomes (referred to as PICO task). 

## Dataset
For 423 sentences, following sets of annotations are available:

Name | Description | #Redundant annotations per Sentence | #Workers
------------ | ------------- | ------------- | ------------- 
Baseline | Annotations were initially collected for entire abstracts, which were then segmented into sentences. | 8-17 |  403
SenBase | Annotations collected on a sentence-level | 3 | 38 
SenSupport (also referred to as DEXA) | Annotations collected on a sentence-level. In addition to SenBase, crowdworkers are supported by showing similar sentences as examples. | 3 | 31 
Expert | Annotations collected by medical experts | 3 | 3 

Note that the annotations for *Baseline* and *Expert* were download from the [GitHub Repository for Nye et al. 2018](https://github.com/bepnye/EBM-NLP). More details on 
their annotation approach can be found in the [ACL2018 paper](https://www.aclweb.org/anthology/P18-1019/).

The annotations for *Baseline*, *SenBase*, and *SenSupport* were collected from workers 
of the Mechanical Turk marketplace.

### Annotations format
You find the different annotation sets for the 423 sentences in the subfolder *data/annotations/*. The annotations are linked to sentences, identified by a unique sentence id (senid).
The senids are in following format **PMID:SENIDX**, describing a PubMedID (PMID) and the index of the sentence (SENIDX). The sentence texts for each senid can be found in *data/sentences.json*. To split a sentence into tokens that align with the annotation sets, you can simply split the sentence by whitespace.

The annotations sets are in following JSON-format:
```
"7831628:5": {
    "annotations": [
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ],
        ...,
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    ],
    "wids": [
        293,
        ...,
        295
    ]
},
....
```
Notice that the JSON files contain the token-level annotations (annotations) for each sentence id and the ids of the worker (wids)
who created the label.

### Computing Kappa Scores
In *evaluation.py*, you find an example code to compute Kappa scores between the different sets of annotations.
When running this script, you should get following output:

```
[1] python evaluation.py

Cohen's Kappa scores to the gold standard labels
===================================
Cohen's Kappa Score participants baseline 0.760
Cohen's Kappa Score participants senbase 0.715
Cohen's Kappa Score participants sensupport 0.780

Cohen's Kappa Score interventions baseline 0.476
Cohen's Kappa Score interventions senbase 0.675
Cohen's Kappa Score interventions sensupport 0.757

Cohen's Kappa Score outcomes baseline 0.343
Cohen's Kappa Score outcomes senbase 0.655
Cohen's Kappa Score outcomes sensupport 0.694
```

The code contains a function to aggregate individual annotations using majority voting. 
For more advanced aggregation methods, we provided the worker ids (wids). The implementation of Dawid-Skene that we used in our paper can be found at 
https://github.com/dallascard/dawid_skene

## Annotation Interfaces
The source code of the annotation interfaces is available in the *annotation_instructions* sub-folder 
of this repository. The sub-folder contains:

* senbase_mturk_designlayout.html: The Mechanical Turk layout design for the SenBase approach.
* sensupport_mturk_designlayout.html: The Mechanical Turk layout design for the SenSupport approach.
* mturk_batch_examples: This folder contains example batches that can be uploaded on the Mechanical Turk platform. The batches 
are compatible with the design layout of SenBase and SenSupport.
* annotation_instructions: This folder contains the annotation instructions for Participants, Interventions, and Outcomes. 
These instructions conform with the instructions of [Nye et al.](https://www.aclweb.org/anthology/P18-1019/), however, are more comprehensive.

We derived the Mechanical Turk layout design from the design of https://github.com/Varal7/ieturk. 

To test our layout designs, you can 
use the Sandbox mode of the Mechanical Turk platform https://requestersandbox.mturk.com/, which is free of charge. You first need to create a new project where 
you copy-paste the design layout, e.g., from *senbase_mturk_designlayout.html*. Afterwards, you need to upload a batch, e.g., *batch_participants.csv*.

A screenshot of the SenBase interface is illustrated below:
![SenBase Annotation Tool](annotation_interfaces/interface_senbase.JPG?raw=true "SenBase Annotation Interface")

A screenshot of the SenSupport interface is illustrated below:
![SenSupport Annotation Tool](annotation_interfaces/interface_sensupport.JPG?raw=true "SenSupport Annotation Interface")

## Contact Us
If you have any further questions, open a new issue in this repository.

## Publication
More details on this project can be found in the following two papers:
```
@inproceedings{zlabinger2020crowd,
  title={Effective Crowd-Annotation of Participants, Interventions, and Outcomes in the Text of Clinical Trial Reports},
  author={Zlabinger, Markus and Sabou, Marta and Hofst\"{a}tter, Sebastian and Hanbury, Allan},
  booktitle={Conference on Empirical Methods in Natural Language Processing (EMNLP-Findings 2020)},
  year={2020},
}
```

```
@inproceedings{zlabinger2020dexa,
  title={DEXA: Supporting Non-Expert Annotators with Dynamic Examples from Experts},
  author={Zlabinger, Markus and Sabou, Marta and Hofst\"{a}tter, Sebastian and Sertkan, Mete and Hanbury, Allan},
  booktitle={Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval},
  pages={2109–2112},
  year={2020}
}
```

