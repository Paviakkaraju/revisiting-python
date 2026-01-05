"""
Build a tiny "stats toolkit" with the folloeing functions:
- mean(values)
- median(values)
- mode(values)
- standard_deviation(values)

Rules:
1️⃣ No using numpy or statistics yet — implement the logic.
2️⃣ Raise clear errors for bad inputs.
3️⃣ Add docstrings + type hints.
"""
def mean(values: list):
    """Mean represents the average of a data. 
    It is calculated by adding all the values and then dividing by the total number of values"""

    n = len(values)
    values_sum = sum(values)
    res = values_sum/n
    return res

def median(values: list):
    """Median represents the middle value of a sorted data.
    It is also called as the 50th percentile.
    It is calculated by sorting the data in either ascending or descending order followed by getting the middle value"""

    n = len(values)
    sorted_values = sorted(values)

    if n%2 != 0:
        ind = (n-1)//2
        res = sorted_values[ind]
        return res
    else:
        ind = (n-2)//2
        res = sorted_values[ind] + sorted_values[ind+1]
        return res/2
    
def mode(values: list)->tuple:
    """Mode represents the most repeated data. It can be represented for both number or text."""
    values_type = [1 if type(data)==int else 0 for data in values]
    n = len(values)

    if sum(values_type) != n:
        print("All elements in the input list must be of same type!")
    else:
        values_count = {}
        for data in values:
            if data in values_count:
                values_count[data] += 1
            else: 
                values_count[data] = 1

        max_value = max(values_count.values())

        res_list = []
        for k,v in values_count.items():
            if v == max_value:
                res_list.append(k)
        res = tuple(res_list)
        return res









