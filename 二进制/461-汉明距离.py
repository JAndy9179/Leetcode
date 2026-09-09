"""
思路: 

汉明距离, 指的是两个数字对应二进制位不同的位置数目, 而按位异或操作(^)的结果正好是不同位置为 1, 相同位置为 0, 之后只需统计按位异或操作后的 1 的数目即可
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        return str(bin(diff)).count("1")