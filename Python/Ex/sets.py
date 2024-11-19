def average(array):
    r=set(array)
    res=sum(r)/len(r)
    return ("{:.3f}".format(res))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)