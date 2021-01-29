from SR.service import getLensdata3, updateLen3


def test1():
    result, row, vol = getLensdata3();
    for i in range(row):
        print(result[i])
    print(row)
    print(vol)

def test2():
    updateLen3();