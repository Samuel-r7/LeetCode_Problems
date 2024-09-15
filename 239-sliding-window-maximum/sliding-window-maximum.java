class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> res = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            // Remove elements from the back of the deque that are smaller than the current element
            while (!q.isEmpty() && q.getLast() < nums[i]) {
                q.removeLast();
            }
            q.addLast(nums[i]);

            // Remove the element from the front of the deque if it's out of the current window
            if (i >= k && nums[i - k] == q.getFirst()) {
                q.removeFirst();
            }

            // Add the maximum element of the current window to the result
            if (i >= k - 1) {
                res.add(q.getFirst());
            }
        }

        // Convert List<Integer> to int[]
        int[] resultArray = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            resultArray[i] = res.get(i);
        }

        return resultArray;
    }
}