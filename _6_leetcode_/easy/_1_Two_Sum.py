class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 2018-7-19 22:52:42
        value = zip(nums, range(len(nums)))
        print(list(value))
        vale2 = list(value) # 这里vale2是空，上面用完之后迭代器为空
        print(vale2)

        value3 = zip(range(len(nums)), nums)
        value4 = dict(value3)
        print(value4)

        #元素作为key这才对




        # value1 = dict(zip(range(len(nums), nums)))
       # print(value1)


        return value


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 2018-7-19 22:53:01
        if len(nums) < 2:
            return False

        value = {}
        size = len(nums)
        for x in range(size):
            checkvalue = target - nums[x]
            if checkvalue in value:
                return [x, value[checkvalue]]
            else:
                value[nums[x]] = x



if __name__ == '__main__':
    s = Solution()
    value = s.twoSum([2,7,11,15], 9)
    print('end')
    # vale = list((1, 2, 3, 4, 5)) # list 还是并不是生成一个迭代器
    # dic1 = dict(vale)