3Sum (Triplets sum = 0) — Solution Steps

Approach 1: Brute Force
Steps:
3টা nested loop চালাও (i, j, k)
প্রতিটা combination থেকে 3টা number নাও
sum check করো = 0 কিনা
duplicate avoid করার জন্য sorted string key বানাও
Set-এ না থাকলে result এ push করো
Complexity:
Time: O(n³)
Space: O(n)


Approach 2: Sorting + Two Pointer (Best / Interview standard)
Steps:
Array sort করো
একটা loop চালাও i = 0 → n-3
যদি i > 0 এবং nums[i] == nums[i-1] → skip (duplicate avoid)
Two pointer নাও:
left = i + 1
right = n - 1
loop চালাও যতক্ষণ left < right:
sum = nums[i] + nums[left] + nums[right]
যদি sum == 0 → result এ push, তারপর left++ & right--, duplicate skip
যদি sum < 0 → left++
যদি sum > 0 → right--
Complexity:
Time: O(n²)
Space: O(1) (result ছাড়া)
Approach 3: HashSet (Two Sum style per element)
Steps:
outer loop: i from 0 to n
প্রতিবার i fix করো
একটা Set নাও (seen)
inner loop j চালাও:
target = -(nums[i] + nums[j])
যদি seen-এ target থাকে → triplet পাওয়া গেছে
না হলে nums[j] add করো seen-এ
duplicate avoid করতে sorted triplet store করো
Complexity:
Time: O(n²)
Space: O(n)