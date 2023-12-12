def wrap(string, max_width):
    l1 = []
    s1 = ''
    for i in range(len(string)):
        if i != 0 and i % max_width == 0:
            l1.append(s1)
            s1 = ''
            s1 = '\n' + s1 + string[i]
        else:
            s1 = s1 + string[i]
    l1.append(s1)
    s = ''.join(l1)
    return s


# import textwrap
# 
# def wrap(s,n):
#     res = textwrap.wrap(s,n)
#     return "/n".join(res)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)