class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result =[]

        # for i in range(len(nums)-k+1):
        #     cur_win = max(nums[i:i+k])
        #     result.append(cur_win)

        # return result

        q = deque()
        res = []

        for i, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if i >=k and nums[i-k]==q[0]:
                q.popleft()

            if i >=k-1:
                res.append(q[0])

        return res