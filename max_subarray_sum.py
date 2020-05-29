def maxSubArray(self, l: List[int]) -> int:
    n=len(l)
    max_so_far=0
    sum_till_here=0
    max_negative=-999999999999
    for i in l:
        sum_till_here+=i
        if sum_till_here>max_so_far:
            max_so_far=sum_till_here
        if sum_till_here<0:
            sum_till_here=0
        if i>max_negative:
            max_negative=i
    if max_so_far==0:
        max_so_far=max_negative
    return max_so_far
