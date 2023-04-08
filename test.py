# 2-D List
matrix = [{13}, {13, 15}, {14}, {16, 14}, {19, 15}, {16, 20}, {17}, {17, 18}, {18, 21}, {19}, {20}, {21}]
  
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]

print(flatten_matrix)