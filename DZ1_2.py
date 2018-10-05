print('Enter the number, operation and the second number')
n1=int(input())
op=str(input())
n2=int(input())
def calc(n1,op,n2):
    if op=='+':
        return int(n1)+int(n2)
    elif op=='-':
        return int(n1)-int(n2)
    elif op=='*':
        return int(n1)*int(n2)
    elif op=="/":
        return int(n1) / int(n2)
    else:
        return 'Unknown operation'
print(calc(n1,op,n2))