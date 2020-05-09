# Tic Tac Toe
import random

def drawBoard(board):
    # 这个函数打印棋盘
    
    # "board"是10个字符串组成的列表（不包括0）
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def inputPlayerLetter():
    # 用户选择‘X'或’O'
    # 返回
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('你想选择 X 或 O?')
        letter = input().upper()
    
    # 列表中第一个字符是玩家字符，第二个是电脑字符
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']
    
def whoGoesFirst():
    # 随机决定谁走第一步
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
def playAgain():
    # 这个函数如果玩家选择重玩返回True，否则返回False
    print('想再玩一局吗?(yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    # 给函数提供游戏板和玩家字符，如果玩家赢则返回True
    # 我们用bo代替board，用le代替letter，这样就不需要输入那么多字母了
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or # 第一行
           (bo[4]==le and bo[5]==le and bo[6]==le) or # 中间一行
           (bo[1]==le and bo[2]==le and bo[3]==le) or # 底部一行
           (bo[7]==le and bo[4]==le and bo[1]==le) or # 左边一列
           (bo[8]==le and bo[5]==le and bo[2]==le) or # 中间一列
           (bo[9]==le and bo[6]==le and bo[3]==le) or # 右边一行
           (bo[7]==le and bo[5]==le and bo[3]==le) or # 斜线
           (bo[9]==le and bo[5]==le and bo[1]==le)) # 斜线

def getBoardCopy(board):
    # 复制游戏画板并返回这个复制的画板
    dupeBoard = []
    
    for i in board:
        dupeBoard.append(i)
        
    return dupeBoard

def isSpaceFree(board, move):
    # 如果下一步下棋的位置为空，则返回True
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while (move not in '1 2 3 4 5 6 7 8 9'.split()) or (not isSpaceFree(board, int(move))):
        print('你下一步棋放在哪个位置?(1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # 从传入的棋盘中返回一个有效的步骤
    # 如果没有有效走法则返回空
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
        
def getComputerMove(board, computerLetter):
    # 传入棋盘和电脑玩家的字符，决定电脑的下一步走法并返回。
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    # 下面是这个游戏中的人工智能算法：
    
    # 首先，检查下一步电脑是否能赢
    for i in range(1, 10):
        copy = getBoardCopy(board) # 复制棋盘
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i # 如果下一步棋能赢，返回这个位置
            
    # 检查玩家下一步会不会赢，如果会，阻止他
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i # 电脑下在玩家能赢的位置，阻止玩家获胜
            
    # 试着下到角落位置，如果那个位置空闲的话
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move
    
    # 试着下到中间位置，如果那个位置空闲的话
    if isSpaceFree(board, 5):
        return 5
    
    # 下到边上的某个位置
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    # 如果棋盘下满了，然会True，否则返回False
    for i in range(1, 10):
        if isSpaceFree(board,i):
            return False
    return True

# 主程序
print('欢迎参加井字棋游戏!')

while True:
    # 复位棋盘
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' 先走.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            # 轮到玩家
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('哇! 你赢了计算机!')
                gameIsPlaying = False
            else:
                turn = 'computer'
        else:
            # 轮到计算机
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('游戏陷入僵局了')
                break
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('计算机打败了你! 你输了.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('游戏陷入僵局了')
                    break
                else:
                    turn = 'player'
                    
    if not playAgain():
        print('Bye~')
        break
