def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    items = {}

    for i, weight in enumerate(weights):
        weight_2 = limit - weights[i]

        if weight_2 not in items:
            items[weight] = i
        else:
            return (i, items[weight_2])

    return None
