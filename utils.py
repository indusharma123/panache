

def matcher(s1,s2):
    return 2*float(len(exploder(s1).intersection(exploder(s2))))/float(len(exploder(s1)) + len(exploder(s2)))

def exploder(s):
    s = s.upper()
    s = [ x for x in s ]
    s = [(s[i],s[i+1]) for i in range(len(s) - 1 ) ]
    return set(s)

#print matcher('FRANCE','french')