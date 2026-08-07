class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        left = 0
        count=0

        for right in range(len(arr)):

            window_sum += arr[right]

            if right - left + 1 > k:
                window_sum -= arr[left]
                left += 1

            if right - left + 1 == k:
                if window_sum / k >= threshold:
                    count += 1
        return count