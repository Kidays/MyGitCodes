from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader
import cv2 as cv
import os
import sys
os.chdir(sys.path[0])

class MyData(Dataset)
    def __init__(self,root_dir,label_dir):
        self.root_dir=root_dir
        self.label_dir=label_dir
        self.path=os.path.join(self.root_dir,self.label)

    def __getitem__(self,idx):