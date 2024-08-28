class Solution:
    def __init__(self) -> None:
        self.inputs = {}
        self.root = None
    
    def bonus(self):
        depth = int(input("Enter the depth:"))
        parent = [self.root]
        child = []
        for _ in range(depth+1):
            for i in parent:
                #print("root",i)
                if i in self.inputs:
                    for j in self.inputs[i]:
                        child.append(j)
            del parent
            parent = []
            while child:
                parent.append(child.pop())
        print("Values at given depth: ",*parent)
    def solve(self):
        ans = []
        n = int(input("Enter no.of relations:"))

        for _ in range(n):
            arr = list(map(int, input("Enter parent, value:").split()))
            if arr[0] in self.inputs:
                self.inputs[arr[0]].append(arr[1])
            else:
                self.inputs[arr[0]] = [arr[1]]

        inpid = int(input("Enter an id:"))

        for val in self.inputs:
            if inpid in self.inputs[val]:
                self.root = val

        for i in self.inputs[self.root]:
            for j in self.inputs[i]:
                if j in self.inputs:
                    for k in self.inputs[j]:
                        ans.append(k)

        print("Grandchildren of the given value:")
        for i in ans:
            print(i, end=' ')
        print()

if __name__ == "__main__":
    sol = Solution()
    sol.solve()
    sol.bonus()

