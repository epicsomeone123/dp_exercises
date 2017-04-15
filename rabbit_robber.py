manhattan_grid = []
n_row = 8
n_col = 8

for r in range(n_row):
    row_list = []
    for c in range(n_col):
        row_list.append(None)
    manhattan_grid.append(row_list)

manhattan_grid[1][1] = 'B'
manhattan_grid[3][0] = 'B'
manhattan_grid[3][2] = 'B'
manhattan_grid[1][6] = 'B'
manhattan_grid[4][4] = 'B'
manhattan_grid[5][1] = 'B'
manhattan_grid[5][5] = 'B'
manhattan_grid[6][6] = 'B'

manhattan_grid[2][3] = 'W'
manhattan_grid[4][5] = 'W'
manhattan_grid[4][7] = 'W'
manhattan_grid[5][3] = 'W'
manhattan_grid[7][2] = 'W'




for row in manhattan_grid:
    print row


#for r in range(len(manhattan_grid)):
#   print manhattan_grid(r)


dp_table = []
for r in range(n_row+1):
    dp_row_list = []
    for c in range(n_col+1):
        dp_row_list.append(0)
    dp_table.append(dp_row_list)

for row in dp_table:
    print row


dp_table[0][0] = 0 # initially, rabbit has no money

for row_index in range(n_row+1):
    for col_index in range(n_col+1):
        nw_block = None
        ne_block = None
        sw_block = None
        if row_index-1 >= 0 and row_index < n_row \
            and col_index-1 >= 0 and col_index < n_col:
            nw_block = manhattan_grid[row_index-1][col_index-1]
            ne_block = manhattan_grid[row_index-1][col_index]
            sw_block = manhattan_grid[row_index][col_index-1]
        print nw_block, ne_block, sw_block

money = 0
for row_index in range(n_row+1):
    for col_index in range(n_col+1):
        if nw_block == 'B' or ne_block == 'B' or sw_block == 'B':
            money += 10
        elif nw_block == 'W' or ne_block == 'W' or sw_block == 'W':
            money -= 20

# for i in range(col_index):
#     for j in range(row_index):
#         dp_table[i][j] = f(manhattan_grid[i][j])





