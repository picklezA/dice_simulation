# version: 0.0.1
# author: picklez

import math
import itertools
from itertools import product
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()
export = cwd + "\\export\\"
image_ext = ".png"

if not os.path.exists(export):
    os.makedirs(export)

def possible_perms(num_of_dice, sides): # removes dups :)
    temp = [list(range(1,sides+1)) for _ in range(num_of_dice)]
    res = list(product(*temp))
    print("Permutations: "+str(len(res)))
    for x in range(len(res)):
        res[x] = sorted(res[x])
    res.sort()
    return list(res for res,_ in itertools.groupby(res))

def sum_list(list):
    hold_list = []
    for i in range(len(list)):
        item = list[i]
        hold_list.append(sum(item))
    return hold_list

def create_figure(num_of_dice, sides):
    print("Running "+str(num_of_dice)+"!")
    plt.rcParams["figure.figsize"] = [7.5, 3.5]
    plt.rcParams["figure.autolayout"] = True
    hold = possible_perms(num_of_dice, sides)
    hold2 = sum_list(hold)
    plt.hist(hold2, bins=500, align='mid', rwidth=1)
    plt.savefig(export+"distrubtion_d"+str(sides)+"_num_dice_"+str(num_of_dice)+image_ext)
    plt.close()

# Before you run, you can change the amount of sides / dice you would like to simulate!
sides = 12
num_of_dice = 3
create_figure(num_of_dice, sides)