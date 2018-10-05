k=0
print('Enter integer number')
x=int(input())
print(x)
if x<0:
    x=x*(-1)
for i in range(2,x+1):
    if x%i==0:
        k+=1
if k==1:
    print('There is no divider')
else:
    print('Diveders are')