def duplicate_encode(word):
    l = word.lower()
    dupes = set([x for x in l if l.count(x) >1])
    
    return ''.join([')' if s in dupes else '(' for s in l ])
