var containsNearbyDuplicate = function (nums, k) {
  const hash = new Map();
  for (var i = 0; i < nums.length; i++) {
    if (i - hash.get(nums[i]) <= k) {
      return true;
    }
    hash.set(nums[i], i);
  }
  return false;
};
