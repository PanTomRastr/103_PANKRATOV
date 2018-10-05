st=[]
print('enter integer number')
x=int(input())
print(x)
if x<0:
    x=x*(-1)
for i in range(1,x+1):
    if x%i==0:
        st.append(i)
        st.append(-i)
print(st)