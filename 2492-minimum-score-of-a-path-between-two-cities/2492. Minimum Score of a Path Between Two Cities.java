class Pair {
    public int val;
    public int weight;
    public Pair(int val, int weight) {
        this.val = val;
        this.weight = weight;
    }
}

class Solution {
    public int minScore(int n, int[][] roads) {
        List<List<Pair>> graph = new ArrayList<>();
        for (int i = 0; i < n+1; i++) graph.add(new ArrayList<>());
        for (int[] road : roads) {
            graph.get(road[0]).add(new Pair(road[1], road[2]));
            graph.get(road[1]).add(new Pair(road[0], road[2]));
        }
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> seen = new HashSet<>();
        q.add(1);
        seen.add(1);

        int res = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (Pair nei : graph.get(cur)) {
                int val = nei.val;
                int weight = nei.weight;
                res = Math.min(res, weight);
                if (!seen.contains(val)) {
                    q.add(nei.val);
                    seen.add(nei.val);
                }
            }
        }
        return res;
    }
}