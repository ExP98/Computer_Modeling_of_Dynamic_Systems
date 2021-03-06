from PIL import Image, ImageDraw
import numpy as np


def julia_visualization(c_re, c_im, ctr, brd=1.5):
    h, w = 600, 800
    c = c_re + 1j * c_im
    img = Image.new('RGB', (w, h))
    pixels = img.load()
    max_iter, curr_iter = 1000, 0
    for x, re in enumerate(np.linspace(-brd, brd, w)):
        for y, im in enumerate(np.linspace(-brd, brd, h)):
            z = re + 1j * im
            for i in range(max_iter):
                curr_iter = i
                z = z ** 2 + c
                if abs(z) > 2:
                    break
            color = [curr_iter, curr_iter, curr_iter]
            color[ctr % 3] = 0
            pixels[x, y] = tuple(color)
    ImageDraw.Draw(img).text((10, h - 20), f"Julia, c = {c}", (255, 255, 255))
    img.save('output_julia/julia_' + str(c_re) + '_' + str(c_im) + '.png')
    # img.show()


# c_list = [(-0.7055, -0.3842), (-0.22, -0.74), (-0.8, 0.156), (-0.7, 0.27015), (0.285, 0.01), (-0.0085, 0.71),
# (-0.12375, 0.56508), (-0.12, 0.74), (-0.39054, -0.58679), (-1.25, 0.0), (0.11031, -0.67037), (-0.194, 0.6557)]
c_list = [(0.285, 0.01)]
for counter, (real, imagine) in enumerate(c_list):
    julia_visualization(real, imagine, counter)
