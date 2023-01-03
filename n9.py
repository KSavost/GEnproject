import random


def r9(r9, big_arr, n9):
    arr = []
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    c = [1, 2, 3]
    for i in range(r9):
        key = random.choice([0, 1])
        ind = random.choice(a) - 1
        arr.append(ind)
        ind1 = random.choice(b) - 1
        b.remove(ind1+1)
        a.remove(ind+1)
        w1 = big_arr[ind1][key][random.randint(0, len(big_arr[ind1][key])-1)]
        big_arr[ind1][key].remove(w1)
        w2 = big_arr[ind1][key][random.randint(0, len(big_arr[ind1][key])-1)]
        big_arr[ind1][key].remove(w2)
        w3 = big_arr[ind1][key][random.randint(0, len(big_arr[ind1][key])-1)]
        big_arr[ind1][key].remove(w3)
        n9[ind] = list(set([w1, w2, w3]))
    for i in a:
        ind = i - 1
        ind1 = random.choice(c) - 1
        w1 = big_arr[ind1][0][random.randint(0, len(big_arr[ind1][0]) - 1)]
        big_arr[ind1][0].remove(w1)
        w2 = big_arr[ind1][0][random.randint(0, len(big_arr[ind1][0]) - 1)]
        big_arr[ind1][0].remove(w2)
        w3 = big_arr[ind1][1][random.randint(0, len(big_arr[ind1][1]) - 1)]
        big_arr[ind1][1].remove(w3)
        n9[ind] = list(set([w1, w2, w3]))
    return n9


def r10(r10, big_arr2, n10):
    arr = []
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    c = [1, 2, 3, 4, 5]
    for i in range(r10):
        key = random.choice([0, 1])
        ind1 = random.choice(b) - 1
        b.remove(ind1+1)
        w1 = big_arr2[ind1][key][random.randint(0, len(big_arr2[ind1][key]) - 1)]
        big_arr2[ind1][key].remove(w1)
        w2 = big_arr2[ind1][key][random.randint(0, len(big_arr2[ind1][key]) - 1)]
        big_arr2[ind1][key].remove(w2)
        w3 = big_arr2[ind1][key][random.randint(0, len(big_arr2[ind1][key]) - 1)]
        big_arr2[ind1][key].remove(w3)
        n10[ind1] = list(set([w1, w2, w3]))
    for i in b:
        ind1 = i - 1
        w1 = big_arr2[ind1][0][random.randint(0, len(big_arr2[ind1][0]) - 1)]
        big_arr2[ind1][0].remove(w1)
        w2 = big_arr2[ind1][0][random.randint(0, len(big_arr2[ind1][0]) - 1)]
        big_arr2[ind1][0].remove(w2)
        w3 = big_arr2[ind1][1][random.randint(0, len(big_arr2[ind1][1]) - 1)]
        big_arr2[ind1][1].remove(w3)
        n10[ind1] = list(set([w1, w2, w3]))
    return n10



def r11(r11, big_arr3, n11):
    arr = []
    a = [1, 2, 3, 4, 5]
    b = [1, 2]
    c = [1, 2]
    for i in range(r11):
        ind = random.choice(a) - 1
        arr.append(ind)
        arrind1 = random.choice(b) - 1
        a.remove(ind+1)
        key1 = random.randint(0, len(big_arr3[arrind1]) - 1)
        ind2 = random.randint(0, len(big_arr3[arrind1][key1])-1)
        ind4 = random.randint(0, len(big_arr3[arrind1][key1]) - 1)
        w1 = big_arr3[arrind1][key1][ind2][random.randint(0, len(big_arr3[arrind1][key1][ind2]) - 1)]
        big_arr3[arrind1][key1][ind2].remove(w1)
        w3 = big_arr3[arrind1][key1][ind4][random.randint(0, len(big_arr3[arrind1][key1][ind4]) - 1)]
        big_arr3[arrind1][key1][ind4].remove(w3)
        n11[ind] = [w1, w3]
    for i in a:
        ind = i - 1
        ind1 = random.choice(c) - 1
        c.remove(ind1 + 1)
        key = random.randint(0, len(big_arr3[ind1]) - 1)
        ind2 = random.randint(0, len(big_arr3[arrind1][key])-1)
        ind4 = random.randint(0, len(big_arr3[arrind1][key-1]) - 1)
        w1 = big_arr3[ind1][key][ind2][random.randint(0, len(big_arr3[ind1][key][ind2]) - 1)]
        big_arr3[ind1][key][ind2].remove(w1)
        w3 = big_arr3[ind1][key-1][ind4][random.randint(0, len(big_arr3[ind1][key-1][ind4]) - 1)]
        big_arr3[ind1][key-1][ind4].remove(w3)
        n11[ind] = [w1, w3]
    return n11




a = ['aboba', 'abiba' 'arbiba', 'arboba']
o = ['o', 'oo', 'ooo', 'oooo']
u = ['u', 'uu', 'uuu', 'uuuu']
e = ['e', 'ee', 'eee', 'eeee']
s = ['s', 'ss', 'sss', 'ssss', 'sssss']
ss = ['ll', 'lll', 'llll', 'lllll']
pru = ['pru', 'pruu', 'pruuu', 'pruuuu']
pre = ['pre', 'pree', 'preee', 'preeee']
tz = ['t', 'tt', 'ttt', 'tttt', 'ttttt']
mz = ['m', 'mm', 'mmm', 'mmmmm', 'mmmmmm']
z = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz']
c = ['c', 'cc', 'ccc', 'cccc', 'ccccc']
pro = ['pr', 'pro', 'proo', 'prooo', 'proooo']
pra = ['pre', 'pr2', 'pree', 'preee', 'preeee']
i = ['i', 'ii', 'iii', 'iiii', 'iiiii']
bl = ['bl', 'bll', 'blll', 'bbll', 'bblll']
ova = ['ov', 'ova', 'ovaa', 'ovaaa', 'ovaaaa']
eva = ['ev', 'eva', 'evaa', 'evaaa', 'evaaaa']
chiv_liv = ['chv', 'chiv', 'cchiv', 'chivv', 'chiiv', 'lv', 'liv', 'livv', 'lliv', 'liiv']
osh = ['o', 'oo', 'ooo', 'oooo']
esh = ['e', 'ee', 'eee', 'eeee']
ize = ['i', 'ii', 'iii', 'iiii', 'iiiii']
ezo = ['ez', 'eez', 'eeez', 'eeeez']
ink = ['in', 'iin', 'iiin', 'iiiin', 'iinn']
enk = ['en', 'een', 'eeen', 'eeeen', 'eenn']
ik = ['ik', 'iik', 'iiik', 'iiiik', 'iikk']
ek = ['ek', 'eek', 'eeek', 'eeeek', 'eekk']
chik = ['chik', 'chiik', 'chiiik', 'chiiiik', 'chiiiiik']
shik = ['shik', 'shiik', 'shiiik', 'shiiiik', 'shiiiiik']
ar1 = [chiv_liv, ink, ize, ik, shik, chik]
ar2 = [ek, enk, ezo, esh, eva]
ar3 = [ova, osh]
ar4 = [esh, eva]
arr = [[chiv_liv, ink, ize, ik, shik, chik], [ek, enk, ezo, esh, eva], [ova, osh]],
print(r11(3, [[ar1, ar2], [ar3, ar4]], [0,0,0,0,0]))