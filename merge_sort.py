def sorted(list, key=None, reverse=False):
    """Sorts the elements of a list in ascending order.

    Args:
    list: The list to be sorted.
    key: A function that takes a list element as an argument and returns a value
        to be used for sorting. The default value is None, which means that the
        elements of the list will be sorted using their natural ordering.
    reverse: A boolean value that indicates whether the list should be sorted in
        ascending (False) or descending (True) order. The default value is False.

    Returns:
    A new list with the elements of the specified list sorted in ascending order.
    """

    if key is None:
        key = lambda x: x

    def merge(left, right, reverse=False):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            # Adjust the comparison based on the reverse parameter
            if (not reverse and key(left[i]) < key(right[j])) or (reverse and key(left[i]) > key(right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


    def sort(list):
        if len(list) <= 1:
            return list
        mid = len(list) // 2
        left = sort(list[:mid])
        right = sort(list[mid:])
        return merge(left, right)

    return sort(list)


mylist = [(2,5), (6,10), (90,20), (75,12),(10,1)]


print(sorted(mylist, key=lambda x: x[1], reverse=True))
