import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import requests
from PIL import Image
import hashlib

# #1
#url = "http://bit.ly/2JnsHnT"
#r = requests.get(url, stream=True).raw
#img = Image.open(r)
# img.show()
# img.save('src.png')

BUF_SIZE = 1024


def copy():
    with open('src.png', 'rb') as f, open('dest.png', 'wb') as df:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            df.write(data)


def hash():
    sha_src = hashlib.sha256()
    sha_dest = hashlib.sha256()

    with open('src.png', 'rb') as sf, open('dest.png', 'rb') as df:
        sha_src.update(sf.read())
        sha_dest.update(df.read())

    print(f"src.png's hash : {sha_src.hexdigest()}")
    print(f"dest.png's hash : {sha_dest.hexdigest()}")
# hash()


# dest_img = mpimg.imread('dest.png')
# pseudo_img = dest_img[:,:,0]

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)
plt.title('Pseudocolor Image')
dest_img = mpimg.imread('dest.png')
pseudo_img = dest_img[:, :, 0]
plt.imshow(pseudo_img)
plt.show()
