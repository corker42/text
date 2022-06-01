a = 0
b = 0
f = open('../bqg_novel/圣墟.txt', mode='r', encoding='utf8')
dic = {' 叶辰':a, '夏若雪':b, }
# for key in dic.keys():
#     for i in f:
#         if key in i:
#             dic[key] = dic[key] + 1
# print(dic)
for i in f:
    if '夏若雪' in i:
        b = b + 1
print(b)