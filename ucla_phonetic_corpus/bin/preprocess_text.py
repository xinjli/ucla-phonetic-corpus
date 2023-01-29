from phonepiece.ipa import read_ipa
from pathlib import Path
from phonepiece.inventory import read_inventory, create_inventory, write_inventory
import shutil
from tqdm import tqdm
import editdistance
import os

if __name__ == '__main__':

    data_dir = Path('./data/')

    ipa = read_ipa()

    # run recognition
    for lang_dir in data_dir.glob('*'):

        lang_id = lang_dir.name

        print("Processing ", lang_id)

        raw_file = open(lang_dir / 'raw', 'r')
        text_file = open(lang_dir / 'text.txt', 'w')

        phoneme_set = set()

        for line in raw_file:
            fields = line.strip().split()
            phonemes = " ".join(fields[1:])
            utt_id = fields[0]
            phonemes = ipa.tokenize(phonemes)
            phoneme_set.update(phonemes)

            text_file.write(utt_id+' ' + ' '.join(phonemes)+'\n')

        inv = create_inventory(lang_id, phoneme_set)
        write_inventory(inv, lang_dir / 'inventory')

        text_file.close()