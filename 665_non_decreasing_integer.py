#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:30:03 2020

@author: sumi
"""

# 665. Non-decreasing Array
# Given an array with n integers, your task is to check if it could become 
# non-decreasing by modifying at most 1 element.

#Example 1:
#Input: [4,2,3]
#Output: True
#Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
#
#Example 2:
#Input: [4,2,1]
#Output: False
#Explanation: You can't get a non-decreasing array by modify at most one element.
#
#Note: The n belongs to [1, 10,000].


class Solution:
    def checkPossibility(self, List):
        """
        :type List : List[int]
        :result type : bool
        """
        count = 0
        for i in range(0,len(List)-1):
            if count > 1 :
                break
            if List[i] > List[i+1]:
                if i > 0:
                    if List[i-1] <= List[i+1] :
                        List[i] = List[i-1]
                    else:
                        List[i+1] = List[i]
                count += 1
        return count <= 1