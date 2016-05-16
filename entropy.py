#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from PIL import Image


def entropy(band):
    hist, _ = np.histogram(band, bins=range(0, 256))
    hist = hist[hist > 0]
    return -np.log2(hist / hist.sum()).sum()


def show_entropy(band_name, band):
    bits = entropy(band)
    per_pixel = bits / band.size
    print("{:3s} entropy = {:.2f} bits, {:.6f} per pixel"
          .format(band_name, bits, per_pixel))


def process(img_file):
    im = Image.open(img_file)
    print(img_file, im.format, im.size, im.mode)
    print()

    rgb = im.convert("RGB")
    hsv = im.convert("HSV")
    grey = im.convert("L")
    r, g, b = [np.asarray(component) for component in rgb.split()]
    h, s, v = [np.asarray(component) for component in hsv.split()]
    l = np.asarray(grey)

    show_entropy("R", r)
    show_entropy("G", g)
    show_entropy("B", b)
    print()

    show_entropy("H", h)
    show_entropy("S", s)
    show_entropy("V", v)
    print()

    show_entropy("L", l)
    print()


process("images/left.png")
process("images/right.png")
