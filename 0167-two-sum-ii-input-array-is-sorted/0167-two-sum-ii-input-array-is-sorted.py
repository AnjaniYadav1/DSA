class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        i = 0
        j = len(arr) - 1

        while i < j:
            total = arr[i] + arr[j]

            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return [i + 1, j + 1]

        return []