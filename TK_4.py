def multiply_by_average(list):
    average = sum(list) / len(list)

    for i in range(0, len(list)):
        list[i] *= average

    return list