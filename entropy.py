#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from PIL import Image


def entropy(band: np.ndarray) -> np.float64:
    """
    Compute the entropy content of an image's band.

    :param band: The band data to analyze.
    :return:     Data entropy in bits.
    """
    hist, _ = np.histogram(band, bins=range(0, 256))
    hist = hist[hist > 0]
    return -np.log2(hist / hist.sum()).sum()


def show_entropy(band_name: str, band: np.ndarray) -> None:
    """
    Analyze and display entropy of an image's band.

    :param band_name: The name of the band to analyze.
    :param band:      The band data to analyze.
    """
    bits = entropy(band)
    per_pixel = bits / band.size
    print("{:3s} entropy = {:.2f} bits, {:.6f} per pixel"
          .format(band_name, bits, per_pixel))


def process(img_file: str) -> None:
    """
    Process the image file.

    :param img_file: The image file.
    """
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


if __name__ == "__main__":
    process("images/left.png")
    process("images/right.png")
