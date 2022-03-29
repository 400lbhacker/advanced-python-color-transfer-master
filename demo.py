#dependencies:
#pip3 install opencv-python==4.2.0.34
#pip3 install numpy==1.19.3
# -*- coding: utf-8 -*-

import cv2
import os
import time



import numpy as np

from src.color_transfer import ColorTransfer, Regrain


def demo():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    img_folder = os.path.join('imgs/content')
    img_folder2 = os.path.join('imgs/style')
    img_names = [
        "1.jpg" 
        #"2.jpg", 

    ]
    ref_names = [
        "2.jpg"
       # "4.jpg", 

    ]
    out_names = [
        "output.png",
        "4.png",
        "5.png",
        "6.png"
    ]
    img_paths = [os.path.join(img_folder, x) for x in img_names]
    ref_paths = [os.path.join(img_folder2, x) for x in ref_names]
    out_paths = [os.path.join(img_folder, x) for x in out_names]
    #out = 'output'
    # cls init
    PT = ColorTransfer(n=300)
    RG = Regrain()

    for img_path, ref_path, out_path in zip(
            img_paths, ref_paths, out_paths):
        # read input img
        img_arr_in = cv2.imread(img_path)
        [h, w, c] = img_arr_in.shape
        print(f"{img_path}: {h}x{w}x{c}")
        # read reference img
        img_arr_ref = cv2.imread(ref_path)
        [h, w, c] = img_arr_ref.shape
        print(f"{ref_path}: {h}x{w}x{c}")
        # pdf transfer
        t0 = time.time()
        img_arr_col = PT.pdf_tranfer(
            img_arr_in=img_arr_in, img_arr_ref=img_arr_ref)
        print(f"pdf transfer time: {time.time() - t0:.2f}s")
        # regrain
        t0 = time.time()
        img_arr_reg = RG.regrain(
            img_arr_in=img_arr_in, img_arr_col=img_arr_col)
        print(f"regrain time: {time.time() - t0:.2f}s")
        # mean transfer
        t0 = time.time()
        img_arr_mt = PT.mean_std_transfer(
            img_arr_in=img_arr_in, img_arr_ref=img_arr_ref
        )
        print(f"mean std transfer time: {time.time() - t0:.2f}s")
        # lab transfer
        t0 = time.time()
        img_arr_lt = PT.lab_transfer(
            img_arr_in=img_arr_in, img_arr_ref=img_arr_ref)
        print(f"lab mean std transfer time: {time.time() - t0:.2f}s")
        # display
        img_arr_out = np.concatenate(
            (img_arr_in, img_arr_ref, img_arr_mt, 
             img_arr_lt, img_arr_reg), axis=1
        )
        #cv2.imwrite(out_path, img_arr_out)
        cv2.imwrite('output/img_arr_mt.png', img_arr_mt)
        cv2.imwrite('output/img_arr_lt.png', img_arr_lt)
        cv2.imwrite('output/img_arr_reg.png', img_arr_reg)
        
                         # Read image
   

        print(f"saved results to /output \n")


if __name__ == "__main__":
    demo()
