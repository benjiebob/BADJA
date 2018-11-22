# BADJA

<img src="gifs/bear.gif" width="24%" height="24%"> <img src="gifs/camel.gif" width="24%" height="25%"> <img src="gifs/cows.gif" width="24%" height="24%"> <img src="gifs/rs_dog.gif" width="24%" height="24%">

BADJA is the Benchmark Animal Dataset of Joint Annotations released with the paper [Creatures Great and SMAL: Recovering the shape and motion of animals from video](https://arxiv.org/abs/1811.05804). If you use this dataset, please consider citing this work:

```
@inproceedings{biggs2018creatures,
  title={{C}reatures great and {SMAL}: {R}ecovering the shape and motion of animals from video},
  author={Biggs, Benjamin and Roddick, Thomas and Fitzgibbon, Andrew and Cipolla, Roberto},
  booktitle={ACCV},
  year={2018}
}
```

Annotations in are provided in this repository as *.json files for a total of 9 video sequences.
1. Seven video sequences from [DAVIS 2017 Video Segmentation dataset](https://arxiv.org/abs/1704.00675) (Pont-Tuset et al. 2017),
2. Two video sequences provided in extra_videos which were sourced by hand. 

Note that raw frames for the tiger and cat sequences have been necessarily omitted from the extra_videos repository due to licensing restrictions.

We annotate 20 joints which are related to positions on the SMAL quadruped mesh (Zuffi et al. 2018) defined in `smal_CVPR2018.pkl'. This can be downloaded from the [SMALR](http://smalr.is.tue.mpg.de/) page.

The position of the first 16 joints (legs, neck, and tail) are given by SMAL model joints. The remainder (nose tip, chin, left ear and right ear) relate to specific SMAL vertices.

| Position            | SMAL Vertex ID | 
| ---------------- | -----| 
| Nose Tip  | 1863 | 
| Chin  | 26 | 
| Left Ear  | 149 | 
| Right Ear  | 2124 |

Annotations are provided approximately every 5 video frames with the exception of rs_dog which is annotated densely.

More detail on which SMAL joints have been annotated can be found in code/joint_catalog.py. The code folder also contains a Python script that displays annotated frames across the dataset.

## Installation
1. Clone the repository
   ```
   git clone https://github.com/benjiebob/BADJA.git
    
2. Download [DAVIS 2017 TrainVal Full-Resolution](https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-trainval-Full-Resolution.zip) image and annotation frames and unpack      to location "BADJA/DAVIS"

3. Download [Extra Videos](http://mi.eng.cam.ac.uk/~bjb56/datasets/badja_extra_videos.zip) and unpack to location `BADJA/extra_videos'

4. Test everything is correctly located and working properly. Demo code requires [numpy](https://pypi.org/project/numpy/), [scipy](https://pypi.org/project/scipy/), [opencv](https://pypi.org/project/opencv-contrib-python/) and [matplotlib](https://pypi.org/project/matplotlib/).
   ```
   python code/view_badja.py
   ```

## Contribute
Please create a pull request or submit an issue if you would like to contribute.





