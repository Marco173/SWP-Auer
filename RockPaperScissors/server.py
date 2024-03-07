from flask import Flask, request
import sqlite3

app = Flask(__name__)


def setup_db():
    connection = sqlite3.connect('SchereSteinPapier.db')
    cursor = connection.cursor()

    query = """CREATE TABLE IF NOT EXISTS stats (
    Eintrags_id INTEGER PRIMARY KEY AUTOINCREMENT,
    winner TEXT NOT NULL,
    winnerSymbol TEXT
    )
    """
    cursor.execute(query)


def save_stats(stats):
    connection = sqlite3.connect('database  .db')
    cursor = connection.cursor()

    # save data to db
    query = insert_query = """
       INSERT INTO stats (winner, winnerSymbol)
       VALUES ('{}','{}')
       """.format(stats['winner'], stats['winnerSymbol'])

    print("executing: ", query)
    cursor.execute(query)
    connection.commit()

@app.route('/stats', methods=['POST'])
def post_statistics():
    if request.is_json:
        print(request.json)
        save_stats(request.json)
        return 'Daten erfolgreich eingelesen'
    else:
        return 'Fehler beim Speichern der Daten'

if __name__ == '__main__':
    setup_db()
    app.run(debug=True)