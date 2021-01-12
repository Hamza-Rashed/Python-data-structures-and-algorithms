def left_join(first, second):

    result = {}

    for f in first:
        result[f]=[first[f]]
        val = None
        if f in second:
            val = second[f]
        result[f].append(val)
    return result