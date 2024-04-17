import os
import shutil
from textnode import TextNode

pwd = os.getcwd()
public_path = os.path.join(pwd, public)
shutil.rmtree(public_path)

def traverse_dir(path):
    for p in os.listdir(path):
        if os.isdir(p):
            shutil.copy(p, public_path)
            print('INFO: Copied dir {p} to public dir')
            return traverse_dir(p)
        else:
            print('INFO: Copied file {p} to public dir')
            shutil.copy(p, public_path)


traverse_dir(pwd)




