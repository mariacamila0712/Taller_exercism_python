def largest(min_factor, max_factor):
    return find_palindrome(min_factor, max_factor, (max_factor**2, (min_factor**2)-1, -1))


def smallest(min_factor, max_factor):
    return find_palindrome(min_factor, max_factor, [min_factor**2, max_factor**2+1])


def find_palindrome(lower, upper, candidates):
    if upper < lower:
        raise ValueError('wrong order')
    for cand in range(*candidates):
        text = str(cand)
        if text == text[::-1]:
            factors = [[f, cand//f] for f in range(lower, upper+1) if cand % f == 0 and lower <= f <= cand//f <= upper]
            if factors != []:
                return cand, factors
    return None, []
