
nums=[2,3,4,567,87,43]
#
# for i in nums:
#     print(i)
#
it=iter(nums)

print(it.__next__())
print(next(it))

for i in nums:
    print(i)