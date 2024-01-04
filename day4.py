#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:52:27 2024

@author: Kristen
"""

f = open('inputday4.txt','r')  # when you open like this you should close. https://realpython.com/python-with-statement/
input = f.readlines()  # input is a builtin function so you shouldn't use it as a var name
sum = 0  # same with sum

def clean(input,i):
    # you don't have to but it can be more readable to have longer var names
    # i dont always follow that but its still a good thing a lot of the time
    k = input[i].split(':')
    l = k[1].split('\n')
    j = l[0].split('|')
    return j

''' Part 1
for i in range(len(input)):
    nums = clean(input,i)

    # you can also .replace("  ", " ") and maybe .strip() before you split then you don't have to do this isnumeric stuff
    g = nums[0].split(' ')
    guess = []
    for j in range(len(g)):
        if g[j].isnumeric() == True:
            guess.append(int(g[j]))
    
    w = nums[1].split(' ')
    win = []
    for j in range(len(w)):
        if w[j].isnumeric() == True:
            win.append(int(w[j]))
    
    cnt = 0
    # checking for value in a list is O(n) vs in a set is O(1)
    for element in guess:
        if win.count(element)!= 0:
            cnt += 1
    
    if cnt != 0:
        rowval = 2**(cnt-1)
    else:
        rowval = 0
    print(rowval)
    sum += rowval
    
print(sum)

'''
# Part 2
import numpy as np

arr = np.zeros((len(input),len(input)))

for i in range(len(input)):
    nums = clean(input,i)
    
    g = nums[0].split(' ')
    guess = []
    for j in range(len(g)):
        if g[j].isnumeric() == True:
            guess.append(int(g[j]))
    
    w = nums[1].split(' ')
    win = []
    for j in range(len(w)):
        if w[j].isnumeric() == True:
            win.append(int(w[j]))
    
    c = 0
    for element in guess:
        if win.count(element)!= 0:
            c += 1
    if c != 0:
        for j in range(c+1):
            arr[i,j+i]=1
    else:
        arr[i,i]=1
# nerd
for j in range(len(input)):
    l=0
    while l < j:
        arr[j,j] += arr[l,j]
        l+=1
    arr[j,j+1:] *= arr[j,j]
        
print(np.trace(arr))


    
