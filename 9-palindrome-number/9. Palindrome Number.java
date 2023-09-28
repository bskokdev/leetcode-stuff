class Solution {
    public boolean isPalindrome(int x) {
        String reversed = "";
		for(int i = Integer.toString(x).length()-1; i >= 0; --i) {
			reversed += Integer.toString(x).charAt(i);
		}
		if(Integer.toString(x).equals(reversed))
			return true;
		return false;
    }
}