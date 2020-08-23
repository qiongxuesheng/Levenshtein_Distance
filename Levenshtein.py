# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:34:10 2020

@author: Thinkpad
"""


def LevenshteinD(word1, word2):
    m = len(word1)
    n = len(word2)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j
    
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    
    if (int(table[-1][-1]))/max(m, n) >= 0.3:
        return "not match"
    else:
        return "match"
    
import pandas as pd


search_list = list(pd.read_csv("C://Users/Thinkpad/Desktop/输出.csv")["业主方"])
whole_list = list(pd.read_csv("C://Users/Thinkpad/Desktop/ACMR.csv")["company"])



match_list = []
name_list = []
iffuzzy_list = []
mid_value = 0
for i in whole_list:
    
    print(i)
    match_value = 0
    
    for j in search_list:
        if LevenshteinD(i, j) == "match":
            match_value += 1 
            mid_value = j
        else:
            match_value += 0
            
    if match_value > 0:
        match_list.append("have match")
        if i == mid_value:
            name_list.append("Original value")
            iffuzzy_list.append("Perfet match")
        else:
            name_list.append(mid_value)
            iffuzzy_list.append("Fuzzy match")
    else:
        match_list.append("Not have match")
        name_list.append("0")
        iffuzzy_list.append("0")

   
#print(match_list)
#print(name_list)
#print(iffuzzy_list)        
match_list_df = pd.DataFrame(match_list)
name_list_df = pd.DataFrame(name_list)
iffuzzy_list_df = pd.DataFrame(iffuzzy_list)

match_list_df.to_excel("C://Users/Thinkpad/Desktop/match.xlsx")
name_list_df.to_excel("C://Users/Thinkpad/Desktop/name_list.xlsx")
iffuzzy_list_df.to_excel("C://Users/Thinkpad/Desktop/iffuzzy.xlsx")