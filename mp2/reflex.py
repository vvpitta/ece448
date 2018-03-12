from blocks import *
from board import *
from boardClass import *
import string

global current
global opponent

def three_unbroken(best_block, boardCells):
    idx = 0
    for blocks in best_block:
        if blocks[0] >= 3:
            for block in blocks[1]:
                block_1 = [boardCells[block[0]].char, boardCells[block[1]].char, boardCells[block[2]].char]
                block_2 = [boardCells[block[1]].char, boardCells[block[2]].char, boardCells[block[3]].char]
                block_3 = [boardCells[block[2]].char, boardCells[block[3]].char, boardCells[block[4]].char]
                if '.' not in block_1:
                    return True, block, idx
                if '.' not in block_2:
                    return True, block, idx
                if '.' not in block_3:
                    return True, block, idx
                idx += 1
    return False, None, 0

def four_unbroken(best_block, boardCells):
    if best_block[0][0] == 4:
        for block in best_block[0][1]:
            block_1 = [boardCells[block[0]].char, boardCells[block[1]].char, boardCells[block[2]].char, boardCells[block[3]].char]
            block_2 = [boardCells[block[1]].char, boardCells[block[2]].char, boardCells[block[3]].char, boardCells[block[4]].char]
            if '.' not in block_1:
                return True, block
            if '.' not in block_2:
                return True, block
        return False, None
    else:
        return False, None

