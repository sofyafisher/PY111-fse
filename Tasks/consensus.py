import collections

word = ["ATTA", "ACTA", "AGCA", "ACAA"]

def get_key(d, value):

    for k, v in d.items():
        if v == value:
            return k

def cons(lst_):
    len_lst = len(lst_)
    len_word = len(lst_[0])
    letters = []
    s = ""

    for _ in range(len_word):
        letters.append([])

    for i in range(len_lst):
        for j in range(len_word):
            letters[j].append(lst_[i][j])

    for a in letters:
        v = collections.Counter(a)
        s += get_key(v, max(v.values()))

    return s
