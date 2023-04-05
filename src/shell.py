from sort import Sort


class ShellSort(Sort):
    @classmethod
    def sort(cls, arr):
        h = len(arr)
        while h > 1:
            h = h // 3 + 1
            for i in range(h, len(arr), 1):
                for j in range(i, h - 1, -h):
                    if arr[j - h] > arr[j]:
                        arr[j - h], arr[j] = arr[j], arr[j - h]
                    else:
                        break
        assert cls.is_sorted(arr)
        return arr
    

if __name__ == '__main__':
    ShellSort.main()