document.addEventListener('DOMContentLoaded', function() {
    const cells = document.querySelectorAll('.cell');
    const status = document.getElementById('status');
    const resetButton = document.getElementById('reset-game');

    cells.forEach(cell => {
        cell.addEventListener('click', handleMove);
    });

    resetButton.addEventListener('click', () => {
        window.location.reload();
    });

    function handleMove(event) {
        const cell = event.target;
        const position = cell.dataset.index;

        if (cell.textContent !== '' || cell.classList.contains('disabled')) {
            return;
        }

        fetch('/make_move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ position: parseInt(position) })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            updateBoard(data.board);

            if (data.winner) {
                handleGameOver(data.winner);
            } else {
                status.textContent = "Your turn (X)";
            }

            if (data.game_over) {
                disableBoard();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    }

    function updateBoard(board) {
        cells.forEach((cell, index) => {
            cell.textContent = board[index];
            if (board[index] === 'X') {
                cell.classList.add('x');
            } else if (board[index] === 'O') {
                cell.classList.add('o');
            }
        });
    }

    function handleGameOver(winner) {
        if (winner === 'tie') {
            status.textContent = "It's a tie!";
            status.classList.add('winner-tie');
        } else {
            status.textContent = `${winner} wins!`;
            status.classList.add(`winner-${winner.toLowerCase()}`);
        }
    }

    function disableBoard() {
        cells.forEach(cell => {
            cell.classList.add('disabled');
            cell.style.cursor = 'not-allowed';
        });
    }
});
