import json
import sys
from collections import defaultdict

import matplotlib.pyplot as plt

def count_reactions(f):
    ms = json.load(f)
    count = defaultdict(int)

    for m in ms:
        if 'reactions' not in m:
            continue
        for r in m['reactions']:
            count[r['name']] += r['count']

    f.close()

    return count

def union_dict_with_sum(d1, d2):
    result = defaultdict(int, d1)

    for k in d2:
        result[k] += d2[k]

    return result


def reactions(fs):
    rs = [count_reactions(open(f)) for f in fs]
    total_reactions = reduce(union_dict_with_sum, rs)

    return total_reactions

def main():
    total = reactions(sys.argv[1:])
    fst = lambda t: t[0]
    snd = lambda t: t[1]
    srs = sorted(total.items(), key=snd, reverse=True)

    keys = ['moroi_all'] + map(fst, srs)
    values = [sum(total['moroi' + s] for s in '234') + total['moroi']] + map(snd, srs)

    left = list(xrange(len(keys)))

    plt.bar(left, values, tick_label=keys, align='center')

    plt.setp(plt.axes().get_xticklabels(), rotation=20, horizontalalignment='right')

    plt.show()

    print srs

if __name__ == '__main__':
    main()
