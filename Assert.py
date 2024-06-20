def avg(m):
    assert len(m) != 0, "the list is empty"
    return sum(m) / len(m)


marks1 = [12,12,12,12]
print("the average of marks1", avg(marks1))