# i3Deep: Efficient 3D interactive segmentation with the nnU-Net

3D interactive segmentation is highly relevant in reducing the annotation time for experts. However, current methods often achieve only small segmentation improvements per interaction as lightweight models are a requirement to ensure near-realtime usage. Models with better predictive performance such as the nnU-Net cannot be employed for interactive segmentation due to their high computational demands, which result in long inference times. To solve this issue, we propose the 3D interactive segmentation framework i3Deep. Slices are selected through uncertainty estimation in an offline setting and afterwards corrected by an expert. The slices are then fed to a refinement nnU-Net, which significantly improves the global 3D segmentation from the local corrections. This approach bypasses the issue of long inference times by moving expensive computations into an offline setting that does not include the expert. For three different anatomies, our approach reduces the workload of the expert by 80.3%, while significantly improving the Dice by up to 39.5%, outperforming other state-of-the-art methods by a clear margin. Even on out-of-distribution data i3Deep is able to improve the segmentation by 19.3%.

## Architecture

![](images/My Framework.png)

1. The presegmentation model is used to run inference on new unseen subjects to provide presegmentations alongside uncertainties from the model.
2. A one-shot slice acquisition function selects multiple slices for each subject in axial, coronal and sagittal orientation from the 3D image based on the quantified uncertainties.
3. The acquired slices of the previous stage are sent to the expert for correction.
4. The corrected slices are projected into an empty volume back into their original positions. Then this volume is concatenated with the original image and used for inference by the refinement model, which significantly improves the segmentation (see Figure 2).

![](images/Refinement nnU-Net.jpg)


## Results

Dice score results of i3Deep against the presegmentation and multiple state-of-the-art baselines evaluated on a brain tumor, pancreas and COVID-19 dataset:

![](images/results/results.png)

### Qualitative examples

![](images/results/qualitative_results/Brain Tumor.png)

![](images/results/qualitative_results/Pancreas.png)

![](images/results/qualitative_results/COVID-19.png)