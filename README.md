# UCLA Phonetic Corpus

This repository contains instructions of the dataset described in our ICASSP 2021 paper `MULTILINGUAL PHONETIC DATASET FOR LOW RESOURCE SPEECH RECOGNITION`.


We would also distribute scripts and baselines here in the future.


If you have any suggestions or find any mistakes in the dataset, please feel free to send email to us (xinjianl [at] cs.cmu.edu) or submit an issue in this repo. Thanks!


## Instructions

Since the entire dataset is too large to be uploaded to Github, we only provide a sample of the first language (`abk`) in this repository. The full dataset can be downloaded from the [release page](https://github.com/xinjli/ucla-phonetic-corpus/releases/tag/v1.0)

It is a cleaned version of the dataset in the paper. Each directory on the top level is corresponding to a language name identified by its 3 character ISO id. There are currently 97 languages in this dataset.

Inside each directory, there will be 3 files and 1 directory

- `raw`: it contains the narrow phone annotations of each utterance. The first field is the utterance id.
- `text.txt`: it contains the segmented and normalized transcription from the raw utterance.
- `inventory`: it is directory contains the unique phoneme/phone inventory for this language. It is derived from `text.txt`
- `audio`: it contains all the wav format audios of each utterance. Its name is the corresponding utterance id.

## Acknowledgements

This dataset is derived from the [UCLA Phonetics Lab Archive](http://archive.phonetics.ucla.edu/). The website contains much more data and resources than we could clean in this dataset. Thank you UCLA Phonetics Lab Archive!

## License

Contents of this dataset and the original website are licensed under a [Creative Commons license](https://creativecommons.org/licenses/by-nc/2.0/). You are free to copy, distribute, or adapt these materials for noncommercial purposes, under the following conditions:

- For any reuse or distribution, you must make clear to others the license terms of this work.
- Any derivative work may be distributed only under a license identical to this one. That is, you cannot claim exclusive right to any creation based on these materials, nor can anyone who further adapts your creation.
- Please attribute the material to the UCLA Phonetics Lab Archive (and this paper). See below for suggested citation format.


## Reference

If you find this work helpful, please cite the following papers

```
@inproceedings{li2021multilingual,
  title={Multilingual phonetic dataset for low resource speech recognition},
  author={Li, Xinjian and Mortensen, David R and Metze, Florian and Black, Alan W},
  booktitle={ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={6958--6962},
  year={2021},
  organization={IEEE}
}

2007. The UCLA Phonetics Lab Archive. Los Angeles, CA: UCLA Department of Linguistics. http://archive.phonetics.ucla.edu/.
```