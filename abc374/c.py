N = input()
K = list(map(int, input().split()))

grp_a = []
grp_b = []

K.sort(reverse=True)
for i, e in enumerate(K):
    if i % 2 == 0:
        grp_a.append(e)
    else:
        grp_b.append(e)

grp_a.sort(reverse=True)
grp_b.sort(reverse=True)

while True:
    diff = sum(grp_a) - sum(grp_b)
    if diff == 0:
        break
    if diff > 0:
        
