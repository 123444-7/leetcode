# [1. 两数之和](https://leetcode.cn/problems/two-sum/)

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```python
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 方法一：两层循环暴力破解
    for i in range(len(nums)):
        fir_num = nums[i]  # 第一个数
        for i2 in range(i + 1, len(nums)):  # 遍历list从第一个数的下一个数开始
            sec_num = nums[i2]
            if fir_num + sec_num == target:  # 若第一个数和第二个数相加等于目标结果，则返回下标
                target_list = [i, i2]
                break
    return target_list
```

```python
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 方法二：一层循环优化
        for i in range(len(nums)):  # 遍历list
            res = target - nums[i]  # 所需第二个数为目标结果减去第一个数
            if res in nums[i + 1:len(nums)]:  # 如果需要的第二个数在list中，则返回第一个数下标和第二个数下标
                target_list = [i, nums.index(res, i + 1)]
                return target_list
```

```python
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 方法三：hash
    m = {}
    for i, x in enumerate(nums):  # 迭代循环列表，i为list下标，x为list值
        y = target - x  # 所需第二个数为目标结果减去第一个数
        if y in m:  # 如果第二个数在m中，则返回下标，如不存在，则将下标以及数字存入m
            return [m[y], i]  #m[y]为第一个数list下标，i为第二个数下标
        m[x] = i
```



