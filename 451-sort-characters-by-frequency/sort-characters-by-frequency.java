class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> countMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }

        // Step 2: Convert the string to a list of characters for sorting
        List<Character> sortedList = new ArrayList<>();
        for (char c : s.toCharArray()) {
            sortedList.add(c);
        }

        // Step 3: Sort by frequency and then lexicographically (character order)
        Collections.sort(sortedList, (a, b) -> {
            int freqA = countMap.get(a);
            int freqB = countMap.get(b);

            if (freqA != freqB) {
                return Integer.compare(freqB, freqA);  // Sort by frequency (descending)
            } else {
                return Character.compare(a, b);  // Sort lexicographically (ascending)
            }
        });

        StringBuilder result = new StringBuilder();
        for (char c : sortedList) {
            result.append(c);
        }

        return result.toString();
        
    }
}