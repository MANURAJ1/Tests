# import pandas as pd, numpy  as np
# from sklearn.model_selection import train_test_split
#
# train = pd.read_csv('/home/r/P1/BigMart/Train_UWu5bXk.csv')
# test = pd.read_csv('/home/r/P1/BigMart/Test_u94Q5KV.csv')
#
# comb = pd.concat([train, test])
# comb.apply(lambda x: x.isna().value_counts()).transpose()
#
# comb.apply(lambda x: x.unique().value_counts()).transpose()
# vowels=['A','E','I','O','U']
# s='BANANA'
# Kevin_count = 0;Stuart_count=0
# Kevin = [];Stuart=[]
# for i in range(len(s)):
#     if s[i] in vowels:
#         for j in range(i+1, len(s) + 1):
#             subs = s[i:j]
#             if subs not in Kevin:
#                 Kevin_count = s.count(subs) + Kevin_count
#                 Kevin.append(subs)
#                 print(s.count(subs), subs)
#     else:
#         for k in range(i+1, len(s)):
#             Stuart_count = s.count(subs) + Stuart_count
#             Stuart.append(subs)
#             print(s.count(subs), subs)


def time_delta(t1, t2):
    i=(time.strptime(t1,'%a %d %b %Y %H:%M:%S %z'))
    k=(time.strptime(t2,'%a %d %b %Y %H:%M:%S %z'))

    x=abs(((i.tm_yday-1)*(3600*24)+(i.tm_hour*3600+(i.tm_min*60)+i.tm_sec)-i.tm_gmtoff)-((k.tm_yday-1)*(3600*24)+(k.tm_hour*3600+(k.tm_min*60)+k.tm_sec)-k.tm_gmtoff))+(i.tm_year-k.tm_year)*(24*3600*365)
    return str(x)

