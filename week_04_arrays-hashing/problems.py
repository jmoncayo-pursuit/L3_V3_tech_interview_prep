
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 4])) #false
print(contains_duplicate([1, 2, 3, 1])) #true

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9)) #[0, 1]
print(two_sum([3, 2, 4], 6)) #[1, 2]


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram")) #true
print(is_anagram("rat", "car")) #false