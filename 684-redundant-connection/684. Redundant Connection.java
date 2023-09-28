class UnionFind {
    private int[] parent;
    private int[] sizeRank;

    public UnionFind(int n) {
        parent = new int[n];
        sizeRank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            sizeRank[i] = 1;
        }
    }

    public int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    public boolean union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa == pb) {
            return false;
        }
        if (sizeRank[pa] < sizeRank[pb]) {
            parent[pa] = pb;
            sizeRank[pb] += sizeRank[pa];
        } else {
            parent[pb] = pa;
            sizeRank[pa] += sizeRank[pb];
        }
        return true;
    }
}

class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        UnionFind uf = new UnionFind(edges.length);
        for (int[] e : edges) {
            if (!uf.union(e[0]-1, e[1]-1)) {
                return new int[] {e[0], e[1]};
            }
        }
        return new int[] {};
    }
}