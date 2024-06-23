from flask import Flask, render_template, request
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
    query = "SELECT Player, Country FROM cricket_table_data"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()

    return render_template('players.html', data=data_list)


@app.route('/stats')
def render_stats_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'IND'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('stats.html', data=data_list)



@app.route('/sa')
def render_sa_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'SA'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('sa.html', data=data_list)


@app.route('/aus')
def render_aus_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'AUS'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('aus.html', data=data_list)


@app.route('/ban')
def render_ban_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'BAN'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('ban.html', data=data_list)

@app.route('/afg')
def render_afg_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'AFG'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('afg.html', data=data_list)

@app.route('/uae')
def render_uae_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'UAE'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('uae.html', data=data_list)

@app.route('/pak')
def render_pak_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'PAK'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('pak.html', data=data_list)

@app.route('/hk')
def render_hk_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'HK'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('hk.html', data=data_list)

@app.route('/eng')
def render_eng_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'ENG'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('eng.html', data=data_list)

@app.route('/png')
def render_png_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'PNG'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('png.html', data=data_list)


@app.route('/nz')
def render_nz_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'NZ'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('nz.html', data=data_list)


@app.route('/ire')
def render_ire_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'IRE'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('ire.html', data=data_list)


@app.route('/wi')
def render_wi_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'WI'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('wi.html', data=data_list)


@app.route('/scot')
def render_scot_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'SCOT'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('scot.html', data=data_list)


@app.route('/nep')
def render_nep_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'NEP'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('nep.html', data=data_list)



@app.route('/zim')
def render_zim_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'ZIM'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('zim.html', data=data_list)


@app.route('/sl')
def render_sl_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Country = 'SL'"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('sl.html', data=data_list)


@app.route('/all')
def render_all_page():  # put application's code here
    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()



    return render_template('all.html', data=data_list)


@app.route('/search', methods=['GET', 'POST'])
def render_search_page():  # put application's code here

    look_up = request.form['Search']
    title = "Search for: '" + look_up + "' "
    look_up = "%" + look_up + "%"

    query = "SELECT Player, Country, Matches, Innings, Not_Outs, Runs, Ave, Balls_Faced, Strike_Rate, Hundreds ,Fiftys, Fours, Sixes, Ducks FROM cricket_table_data WHERE Player LIKE ? OR Country LIKE ? OR Matches LIKE ? OR Innings LIKE ? OR Not_Outs LIKE ? OR Runs LIKE ? OR Ave LIKE ? OR Balls_Faced LIKE ? OR Strike_Rate LIKE ? OR Hundreds LIKE ? OR Fiftys LIKE ? or Fours LIKE ? OR Sixes LIKE ? OR Ducks LIKE ?"

    connection = create_connection(DATABASE)

    cursor = connection.cursor()
    cursor.execute(query, (look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up))

    data_list = cursor.fetchall()



    return render_template('all.html', data=data_list, page_title = title)

if __name__ == '__main__':
    app.run()
