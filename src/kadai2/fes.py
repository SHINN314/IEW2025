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
    m = minimum_uncalculated(is_calculated_list)
    k = 0
    is_exist = False

    # indution step
    while (m != -1):
        # step1
        grandy_numbers[m] = k
        is_calculated_list[m] = True

        # step2
        for t in set_t:
            # check if m + t exceeds n
            if m + t > n:
                break

            # check if grandy number is already calculated
            if is_calculated_list[m + t]:
                continue

            # all search for m_prime < m + t
            for m_prime in range(0, m + t):
                if grandy_numbers[m_prime] == k and (m + t - m_prime) not in set_t:
                    is_exist = True
                    break

            if not is_exist:
                # if not exist, set grandy number
                grandy_numbers[m + t] = k
                is_calculated_list[m + t] = True

            # reset is_exist for next t
            is_exist = False

        # update is_calculated_list
        k += 1
        m = minimum_uncalculated(is_calculated_list)
        # is_exist = False

    return grandy_numbers

def main():
    set_t = {2, 3, 5}
    n = 14
    result = fes(set_t, n)
    for i in range(n + 1):
        print(f"Grundy number for {i} stones: {result[i]}")

if __name__ == "__main__":
    main()