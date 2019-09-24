#!/usr/bin/python
from PIL import Image
import os, sys

path = ""
out_path = ""
dirs = os.listdir( path )

# structure
# path/subFolder/label_dir/
# this folder contains a mix of PNG and other files

def resize(path):
  for subFolder  in os.listdir(path):
    # print(subFolder)
    for label_dir in os.listdir(path + subFolder):
      for item in os.listdir(path + subFolder + '/' + label_dir):
        filename, ext = os.path.splitext(item)
        if (ext == '.png'):
          print(filename)
          im = Image.open(path + subFolder + '/' + label_dir + '/' + item)
          imResize = im.resize((160,160), Image.ANTIALIAS)
          imResize.save(out_path + subFolder + filename + '_' + label_dir + '.png', 'PNG')

resize(path)