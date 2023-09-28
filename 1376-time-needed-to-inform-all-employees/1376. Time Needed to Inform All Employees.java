class Pair {
    public int first;
    public int second;
    public Pair(int f, int s) {
        this.first = f;
        this.second = s;
    }
}

class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) {
                graph.putIfAbsent(manager[i], new ArrayList<>());
                graph.get(manager[i]).add(i);
            }
        }
        Queue<Pair> q = new ArrayDeque<>();
        q.add(new Pair(headID, 0));
        int res = 0;
        while (!q.isEmpty()) {
            Pair cur = q.poll();
            int employee = cur.first;
            int time = cur.second;
            res = Math.max(res, time);
            if (graph.containsKey(employee)) {
                for (int nextEmployee : graph.get(employee)) {
                    q.add(new Pair(nextEmployee, time + informTime[employee]));
                }
            }
        }
        return res;
    }
}