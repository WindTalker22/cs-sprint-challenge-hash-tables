def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    count = {}

    for arr in arrays:
        for num in arr:
            if num not in count:
                count[num] = 0

            count[num] += 1

    result = [num for num, freq in count.items() if freq == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
