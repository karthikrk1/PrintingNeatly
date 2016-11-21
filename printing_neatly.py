#!/bin/python35
'''
CS 6363.006 - Design and Analysis of Algorithms

This programming project is the implementation of the Dynamic Program printing neatly.
Write your program to accept its input from a file if the name of the file
is given in the command line, or read its input from the console.
The default value of M is 80.  If the command line has a second parameter,
then use it as the value of M.

Authors: Karthik Ramakrishnan, Rahul Aravind Mehalingam, Ramya Elangovan, Preethi Sekar

'''
from sys import argv
import sys
import math

# DP Algorithm

def printing_neatly(words, M=80):
    '''
    This is the Dynamic Program algorithm for printing neatly to the console. The algorithm computes the penalty for each line and then calls the 
    printToConsole() method to print it into the console. The first line of the out put is the penalty for the entire text
    
    Input:
        words - The list of words formed by reading the input file and then splitting based on the new line and space characters.
        M - The length of the line. Defaults to 80. It can be overridden by the method call.
        
    '''
    cost = [[0 for j in range(len(words))] for i in range(len(words))] # Cost matrix
    
    # Build the cost matrix
    for i in range(0,len(words)):
        cost[i][i]= M - len(words[i]);
        for j in range(i+1,len(words)):
            cost[i][j] = cost[i][j-1] - len(words[j]) -1 
    
    for i in range(0,len(words)):
        for j in range(i,len(words)):
            if cost[i][j] < 0:
                cost[i][j] = sys.maxsize
            else:
                cost[i][j] = math.pow(cost[i][j], 3)
                
    
    minCost = [0] * len(words)
    out = [0]*len(words)
    for k in range(len(words)-1,-1,-1):
        minCost[k] = cost[k][len(words)-k]
        out[k] =  len(words)
        for l in range(len(words)-1,k,-1):
            if cost[k][l-1] == sys.maxsize:
                continue
            if minCost[k] > minCost[l] + cost[k][l-1]:
                minCost[k] = minCost[l] + cost[k][l-1]
                out[k] = l;
    
    
    print(minCost[0])
    print('\n')
    print(printUtil(words,out))

# Printing function 

def printUtil(words, out):
    '''
    This is the implementation of the utility function that prints to the console. This utility function is called by the 
    printing_neatly method. This function prints to the console.
    
    Input:
    '''
    
    i = 0
    temp=[]
    while True:
        j = out[i]
        for k in range(i, j):
            temp.append(words[k])
        temp.append('\n')
        i=j
        if j==len(words):
            break
    
    output = ''.join(temp) 
    return output

# Driver code

def main(argv):
    # This is the length of the line
    input_file = open(sys.argv[1],'r')
    # The file is read and stored in a words list which is a list of lists.
    # In order to flatten the list of lists into a single list, we have used a Pythonic trick to flatten the list
    words = [s.split() for s in input_file.read().splitlines()]
    words = sum(words,[]) 
    if len(sys.argv)>2:
        M =sys.argv[2]
        printing_neatly(words, M)
    else:
        printing_neatly(words)
    # print(words)
    
if __name__=="__main__":
    main(sys.argv[1:])
    
        
        
    