from flask import Flask, render_template, request, jsonify, session
from flask_bootstrap import Bootstrap5
import random
import copy

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = 'your-secret-key-here'

def check_winner(board):
    # Check rows, columns and diagonals
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    
    if "" not in board:
        return "tie"
    return None

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ""]

def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    
    if result == 'O':
        return 10 - depth
    elif result == 'X':
        return depth - 10
    elif result == 'tie':
        return 0
        
    if is_maximizing:
        best_score = float('-inf')
        for pos in get_empty_cells(board):
            board[pos] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[pos] = ''
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for pos in get_empty_cells(board):
            board[pos] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[pos] = ''
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    
    # First move randomization for variety
    empty_cells = get_empty_cells(board)
    if len(empty_cells) >= 8:  # If it's first or second move
        return random.choice(empty_cells)
    
    # Use minimax for subsequent moves
    for pos in empty_cells:
        board[pos] = 'O'
        score = minimax(board, 0, False, alpha, beta)
        board[pos] = ''
        if score > best_score:
            best_score = score
            best_move = pos
    
    return best_move

@app.route('/')
def index():
    # Initialize or reset the game board
    session['board'] = [""] * 9
    session['current_player'] = 'X'
    session['game_over'] = False
    return render_template('index.html', board=session['board'])

@app.route('/make_move', methods=['POST'])
def make_move():
    if session.get('game_over', False):
        return jsonify({'error': 'Game is over'}), 400
        
    position = request.json.get('position')
    if not isinstance(position, int) or position < 0 or position > 8:
        return jsonify({'error': 'Invalid position'}), 400
        
    board = session.get('board', [""] * 9)
    if board[position] != "":
        return jsonify({'error': 'Position already taken'}), 400
        
    # Player's move
    board[position] = 'X'
    winner = check_winner(board)
    
    if winner is None:
        # Computer's move using minimax
        computer_position = get_best_move(board)
        if computer_position is not None:
            board[computer_position] = 'O'
            winner = check_winner(board)
    
    session['board'] = board
    
    if winner:
        session['game_over'] = True
        return jsonify({
            'board': board,
            'winner': winner,
            'game_over': True
        })
    
    return jsonify({
        'board': board,
        'winner': None,
        'game_over': False
    })

if __name__ == '__main__':
    app.run(debug=True)
