import HashSet.TwoSum;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {


        int[] arrayInt = new int[5];
        for (int i=0; i<arrayInt.length; i++){
            arrayInt[i] = (int) Math.round((Math.random() * 10));
        }

        TwoSum test = new TwoSum();
        int k = 8;
        System.out.println(k);
        System.out.println(Arrays.toString(arrayInt));
        System.out.println(Arrays.toString(test.twoSumIndex(arrayInt, k)));
        System.out.println(Arrays.toString(test.twoSumNumber(arrayInt, k)));
    }
}