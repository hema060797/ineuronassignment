# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:15:57 2020

@author: hemahemu
"""
wordlist=["today","is","a","beautiful","day"]
def wordlength(wordlist):
    return list(map(lambda x:len(x),wordlist))
print("words length in  array =>" +str(wordlength(wordlist)))