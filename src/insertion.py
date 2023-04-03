from sort import Sort


class InsertionSort(Sort):
    @classmethod
    def sort(cls, arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                else:
                    break
        assert cls.is_sorted(arr)
        return arr


if __name__ == '__main__':
    InsertionSort.main()