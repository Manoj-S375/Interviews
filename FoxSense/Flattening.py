""""
Question: Given a linked list with some node having child pointer, that points to other linked list. You have the flatten
the linked list at the single level.

Example:
1 2 3 4 5
    |
    6 7 8 10
        |
        9

Output:
1 2 3 6 7 8 9 10 4 5
"""
from typing import List, Tuple

class Solution:
    def flatten(self, nodes: List[Tuple[int, int, List[int]]], levels: int) -> List[int]:
        ans = []
        inx = 0
        remains = []

        for level in range(levels+1):
            while inx <= nodes[level][0]:
                ans.append(nodes[level][2][inx])
                inx += 1
            remains.append(inx)
            inx = 0
        
        for i in range(levels, -1, -1):
            ans.extend(nodes[i][2][remains[i]:])

        return ans
        

if __name__ == "__main__":
    sol = Solution()
    nodes = []

    temp = list(map(int, input("Enter the values for first level:").split()))
    index = int(input("Enter the index for child:"))
    nodes.append((index, len(temp), temp))
    levels = int(input("Enter no.of levels:"))

    for i in range(levels):
        temp = list(map(int, input("Enter the values for the list:").split()))
        index = int(input("Enter the index for child:"))
        nodes.append((index, len(temp), temp))
    
    print("The flatten list:", *sol.flatten(nodes=nodes, levels=levels))