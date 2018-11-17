def poly(string=''):
    s = string
    s = s + '/'
    coef = ''
    st = ''
    r = ''
    n = ''
    v = ''
    for i in range(0, len(s)):
        if s[i] == '^':
            if s[i + 1] == '-' or s[i + 1] == '+':
                return('Это не полином')
        if s[i] == 'x':
            j = i + 1
            if s[j] == '^':
                k = j + 1
                while k != len(s) - 1 and s[k] != '+' and s[k] != '-':
                    st = st + s[k]
                    k = k + 1
            st = st + ','
        if s[i] == 'x':
            j = i - 1
            while s[j + 1] != '-' and s[j + 1] != '+' and j >= 0:
                r = r + s[j]
                j = j - 1
            r = [r for r in r]
            r.reverse()
            if r == ['+'] or r == ['-']:
                r = r + ['1']
            for i in range(0, len(r)):
                n = n + r[i]
            coef = coef + n
            r = ''
            n = ''
            coef = coef + ','
    st = st.split(',')
    del st[len(st) - 1]
    coef = coef.split(',')
    del coef[len(coef) - 1]
    for i in range(0, len(st)):
        if st[i] == '':
            st[i] = '1'
        if st[i - 1] == '0':
            del st[i - 1]
            del coef[i - 1]
    for i in range(0, len(coef)):
        if coef[i] == '':
            coef[i] = '1'
        if coef[i] == '0' or coef[i] == '+0' or coef[i] == '-0':
            del coef[i]
            del st[i]
    for i in range(0, len(st)):
        count = int(coef[i]) * int(st[i])
        coef[i] = count
        if i > 0 and coef[i] > 0:
            coef[i] = '+' + str(coef[i])
        st[i] = int(st[i]) - 1
        st[i] = str(st[i])
        coef[i] = str(coef[i])
    for i in range(0, len(st)):
        if st[i] == '0':
            v = v + coef[i]
        else:
            v = v + coef[i] + 'x^' + st[i]
    return(v)
