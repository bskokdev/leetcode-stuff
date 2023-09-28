public class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
    	int min = 0;
    	int max = letters.length-1;

    	if(target >= letters[max]) {
    		return letters[0];
    	}

    	while(min <= max) {
    		int mid = min + (max - min) / 2;
    		if(target < letters[mid]) {
				max = mid - 1;
    		} else {
    			min = mid + 1;
    		}
    	}
    	return letters[min];
    }
}