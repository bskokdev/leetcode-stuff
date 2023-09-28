class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> baskets = new HashMap<>();
        int left = 0;
        int res = 0;
        for (int r = 0; r < fruits.length; r++) {
            baskets.put(fruits[r], baskets.getOrDefault(fruits[r], 0) + 1);
            if (baskets.size() > 2) {
                baskets.put(fruits[left], baskets.get(fruits[left]) - 1);
                if (baskets.get(fruits[left]) == 0) {
                    baskets.remove(fruits[left]);
                }
                left++;
            }
            res = Math.max(r - left + 1, res);
        }
        return res;
    }
}