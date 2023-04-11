import random

from sort import Sort


class QuickSort(Sort):
    @classmethod
    def sort(cls, arr):
        random.shuffle(arr)
        cls.quick_sort(arr, 0, len(arr))
        cls.is_sorted(arr)
        return arr
    
    @classmethod
    def quick_sort(cls, arr, low, high):
        if high - low <= 1:
            return
        j = cls.partition(arr, low, high)
        cls.quick_sort(arr, low, j)
        cls.quick_sort(arr, j + 1, high)
    
    @classmethod
    def partition(cls, arr, low, high) -> int:
        i = low + 1
        j = high - 1
        while True:
            while arr[i] < arr[low]:
                if i == high - 1: break
                i += 1
            while arr[j] > arr[low]:
                if j == low: break
                j -= 1
            if i >= j: break
            arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
            

if __name__ == '__main__':
    QuickSort.main()
