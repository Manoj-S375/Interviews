def check(n):
    i = 2

    while (i * i <= n):
        if n % i == 0:
            return False

        i += 1
    return True


def recursive(num, ds, inx):
    if inx < 0:
        return 
    for i in range(inx, -1, -1):
        for j in range(1, 10):
            n = num[0:i] + str(j) + num[i+1:]
            if check(int(n)) and n not in ds:
                ds.append(n)
                #print(n, num)
                recursive(n, ds, inx-1)
                recursive(n, ds, inx)
        
    return 

def solve():
    ans = []
    val = list(map(int, input("Enter 2 numbers:").split()))

    #ans.append(str(val[0]))
    # temp = ["99901"]
    # size = 0

    # while size < len(temp):
    #     nn = temp[size]
    #     for i in range(4, -1, -1):
    #         for j in range(1, 10):
    #             n = nn[0:i] + str(j) + nn[i+1:]
    #             if check(int(n)) and n != nn:
    #                 ans.append(n)
    #                 temp.append(str(n))
    #     print(*temp)
        
    #     size += 1

    recursive(str(val[0]), ans, 3)
    print(*ans)

if __name__ == "__main__":
    solve()