# # def binarysearch(arr,n,k):
# #     low=0
# #     high=n-1
# #     while low <high:
# #         mid=(low+high)//2
# #         if arr[mid]==k:
# #             return mid
# #         elif arr[mid]<k:
# #             low=mid+1
# #         elif arr[mid]>k:
# #             high=mid-1
# #     return -1
# #User function template for Python
#
# class Solution:
#     def bini(self,arr,n,k):
#         # code here
#         left = 0
#         right = n - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if arr[mid] == k:
#                 return mid
#             elif arr[mid] < k:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1
# n=5
# arr=[1,2,3,4,5]
# k=int(input())
# obj=Solution()
# print(obj.bini(arr,n,k))
# # print(binarysearch)
a=[1,2,3,4,2]
count=0
target=6
# # b=len(a)-1
# for i in range(len(a)-1):
#     if a[i] + a[i+1] == target:
#         count += 1
#         print([a[i],a[i+1]],end=" ")
# print(count)


