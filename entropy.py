#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from PIL import Image


def entropy(band):
    hist, _ = np.histogram(band, bins=range(0, 256))
    hist = hist[hist > 0]
    return -np.log2(hist / hist.sum()).sum()


def show_entropy(name, e, sz):
    print("{} entropy = {:.2f} bits, {:.6f} per pixel".format(name, e, e / sz))


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

    show_entropy("R", entropy(r), r.size)
    show_entropy("G", entropy(g), g.size)
    show_entropy("B", entropy(b), b.size)
    print()

    show_entropy("H", entropy(h), h.size)
    show_entropy("S", entropy(s), s.size)
    show_entropy("V", entropy(v), v.size)
    print()

    show_entropy("L", entropy(l), l.size)
    print()


process("images/left.png")
process("images/right.png")
