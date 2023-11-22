"""
На вход дается целочисленный массив (числа расположены хаотично) и число,
которое соответствует сумме двух чисел (сумма состоит строго из 2 чисел, если таких нет, то вернуть None)
из массива. Необходимо найти индексы этих 2 чисел и вернуть их в виде списка.
ПО УСЛОВИЮ - РЕШЕНИЕ ТОЛЬКО ОДНО
"""
from typing import Union, List, Tuple
import random

from Python.TestTime import test_time


class Solution:
    @staticmethod
    @test_time
    def two_sum(nums: Union[List[int], Tuple[int]], target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        array_of_index = {}
        for index_num, num in enumerate(nums):
            comp = target - num
            if comp in array_of_index:
                return [array_of_index[comp], index_num]

            array_of_index[num] = index_num

        return None


# Генерация тестовых данных
integer_array: List[int] = [random.randint(1, 100) for i in range(1, random.randint(1, 1000))]
test_target: int = 10


# Запуск функции
solution = Solution().two_sum(nums=integer_array, target=test_target)
print(solution)
