#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:38:13 2020

@author: sumi
"""

#Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
#Example 1:
#Input: [3, 2, 1]
#
#Output: 1
#
#Explanation: The third maximum is 1.
#Example 2:
#Input: [1, 2]
#
#Output: 2
#
#Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#Example 3:
#Input: [2, 2, 3, 1]
#
#Output: 1
#
#Explanation: Note that the third maximum here means the third maximum distinct number.
#Both numbers with value 2 are both considered as second maximum.

class Solution:
    def thirdMax(self, List):
        """
        :type List : List[int]
        :result type : int 
        """
        import numpy as np
        unique_elements = set(List)
        sorted_elements = sorted(set(List))
        if len(sorted_elements) >= 3:
            return sorted_elements[-3]
        else:
            return np.max(sorted_elements)














