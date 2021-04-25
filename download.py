import sys

import requests
import os
import requests
from tqdm import tqdm

def download(url, path):

    chunksize = 1024 * 1024

    r = requests.get(url, stream=True)
    filename = os.path.basename(url)
    filename = os.path.join(path, filename)
    filesize = r.headers.get('content-length')
    filesize = int(filesize)
    if r.status_code == 200:
        with open(filename, 'wb') as p3t,tqdm(unit='B', unit_scale=True, unit_divisor=1024, file=sys.stdout, total=filesize, desc=filename)as progress:
            for chunk in r.iter_content(chunk_size=chunksize):
                if chunk:
                    p3t.write(chunk)
                    progress.update(chunksize)
    else:
        print('NOT found', filename)
        with open('NOTFOUND.txt', 'a') as nf:
            nf.write(str(url) + '\n')
    return 0
