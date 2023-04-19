import sys

from algs4.sequential_search_st import SequentialSearchST
from algs4.binary_serach_st import BinarySerachST


class STClassFactory:
    st_classes = {
        'sequential': SequentialSearchST,
        'binary': BinarySerachST
    }

    @classmethod
    def create_class(cls, name: str):
        try:
            st_class = cls.st_classes[name]
            return st_class
        except KeyError as exc:
            raise ValueError(f'class {name} is not supported') from exc


class FrequencyCounter:
    min_len: int = 1

    def __init__(self, st, min_len=None):
        self.st = st
        self.distinct = 0
        self.words = 0
        if min_len:
            self.min_len = min_len

    def main(self):
        for line in sys.stdin:
            for word in line.split():
                if len(word) < self.min_len:
                    continue
                self.words += 1
                if not self.st.contains(word):
                    self.st.put(word, 1)
                    self.distinct += 1
                else:
                    self.st.put(word, self.st.get(word) + 1)
        max_wd = ''
        max_wd_val = 0
        for word in self.st.keys():
            cur_wd_val = self.st.get(word)
            if cur_wd_val > max_wd_val:
                max_wd = word
                max_wd_val = cur_wd_val
        print(f'{max_wd} {max_wd_val}')
        print(f'distinct = {self.distinct}')
        print(f'words = {self.words}')


if __name__ == '__main__':
    min_len = int(sys.argv[1])
    try:
        st_cls = sys.argv[2].lower()
    except IndexError as exc:
        st_cls = 'sequential'
    st = STClassFactory.create_class(st_cls)()
    fc = FrequencyCounter(st, min_len)
    fc.main()
