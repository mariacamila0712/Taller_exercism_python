def equilateral(sides):
    return len(set(sides)) == 1 and validation(sides)


def isosceles(sides):
    return len(set(sides)) < 3 and validation(sides)


def scalene(sides):
    return len(set(sides)) == 3 and validation(sides)


def validation(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] >= sides[2] and sides[0] > 0
