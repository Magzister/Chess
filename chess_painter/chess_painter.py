import chess_painter.unicode_chess_symbols as ucs


def draw_board(board: list) -> None:
    is_white_tile = True
    for row in board:
        board_row = ''
        for figure in row:
            if is_white_tile:
                board_row += ucs.WHITE_TILE.format(
                    data=ucs.CHESS_PIECES[figure]
                )
            else:
                board_row += ucs.BLACK_TILE.format(
                    data=ucs.CHESS_PIECES[figure]
                )
            is_white_tile = not is_white_tile
        is_white_tile = not is_white_tile
        print(board_row)

