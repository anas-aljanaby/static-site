import os
import shutil
from textnode import TextNode

pwd = os.getcwd()
public_path = os.path.join(pwd, public)
shutil.rmtree(public_path)

def traverse_dir(path):
    for p in os.listdir(path):
        if os.isdir(p):
            return traverse_dir(p)
        else:
            shutil.copy(p, public_path)


traverse_dir()




