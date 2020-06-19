"""
The goal of this exercise is to convert a string to a new string 
where each character in the new string is "(" if that character appears only once in the original string, 
or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

"""

def duplicate_encode(word):
    # converting to lower case
    l = word.lower()
    
    # finding the set of chars with duplicates
    dupes = set([x for x in l if l.count(x) >1])
    
    # returning ')' if char is a member of dupes and '(' else
    return ''.join([')' if s in dupes else '(' for s in l ])
