with open ('蹈虚 .txt', 'r', encoding='utf8') as f1,\
    open ('蹈虚1 .txt', 'a+', encoding='utf8') as f2:
    for old in f1:
        new = old.replace('     ', '\n')
        f2.write(new)