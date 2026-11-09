# Solution নামে একটি class তৈরি করা হয়েছে
class Solution:

    # removeDuplicates নামে একটি function তৈরি করা হয়েছে
    # nums হলো input list বা array
    def removeDuplicates(self, nums):

        # k = 1 দিয়ে শুরু করছি
        # কারণ প্রথম element সবসময় unique হিসেবে ধরা হচ্ছে
        # k দিয়ে unique element-এর সংখ্যা বোঝানো হচ্ছে
        k = 1

        # for loop index 1 থেকে শুরু হবে
        # len(nums) পর্যন্ত চলবে (শেষ index বাদ যাবে)
        # কারণ আমরা প্রতিটি element-এর আগের element-এর সাথে তুলনা করব
        for j in range(1, len(nums)):

            # বর্তমান element এবং আগের element তুলনা করছি
            # যদি দুটো element সমান না হয়,
            # তাহলে বুঝব নতুন একটি unique element পাওয়া গেছে
            if nums[j] != nums[j - 1]:

                # নতুন unique element-টি nums[k] index-এ রাখছি
                # অর্থাৎ duplicate element বাদ দিয়ে
                # unique element-গুলো সামনে সাজাচ্ছি
                nums[k] = nums[j]

                # একটি নতুন unique element পাওয়া গেছে
                # তাই k-এর মান ১ বাড়িয়ে দিচ্ছি
                k += 1

        # সবগুলো element check করা শেষ
        # এখন k-এর মধ্যে মোট unique element-এর সংখ্যা আছে
        return k


# ---------------- Main Program ----------------

# একটি sorted list তৈরি করছি
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Solution class-এর একটি object তৈরি করছি
obj = Solution()

# removeDuplicates function call করছি
# function থেকে যে unique element-এর সংখ্যা return হবে,
# সেটি k variable-এর মধ্যে রাখছি
k = obj.removeDuplicates(nums)

# মোট কয়টি unique element আছে তা print করছি
print("Number of unique elements:", k)

# nums[:k] দিয়ে list-এর প্রথম k টি element দেখাচ্ছি
# অর্থাৎ শুধু unique element-গুলো print করছি
print("Unique elements:", nums[:k])