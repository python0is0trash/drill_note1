import sqlite3

def select_info_from_db():
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
    return platoons, cadets
