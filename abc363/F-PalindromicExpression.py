sosuu_list = [2, 3, 5, 7]

def soinsuu_bunkai(n):
    elements = []
    while True:
        found = False
        for sosuu in sosuu_list:
            print(f"{n} % {sosuu} == {n%sosuu}")
            if n % sosuu == 0:
                elements += [str(sosuu), "*"]
                n = n / sosuu
                print(f"{n=}")
                found = True
                break
        if not found:
            elements.append(n)
            break
    return elements
# N = int(input())
print(soinsuu_bunkai(101))