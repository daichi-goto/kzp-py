def result(jp,rush):
    p0 = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []
    p9 = []
    p10 = []
    for i in jp:
        print(i)
        if i >= 0 and i < 100:
            p0.append(i)
        elif i >= 100 and i < 200:
            p1.append(i)
        elif i >= 200 and i < 300:
            p2.append(i)
        elif i >= 300 and i < 400:
            p3.append(i)
        elif i >= 400 and i < 500:
            p4.append(i)
        elif i >= 500 and i < 600:
            p5.append(i)
        elif i >= 600 and i < 700:
            p6.append(i)
        elif i >= 700 and i < 800:
            p7.append(i)
        elif i >= 800 and i < 900:
            p8.append(i)
        elif i >= 900 and i < 1000:
            p9.append(i)
        else:
            p10.append(i)
    print(len(p0))
    print(len(p1))
    print(len(p2))
    print(len(p3))
    print(len(p4))
    print(len(p5))
    print(len(p6))
    print(len(p7))
    print(len(p8))
    print(len(p9))
    print(len(p10))