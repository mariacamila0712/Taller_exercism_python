def triplets_with_sum(number):
    return [
        [a, b, number - a - b]
        for a in range(1, number + 1)
            for b in range(a + 1, number - a)
                if b < (number - a - b) and a*a + b*b == (number - a - b)**2
    ]