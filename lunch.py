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

    # if more than one center cell choose the cell with the most carrots
    if nrows%2==0 and ncols%2!=0:
        if garden[nrows//2][ncols//2] > garden[(nrows//2)-1][ncols//2]:
            row=nrows//2
            col=ncols//2

        else:
            row=(nrows//2)-1
            col=ncols//2

    elif nrows%2!=0 and ncols%2!=0:
            row=nrows//2
            col=ncols//2

    elif nrows%2!=0 and ncols%2==0:
        if garden[nrows//2][ncols//2] > garden[nrows//2][(ncols//2)-1]:
            row=nrows//2
            col=ncols//2

        else:
            row=nrows//2
            col=(ncols//2)-1     

    elif nrows%2 ==0 and ncols %2==0:
        if garden[nrows//2][ncols//2] > garden [(nrows//2)-1][ncols//2]:
            row1=nrows//2
            col1=ncols//2

        else:
            row1 = (nrows//2)-1
            col1 = ncols//2

        if  garden[nrows//2][(ncols//2)-1] > garden[(nrows//2)-1][(ncols//2)-1]:
            row2=nrows//2
            col2=(ncols//2)-1
        else:
            row2=(nrows//2)-1
            col2=(ncols//2)-1

        if garden[row1][col1] > garden[row2][col2]:
            row=row1
            col = col1
        else:
            row=row2
            col=col2

    center=(row,col)

    print('center=====>','row ',row,'col ', col)

    # at_rest set to False by default
    at_Rest = False

    carrots = 0

    # lev starts at center and number is changed to zero

    row,col = center
    garden[row][col] = 0

    while not at_Rest:

        # if row >= 0 and row<= nrows and col >=0 and col <= ncol
        # check W cell and assign max
        # check N cell, if num is larger than max assign max to num
        # check E cell, if num is larger thant max assign max to num
        # check S cell, if num is larger than max assign max to num
        west_cell = garden[row][col-1]
        print('west ====>', west_cell)

        north_cell = garden[row-1][col]
        print('north ====>', north_cell)

        east_cell =garden[row+1][col]
        print('east ====>', east_cell)
        
        south_cell = garden[row][col+1]
        print('south ====>', south_cell)

        print('row===>', row, 'col====>', col)
        # Check west
        # if col-1 >= 0 and garden[row][col-1] != 0:
        if garden[row][col-1] != 0:
            if garden[row][col] >= west_cell:
                row = row
                col = col -1
                new_cell = (row,col)
                print('carrots in west cell =====>', garden[row][col])

        # Check North   
        if row -1 >= 0 and garden[row-1][col] > west_cell :
            if garden[row][col] >= north_cell:
                row = row-1
                col = col
                new_cell = (row,col)
                print('carrots in west cell =====>', garden[row][col])

        # check east
        if row+1 <= nrows and garden[row + 1][col] > north_cell:
            if garden[row][col] >= east_cell:
                row = row + 1
                col = col
                new_cell = (row,col)
                print('carrots in west cell =====>', garden[row][col])

        # check south
        if col+1 <= ncols and garden[row][col +1] > east_cell:
            if garden[row][col] >= south_cell:
                row = row
                col = col + 1
                new_cell = (row,col)
                print('carrots in west cell =====>', garden[row][col])
        
        #if max did not move  from center
        if (row,col) == center:
            at_Rest= True

        else:
            # move lev into max location and set as new center
            row,col= new_cell
            center = new_cell
            carrots += garden[row][col]
            print('carrots======>',carrots)

    return carrots



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
