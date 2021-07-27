def func_wrap():
    #从外部接受文本
    newslist_digest = news['digest']
    #设置换行数，此处设置每二十个字符换一次行
    n = int(len(newslist_digest) % 20)
    #创建一个新列表去接受换行后的字符串
    newslist_digest_print = []
    #使用循环，创建一个新字符串去存储换行后的文本
    for nn in range(n):
        #设置首行缩进
        if nn == 0:
            digests = '    '
            beginning = nn * 20
            ending = (nn+1) * 20 - 2
        else:
            digests = ''
            beginning = nn * 20
            ending = (nn + 1) * 20
        #切片后的字符串
        for digest in newslist_digest[beginning: ending]:
                digests += digest
        #去除多余的空字符，防止出现无效字符串
        if digests != '':
            #将切片后的字符串放进列表
            newslist_digest_print.append(digests)
    #输出换行后的字符串
    for un in newslist_digest_print:
        print(un)
