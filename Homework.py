#New file has been opened master.


 # \ is used for multiline code
board=[' ',' ',' '],   \
		[' ',' ',' '],  \
		[' ',' ',' ']

player = "O"


def p_board(board,player):


	if player=="X":
		player = "O"
		print("P2s turn")
	else:
		player = "X"
		print("P1s turn")


	print( board[0][0] + '|' + board[0][1] + '|' + board[0][2] )
	print('-+-+-')
	print( board[1][0] + '|' + board[1][1] + '|' + board[1][2] )
	print('-+-+-')
	print( board[2][0] + '|' + board[2][1] + '|' + board[2][2] )


	p_input=input("Enter position on your numpad 1-9: ")
	if p_input == "1":
		if board[2][0] != "X" and board[2][0] != "O":
			board[2][0] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "2":

		if board[2][1] != "X" and board[2][1] != "O":
			board[2][1] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "3":
		if board[2][2] != "X" and board[2][2] != "O":
			board[2][2] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "4":

		if board[1][0] != "X" and board[1][0] != "O":
			board[1][0] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "5":

		if board[1][1] != "X" and board[1][1] != "O":
			board[1][1] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "6":

		if board[1][2] != "X" and board[1][2] != "O":
			board[1][2] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "7":

		if board[0][0] != "X" and board[0][0] != "O":
			board[0][0] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "8":

		if board[0][1] != "X" and board[0][1] != "O":
			board[0][1] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)

	elif p_input == "9":

		if board[0][2] != "X" and board[0][2] != "O":
			board[0][2] = player
			return p_board(board,player)
		else:
			print("Already occupied")
			return p_board(board,player)






p_board(board,player)