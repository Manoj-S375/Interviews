"""
Question: Given two integers say k and n, where:
n = no.of people
k = some integer
The people are arranged in circular fashion, and for every round the person in kth position is killed. Find the person 
remaining atlast.
"""

class Solution:
    def circular_kill(self, n: int, k:int)->int:
        persons = [i for i in range(1, n+1)]
        inx = k-1

        while len(persons) > 1:
            del persons[inx]
            inx = (inx + k-1) % len(persons)

        return persons[0]

if __name__ == "__main__":
    sol= Solution()
    n, k = map(int, input("Enter n and k values:").split())
    print("The last person alive is:", sol.circular_kill(n=n, k=k))