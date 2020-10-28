class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        st = []
        
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]
        
        st.append(nums[0])
        ans = []
        
        for i in range(1, n):
            if not st:
                st.append(nums[i])
            else:
                if st and nums[i] == (st[-1] + 1):
                    st.append(nums[i])

                else:
                    end = st[-1]
                    st.pop()

                    if not st:
                        ans.append(str(end))

                    else:
                        while len(st) > 1:
                            st.pop()

                        start = st[-1]
                        st.pop()
                        ans.append(str(start) + "->" + str(end))
                    st.append(nums[i])
        if st:
            end = st[-1]
            st.pop()
            if not st:
                ans.append(str(end))
            else:
                while len(st) > 1:
                    st.pop()
                start = st[-1]
                st.pop()
                ans.append(str(start) + "->" + str(end))
        return ans