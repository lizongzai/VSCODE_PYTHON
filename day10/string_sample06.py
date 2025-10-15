a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(a)
print(b, c)  # b'\xe9\xaa\x86\xe6\x98\x8a' b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))
print(c.decode('gbk'))