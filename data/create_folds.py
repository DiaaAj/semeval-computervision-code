import os
import json
import random

if __name__ == '__main__':
    how_many_folds = 6
    use_fold_zero_from_old = False
    use_dev_set = False

    label_file = os.path.join('training_set_task3', 'task3DataAugmented.txt')
    with open(label_file, 'r', encoding='utf8') as f:
        targets_train = json.load(f)

    label_file_dev = os.path.join('dev_set_task3', 'dev_set_task3.txt')
    with open(label_file_dev, 'r', encoding='utf8') as f:
        targets_dev = json.load(f)

    train_ids = [x['id'] for x in targets_train]
    dev_ids = [x['id'] for x in targets_dev]

    folds = {}
    folds[0] = dev_ids
    folds[1] = train_ids
    
    print(folds)

    # dump on file
    out_file = 'folds.json'
    with open(out_file, 'w') as f:
        json.dump(folds, f)
    print('DONE')

