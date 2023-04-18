from algs4.sort import Sort


class SelectionSort(Sort):
    @classmethod
    def sort(cls, arr: list):
        for i in range(len(arr) - 1):
            min_idx = i
            for j in range(i, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        assert cls.is_sorted(arr)
        return arr
    

if __name__ == '__main__':
    SelectionSort.main()
            