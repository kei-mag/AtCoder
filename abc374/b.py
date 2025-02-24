str_a = input()
str_b = input()

for i in range(max(len(str_a), len(str_b))):
    print(">>", i)
    try:
        if str_a[i] != str_b[i]:
            print(i+1)
            exit()
    except IndexError:
        print(i+1)
        exit()
print(0)