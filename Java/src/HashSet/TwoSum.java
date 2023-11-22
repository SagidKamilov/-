package HashSet;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class TwoSum {
    public int[] twoSumNumber(int[] nums, int k){
        Set<Integer> setNums = new HashSet<>();
        for (int i=0; i < nums.length; i++) {
            int numberToFind = k - nums[i];
            if (setNums.contains(numberToFind)) {
                return new int[]{numberToFind, nums[i]};
            }
            setNums.add(nums[i]);
        }
        return new int[0];
    }

    public int[] twoSumIndex(int[] nums, int k){
        Set<Integer> setIndex = new HashSet<>();
        for (int i=0; i < nums.length; i++) {
            int numberToFind = k - nums[i];
            if (setIndex.contains(numberToFind)) {
                int indexNum = findIndex(nums, numberToFind);
                return new int[]{indexNum, i};
            }
            setIndex.add(nums[i]);
        }
        return new int[0];
    }

    // Проблема: при наличии 2 одинаковых чисел, поиск выберет индекс первого попавшегося числа
    // Примечание: работает даже в неотсортированном массиве
    int findIndex(int[] nums, int value){
        for (int i=0; i < nums.length; i++) {
            if (nums[i] == value) {
                return i;
            }
        }
        return -1;
    }
}
