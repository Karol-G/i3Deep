from skimage.segmentation._watershed import watershed
from i3Deep import utils
import os
from evaluate import evaluate
import numpy as np
from tqdm import tqdm

def compute_predictions(image_path, mask_path, gt_path, save_path, nr_modalities, class_labels):
    image_filenames = utils.load_filenames(image_path)[::nr_modalities]
    mask_filenames = utils.load_filenames(mask_path)

    for i in tqdm(range(len(image_filenames))):
        image, affine, spacing, header = utils.load_nifty(image_filenames[i])
        mask, _, _, _ = utils.load_nifty(mask_filenames[i])
        labels = np.unique(mask)
        # labels = labels[labels > 0]
        for label in np.flip(labels):
            mask[mask == label] = label + 1
        mask = mask.astype(np.uint8)
        mask = watershed(image=image, markers=mask)
        for label in labels:
            mask[mask == label + 1] = label
        utils.save_nifty(save_path + os.path.basename(mask_filenames[i][:-12] + ".nii.gz"), mask, affine, spacing, header, is_mask=True)
    results = evaluate(gt_path, save_path, class_labels)
    return results