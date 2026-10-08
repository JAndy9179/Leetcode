"""
思路: 拓扑排序
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict


        indegree = [0 for _ in range(numCourses)]
        required_dict = defaultdict(list)
        for pair in prerequisites:
            required_dict[pair[0]].append(pair[1])
            indegree[pair[0]] += 1

        queue = [i for i, ind in enumerate(indegree) if ind == 0]
        seen = [c in queue for c in range(numCourses)]
        num_pop = 0
        while queue:
            course_pop = queue.pop(0)
            for c, l in required_dict.items():
                if course_pop in l:
                    l.remove(course_pop)
                    indegree[c] -= 1
                if indegree[c] == 0 and not seen[c]:
                    seen[c] = True
                    queue.append(c)
            num_pop += 1

        return num_pop == numCourses


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
