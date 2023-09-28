import java.math.BigInteger;
class Solution {
    public int[] plusOne(int[] digits) {
       StringBuilder sb = new StringBuilder();
        for(int i = 0; i<digits.length; i++) {
            sb.append(digits[i]);
        }

        BigInteger incrementedNum = new BigInteger(sb.toString()).add(BigInteger.ONE);

        StringBuilder temp = new StringBuilder();
        temp.append(incrementedNum);

        int[] output = new int[temp.length()];
        for(int i = 0; i<output.length; i++) {
            output[i] = Integer.parseInt(String.valueOf(temp.charAt(i)));
        }
        return output;
    }
}