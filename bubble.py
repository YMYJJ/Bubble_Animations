
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from IPython.display import display, clear_output
	
count = 0
fig, ax1 = plt.subplots()
# draw axis
def draw(l, v):

    global count
    global fig
    global ax1
    
    
    ax1.cla()
    # draw  axis
    ax1.axis([0, len(l) + 1, 1, 110]) 
    xmajorLocator = MultipleLocator(1)
    ymajorLocator = MultipleLocator(20)
    ax1.xaxis.set_major_locator(xmajorLocator)
    ax1.yaxis.set_major_locator(ymajorLocator)

    # draw histograms
    x = [x + 1 for x in range(len(l))]
    bar = plt.bar(x, l)

    # draw numbers
    for a, b in zip(x, l):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
    
    # draw moves
    for ba, y in zip(bar, l):
        if y == v:
            ba.set(color="red")
    plt.pause(0.5)

    clear_output(wait = True)
    display(fig)
    clear_output(wait = True)
    plt.pause(0.01)
    count += 1


def sort(l):
    for i in range(0, len(l)):
        change = False
        for j in range(len(l)-1, i, -1):
            draw(l, l[j])
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j - 1], l[j]
                change = True
        if not change:
            print("return")
            return

l = [5, 23, 43, 95, 62, 76, 34]
plt.pause(3)
sort(l)
plt.show()