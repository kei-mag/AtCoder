from itertools import permutations

N, K = [int(e) for e in input().split(" ")]
S = input()
# zzyyx (yxy, yzy, zxz, zyz)
# zyxyz, yxyzz, zzyxy, xyzyz, yzyxz, yzyzx, xzyzy, zxyzy

# 長さN=5の文字列T="aabcd", 長さK=3の回文
# i=(4-3)=2 T_2+j = T_2+3+1-j
# T_3 = T_5

# K=1 全部だめ
# K=2 同じ文字 aa, bb 
# K=3 aba 
# K=4 abba
# K=5 abcba

# K=3 S=aaabbc     aba 532/2!2!

def is_kaibun(s):
    for h, t in zip(range())

"".join(s) for s in permutations(S)