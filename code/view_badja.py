###########################################################################################################################
# Benjamin Biggs | bjb56@cam.ac.uk | http://mi.eng.cam.ac.uk/~bjb56/                                                      #
# Please cite `Creatures Great and SMAL: Recovering the shape and motion of animals from video' if you use this dataset   #
###########################################################################################################################

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))

from badja_data import BADJAData
from joint_catalog import SMALJointInfo
import matplotlib.pyplot as plt
import numpy as np
import cv2

def draw_joints_on_image(rgb_img, joints, visibility, region_colors, marker_types):
    joints = joints[:, ::-1] # OpenCV works in (x, y) rather than (i, j)

    disp_img = rgb_img.copy()    
    for joint_coord, visible, color, marker_type in zip(joints, visibility, region_colors, marker_types):
        if visible:
            joint_coord = joint_coord.astype(int)
            cv2.drawMarker(disp_img, tuple(joint_coord), color, marker_type, 30, thickness = 10)
    return disp_img

def main():
    smal_joint_info = SMALJointInfo()
    badja_data = BADJAData()

    data_loader = badja_data.get_loader()

    for rgb_img, sil_img, joints, visible, name in data_loader:
        rgb_vis = draw_joints_on_image(rgb_img, joints, visible, smal_joint_info.joint_colors, smal_joint_info.annotated_markers)
        sil_vis = draw_joints_on_image(sil_img, joints, visible, smal_joint_info.joint_colors, smal_joint_info.annotated_markers)

        plt.suptitle('Input image: {0}'.format(name))
        plt.subplot(121)
        plt.imshow(rgb_vis.astype(np.uint8))
        plt.subplot(122)
        plt.imshow(sil_vis.astype(np.uint8))
        plt.draw()
        plt.pause(0.5)

if __name__ == '__main__':
    main()