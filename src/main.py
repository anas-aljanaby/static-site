import os
import shutil
from textnode import TextNode
from generate_pages import generate_page, generate_pages_recursive


DEBUG = 1 

pwd = os.getcwd()
public_path = os.path.join(pwd, 'public')
static_path = os.path.join(pwd, 'static')
if os.path.exists(public_path):
    shutil.rmtree(public_path)


def copy_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        if DEBUG:
            print(f' * {from_path} -> {dest_path}')
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)
            

copy_files(static_path, public_path)

#generate_page('content/index.md', dest_path='public/index.html', template_path='template.html')

generate_pages_recursive('content', 'template.html', 'public')

