class Solution {
    public String addBinary(String a, String b) {
        int valueA = Integer.parseInt(a, 2);
        int valueB = Integer.parseInt(b, 2);
        
        return Integer.toBinaryString(valueA + valueB); // returns sum
    }
}