"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 方法一：两层循环暴力破解
        # for i in range(len(nums)):
        #     fir_num = nums[i]
        #     for i2 in range(i + 1, len(nums)):
        #         sec_num = nums[i2]
        #         if fir_num + sec_num == target:
        #             target_list = [i, i2]
        #             break
        # return target_list

        # 方法二：一层循环优化
        # for i in range(len(nums)):
        #     res = target - nums[i]
        #     if res in nums[i + 1:len(nums)]:
        #         target_list = [i, nums.index(res, i + 1)]
        #         return target_list

        # 方法三：hash
        m = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in m:
                return [m[y], i]
            m[x] = i


a = Solution()
result = Solution.twoSum(a, [2, 7, 11, 15], 26)
print(result)
