def main():
    expr_tree = ["*","+","-","a","b","c","d"]
    iterator = iter(expr_tree)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    # Iterator is exhausted. It's a single-use, disposable objects.
    # You have to call it again if you want to use it 
    # again.
    iterator = iter(expr_tree)
    print(next(iterator))
print(__name__)
if __name__ == '__main__':
    main()


class LevelOrderIterator:
    # Pass in a sequence.
    def __init__(self, sequence):
        # Make sure the sequence represents a perfect binary tree, described
        # as 2 to the nth power minus 1, where n is the height of the tree.
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                " a perfect binary tree with length 2 to the h power -1"
            )
        # Store the passed in sequence in a 
        # private-by-convention attribute "underscore sequence"
        self._sequence = sequence
        self._index = 0
            
    def __next__(self):
        # Run a check first to make sure the iterator
        # hasn't run beyond the length of the passed-in sequence
        # If it has, raise the appropriate Error
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index += 1
        return result

    # The class is not a conforming iterator, until it 
    # implements dunder iter, which must return an iterator.
    # Which iterator? Itself.
    def __iter__(self):
        return self


class PreOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                " a perfect binary tree with length 2 to the n power minus 1"
            )
        self._sequence = sequence
        # Python has no stack, but list has what we need
        # to use one, as a stack. (LIFO)
        self._stack = [0]

    def __next__(self):
        # Check the stack. If it's empty, stop iteration.
        if len(self._stack) == 0:
            raise StopIteration

        # Pop the top value off the stack to get the current index
        index = self._stack.pop()
        result = self._sequence[index]

        # Pre-order: Push right child first so left child is
        # popped and processed first. (LIFO)
        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = _left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result

    def __iter__(self):
        return self


class InOrderIterator:
    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                "a perfect binary tree with length 2 to the nth power minus 1"
            )
        self._sequence = sequence
        self._stack = []
        self._index = 0

    def __next__(self):
        if (len(self._stack) == 0) and (self._index >= len(self._sequence)):
            raise StopIteration
        
        # Push left children onto the stack while possible
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)
        
        # Pop from stack and process, before moving to the right child
        index = self._stack.pop()
        result = self._sequence[index]
        self._index = _right_child(index)
        return result
    
    def __iter__(self):
        return self


# Our binary tree iterators are limited to perfect binary trees,
# where all nodes are present in all levels. Sentinel objects help solve 
# this problem by representing missing nodes.
# Example: r + p * q
# missing = object()
# expr_tree = ["+", "r", "*", missing, missing, "p", "q"]

# The two references to 'missing' in the expression tree prevent us from 
# rendering the tree as an infix expression, because python cannot join the 
# objects to the string. That's where filters come in.

missing = object()


class SkipMissingIterator():
    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item
            
    def __iter__(self):
        return self


class TranslationIterator:
    
    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iterable

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)
    
    def __iter__(self):
        return self


def _left_child(index):
    return 2 * index + 1


def _right_child(index):
    return 2 * index + 2


def _is_perfect_length(sequence):
    n = len(sequence)
    return ((n+1) & n == 0) and (n != 0)

