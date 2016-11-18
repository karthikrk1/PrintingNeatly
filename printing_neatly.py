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

# DP Algorithm

def printing_neatly(words, M=80):
    '''
    This is the Dynamic Program algorithm for printing neatly to the console. The algorithm computes the penalty for each line and then calls the 
    printToConsole() method to print it into the console. The first line of the out put is the penalty for the entire text
    
    Input:
        words - The list of words formed by reading the input file and then splitting based on the new line and space characters.
        M - The length of the line. Defaults to 80. It can be overridden by the method call.
        
    '''
    # TODO: Implementation
    return None

# Printing function 

def printToConsole():
    '''
    This is the implementation of the utility function that prints to the console. This utility function is called by the 
    printing_neatly method. This function prints to the console.
    
    Input:
    '''
    # TODO: Print funtion
    return None 

# Driver code

def main(argv):
    # This is the length of the line
    input_file = open(argv[1],'r')
    if len(argv)>1:
        M =argv[2]
    # The file is read and stored in a words list which is a list of lists.
    # In order to flatten the list of lists into a single list, we have used a Pythonic trick to flatten the list
    words = [s.split() for s in input_file.read().splitlines()]
    words = sum(words,[]) 
    print(words)
    
if __name__=="__main__":
    main(argv[1:])
    
        
        
    