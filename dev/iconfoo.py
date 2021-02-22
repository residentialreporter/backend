# Ionic Icon helper to overwrite old icons with the required sizes.

import sys
import os
from PIL import Image
from copy import copy

input_image = sys.argv[1]
output_folder = sys.argv[2]
platform = sys.argv[3]

android_sizes = {
    'hdpi': 72,
    'ldpi': 32,
    'mdpi': 48,
    'xhdpi': 96,
    'xxhdpi': 144,
    'xxxhdpi': 192
}

icon = Image.open(input_image).convert("RGBA")

for _, _, files in os.walk("./"):
    for item in files:
        if not item.endswith("png"):
            continue
        item = str(item)
        print(item)

        if platform == 'ios':
            prefix = "icon-"
            try:
                _, rest = item.split(prefix, 1)
            except ValueError:
                _, rest = item.split(prefix.rstrip("-"), 1)

            size, _ = rest.split(".png")

            if "@" in size:
                pixels, zoom = size.split("@")

                if pixels == 'small':
                    pixels = 29
                elif pixels == '':
                    pixels = 57
                else:
                    pixels = float(pixels)

                zoom = int(zoom.rstrip("x"))
            else:
                try:
                    pixels = float(size)
                except ValueError:
                    pixels = 29
                zoom = 1

            pixels = int(pixels * zoom)
            print(pixels)
        elif platform == 'android':
            prefix = "drawable-"

            try:
                _, rest = item.split(prefix, 1)
            except ValueError as e:
                print("Value error:", e)
                continue

            size, _ = rest.split("-icon.png")

            pixels = android_sizes[size]

            print(pixels)

        resized_icon = copy(icon)

        resized_icon = resized_icon.resize((pixels, pixels), Image.BILINEAR)

        output = os.path.join(output_folder, item)
        print("Writing to ", output)
        resized_icon.save(output)



