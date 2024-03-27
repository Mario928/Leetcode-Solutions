class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        logK = math.log(k)

        # Calculate prefix sum of logarithms of elements
        logs_prefix_sum = [0]
        for num in nums:
            logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))

        total_count = 0
        # Calculate subarray count with product less than k
        for i, log_num in enumerate(logs_prefix_sum):
            j = bisect.bisect(logs_prefix_sum, log_num + logK - 1e-9, i+1)
            total_count += j - i - 1
        return total_count