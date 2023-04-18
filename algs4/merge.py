from typing import List

from algs4.sort import Sort


class MergeSort(Sort):
    aux: List
    @classmethod
    def sort(cls, arr):
        cls.aux = arr[:]
        cls.merge_sort(arr, 0, len(arr))
        assert cls.is_sorted(arr)
        return arr
    
    @classmethod
    def merge_sort(cls, arr, low, high):
        if high - low <= 1:
            return
        mid = low + (high - low) // 2        
        cls.merge_sort(arr, low, mid)
        cls.merge_sort(arr, mid, high)
        cls.merge(arr, low, mid, high)

    @classmethod
    def merge(cls, arr, low, mid, high):
        cls.aux[low:high] = arr[low:high]
        i = low
        j = mid
        for k in range(low, high):
            if i >= mid:
                arr[k] = cls.aux[j]
                j += 1
            elif j >=high:
                arr[k] = cls.aux[i]
                i += 1
            elif cls.aux[i] <= cls.aux[j]:
                arr[k] = cls.aux[i]
                i += 1
            else:
                arr[k] = cls.aux[j]
                j += 1

        
if __name__ == '__main__':
    MergeSort.main()