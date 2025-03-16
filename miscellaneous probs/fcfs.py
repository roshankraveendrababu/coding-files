#write an python script to implement the FCFS scheduling algorithm
#input: number of processes, burst time of each process
#output: waiting time for each process, average waiting time
#test the script with the following input:
#number of processes: 4
#burst time of each process: 3 5 2 8
import sys
import time
import random
import numpy as np
from typing import List
from collections import deque
from collections import defaultdict
import matplotlib.pyplot as plt
import math
# Function to calculate waiting time for each process
def findWaitingTime(processes: List[int], n: int,
                     bt: List[int], wt: List[int]):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]
# Function to calculate turn around
# time for each process
def findTurnAroundTime(processes: List[int], n: int,
                          bt: List[int], wt: List[int], tat: List[int]):
     for i in range(n):
          tat[i] = bt[i] + wt[i]
          # Function to calculate average waiting time
def findavgTime(processes: List[int], n: int, bt: List[int]):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes Burst Time Waiting",
              "Time Turn-Around Time")
    for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            print(" ", i + 1, "\t\t", bt[i],
                  "\t\t", wt[i], "\t\t", tat[i])
    print("\nAverage waiting time = %.5f "%(total_wt /n))
    print("Average turn around time = ", total_tat / n)
# Driver code
if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]
    findavgTime(processes, n, burst_time)
#end of the code
#output
#Processes Burst Time Waiting Time Turn-Around Time
# 1 10 0 10
# 2 5 10 15
# 3 8 15 23
# Average waiting time = 8.33333
# Average turn around time = 16.0
#end of the output
#end of the script
#end of the code
#end of the snippet
