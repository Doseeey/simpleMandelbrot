from numba import jit
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import os

def cls(): print('\n' * 100)

@jit
def mandelbrot(c,maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter)
        perc = i/width*100
        print(round(perc, 2), '%')
    return (r1,r2,n3)


def mandelbrot_image(xmin, xmax, ymin, ymax, width=500, height=500, maxiter=1000):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height
    x, y, z = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, maxiter)

    fig, ax = plt.subplots(dpi=72)
    #ticks = np.arange(0, img_width, 3 * dpi)
    #x_ticks = xmin + (xmax - xmin) * ticks / img_width
    #plt.xticks(ticks, x_ticks)
    #y_ticks = ymin + (ymax - ymin) * ticks / img_width
    #plt.yticks(ticks, y_ticks)

    ax.imshow(z.T, origin='lower', cmap=plt.cm.twilight_shifted)

mandelbrot_image(-2.0,0.5,-1.25,1.25)