# Function to print board with current position mappings provided through board_dict
def print_board(board_dict):
	
	print('|-----|-----|-----|')

	# Counter variable to be incremented after each row is printed in order to print the initial position values of the row
	i = 0

	# Prints each square with either its default position number or the first letter of the player who took that square
	for index in range(1,4):
		current_square = 1 + 3*i

		print('|  ' + board_dict[current_square] + '  |  ' + board_dict[current_square + 1] + '  |  '+board_dict[current_square + 2] + '  |')
		print('|     |     |     |')
		print('|-----|-----|-----|')
		i += 1
	print('\n')

# Prompts either player with print_board() displayed to choose a position to make a move on
# Selection [1-9], does not allow selecting tiles that have already been taken
# returns a string containing the selected move
def select_move(player, acceptable_moves):
	pos_choice = ''
	
	# after first entry, checks that the user's input is in the list of acceptable moves
	while pos_choice not in acceptable_moves:
		pos_choice = input('{}, where would you like to play? (Type an available position)\n'.format(player))

		if pos_choice not in acceptable_moves:
			print("Sorry, the position you entered either has already been played or does not exist.\n")

	return pos_choice


# Takes current board status and checks to see if a player has won
# game_over() == True when (1) Tic Tac Toe achieved (vertical, horizontal, diagonal) OR (2) All positions marked by either player (tie)
# Returns a boolean indicating status of the game
def game_over(board_dict, p1, p2):
	conditions = [
		(1, 2, 3), (4, 5, 6), (7, 8, 9),
		(1, 4, 7), (2, 5, 8), (3, 6, 9),
		(1, 5, 9), (3, 5, 7)
	]
	
	#GAME TIED, (OVER)
	if tied(board_dict, p1, p2):
		return True
	#GAME WON
	for condition in conditions:
		if board_dict[condition[0]] == board_dict[condition[1]] == board_dict[condition[2]]:
			return True

	return False

# Checks for a tie in game_over() so game doesn't continue after all positions are taken
def tied(board_dict, p1, p2):
	for key, value in board_dict.items():
		if value != p1[0] and value != p2[0]:
			return False
	return True



# Game loop, ends when game_over() is True due to a tie or a player achieving Tic-Tac-Toe
def start_game():
	print("Welcome to Tic Tac Toe!\n")

	p1_name = input("Select a name for player 1: ")
	
	p2_name = input("Select a name for player 2: ")

	print("\nExcellent! Let's begin.\n\n\n")

	# Sets a string to be placed on the board when a user makes a move, uses first letter of name
	p1_marker = p1_name[0]
	p2_marker = p2_name[0]

	# Dictionary stores current state of game, values default to position key
	# List of acceptable moves starts with all positions, index removed after a user selects that position as a move
	board_conditions = {1:'1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
	acceptable_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	current_player = p1_name

	while not game_over(board_conditions, p1_name, p2_name):
		print('{}\'s turn!\n'.format(current_player))
		
		print_board(board_conditions)
		
		move = select_move(current_player, acceptable_moves)

		# Removes the selected move from the list of future possible moves
		acceptable_moves.remove(move)
		
		# Changes board dictionary to reflect move made based on player who performed the move
		# Switches the player
		if current_player == p1_name:
			board_conditions[int(move)] = p1_marker
			current_player = p2_name
		else:
			board_conditions[int(move)] = p2_marker
			current_player = p1_name

	# While loop ends when game_over() is True, presents results based on whether or not a tie occurred
	print("Game over!")
	
	if tied(board_conditions, p1_name, p2_name):
		print("It was a tie!\n")
	else:
		if current_player == p1_name:
			winner = p2_name
		else:
			winner = p1_name
		print("{} won! Here is the final board:\n".format(winner))
	
	# Prints the final board	
	print_board(board_conditions)


start_game()





