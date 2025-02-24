N, T, P = [int(e) for e in input().split(" ")]
L = [int(l) for l in input().split(" ")]
rem_L = []
count = 0
for l in L:
    if (diff := T - l) > 0:
        rem_L.append(diff)
    else:
        count += 1
if (diff_people := P - count) <= 0:
    print(0)
else:
    rem_L.sort()
    print(f"{count=}")
    print(f"{rem_L=}")
    print(f"{diff_people=}")
    print(rem_L[diff_people-1])
