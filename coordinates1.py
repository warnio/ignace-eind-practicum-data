import glob
import re

coordinate1_filepaths = {
    re.sub(r'^.*VID_(.*)_(?:green|purple)\.npy$', r'\1', path): {
        'green': path,
        'purple': re.sub(r'green(?=\.npy$)', r'purple', path)
    }
    for path in glob.glob('coords/VID_*_green.npy')
}