def reflex(boardCells, board, player, p1_moves, p2_moves, p1_idx, p2_idx, current, opponent):
    best_count_red, winning_blocks_red = winning_blocks(boardCells, 'red')
    best_count_blue, winning_blocks_blue = winning_blocks(boardCells, 'blue')

    if player == 'red':
        four_red, block_red = four_unbroken(best_count_red, boardCells)
        four_blue, block_blue = four_unbroken(best_count_blue, boardCells)
        three_blue, block_3_blue, idx = three_unbroken(best_count_blue, boardCells)
        if p1_idx == 0 and p2_idx == 0:
            boardCells[(3,3)].set_char(p1_moves[p1_idx])
            board[boardCells[(3,3)].idx] = boardCells[(3,3)].char
            board_string = ''.join(board)
            print board_string
            if current == 'reflex' and opponent == 'reflex':
                return reflex(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='reflex', opponent ='reflex')
            elif current == 'reflex' and opponent == 'minimax':
                return minimax_setup(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='minimax', opponent = 'reflex')
            for coord in block_red:
                if boardCells[coord].char == '.':
                    boardCells[coord].set_char(p1_moves[p1_idx])
                board[boardCells[coord].idx] = boardCells[coord].char
                board_string = ''.join(board)
                print board_string
                return boardCells
        elif four_blue == True:
            for coord in block_blue:
                if boardCells[coord].char == '.':
                    boardCells[coord].set_char(p1_moves[p1_idx])
            board[boardCells[coord].idx] = boardCells[coord].char
            board_string = ''.join(board)
            print board_string
            if opponent == 'reflex' and current == 'reflex':
                return reflex(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='reflex', opponent ='reflex')
            elif current == 'reflex' and opponent == 'minimax':
                return minimax_setup(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current = 'minimax', opponent = 'reflex')

        elif three_blue == True:
            if boardCells[block_3_blue[0]].char != '.' and boardCells[block_3_blue[1]].char != '.' and boardCells[block_3_blue[2]].char != '.':
                boardCells[block_3_blue[3]].set_char(p1_moves[p1_idx])
                board[boardCells[block_3_blue[3]].idx] = boardCells[block_3_blue[3]].char
            elif boardCells[block_3_blue[1]].char != '.' and boardCells[block_3_blue[2]].char != '.' and boardCells[block_3_blue[3]].char != '.':
                if boardCells[block_3_blue[0]].char == '.':
                    boardCells[block_3_blue[0]].set_char(p1_moves[p1_idx])
                    board[boardCells[block_3_blue[0]].idx] = boardCells[block_3_blue[0]].char
                else:
                    boardCells[block_3_blue[4]].set_char(p1_moves[p1_idx])
                    board[boardCells[block_3_blue[4]].idx] = boardCells[block_3_blue[4]].char
            else:
                boardCells[block_3_blue[1]].set_char(p1_moves[p1_idx])
                board[boardCells[block_3_blue[1]].idx] = boardCells[block_3_blue[1]].char
            board_string = ''.join(board)
            print board_string
            if opponent == 'reflex' and current == 'reflex':
                return reflex(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current = 'reflex', opponent = 'reflex')
            elif current == 'reflex' and opponent == 'minimax':
                return minimax_setup(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current = 'minimax', opponent ='reflex')
        else:
            if best_count_red[0][1] != [] or best_count_red[1][1] != [] or best_count_red[2][1] != [] or best_count_red[3][1] != []:
                for blocks in best_count_red:
                    if blocks[1] != []:
                        block = blocks[1][0]
                        zero_block = ['.', '.', '.', '.', '.']
                        curr_block = [boardCells[block[0]].char, boardCells[block[1]].char, boardCells[block[2]].char, boardCells[block[3]].char, boardCells[block[4]].char]
                        if zero_block == curr_block:
                            boardCells[block[0]].set_char(p1_moves[p1_idx])
                            board[boardCells[block[0]].idx] = boardCells[block[0]].char
                            board_string = ''.join(board)
                            print board_string
                            if opponent == 'reflex' and current == 'reflex':
                                return reflex(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='reflex', opponent ='reflex')
                            elif current == 'reflex' and opponent == 'minimax':
                                return minimax_setup(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='minimax', opponent ='reflex')

                        else:
                            for i in range(len(block)):
                                if (boardCells[block[i]].char == '.' and boardCells[block[i+1]].char != '.' and i != 4) or (boardCells[block[i]].char == '.' and boardCells[block[i-1]].char != '.' and i != 0):
                                    boardCells[block[i]].set_char(p1_moves[p1_idx])
                                    board[boardCells[block[i]].idx] = boardCells[block[i]].char
                                    board_string = ''.join(board)
                                    print board_string
                                    if opponent == 'reflex' and current == 'reflex':
                                        return reflex(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='reflex', opponent= 'reflex')
                                    elif current == 'reflex' and opponent == 'minimax':
                                        return minimax_setup(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current= 'minimax', opponent ='reflex')
            else:
                for y in range (7):
                    for x in range(7):
                        if boardCells[(x,y)].char == '.':
                            boardCells[(x,y)].set_char(p1_moves[p1_idx])
                            board[boardCells[(x,y)].idx] = boardCells[(x,y)].char
                            board_string = ''.join(board)
                            print board_string
                            if opponent == 'reflex' and current == 'reflex':
                                return reflex(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx + 1), p2_idx, current ='reflex', opponent ='reflex')
                            elif current == 'reflex' and opponent == 'minimax':
                                return minimax_setup(boardCells, board, 'blue', p1_moves, p2_moves, (p1_idx+1), p2_idx, current ='minimax', opponent ='reflex')
                return boardCells
    else:
        four_red, block_red = four_unbroken(best_count_red, boardCells)
        four_blue, block_blue = four_unbroken(best_count_blue, boardCells)
        three_red, block_3_red, idx = three_unbroken(best_count_red, boardCells)
        if p1_idx == 0 and p2_idx == 0:
            boardCells[(3,3)].set_char(p2_moves[p2_idx])
            board[boardCells[(3,3)].idx] = boardCells[(3,3)].char
            board_string = ''.join(board)
            print board_string
            if current == 'reflex' and opponent == 'reflex':
                return reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='reflex', opponent ='reflex')
            elif current == 'reflex' and opponent == 'minimax':
                return minimax_setup(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='minimax', opponent ='reflex')

        elif four_blue == True:
            for coord in block_blue:
                if boardCells[coord].char == '.':
                    boardCells[coord].set_char(p2_moves[p2_idx])
                board[boardCells[coord].idx] = boardCells[coord].char
                board_string = ''.join(board)
                print board_string
                return boardCells
        elif four_red == True:
            for coord in block_red:
                if boardCells[coord].char == '.':
                    boardCells[coord].set_char(p2_moves[p2_idx])
            board[boardCells[coord].idx] = boardCells[coord].char
            board_string = ''.join(board)
            print board_string
            if current == 'reflex' and opponent == 'reflex':
                return reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='reflex', opponent ='reflex')
            elif current == 'reflex' and opponent == 'minimax':
                return minimax_setup(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='minimax', opponent='reflex')
        elif three_red == True:
            if boardCells[block_3_red[0]].char != '.' and boardCells[block_3_red[1]].char != '.' and boardCells[block_3_red[2]].char != '.':
                boardCells[block_3_red[3]].set_char(p2_moves[p2_idx])
                board[boardCells[block_3_red[3]].idx] = boardCells[block_3_red[3]].char
            elif boardCells[block_3_red[1]].char != '.' and boardCells[block_3_red[2]].char != '.' and boardCells[block_3_red[3]].char != '.':
                if boardCells[block_3_red[0]].char == '.':
                    boardCells[block_3_red[0]].set_char(p2_moves[p2_idx])
                    board[boardCells[block_3_red[0]].idx] = boardCells[block_3_red[0]].char
                else:
                    boardCells[block_3_red[4]].set_char(p2_moves[p2_idx])
                    board[boardCells[block_3_red[4]].idx] = boardCells[block_3_red[4]].char
            else:
                boardCells[block_3_red[1]].set_char(p2_moves[p2_idx])
                board[boardCells[block_3_red[1]].idx] = boardCells[block_3_red[1]].char
            board_string = ''.join(board)
            print board_string
            if current == 'reflex' and opponent == 'reflex':
                return reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx + 1), current ='reflex', opponent ='reflex')
            elif current == 'reflex' and opponent == 'minimax':
                return minimax_setup(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current = 'minimax', opponent ='reflex')
        else:
            if best_count_blue[0][1] != [] or best_count_blue[1][1] != [] or best_count_blue[2][1] != [] or best_count_blue[3][1] != []:
                for blocks in best_count_blue:
                    if blocks[1] != []:
                        block = blocks[1][0]
                        zero_block = ['.', '.', '.', '.', '.']
                        curr_block = [boardCells[block[0]].char, boardCells[block[1]].char, boardCells[block[2]].char, boardCells[block[3]].char, boardCells[block[4]].char]
                        if zero_block == curr_block:
                            boardCells[block[0]].set_char(p2_moves[p2_idx])
                            board[boardCells[block[0]].idx] = boardCells[block[0]].char
                            board_string = ''.join(board)
                            print board_string
                            if current == 'reflex' and opponent == 'reflex':
                                return reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx + 1), current ='reflex', opponent ='reflex')
                            elif current == 'reflex' and opponent == 'minimax':
                                return minimax_setup(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='minimax', opponent ='reflex')
                        else:
                            for i in range(len(block)):
                                if (boardCells[block[i]].char == '.' and boardCells[block[i+1]].char != '.' and i != 4) or (boardCells[block[i]].char == '.' and boardCells[block[i-1]].char != '.' and i != 0):
                                    boardCells[block[i]].set_char(p2_moves[p2_idx])
                                    board[boardCells[block[i]].idx] = boardCells[block[i]].char
                                    board_string = ''.join(board)
                                    print board_string
                                    if current == 'reflex' and opponent == 'reflex':
                                        return reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx + 1), current ='reflex', opponent ='reflex')
                                    elif current == 'reflex' and opponent == 'minimax':
                                        return minimax_setup(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='minimax', opponent ='reflex')
            else:
                for y in range (7):
                    for x in range(7):
                        if boardCells[(x,y)].char == '.':
                            boardCells[(x,y)].set_char(p2_moves[p2_idx])
                            board[boardCells[(x,y)].idx] = boardCells[(x,y)].char
                            board_string = ''.join(board)
                            print board_string
                            if current == 'reflex' and opponent == 'reflex':
                                return reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='reflex', opponent ='reflex')
                            elif current == 'reflex' and opponent == 'minimax':
                                return minimax_setup(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, (p2_idx+1), current ='minimax', opponent ='reflex')
                return boardCells

p1_moves = list(string.ascii_lowercase)
p2_moves = list(string.ascii_uppercase)
p1_idx = 1
p2_idx = 1

board, boardCells = initBoard()

boardCells[(1,1)].set_char(p1_moves[0])
boardCells[(5,5)].set_char(p2_moves[0])

for x in range(7):
    for y in range(7):
        board[boardCells[(x,y)].idx] = boardCells[(x,y)].char
        board[boardCells[(x,y)].idx] = boardCells[(x,y)].char

board_string = ''.join(board)
print board_string

boardCells = reflex(boardCells, board, 'red', p1_moves, p2_moves, p1_idx, p2_idx, 'reflex', 'reflex')

for x in range(7):
    for y in range(7):
        board[boardCells[(x,y)].idx] = boardCells[(x,y)].char
        board[boardCells[(x,y)].idx] = boardCells[(x,y)].char

board_string = ''.join(board)
print board_string
file = open('r_agent.txt', 'w')
file.write(board_string)
