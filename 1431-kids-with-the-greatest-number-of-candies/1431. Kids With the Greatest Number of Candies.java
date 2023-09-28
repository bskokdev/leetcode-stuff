class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> willHaveMostWhenReceivesExtra = new ArrayList<Boolean>();
        for(int i = 0; i<candies.length; i++) {
        	int maxValue = maxValue(candies);
        	if((candies[i] + extraCandies) >= maxValue)
        		willHaveMostWhenReceivesExtra.add(true);
        	else
        		willHaveMostWhenReceivesExtra.add(false);
        }
        return willHaveMostWhenReceivesExtra;
    }
    public int maxValue(int[] arr) {
    	int max = 0;
    	for(int i = 0; i<arr.length; i++) {
    		if(arr[i] > max)
    			max = arr[i];
    	}
    	return max;
    }
}