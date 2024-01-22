def transpose(table):
    """Returns: copy of table with rows and columns swapped
    Precondition: table is a (non-ragged) 2d List"""
    n_rows = len(table)
    n_cols = len(table[0]) # All rows have same no. cols
    new_table = [] # Result accumulator
    for c in range(n_cols):
        row = [] # Single row accumulator
        for r in range(n_rows):
            row.append(table[r][c]) # Build up new row
        new_table.append(row) # Add new row to new table
    return new_table
d = [[1,2], [3, 4], [5, 6]]
d_v2 = transpose(d)
print(d_v2)