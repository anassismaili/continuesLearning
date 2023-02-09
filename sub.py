def subsetsum(array, num):
    if sum(array) == num:
        return array
    if len(array) > 1:
        for subset in (array[:-1], array[1:]):
            result = subsetsum(subset, num)
            if result is not None:
                return result

s = [1,2,5,9,10]
T = 14
print(subsetsum(s, T))