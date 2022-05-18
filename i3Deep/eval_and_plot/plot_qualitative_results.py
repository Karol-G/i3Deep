import matplotlib.pyplot as plt
import numpy as np
from i3Deep import utils
import os

def plot():
    for i, task in enumerate(tasks):
        filenames = utils.load_filenames(base_path + task + "/qualitative_results/cropped/")
        fig = plt.figure(constrained_layout=True)
        gs = fig.add_gridspec(2, 3)
        # gs.update(wspace=0.0025, hspace=0.0025)  # set the spacing between axes.
        for j, filename in enumerate(filenames):
            image = plt.imread(filename)
            method = os.path.basename(filename)[:-4]
            name = methods[method]
            ax = fig.add_subplot(gs[gridspec_indices[method][0], gridspec_indices[method][1]])
            ax.imshow(image)
            ax.set_title(name)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            ax.axis('off')
        # plt.tight_layout()
        # plt.margins(0, 0)
        plt.suptitle(task_names[i], fontsize=16)
        # plt.show()
        plt.savefig(base_path + "qualitative_results/" + task_names[i] + ".png", bbox_inches='tight')
        plt.clf()


if __name__ == '__main__':
    base_path = "C:/Users/k539i/Documents/syncthing-DKFZ/My Papers/i3Deep/Evaluation results & Overleaf/Results/"
    tasks = ["Task002_BrainTumour_guided", "Task008_Pancreas_guided", "Task070_guided_all_public_ggo"]
    task_names = ["Brain Tumor", "Pancreas", "COVID-19"]
    methods = {"automatic": "Presegmentation", "gt": "Ground Truth", "my_method": "i3Deep", "P_Net": "P-Net", "random_walker": "Random Walker", "watershed": "Watershed", "graphcut": "GraphCut"}
    # gridspec_indices = [[slice(0, 1), slice(0, 1)], [slice(0, 1), slice(1, 2)], [slice(0, 1), slice(2, 3)], [slice(1, 2), slice(0, 1)], [slice(1, 2), slice(1, 2)], [slice(1, 2), slice(2, 3)]]
    gridspec_indices = {"gt": [slice(0, 1), slice(0, 1)],
                        "automatic": [slice(0, 1), slice(1, 2)],
                        "my_method": [slice(0, 1), slice(2, 3)],
                        "P_Net": [slice(1, 2), slice(0, 1)],
                        "watershed": [slice(1, 2), slice(1, 2)],
                        "random_walker": [slice(1, 2), slice(2, 3)],
                        "graphcut": [slice(1, 2), slice(2, 3)]}
    plot()
