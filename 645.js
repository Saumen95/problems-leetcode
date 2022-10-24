/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function (nums) {
  let unique = new Map();
  result = [];
  for (nums in nums) {
    if (unique.has(num)) {
        result[0] = num;
        unique.set(num, true);
    }
      for (let i = 0; i < nums.length; i++) {
          if (!unique.has(i)) {
              result[1] = i;

}
      }
      return result;
};
