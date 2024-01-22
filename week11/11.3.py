def is_lower_triangular(matrix):
    for i in range(0, len(matrix)):
	    for j in range(i + 1, len(matrix)):
		    if(matrix[i][j] != 0):
			    		return False
   			#return True
 
is_lower_triangular([[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
)