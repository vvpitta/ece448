'''
Code for reflex agent
red = lowercase
blue = uppercase
'''

from board import *
from boardClass import *
import string

p1_moves = list(string.ascii_lowercase)
p2_moves = list(string.ascii_uppercase)

def winning_blocks_lr(boardCells, player):
    winning_blocks = []
    best_count = 0
    best_block = []

    if player == 'red':
        for y in range(7):
            for x in range(3):
                block = []
                count = 0
                invalid = False
                for i in range(x, x+5):
                    if boardCells[(i,y)].char in p2_moves:
                        invalid = True
                        break
                    elif boardCells[(i,y)].char != '.':
                        count += 1
                        block.append((i,y))
                    else:
                        block.append((i,y))
                if invalid == True:
                    continue
                elif count == best_count:
                    best_count = count
                    best_block.append(block)
                    winning_blocks.append(block)
                elif count > best_count:
                    best_count = count
                    best_block = []
                    best_block.append(block)
                    winning_blocks.append(block)
                else:
                    winning_blocks.append(block)
    elif player == 'blue':
        for y in range(7):
            for x in range(3):
                block = []
                count = 0
                invalid = False
                for i in range(x, x+5):
                    if boardCells[(i,y)].char in p1_moves:
                        invalid = True
                        break
                    elif boardCells[(i,y)].char != '.':
                        count += 1
                        block.append((i,y))
                    else:
                        block.append((i,y))
                if invalid == True:
                    continue
                elif count == best_count:
                    best_count = count
                    best_block.append(block)
                    winning_blocks.append(block)
                elif count > best_count:
                    best_count = count
                    best_block = []
                    best_block.append(block)
                    winning_blocks.append(block)
                else:
                    winning_blocks.append(block)

    return best_count, best_block, winning_blocks

def winning_blocks_ud(boardCells, player):
    winning_blocks = []
    best_count = 0
    best_block = []


    if player == 'red':
        for x in range(7):
            for y in range(3):
                block = []
                count = 0
                invalid = False
                for i in range(y, y+5):
                    if boardCells[(x,i)].char in p2_moves:
                        invalid = True
                        break
                    elif boardCells[(x,i)].char != '.':
                        count += 1
                        block.append((x,i))
                    else:
                        block.append((x,i))
                if invalid == True:
                    continue
                elif count == best_count:
                    best_count = count
                    best_block.append(block)
                    winning_blocks.append(block)
                elif count > best_count:
                    best_count = count
                    best_block = []
                    best_block.append(block)
                    winning_blocks.append(block)
                else:
                    winning_blocks.append(block)
    elif player == 'blue':
        for x in range(7):
            for y in range(3):
                block = []
                count = 0
                invalid = False
                for i in range(y, y+5):
                    if boardCells[(x,i)].char in p1_moves:
                        invalid = True
                        break
                    elif boardCells[(x,i)].char != '.':
                        count += 1
                        block.append((x,i))
                    else:
                        block.append((x,i))
                if invalid == True:
                    continue
                elif count == best_count:
                    best_count = count
                    best_block.append(block)
                    winning_blocks.append(block)
                elif count > best_count:
                    best_count = count
                    best_block = []
                    best_block.append(block)
                    winning_blocks.append(block)
                else:
                    winning_blocks.append(block)

    return best_count, best_block, winning_blocks

