# Tic Tac Toe Game with Flask

A modern, responsive Tic Tac Toe game built using Flask and Bootstrap. Created using Windsurf IDE in under 5 minutes!

## 🚀 Quick Overview

This project demonstrates how quickly you can create a full-stack web application using Windsurf IDE. The game features a clean UI, player vs computer gameplay, and real-time updates.

## 🛠️ Technologies Used

- **Backend**: Flask 3.0.0 (Python web framework)
- **Frontend**: 
  - Bootstrap 5 (via bootstrap-flask)
  - JavaScript (for game logic)
  - CSS3 (for styling)
- **Development Environment**: Windsurf IDE

## 📁 Project Structure

```
tic_tac_toe/
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── templates/
│   ├── base.html      # Base template with common elements
│   └── index.html     # Game board template
└── static/
    ├── css/
    │   └── style.css  # Game styling
    └── js/
        └── game.js    # Game logic
```

## 💻 How It Works

### Backend (app.py)
- Uses Flask for routing and game logic
- Implements session management for game state
- Provides RESTful endpoints for game moves
- Includes computer player logic

### Frontend
- **HTML Templates**:
  - `base.html`: Common layout and Bootstrap setup
  - `index.html`: Game board and controls
- **JavaScript (game.js)**:
  - Handles player moves
  - Makes AJAX calls to backend
  - Updates UI in real-time
- **CSS (style.css)**:
  - Responsive grid layout
  - Smooth animations
  - Modern styling

## 🎮 Game Features

1. **Player vs Computer**: Play against a computer opponent
2. **Real-time Updates**: Instant feedback for moves
3. **Win Detection**: Automatically detects wins and ties
4. **Responsive Design**: Works on all screen sizes
5. **Easy Restart**: Quick game reset option

## 🌟 Created with Windsurf IDE

This project showcases the power of Windsurf IDE:
- **Quick Setup**: Created complete project structure in seconds
- **Smart Suggestions**: Automated code completion and suggestions
- **Integrated Tools**: All necessary development tools in one place
- **Real-time Preview**: Instant feedback during development

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Visit http://localhost:5000 in your browser

## 🎯 How to Play

1. Open the game in your browser
2. Click any empty cell to place your X
3. Computer automatically responds with O
4. First to get three in a row wins!
5. Click "New Game" to start over

## 💡 Code Highlights

### Session Management
```python
@app.route('/')
def index():
    session['board'] = [""] * 9
    session['current_player'] = 'X'
    session['game_over'] = False
    return render_template('index.html', board=session['board'])
```

### Win Detection
```python
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
```

### AJAX Game Updates
```javascript
fetch('/make_move', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ position: parseInt(position) })
})
```

## 🎨 Styling Example
```css
.game-board {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    max-width: 300px;
    margin: 0 auto;
}
```

## ✨ Why Windsurf IDE?

I'm thrilled to have created this project in mere minutes! Windsurf IDE's automation and smart templates saved me hours of tedious work. The fact that I can create a full-stack web app so quickly is a testament to the incredible technology we have today.

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add difficulty levels for computer player
- Implement multiplayer support
- Add sound effects and animations
- Create a game history feature
