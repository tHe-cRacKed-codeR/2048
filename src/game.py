from logic import *

mat = []
# [1,3,0,5],[2,6,0,4],[9,256,0,1],[1024,256,512,6]


def pri(mat):
	for item in mat:
		print(item)

state = True
def status(mat):
	for i in range(4):
		for j in range(4):
			if mat[i][j] == 2048:
				print("\nYOU WON!!\n\\^^/")
				quit()

mat = start(mat)
mat = spawn(mat)

try:
	while True:
		mat = spawn(mat)
		pri(mat)
		status(mat)
		move = str(input("Type Your Move :"))
		if move == 's':
			mat = down(mat)
		if move == 'w':
			mat = up(mat)
		if move == 'a':
			mat = left(mat)
		if move == 'd':
			mat = right(mat)
except:
	print('\nGame was quit !!')