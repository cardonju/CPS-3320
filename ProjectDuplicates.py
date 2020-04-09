import os
import collections
import hashlib

#Defining path to be scanned
path = '/Users/Juan/Downloads/untitled'

files = {}
#scanning path and adding files to dictionary
for r, d, f in os.walk(path):
    for file in f:
        
            files.update({os.path.join(r, file) : file})

print()
 

# finding duplicate values 
# from dictionary 
#convert dictionary values to keys  then find the duplicate keys
rev_dict = {} 
  
for key, value in files.items(): 
    rev_dict.setdefault(value, set()).add(key) 
      
result = [key for key, values in rev_dict.items() if len(values) > 1] 
  
# printing result 
 

print(*result, sep = "\n")




