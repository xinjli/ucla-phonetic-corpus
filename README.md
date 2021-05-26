# UCLA Phonetic Corpus

This repository contains instructions of the dataset described in our ICASSP 2021 paper `MULTILINGUAL PHONETIC DATASET FOR LOW RESOURCE SPEECH RECOGNITION`.


We would also distribute scripts and baselines here in the future.


If you have any suggestions or find any mistakes in the dataset, please feel free to send email to us (xinjianl [at] cs.cmu.edu) or submit an issue in this repo. Thanks!


## Instructions

Since the entire dataset is too large to be uploaded to Github, we only provide a sample of the first language (`abk`) in this repository. The full dataset can be downloaded [here](https://www.pyspeech.com/static/data/ucla_phonetic_corpus.tar.gz). 


It is a cleaned version of the dataset in the paper. Each directory on the top level is corresponding to a language name identified by its 3 character ISO id. There are currently 97 languages in this dataset.


Inside each directory, there will be 1 file and 1 directory

- `text`: it contains the narrow phone annotations of each utterance. The first field is the utterance id.
- `audio`: it contains all the wav format audios of each utterance. Its name is the corresponding utterance id.


## Acknowledgements

This dataset is derived from the [UCLA Phonetics Lab Archive](http://archive.phonetics.ucla.edu/). The website contains much more data and resources than we could clean in this dataset. Thank you UCLA Phonetics Lab Archive!

## Reference

If you find this work helpful, please cite the following paper

```
Li, Xinjian, et al. "Multilingual phonetic dataset for low resource speech recognition." ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2021.
```