class Solution:
    def reversePairs(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Count reverse pairs
            count_pairs(left, right)
            
            # Merge step
            return merge(left, right)
        
        def count_pairs(left, right):
            nonlocal count
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
        
        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        count = 0
        merge_sort(nums)
        return count


# Driver Code
nums = [1, 3, 2, 3, 1]
sol = Solution()
print(sol.reversePairs(nums))  # Output: 2