# program finite excluded substraction algorithm

def minimum_uncalculated(is_calculated_list):
    """
    Find the minimum uncalculated index in the list.

    Parameters
    ----------
    is_calculated_list : list
        List of booleans indicating whether the index has been calculated.

    Returns
    -------
    int
        The minimum uncalculated index.
    """
    for i, calculated in enumerate(is_calculated_list):
        if not calculated:
            return i
    return -1  # If all indices are calculated

def fes(set_t, n):
    """
    Subtract grandy number sequence of all but Nim.

    Parameters
    ----------
    set_t : set
        Set of integers which are unremovable.
    n : int
        The number of stones.

    Returns
    -------
    list
        The list of Grundy numbers.
    """
    is_calculated_list = [False] * (n + 1)
    grandy_numbers = [-1] * (n + 1)

    for i in range(n + 1):
        m = minimum_uncalculated(is_calculated_list)

        if m == -1:
            break

        grandy_numbers[m] = i
        is_calculated_list[m] = True

        for t in set_t:
            if m + t > n:
                continue

            if not is_calculated_list[m + t]:
                for m_prime in range(m + t):
                    if is_calculated_list[m_prime]:
                        break
                    elif grandy_numbers[m_prime] == i and m + t - m_prime not in set_t:
                        break

            grandy_numbers[m + t] = i
            is_calculated_list[m + t] = True

    return grandy_numbers

def main():
    set_t = {2, 3, 5}
    n = 10
    result = fes(set_t, n)
    for i in range(n + 1):
        print(f"Grundy number for {i} stones: {result if i == n else fes(set_t, i)}")

if __name__ == "__main__":
    main()