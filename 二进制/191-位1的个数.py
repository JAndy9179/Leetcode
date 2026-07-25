class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            if n & 1 == 1:
                cnt += 1
            n = n >> 1
        return cnt


if __name__ == '__main__':
    test = Solution()
    print(test.hammingWeight(13))
