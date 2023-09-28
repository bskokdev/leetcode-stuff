class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> dissapeared = new ArrayList<>();
        Set<Integer> validNumbers = new HashSet<>();
        for (int num : nums) {
          validNumbers.add(num);
        }
        for (int i = 1; i <= nums.length; i++) {
          if (!validNumbers.contains(i)) {
            dissapeared.add(i);
          }
        }
        return dissapeared;
    }
}