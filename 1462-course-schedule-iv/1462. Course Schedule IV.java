class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        int[] inDegree = new int[numCourses];
        for (int[] pre : prerequisites) {
            graph.putIfAbsent(pre[0], new ArrayList<>());
            graph.get(pre[0]).add(pre[1]);
            inDegree[pre[1]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.add(i);
        }
        Map<Integer, Set<Integer>> preMp = new HashMap<>();
        while (!q.isEmpty()) {
            int cur = q.poll();
            inDegree[cur]--;
            for (int nei : graph.getOrDefault(cur, new ArrayList<>())) {
                // for each adj node, add cur node as prerequisite
                // as well as cur node's prerequisites
                preMp.putIfAbsent(nei, new HashSet<>());
                preMp.get(nei).add(cur);
                preMp.get(nei).addAll(preMp.getOrDefault(cur, new HashSet<>()));
                if (--inDegree[nei] == 0) {
                    q.add(nei);
                }
            }
        }
        List<Boolean> res = new ArrayList<>();
        for (int[] query : queries) {
            Set<Integer> preSet = preMp.getOrDefault(query[1], new HashSet<>());
            if (preSet.contains(query[0])) {
                res.add(true);
            } else {
                res.add(false);
            }
        }
        return res;
    }
}