from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# ตัวแปรเก็บสถานะเกม
game_data = {
    'number': random.randint(1, 100),
    'attempts': 0,
    'history': [],
    'game_over': False
}

@app.route('/', methods=['GET', 'POST'])
def index():
    global game_data

    if request.method == 'POST':
        if 'guess' in request.form:
            guess = int(request.form['guess'])
            game_data['attempts'] += 1
            game_data['history'].append(guess)

            if guess < game_data['number']:
                message = 'Too low!'
            elif guess > game_data['number']:
                message = 'Too high!'
            else:
                message = 'You win!'
                game_data['game_over'] = True

            if game_data['attempts'] >= 10 and not game_data['game_over']:
                message = 'You lose! The number was {}.'.format(game_data['number'])
                game_data['game_over'] = True

            return render_template('index.html', message=message, game_data=game_data)

        elif 'new_game' in request.form:
            # รีเซ็ตเกม
            game_data = {
                'number': random.randint(1, 100),
                'attempts': 0,
                'history': [],
                'game_over': False
            }
            return redirect(url_for('index'))

    return render_template('index.html', game_data=game_data)

if __name__ == '__main__':
    app.run(debug=True)