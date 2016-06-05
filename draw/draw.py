import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

def draw_figure(x, y, label, legend, num):
    fig.add_subplot(2, 1, num)
    plt.plot(x, y, label = `label`)
    plt.legend(loc='upper left')
    #plt.grid(True)
    
array_x1 = [1, 2, 3, 4, 5]
array_y1 = [4, 5, 8, 10, 12]
array_y2 = [7, 8, 11, 22, 23]
x_label = "x"
y_label = "y"
title = "test"

draw_figure(array_x1, array_y1, 1, y_label, 1)
draw_figure(array_x1, array_y2, 2, y_label, 1)
draw_figure(array_x1, array_y2, 3, y_label, 2)
plt.savefig("test.png")
plt.show()
