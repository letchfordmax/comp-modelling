from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+ 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

triangle = Solution().generate(5)
max_width = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    row_str = ' '.join(map(str, row))
    print(row_str.center(max_width))
