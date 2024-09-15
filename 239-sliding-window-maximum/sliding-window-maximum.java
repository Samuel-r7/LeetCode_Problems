class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> res = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            while (!q.isEmpty() && q.getLast() < nums[i]) {
                q.removeLast();
            }
            q.addLast(nums[i]);

            if (i >= k && nums[i - k] == q.getFirst()) {
                q.removeFirst();
            }

            if (i >= k - 1) {
                res.add(q.getFirst());
            }
        }

        int[] resultArray = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            resultArray[i] = res.get(i);
        }

        return resultArray;
    }
}