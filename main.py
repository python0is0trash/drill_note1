# from openpyxl.styles import (PatternFill)
import sqlite3
from flask import Flask, render_template, jsonify

# workbook_fill = PatternFill(
#     fill_type=None,
#     fgColor='FFFFFFFF'
# )

app = Flask(__name__)


@app.route('/')
def start_page():
    connection = sqlite3.connect("./data_bases/students.sqlite3")
    cursor = connection.cursor()
    cursor.execute('''
        SELECT DISTINCT
            platoon
        FROM
            cadets
        ORDER BY
            platoon;
    ''')
    platoons = cursor.fetchall()
    cursor.execute('''
        SELECT
            cadet
        FROM
            cadets
        WHERE
            platoon == {platoon}
        ORDER BY
            platoon, cadet;
    '''
                   .format(platoon=platoons[0][0]))
    cadets = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    for i in range(len(platoons)):
        platoons[i] = platoons[i][0]
    for i in range(len(cadets)):
        cadets[i] = cadets[i][0]
    return render_template('stroevka1.html', name=__name__,
                           platoons=platoons,
                           cadets=cadets,
                           date_today="10.11.2023")


if __name__ == '__main__':
    app.run(debug=True)
