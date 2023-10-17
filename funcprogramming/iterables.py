#expr_tree = ["*","+","-","a","b","c","d"]
#iterator = iter(expr_tree)
#print(iterator)
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

#iterator = iter(expr_tree)
#for item in iterator:
#    print(item)
"""True if sequence has length 2 to the power of h - 1, otherwise False
"""
def _is_perfect_length(sequence):
    n = len(sequence)
    return ((n+1) & n == 0) and (n != 0)



class LevelOrderIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
            
    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index += 1
        return result

    def __iter__(self):
        return self

def _left_child(index):
    return 2 * index + 1

def _right_child(index):
    return 2 * index + 2

class PreOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                " a perfect binary tree with length 2 to the h power -1"
            )
        self._sequence = sequence
        self._stack = [0]

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        index = self._stack.pop()
        result = self._sequence[index]

        # Pre-order: Push right child first so left child is
        # popped and processed first. Last-in, first-out
        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = _left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result

    def __iter__(self):
        return self