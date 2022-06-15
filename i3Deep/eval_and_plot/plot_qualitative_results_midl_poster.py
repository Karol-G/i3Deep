import matplotlib.pyplot as plt
import numpy as np
from i3Deep import utils
import os
from os.path import join

# def plot():
#     for i, task in enumerate(tasks):
#         filenames = utils.load_filenames(base_path + task + "/qualitative_results/cropped/")
#         fig = plt.figure(constrained_layout=True)
#         gs = fig.add_gridspec(2, 3)
#         # gs.update(wspace=0.0025, hspace=0.0025)  # set the spacing between axes.
#         for j, filename in enumerate(filenames):
#             image = plt.imread(filename)
#             method = os.path.basename(filename)[:-4]
#             name = methods[method]
#             ax = fig.add_subplot(gs[gridspec_indices[method][0], gridspec_indices[method][1]])
#             ax.imshow(image)
#             ax.set_title(name)
#             ax.axes.xaxis.set_visible(False)
#             ax.axes.yaxis.set_visible(False)
#             ax.axis('off')
#         # plt.tight_layout()
#         # plt.margins(0, 0)
#         plt.suptitle(task_names[i], fontsize=16)
#         # plt.show()
#         plt.savefig(base_path + "qualitative_results/" + task_names[i] + ".png", bbox_inches='tight')
#         plt.clf()

def plot():
    grid_size = (2, 3)
    # fig = plt.figure(figsize=(8, 8))
    # gs = fig.add_gridspec(3, 3, width_ratios=[0.1, 0.3, 0.3])
    # gs = fig.add_gridspec(3, 3)
    # gs.update(wspace=0.0025, hspace=0.0025)  # set the spacing between axes.
    for i, task in enumerate(tasks):
        # gs = fig.add_gridspec(*grid_size)
        fig, axs = plt.subplots(*grid_size)
        for j, method in enumerate(methods):
            image = plt.imread(join(base_path, task, "qualitative_results", "cropped", method + ".png"))
            name = methods[method]
            # x = slice(i, i + 1)
            if j < grid_size[1]:
                # x = slice(0, 1)
                # y = slice(j, j + 1)
                x = 0
                y = j
                # x = j
                # y = 0
            else:
                # x = slice(1, 2)
                # y = slice(j - grid_size[0], j + 1 - grid_size[0])
                x = 1
                y = j - grid_size[1]
                # x = j - grid_size[0]
                # y = 1
            print("j: {}, x: {}, y: {}".format(j, x, y))
            # ax = fig.add_subplot(gs[x, y])
            axs[x][y].imshow(image)
            axs[x][y].set_title(name)
            axs[x][y].axes.xaxis.set_visible(False)
            axs[x][y].axes.yaxis.set_visible(False)
            axs[x][y].axis('off')
        # plt.tight_layout()
        # plt.margins(0, 0)
        # plt.suptitle(task_names[i], fontsize=16)
        # # plt.show()
        # plt.subplots_adjust(wspace=0, hspace=0)
        fig.savefig(base_path + "qualitative_results/" + task + "_highres.svg", bbox_inches='tight')
        plt.clf()


if __name__ == '__main__':
    base_path = "C:/Users/k539i/Documents/syncthing-DKFZ/My Papers/i3Deep/Evaluation results & Overleaf/Results/"
    tasks = ["Task002_BrainTumour_guided"]
    task_names = ["Brain Tumor", "Pancreas", "COVID-19"]
    methods = {"gt": "Ground Truth", "automatic": "Preseg.", "my_method": "i3Deep", "P_Net": "P-Net", "watershed": "Watershed", "random_walker": "Random Walker"}
    plot()
