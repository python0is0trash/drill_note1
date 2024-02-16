# from openpyxl.styles import (PatternFill)
from flask import Flask, render_template, jsonify
from data_bases.db import select_info_from_db
from datetime import datetime, date

# workbook_fill = PatternFill(
#     fill_type=None,
#     fgColor='FFFFFFFF'
# )

app = Flask(__name__)


@app.route('/')
def start_page():
    return render_template('stroevka1.html', name=__name__,
                           platoons=select_info_from_db()[0],
                           cadets=select_info_from_db()[1],
                           date_today="{}-{}-{}".format(date.today().day, date.today().month, date.today().year))


if __name__ == '__main__':
    app.run(debug=True)
