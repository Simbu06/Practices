def count_substring(string, sub_string):
    x = list(string)
    y = list(sub_string)
    z = []
    for i in range(len(x)):
        if y[0] not in x:
            break
        if x[i] in y and x[i] not in z:
            z.append(x[i])
    return len(z)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)