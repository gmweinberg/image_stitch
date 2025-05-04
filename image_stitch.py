#!/usr/bin/env python
import time
from PIL import Image


def corner_crop(im, corner, width, height):
    if corner[0].lower() == 'l': # lower
        upper = im.height - height
        lower = im.height
    else:
        upper = 0
        lower = height
    if corner[1].lower() == 'l': # left
        left = 0
        right = width
    else:
        left = im.width - width
        right = width
    #print("corner_crop", "width", right - left, "height", lower - upper)
    return im.crop((left, upper, right, lower))

# combine 4 images into one. 
def quad_image(ll, lr, ul, ur):
    quad = Image.new(ll.mode, (ll.width + lr.width, ll.height + ul.height))
    quad.paste(ul, (0, 0, ul.width, ul.height))
    quad.paste(ur, (ul.width, 0, ul.width + ur.width, ur.height))
    quad.paste(ll, (0, ul.height, ll.width, ll.height + ul.height))
    quad.paste(lr, (ll.width, ur.height, ll.width + lr.width, lr.height  + ur.height))
    return quad

def gen_onyxia(tw, th):
    basedir = "/home/gweinberg/Pictures/onyxia/"
    # raw images
    ll = Image.open(basedir + "ll.png")
    lr = Image.open(basedir + "lr.png")
    ul = Image.open(basedir + "ul.png")
    ur = Image.open(basedir + "ur.png")

    # should have the same height
    # top and bottom should have the same width
    rw = 450
    lh = th / 2

    llc = corner_crop(ll, "ll", rw, th/2)
    # ll.show()
    lrc = corner_crop(lr, "lr", tw - rw, th/2)
    #lr.show()
    ulc = corner_crop(ul, "ul", rw, th / 2)
    urc = corner_crop(ur, "ur", tw - rw, th/2)

    onyxia = quad_image(llc, lrc, ulc, urc)
    return onyxia


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    # TODO you know what
    tw = 820
    th = 1600
    onyxia = gen_onyxia(tw, th)
    onyxia.show()
