from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = 'cricket_database.db'

def create_connection(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection

    except Error as e:
        print(e)
        return None


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('index.html')

@app.route('/players')
def render_players_page():  # put application's code here
    return render_template('players.html')

@app.route('/stats')
def render_stats_page():  # put application's code here
    return render_template('stats.html')

@app.route('/all')
def render_all_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('all.html', data=data_list)




if __name__ == '__main__':
    app.run()
