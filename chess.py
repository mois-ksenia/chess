figures = {
    'lw':'♖', 'kw':'♘', 'sw':'♗', 'Kw':'♔', 'Qw':'♕', 'pw':'♙',
    'lb':'♜', 'kb':'♞', 'sb':'♝', 'Kb':'♚', 'Qb':'♛', 'pb':'♟'
}

def getFigure(fig):
    if (len(fig) != 0):
        return figures.get(fig[0] + fig[2])
    return ''

board = [
    ['l1w', 'k1w', 's1w', 'K1w'  , 'Q1w'   , 's2w' , 'k2w', 'l2w'],
    ['p1w', 'p2w', 'p3w', 'p4w'  , 'p5w'   , 'p6w' , 'p7w', 'p8w'],
    [''   , ''   , ''   , ''     , ''      , ''    , ''   , ''   ],
    [''   , ''   , ''   , ''     , ''      , ''    , ''   , ''   ],
    [''   , ''   , ''   , ''     , ''      , ''    , ''   , ''   ],
    [''   , ''   , ''   , ''     , ''      , ''    , ''   , ''   ],
    ['p1b', 'p2b', 'p3b', 'p4b'  , 'p5b'   , 'p6b' , 'p7b', 'p8b'],
    ['l1b', 'k1b', 's1b', 'K1b'  , 'Q1b'   , 's2b' , 'k2b', 'l2b']
    ]

i = 0
while i < 8:
    a = getFigure(board[i][0]) + ' ' + getFigure(board[i][1]) + ' ' + getFigure(board[i][2]) + ' ' + getFigure(board[i][3]) + ' ' + getFigure(board[i][4]) + ' ' + getFigure(board[i][5]) + ' ' + getFigure(board[i][6]) + ' ' + getFigure(board[i][7])
    print(a)
    i = i + 1