class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        Map<Integer, Integer> mp = new HashMap<>();
        int mostGaps = 0;
        for (List<Integer> row : wall) {
            int position = 0;
            for (int i = 0; i < row.size() - 1; i++) {
                position += row.get(i);
                mp.put(position, mp.getOrDefault(position, 0) + 1);
                mostGaps = Math.max(mostGaps, mp.get(position));
            }
        }
        return wall.size() - mostGaps;
        
    }
}