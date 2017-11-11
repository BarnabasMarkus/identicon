#!/usr/bin/env python3
# I D E N T I C O N   G E N E R A T O R

# Project   Identicon Generator
# Author    Barnabas Markus
# Email     barnabasmarkus@gmail.com
# Date      11.11.2017
# Python    3.6.0
# License   MIT


from PIL import Image, ImageDraw


COLORS = ('#62e0a3', '#e0627d', '#8762e0', '#5bb2ff')

extend = lambda xs: xs + xs[5:10] + xs[0:5]
chunk = lambda xs, size: [xs[s:s+size] for s in range(0, len(xs), size)]
rotate = lambda xxs: [[xs[i] for xs in xxs] for i in range(5)]


def get_color(user_id):
    color_id = user_id % len(COLORS)
    return COLORS[color_id]


def get_pixels(user_id):
    value = user_id % (2 ** 15)
    bits = '{:015b}'.format(value)
    pixels = rotate(chunk(extend(bits), 5))
    return pixels


class Identicon(object):

    def __init__(self, user_id):
        self.user_id = user_id
        self.color = get_color(user_id)
        self.pixels = get_pixels(user_id)
        self.draw()

    def draw(self, pixel=70,border=35, size=420, background='#F6F6F6'):

        self.image = Image.new("RGB", (size, size), background)
        draw = ImageDraw.Draw(self.image)

        for i in range(5):
            for j in range(5):
                if self.pixels[i][j] == '1':
                    x = j * pixel + border
                    y = i * pixel + border
                    draw.rectangle(
                        ((x, y), (x + pixel, y + pixel)), fill=self.color)

    def show(self):
        self.image.show()

    def save(self, extension='.jpg'):
        fname = str(self.user_id) + extension
        self.image.save(fname, "JPEG")
