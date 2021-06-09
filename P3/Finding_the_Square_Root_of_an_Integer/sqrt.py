def sqrt(num):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(num, int) or num < 0:
        return None

    if(num == 1):
        return num

    def f(x): return x**2 - num

    lowest = 0
    highest = num
    f_lowest = f(lowest)

    def find_root(lowest, highest, f_lowest):
        middle = (highest + lowest)//2
        f_middle = f(middle)

        if(middle == lowest or f_middle == 0):
            return middle

        if f_lowest*f_middle < 0:
            return find_root(lowest, middle, f_lowest)
        else:
            return find_root(middle, highest, f_middle)

    return find_root(lowest, highest, f_lowest)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Edge cases
print("Pass" if (None is sqrt(-1)) else "Fail")
print("Pass" if (None is sqrt("1")) else "Fail")
print("Pass" if (None is sqrt(2.1)) else "Fail")
