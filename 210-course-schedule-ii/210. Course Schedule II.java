class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        int[] inDegree = new int[numCourses];
        for (int[] pre : prerequisites) {
            graph.putIfAbsent(pre[1], new ArrayList<>());
            graph.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.add(i);
        }
        int[] order = new int[numCourses];
        int i = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            order[i++] = cur;
            inDegree[cur]--;
            for (int nei : graph.getOrDefault(cur, new ArrayList<>())) {
                if (--inDegree[nei] == 0) {
                    q.add(nei);
                }
            }
        }
        if (i == numCourses) {
            return order;
        }
        return new int[0];
    }
}