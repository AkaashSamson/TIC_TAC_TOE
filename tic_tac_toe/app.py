from flask import Flask, render_template, request, jsonify, session
from flask_bootstrap import Bootstrap5
import random

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
        # Computer's move
        empty_positions = [i for i, val in enumerate(board) if val == ""]
        if empty_positions:
            computer_position = random.choice(empty_positions)
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
