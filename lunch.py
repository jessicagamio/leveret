"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])


    # at_rest set to False by default
    at_Rest = False

    # carrots = 0

    # Get center cell of garden
    # lev moved to center cell
    row = nrows//2
    col = ncols//2

    # lev starts at center
    lev = garden[row, col-1]

    while not at_Rest:


        # if row >= 0 and row<= nrows and col >=0 and col <= ncol
        # check W cell and assign max
        # check N cell, if num is larger than max assign max to num
        # check E cell, if num is larger thant max assign max to num
        # check S cell, if num is larger than max assign max to num

        # Check west
        if col-1 >= 0 and garden[row, col-1] != 0:
            west_cell = garden[row, col-1]
            if max >= west_cell:
                row = row
                col = col -1
                max = west_cell

        # Check North   
        if row -1 >= 0 and garden[row-1, col] > west_cell :
            north_cell = garden[row-1, col]
            if max >= north_cell:
                row = row-1
                col = col
                max = north_cell

        # check east
        if row+1 <= nrows and garden[row + 1, col] > north_cell:
            east_cell =garden[row+1, col]
            if max >= east_cell:
                row = row + 1
                col = col
                max = east_cell

        # check south
        if col+1 <= ncols and garden[row, col +1] > east_cell:
            south_cell = garden[row, col+1]
            if max >= south_cell:
                row = row
                col = col + 1
                max = south_cell
        
        #if max did not move return carrot
        if max == lev:
            at_Rest= Trues

        else:
            # move lev into max location
            lev = max
            carrots += max

    return carrots



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
