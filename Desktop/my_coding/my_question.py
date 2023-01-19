# why using generator?

# for exmaple: making 1~10 sequence

n = 10
def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1


def I_think(n):
    i = 0
    while i < n:
        return i
        i += 1


tmp = 0
def I_think2(n):
    while tmp < n:
        print()

for i in generator(n):
    print(i)

print(I_think(n))