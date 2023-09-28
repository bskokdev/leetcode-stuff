class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // time = distance / speed
        int n = position.length;
        List<int[]> cars = zip(position, speed, n);
        cars.sort((a, b) -> b[0] - a[0]);

        int res = 0;
        double lastTimeFleet = 0;
        for (int[] car : cars) {
            double curTime = (double) (target - car[0]) / car[1];
            if (curTime > lastTimeFleet) {
                res++;
                lastTimeFleet = curTime;
            }
        }
        return res;
    }

    private List<int[]> zip(int[] position, int[] speed, int n) {
        List<int[]> list = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            list.add(new int[] {position[i], speed[i]});
        }
        return list;
    }
}