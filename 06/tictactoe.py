def TicTacDraw(board):
    n=len(board)
    for x in range(n):
        row=' '
        for y in range(n):
            if board[x][y]==0:
                row+='O | '
            elif board[x][y]==1:
                row+='X | '
            elif board[x][y]==2:
                row+='  | '
            else:
                print('Error occurs: Invalid input!')
                exit()
        print(row[:-2])
        if x<n-1:
            print((4*n-1)*'-')

if __name__=='__main__':
    test_1=[[0,1,2],[2,0,0],[1,1,2]]
    TicTacDraw(test_1)
