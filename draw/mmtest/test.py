import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import plot


def draw_figure(x, y, labelparam, legend, title, num):
    #plt.figure(figsize = (12,20) , dpi = 100)
    num = 5
    f, axs = plt.subplots(5,1,figsize=(15,15))
    for i in range(num):
        #print int(i + 2) %2
        #plt.subplot(num, 2, i + 1, ).autoscale_view(True,True,True)
        
        #plt.subplot().figsize = (9 , 9)
        axs[i].plot(x, y, label = labelparam)
        #plt.axis('equal')
    
    #plt.savefig("test.png", dpi = 100)
    plt.show()
            
array_x1 = [1, 2, 3, 4, 5]
array_y1 = [4, 5, 8, 10, 12]
array_y2 = [7, 8, 11, 22, 23]
x_label = "x"
y_label = "y"
title = "test"

draw_figure(array_x1, array_y2, "data", y_label, "graph1", 1)
#plt.savefig("new.png")
#draw_figure(array_x1, array_y2, 2, y_label, "graph2", 1)
#draw_figure(array_x1, array_y2, 3, y_label, "graph3", 2)
