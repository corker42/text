# import os
# path = r"C:\Users\sanyuan\Desktop\np_text\bqg_novel\风起龙城\\"
# f = os.listdir(path)
# for i in f:
#     try:
#         old = path + '\\' + i
#         tem = i.split("章")[0]
#         # os.rename(old,new)
#     except IndexError:
#         print(old)
#         continue
# dic = {'零':0,'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}
# for dr in f:
#     old = path + '\\' + dr
#     tem1 = dr.split("章")
#     tem = tem1[0]
#     try:
#         if len(tem) == 3:
#             if tem[1] == '十':
#                 new = path + '\\' + str(dic[tem[0]]) + str(dic[tem[2]]) + tem1[1]
#                 os.renames(old, new)
#             else:
#                 new = path + '\\' + str(dic[tem[0]]) + str(dic[tem[1]])+ str(dic[tem[2]]) + tem1[1]
#                 os.renames(old, new)
#         elif len(tem) == 2:
#             if tem[1] == '十':
#                 new = path + '\\' + str(dic[tem[0]]) + '0' + tem1[1]
#                 os.renames(old, new)
#             elif tem[0] == '十':
#                 new = path + '\\' + '1' + str(dic[tem[1]]) + tem1[1]
#                 os.renames(old, new)
#             elif tem[1] == '百':
#                 new = path + '\\' + str(dic[tem[0]]) + '00' + tem1[1]
#                 os.renames(old, new)
#             else:
#                 new = path + '\\' + str(dic[tem[0]]) + str(dic[tem[1]]) + tem1[1]
#                 os.renames(old, new)
#         elif len(tem) == 1:
#             if tem[0] != '十':
#                 new = new = path + '\\' + str(dic[tem[0]]) + tem1[1]
#                 os.renames(old, new)
#             else:
#                 new = new = path + '\\' + '10' + tem1[1]
#     except IndexError:
#         print(dr)
#         continue
#     except KeyError:
#         print(dr)
#         continue










