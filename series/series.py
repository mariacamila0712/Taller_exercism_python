def slices(series, length):
    if not series or length <= 0 or length > len(series):
        raise ValueError("Invalid input")
    
    return [series[n:n+length] for n in range(0, len(series)-length+1)]
