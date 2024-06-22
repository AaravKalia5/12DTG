from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('index.html')

@app.route('/players.html')
def render_players_page():  # put application's code here
    return render_template('players.html')

@app.route('/stats.html')
def render_stats_page():  # put application's code here
    return render_template('stats.html')

@app.route('/all.html')
def render_all_page():  # put application's code here
    return render_template('all.html')


if __name__ == '__main__':
    app.run()
