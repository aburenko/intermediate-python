from multiprocessing import Pool

def job(num):
    return num * 2


if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, range(20))
    data333 = p.map(job, [333])
    data_two = p.map(job, [5,15])
    p.close()
    print(data)
    print(data333)
    print(data_two)

# eof
