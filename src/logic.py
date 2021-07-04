import random

# create the matrix

def start(mat):
	for i in range(4):
		mat.append([0]*4)

	return mat

def spawn(mat):
	stat = 0
	r = random.randint(0,3)
	c = random.randint(0,3)

	while mat[r][c] != 0:
		r = random.randint(0,3)
		c = random.randint(0,3)
		for i in range(4):
			for j in range(4):
				if mat[i][j] == 0:
					stat += 1
		if stat == 0:
			print('You lost')
			quit()

	mat[r][c] = random.choice([2,4])

	return mat

# matrix manipulations

def trans(mat):
	n_mat = []
	for i in range(4):
		n_mat.append([]*4)

	for i in range(4):
		for j in range(4):
			n_mat[i].append(mat[j][i])

	return n_mat

def rev(mat):
	n_mat = []
	for i in range(4):
		n_mat.append([]*4)

	for i in range(4):
		for j in range(4):
			n_mat[i].append(mat[i][-(j+1)])

	return n_mat

def arr(mat):
	n_mat = []
	for i in range(4):
		n_mat.append([]*4)

	for i in range(4):
		for j in range(4):
			if mat[i][j] != 0:
				n_mat[i].append(mat[i][j])

	for i in range(4):
		if len(n_mat[i]) != 4:
			req = int(4-len(n_mat[i]))
			for k in range(req):
				n_mat[i].append(0)

	return n_mat

def merge(mat):
	for i in range(4):
		for j in range(3):
			if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
				mat[i][j] *= 2
				mat[i][j+1] = 0

	return mat


# movements

def up(mat):
	mat = trans(mat)
	mat = arr(mat)
	mat = merge(mat)
	mat = arr(mat)
	mat = trans(mat)
	
	return mat

def down(mat):
	mat = trans(mat)
	mat = rev(mat)
	mat = arr(mat)
	mat = merge(mat)
	mat = arr(mat)
	mat = rev(mat)
	mat = trans(mat)
	
	return mat

def left(mat):
	mat = arr(mat)
	mat = merge(mat)
	mat = arr(mat)

	return mat

def right(mat):
	mat = rev(mat)
	mat = arr(mat)
	mat = merge(mat)
	mat = arr(mat)
	mat = rev(mat)
	
	return mat
