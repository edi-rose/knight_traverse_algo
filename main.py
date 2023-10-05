import random
import numpy as np

# 8x8 board filled with 0's
board = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
]

# each position on the board is represented as a tuple (row, column)
# the top left corner is (0,0) and the bottom right corner is (7,7)
# we can access the value of a position on the board by using board[row][column]

# a function which takes the board and finds a next move for the knight
# the function should return a tuple (row, column) of the next move
# for now it is good enough if the move is random
# we will improve this function later
# the knight can move first in any direction by 2 and then in any direction by 1
# so if we say up is 0, right is 1, down is 2 and left is 3

def find_latest_move(board):
    highest_move = 0
    move_position = (0,0)
    for row in range(8):
        for column in range(8):
            if board[row][column] > highest_move:
                highest_move = board[row][column]
                move_position = (row, column)
    return move_position


def find_legal_moves(board):
    legal_moves = []
    latest_move = find_latest_move(board) 
    #knight moves are directional x,y +2,-2,+1,-1 and +1,-1,+2,-2 
    knight_moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for possible_move in knight_moves:
        if check_move_legal(board, (latest_move[0]+possible_move[0], latest_move[1]+possible_move[1])):
            legal_moves.append((latest_move[0]+possible_move[0], latest_move[1]+possible_move[1]))
    return legal_moves

# a function which takes the board and a move and checks if the move is legal
# a move is legal if the knight is not moving off the board
# and if the knight is not moving to a position it has already visited
def check_move_legal(board, move):
    if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
        return False
    if board[move[0]][move[1]] != 0:
        return False
    return True

def reset_board():
    for row in range(8):
        for column in range(8):
            board[row][column] = 0

def main():
    move_count = 0
    starting_postion = (0,0)
    board[starting_postion[0]][starting_postion[1]] = 1
    move_count =1
    while move_count < 64:
        legal_moves = find_legal_moves(board)

        if len(legal_moves) == 0:
            if starting_postion[1] < 7:
                starting_postion = (starting_postion[0], starting_postion[1] + 1)
            elif starting_postion[0] < 7:
                starting_postion = (starting_postion[0] + 1, starting_postion[1])
            else:
                starting_postion = (0,0)
            reset_board()
            print(move_count)
            board[starting_postion[0]][starting_postion[1]] = 1
            move_count = 1
            continue
        # now we just choose a random legal move and make it, this should be improved later
        move = random.choice(legal_moves)
        board[move[0]][move[1]] = move_count + 1
        move_count += 1
        if move_count > 58:
            printboard()
    print("SUCCESS")
    printboard()

def printboard():
    for row in range(8):
        for column in range(8):
            print(board[row][column], end=" ")
        print()

def fleurys_algorithm(board, legal_moves, move_count):
    for move in legal_moves:
        new_board = board
        new_board[move[0]][move[1]] = move_count + 1
        if is_connected(new_board):
            print('its connected')
            return move
    return random.choice(legal_moves)

def is_connected(board):
    free_nodes = []
    for row in range(8):
        for column in range(8):
            if board[row][column] == 0:
                free_nodes.append((row, column))
    start = free_nodes[0]
    stack = [start]
    visted = [start]
    fake_board = board
    #now see if we can get to each of the other nodes from the start node
    while len(stack) > 0:
        current_node = stack[0]
        fake_board[current_node[0]][current_node[1]] = 1
        legal_moves = find_legal_moves(fake_board)
        for move in legal_moves:
            if move not in visted:
                stack.append(move)
                visted.append(move)
        stack.pop(0)
    if len(visted) == len(free_nodes):
        return True
    return False


    

def creates_bridge(board, move, move_count):
    new_board = board
    new_board[move[0]][move[1]] = move_count + 1
    #now we want to check if the board is disconnected
    return is_connected(new_board)

# def get_bridges(board, legal_moves, move_count):
#     bridges = []
#     for move in legal_moves: 
#         new_board = board
#         new_board[move[0]][move[1]] = move_count + 1
#         if len(find_legal_moves(new_board)) == 1:
#             bridges.append(move)
#     return bridges
        
reset_board()
main()