from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
  
#strings to compare

s1 = "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
s2 = "Two things are interminable: the universe and human idiocy; and I don't know about the universe."

#implementing all different ratios 
print ("FuzzyWuzzy Ratio: ", fuzz.ratio(s1, s2) )
print ("FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2) )
print ("FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2)) 
print ("FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2)) 
print ("FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2),'\n\n')