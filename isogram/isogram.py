def is_isogram(string):
    string = string.replace(' ','')
    string = string.replace('-','')
    string = string.lower()
    unique = set(string)
    return len(unique) == len(string)
