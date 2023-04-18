from algs4.sort import Sort


class HeapSort(Sort):

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        for i in range(N // 2 - 1, -1, -1):
            cls.sink(arr, i, N)
        for n in range(N, 1, -1):
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            cls.sink(arr, 0, n - 1)
        cls.is_sorted(arr)
        return arr

    @classmethod
    def sink(cls, arr, k, N):
        while 2 * k + 1 < N:
            j = 2 * k + 1
            if j + 1 < N and arr[j] < arr[j + 1]:
                j += 1
            if arr[k] > arr[j]:
                break
            arr[k], arr[j] = arr[j], arr[k]
            k = j


if __name__ == '__main__':
    HeapSort.main()