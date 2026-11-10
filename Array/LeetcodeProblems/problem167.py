
class Solution:
    def twoSum(self, numbers, target):

        # Problem:
        # We are given a sorted integer array 'numbers'
        # and an integer 'target'.
        # We need to find two numbers whose sum equals target.
        # We have to return their 1-based indices.
        # Exactly one solution exists.

        # Approach: Two Pointer Technique

        # Initialize two pointers
        # i starts from the first index
        # j starts from the last index
        i = 0
        j = len(numbers) - 1

        # Run the loop while i is smaller than j
        while i < j:

            # Calculate the sum of two pointer values
            if numbers[i] + numbers[j] < target:

                # If sum is smaller than target,
                # move the left pointer one step right
                # to increase the sum
                i += 1

            elif numbers[i] + numbers[j] > target:

                # If sum is greater than target,
                # move the right pointer one step left
                # to decrease the sum
                j -= 1

            else:

                # If sum equals target,
                # we have found the required two numbers.
                # Return their 1-based indices
                return [i + 1, j + 1]


# Example:
# numbers = [2, 7, 11, 15]
# target = 9
#
# Step 1: 2 + 15 = 17 (greater than 9), j--
# Step 2: 2 + 11 = 13 (greater than 9), j--
# Step 3: 2 + 7 = 9 (target found!)
#
# Output: [1, 2]


# Time Complexity: O(n)
# Because each pointer moves at most n times.

# Space Complexity: O(1)
# Because we use only two pointers
# and no extra data structure.
nums = [2, 7, 11, 15]
target = 9

obj = Solution()
result = obj.twoSum(nums, target)
print(result)