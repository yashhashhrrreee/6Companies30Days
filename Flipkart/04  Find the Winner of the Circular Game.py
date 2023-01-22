class Solution:
    def sol(self, n, k, arr, i=0):
        if len(arr) == 1:
            return arr[0]
        else:
            index = (i + k - 1) % len(arr)
            arr.pop(index)
            i = index
            return self.sol(n, k, arr, i)

    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        return self.sol(n, k, arr)
