def smile(string=''):
    s = string
    d = ''
    f = ''
    a = ''
    e = []
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == ')' or s[i] == '[':
            a = a + s[i]

        if s[i] == ']' or s[i] == '{' or s[i] == '}':
            a = a + s[i]
    if a == '':
        return True
    if len(a) % 2 != 0:
        return False
    if a[0] == ')' or a[0] == ']' or a[0] == '}':
        return False
    for i in range(0, len(a)):
        if a[i] == '(' or a[i] == '{' or a[i] == '[':
            e.append(i)
            d = d + a[i]
    if a != '':
        a = [a for a in a]
        e.reverse()

        for i in range(0, len(e)):
            q = int(e[i])
            if a[q + 1] == ')' or a[q + 1] == ']' or a[q + 1] == '}':
                d = d + a[q + 1]
                f = d[len(d) - 2] + d[len(d) - 1]
            if f == '[]' or f == '{}' or f == '()':
                d = d[:-2]
                del a[e[i]]
                del a[e[i]]
        if d == '':
            return True
        else:
            return False
