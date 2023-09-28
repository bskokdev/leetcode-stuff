class Solution {
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.computeIfAbsent(e[0], k -> new ArrayList<>()).add(e[1]);
            graph.computeIfAbsent(e[1], k -> new ArrayList<>()).add(e[0]);
        }
        return dfs(0, -1, graph, hasApple);
    }

    private int dfs(int node, int parent, Map<Integer, List<Integer>> graph, List<Boolean> hasApple) {
        int curNodeMinTime = 0;
        if (graph.containsKey(node)) {
            for (int nei : graph.get(node)) {
                // cycle prevention
                if (nei != parent) {
                    curNodeMinTime += dfs(nei, node, graph, hasApple);
                }
            }
        }
        if (node != 0 && (hasApple.get(node) || curNodeMinTime > 0)) {
            curNodeMinTime += 2;
        }
        return curNodeMinTime;
    }
}