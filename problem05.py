def are_strict_sentences_anagrams(s, t):
    s = s.lower()
    t = t.lower()
    
    return sorted(s) == sorted(t)

