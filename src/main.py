import os
import shutil
from textnode import TextNode
from generate_page import generate_page


DEBUG = 0 

pwd = os.getcwd()
public_path = os.path.join(pwd, 'public')
static_path = os.path.join(pwd, 'static')
if os.path.exists(public_path):
    shutil.rmtree(public_path)

os.mkdir(public_path)

def copy_files(static_path=static_path, cursor=''):
    path = os.path.join(static_path, cursor)

    for p in os.listdir(path):
        if os.path.isdir(os.path.join(path, p)):
            new_cursor = os.path.join(cursor, p)
            current_path = os.path.join(public_path, new_cursor)
            os.mkdir(current_path)
            if DEBUG:
                print(f'INFO: Copied dir {new_cursor} to public dir')
                print(f'INFO: Traversing {new_cursor}')
            copy_files(cursor=new_cursor)
        else:
            if DEBUG:
                print(f'INFO: Copied file {os.path.join(cursor, p)} to public dir')
            shutil.copy(os.path.join(static_path, cursor, p), os.path.join(public_path, cursor, p))
            

copy_files(os.path.join(pwd, 'static'))

generate_page('content/index.md', dest_path='public/index.html', template_path='template.html')

             


