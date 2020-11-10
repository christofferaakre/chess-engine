import chess
from chessboard import display

board = chess.Board()
position = chess.STARTING_BOARD_FEN

while True:
    display.start(position)
    move = input('Make your move: ')
    try:
        board.push_san(move)
        position = board.fen()
        display.start(position)
    except:
        print(f"Invalid move, try again")
    finally:
        if board.is_game_over():
            print(f"Game over. {board.result()}")
            break