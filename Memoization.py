from time import time

def memoize(f):
    results = {}

    def helper(*args, **kwargs):
        if args[0] not in results:
            results[args[0]] = f(*args, **kwargs)
        return results[args[0]]

    return helper


@memoize
def lin_comb(x, weights):
    assert len(weights) == 4
    assert x > 0 and x < 41

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if x == i*weights[0] + j*weights[1] + k*weights[2] + l*weights[3]:
                        comb = {weights[ind]:[i, j, k, l][ind] for ind in range(4)}

    return comb

def weight(x):
    """
       x is the weight to be weighted. Find weights to be used for weighting x.
    """
    weights = (1, 3, 9, 27)

    used_weights = lin_comb(x, weights)

    left = []
    right = []

    for w in used_weights:
        if used_weights[w] == -1:
            left.append(w)
        elif used_weights[w] == 1:
            right.append(w)
            
    return {'left': left, 'right': right}



if __name__ == '__main__':
    """
    Our exercise is an old riddle, going back to 1612. The French Jesuit Claude-Gaspar Bachet phrased it. We have to weigh quantites (e.g. sugar or flour) from 1 to 40 pounds. What is the least number of weights that can be used on a balance scale to way any of these quantities.

    The first idea might be to use weights of 1, 2, 4, 8, 16 and 32 pounds. This is a minimal number, if we restrict ourself to put weights on one side and the stuff, e.g. the sugar, on the other side. But it is possible to put weights on both pans of the scale. Now, we need only four weights, i.e. 1, 3, 9, 27

    Write a Python function weigh(), which calculates the weights needed and their distribution on the pans to weigh any amount from 1 to 40. 
    """
    to_be_weighted = range(1, 41)

    # First run computes and memoizes
    t0 = time()
    for w in to_be_weighted:
        print(weight(w))
    print(time() - t0, 'seconds passed in the first run')

    # Second run uses memoized results
    t0 = time()
    for w in to_be_weighted:
        print(weight(w))
    print(time() - t0, 'seconds passed in the second run')



