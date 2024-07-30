from collections import OrderedDict
dic=OrderedDict()
for i in range(int(input())):
    item = input().split()
    pro=' '.join(item[:-1])
    pri = int(item[-1])
    if pro in dic:
        dic[pro] += pri
    else:
        dic[pro] = pri
for i,j in dic.items():
    print(i,j)