# from collections import defaultdict 
  
# MAX_CHARS = 256
  
# # Function to find smallest window  
# # containing 
# # all distinct characters 
  
  
# def findSubString(str): 
#     n = len(str) 
      
#     # Count all distinct characters. 
#     dist_count = len(set([x for x in str])) 
  
#     # Now follow the algorithm discussed in below 
#     # post. We basically maintain a window of characters 
#     # that contains all characters of given string. 
#     curr_count = defaultdict(lambda: 0) 
#     count = 0
#     for j in range(n): 
#         curr_count[str[j]] += 1
#         # If any distinct character matched, 
#         # then increment count 
  
#         if curr_count[str[j]] == 1: 
#             count += 1
  
#         # Try to minimize the window i.e., check if 
#         # any character is occurring more no. of times 
#         # than its occurrence in pattern, if yes 
#         # then remove it from starting and also remove 
#         # the useless characters. 
  
#         if count == dist_count: 
#             while curr_count[str[start]] > 1: 
#                 if curr_count[str[start]] > 1: 
#                     curr_count[str[start]] -= 1
#                 start += 1
  
#             # Update window size 
#             len_window = j - start + 1
#             if min_len > len_window: 
#                 min_len = len_window 
#                 start_index = start 
  
#     # Return substring starting from start_index 
#     # and length min_len """ 
#     return str[start_index: start_index + min_len] 
      
# # Driver code 
# if __name__=='__main__': 
#     print("Smallest window containing all distinct characters is: {}"
#          .format(findSubString("aabcbcdbca"))) 

s = "abcda"
maxl=0
templ=0
start=0
end=0
dict1={}
stopind=0
while(end<len(s)):
    if s[end] not in dict1:
        dict1[s[end]]=end
        templ+=1
    else:
        if(dict1[s[end]]<stopind):
            templ+=1
            dict1[s[end]]=end
        else:
            maxl=max(templ,maxl)
            templ=templ-(dict1[s[end]]-stopind)
            stopind=dict1[s[end]]+1
            dict1[s[end]]=end
    end+=1
print(max(maxl,templ))