from flask import Flask, render_template
from random import randint


app = Flask('rock paper')


def computer_move():
    options = ['rock','paper','scissors']
    move = options[randint(0,2)]
    return move

def winner(computer_move, player_move):
    if computer_move == player_move:
        winner = 'tie'
    elif player_move == 'rock' and computer_move == 'paper':
        winner = 'computer'
    elif player_move == 'paper' and computer_move == 'scissors':
        winner = 'computer'
    elif player_move == 'scissors' and computer_move == 'rock':
        winner = 'computer'
    else:
        winner = 'player'

    return winner     

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shaun/<choice>')
def shaun(choice):
    # return '<h1>this is winner</h1>'
    player_move = choice
    computer = computer_move()
    winner_g=winner(computer,player_move)
    print(winner_g)
   
    

    return render_template('winner.html',shaun = winner_g,computer=computer,player_move=player_move)

   



if __name__ =="__main__":
    app.run()
