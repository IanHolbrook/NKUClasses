import requests
import argparse as ap
from PIL import Image

pobj = ap.ArgumentParser()
pobj.add_argument('-H', dest='H', type=str, help='input the city')
pobj.add_argument('-I', '--image', action='store', dest='I', type=int, required=False, help='input image')
pobj.add_argument('-S', '--sign', action='store', dest='S', type=int, required=False, help='sign the image.')
pobj.add_argument('-R', '--resize', action='store', dest='R', type=int, nargs='*', required=False, help='resize the image.')
pobj.add_argument('-RO', '--rotate', action='store', dest='RO', type=int, required=False, help='rotate the image.')
pobj.add_argument('-C', '--crop', action='store', dest='C', type=int, nargs='*', required=False, help='crop the image.')
pobj.add_argument('-U', '--upload', action='store', dest='U', type=int, nargs='*', required=False, help='upload the image.')

result = pobj.parse_args()
h = result.H
i = result.I
s = result.S
r = result.R
ro = result.RO
c = result.C
u = result.U

if h:
    exit()
if i:
    image = result.i
if s:
    def operation_signature(image, watermark_image_path, output_image_path):
        base_image = Image.open(image)
        watermark = Image.open(watermark_image_path).convert("RGBA")
        position = base_image.size
        newsize = (int(position[0] * 8 / 100), int(position[0] * 8 / 100))
        watermark = watermark.resize(newsize)
        new_position = position[0] - newsize[0] - 20, position[1] - newsize[1] - 20
        transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))
        transparent.paste(base_image, (0, 0))
        transparent.paste(watermark, new_position, watermark)
        image_mode = base_image.mode
        if image_mode == 'RGB':
            transparent = transparent.convert(image_mode)
        else:
            transparent = transparent.convert('P')
        transparent.save(output_image_path, optimize=True, quality=100)
if r:
    resize_val = r
    def operation_resize(image, resize_val):
        myimage = Image.open(image)
        resizedImage = myimage.resize((resize_val[0], resize_val[1]))
        resizedImage.save('resized.png')
if ro:
    angle = ro
    def operation_rotate(image, angle):
        myimage = Image.open(image)
        rotatedImage = myimage.rotate(angle)
        rotatedImage.save('rotated90.png')
if c:
    crop_val = []
    crop_val.append(c)
    def operation_crop(image,crop_val):
        myimage = Image.open(image)
        croppedIm = myimage.crop(crop_val[0], crop_val[1], crop_val[2], crop_val[3])
        croppedIm.save('cropped.png')
if u:
    url=input("input where to upload: ")
    files={'media':open(image,'rb')}
    requests.post(url, files=files)