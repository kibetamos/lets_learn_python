t=int(input())
for i in range(t):
    s = input()
    a, b= s[::2], s[1::2]
    print(a, b)