# https://www.hackerrank.com/challenges/jumping-on-the-clouds

def jumpingOnClouds(c):
    i = 0
    steps = 0
    length = len(c)

    while i < length - 1:
        if i < length - 2:
            if c[i+2] == 0:
                i += 2
                steps += 1
        elif c[i+1] == 0:
            i += 1
            steps += 1
        else:
            return False
    print(steps)
    return steps

if __name__ == "__main__":
    s = [int(i) for i in "0 0 1 0 0 1 0".split()]

    print(jumpingOnClouds(s))