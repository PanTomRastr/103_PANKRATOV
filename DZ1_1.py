def rotate(a):
    k = a[len(a)-1]
    for x in range((len(a)-1), 0 , -1):
        a[x] = a[x-1]
    a[0] = k
    return a
f=list(input())
print(rotate(f))