def winning_blocks_diagr(boardCells, player):
    winning_blocks = []
    best_count = 0
    best_block = []

    if player == 'red':
        for y in range(3):
            block = []
            count = 0
            invalid = False
            for i in range(y, y+5):
                if boardCells[(i,i)].char in p2_moves:
                    invalid = True
                    break
                elif boardCells[(i,i)].char != '.':
                    count += 1
                    block.append((i,i))
                else:
                    block.append((i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        for y in range(1,3):
            block = []
            count = 0
            invalid = False
            for i in range(y, y+5):
                if boardCells[(i-1,i)].char in p2_moves:
                    invalid = True
                    break
                elif boardCells[(i-1,i)].char != '.':
                    count += 1
                    block.append((i-1,i))
                else:
                    block.append((i-1,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        y = 2
        block = []
        count = 0
        invalid = False
        for i in range(y, y+5):
            if boardCells[(i-2,i)].char in p2_moves:
                invalid = True
                break
            elif boardCells[(i-2,i)].char != '.':
                count += 1
                block.append((i-2,i))
            else:
                block.append((i-2,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)

        for y in range(2):
            block = []
            count = 0
            invalid = False
            for i in range(y, y+5):
                if boardCells[(i+1,i)].char in p2_moves:
                    invalid = True
                    break
                elif boardCells[(i+1,i)].char != '.':
                    count += 1
                    block.append((i+1,i))
                else:
                    block.append((i+1,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        y = 0
        block = []
        count = 0
        invalid = False
        for i in range(y, y+5):
            if boardCells[(i+2,i)].char in p2_moves:
                invalid = True
                break
            elif boardCells[(i+2,i)].char != '.':
                count += 1
                block.append((i+2,i))
            else:
                block.append((i+2,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)


    elif player == 'blue':
        for y in range(3):
            block = []
            count = 0
            invalid = False
            for i in range(y, y+5):
                if boardCells[(i,i)].char in p1_moves:
                    invalid = True
                    break
                elif boardCells[(i,i)].char != '.':
                    count += 1
                    block.append((i,i))
                else:
                    block.append((i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        for y in range(1,3):
            block = []
            count = 0
            invalid = False
            for i in range(y, y+5):
                if boardCells[(i-1,i)].char in p1_moves:
                    invalid = True
                    break
                elif boardCells[(i-1,i)].char != '.':
                    count += 1
                    block.append((i-1,i))
                else:
                    block.append((i-1,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        y = 2
        block = []
        count = 0
        invalid = False
        for i in range(y, y+5):
            if boardCells[(i-2,i)].char in p1_moves:
                invalid = True
                break
            elif boardCells[(i-2,i)].char != '.':
                count += 1
                block.append((i-2,i))
            else:
                block.append((i-2,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)

        for y in range(2):
            block = []
            count = 0
            invalid = False
            for i in range(y, y+5):
                if boardCells[(i+1,i)].char in p1_moves:
                    invalid = True
                    break
                elif boardCells[(i+1,i)].char != '.':
                    count += 1
                    block.append((i+1,i))
                else:
                    block.append((i+1,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        y = 0
        block = []
        count = 0
        invalid = False
        for i in range(y, y+5):
            if boardCells[(i+2,i)].char in p1_moves:
                invalid = True
                break
            elif boardCells[(i+2,i)].char != '.':
                count += 1
                block.append((i+2,i))
            else:
                block.append((i+2,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)

    return best_count, best_block, winning_blocks

def winning_blocks_diagl(boardCells, player):
    winning_blocks = []
    best_count = 0
    best_block = []

    if player == 'red':
        y = 4
        block = []
        count = 0
        invalid = False
        for i in range(y-4, y+1):
            if boardCells[(4-i,i)].char == (boardCells[(4-i,i)].char.upper()):
                invalid = True
                break
            elif boardCells[(4-i,i)].char != '.':
                count += 1
                block.append((4-i,i))
            else:
                block.append((4-i,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)

        for y in range(4,6):
            block = []
            count = 0
            invalid = False
            for i in range(y-4, y+1):
                if boardCells[(5-i,i)].char == (boardCells[(5-i,i)].char.upper()):
                    invalid = True
                    break
                elif boardCells[(5-i,i)].char != '.':
                    count += 1
                    block.append((5-i,i))
                else:
                    block.append((5-i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        for y in range(4,7):
            block = []
            count = 0
            invalid = False
            for i in range(y-4, y+1):
                if boardCells[(6-i,i)].char == (boardCells[(6-i,i)].char.upper()):
                    invalid = True
                    break
                elif boardCells[(6-i,i)].char != '.':
                    count += 1
                    block.append((6-i,i))
                else:
                    block.append((6-i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        for y in range(5,7):
            block = []
            count = 0
            invalid = False
            for i in range(y-4, y+1):
                if boardCells[(7-i,i)].char == (boardCells[(7-i,i)].char.upper()):
                    invalid = True
                    break
                elif boardCells[(7-i,i)].char != '.':
                    count += 1
                    block.append((7-i,i))
                else:
                    block.append((7-i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        y = 6
        block = []
        count = 0
        invalid = False
        for i in range(y-4, y+1):
            if boardCells[(8-i,i)].char == (boardCells[(8-i,i)].char.upper()):
                invalid = True
                break
            elif boardCells[(8-i,i)].char != '.':
                count += 1
                block.append((8-i,i))
            else:
                block.append((8-i,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)

    elif player == 'blue':
        y = 4
        block = []
        count = 0
        invalid = False
        for i in range(y-4, y+1):
            if boardCells[(4-i,i)].char != (boardCells[(4-i,i)].char.upper()):
                invalid = True
                break
            elif boardCells[(4-i,i)].char != '.':
                count += 1
                block.append((4-i,i))
            else:
                block.append((4-i,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)

        for y in range(4,6):
            block = []
            count = 0
            invalid = False
            for i in range(y-4, y+1):
                if boardCells[(5-i,i)].char != (boardCells[(5-i,i)].char.upper()):
                    invalid = True
                    break
                elif boardCells[(5-i,i)].char != '.':
                    count += 1
                    block.append((5-i,i))
                else:
                    block.append((5-i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        for y in range(4,7):
            block = []
            count = 0
            invalid = False
            for i in range(y-4, y+1):
                if boardCells[(6-i,i)].char != (boardCells[(6-i,i)].char.upper()):
                    invalid = True
                    break
                elif boardCells[(6-i,i)].char != '.':
                    count += 1
                    block.append((6-i,i))
                else:
                    block.append((6-i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        for y in range(5,7):
            block = []
            count = 0
            invalid = False
            for i in range(y-4, y+1):
                if boardCells[(7-i,i)].char != (boardCells[(7-i,i)].char.upper()):
                    invalid = True
                    break
                elif boardCells[(7-i,i)].char != '.':
                    count += 1
                    block.append((7-i,i))
                else:
                    block.append((7-i,i))
            if invalid == True:
                invalid = False
            elif count == best_count:
                best_count = count
                best_block.append(block)
                winning_blocks.append(block)
            elif count > best_count:
                best_count = count
                best_block = []
                best_block.append(block)
                winning_blocks.append(block)
            else:
                winning_blocks.append(block)

        y = 6
        block = []
        count = 0
        invalid = False
        for i in range(y-4, y+1):
            if boardCells[(8-i,i)].char != (boardCells[(8-i,i)].char.upper()):
                invalid = True
                break
            elif boardCells[(8-i,i)].char != '.':
                count += 1
                block.append((8-i,i))
            else:
                block.append((8-i,i))
        if invalid == True:
            invalid = False
        elif count == best_count:
            best_count = count
            best_block.append(block)
            winning_blocks.append(block)
        elif count > best_count:
            best_count = count
            best_block = []
            best_block.append(block)
            winning_blocks.append(block)
        else:
            winning_blocks.append(block)


    return best_count, best_block, winning_blocks



def winning_blocks(boardCells, player):
    best_count_lr, best_block_lr, winning_blocks_lr1 = winning_blocks_lr(boardCells, player)
    best_count_ud, best_block_ud, winning_blocks_ud1 = winning_blocks_ud(boardCells, player)
    best_count_dr, best_block_dr, winning_blocks_dr = winning_blocks_diagr(boardCells, player)
    best_count_dl, best_block_dl, winning_blocks_dl = winning_blocks_diagl(boardCells, player)

    winning_blocks_total = winning_blocks_dl + winning_blocks_dr + winning_blocks_lr1 + winning_blocks_ud1

    count_block = [(best_count_lr, best_block_lr), (best_count_ud, best_block_ud), (best_count_dr, best_block_dr), (best_count_dl, best_block_dl)]
    fin_block = sorted(count_block, key = lambda x: x[0], reverse = True)

    return fin_block, winning_blocks_total
