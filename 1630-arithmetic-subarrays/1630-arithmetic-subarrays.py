class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []

        for i in range(len(l)):
            subarray = nums[l[i]: r[i] + 1]
            ans.append(self.check(subarray))

        return ans

    def check(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True
