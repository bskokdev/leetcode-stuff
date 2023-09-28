class Pair {
    public String first;
    public double second;

    public Pair(String f, double s) {
        this.first = f;
        this.second = s;
    }
}

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, List<Pair>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);
            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(a).add(new Pair(b, values[i]));
            graph.get(b).add(new Pair(a, 1/values[i]));
        }

        double[] res = new double[queries.size()];
        int i = 0;
        for (List<String> query : queries) {
            res[i++] = evaluate(query.get(0), query.get(1), graph);
        }
        return res;
    }

    private double evaluate(String a, String b, Map<String, List<Pair>> graph) {
        if (!graph.containsKey(a) || !graph.containsKey(b)) {
            return -1;
        }

        Queue<Pair> q = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        q.add(new Pair(a, 1.0));
        while (!q.isEmpty()) {
            Pair cur = q.poll();
            String var = cur.first;
            double product = cur.second;
            if (var.equals(b)) {
                return product;
            }
            seen.add(var);
            for (Pair p : graph.getOrDefault(var, new ArrayList<>())) {
                if (!seen.contains(p.first)) {
                    q.add(new Pair(p.first, p.second * product));
                }
            }
        }
        return -1;
    }
}