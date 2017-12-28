#!/bin/bash
export PATH=$HOME/anaconda3/bin:$PATH
cd ~/Dropbox/pytorch/Project_1/

python main_train_WS_2D.py
python train_plot.py
python test_plot.py
