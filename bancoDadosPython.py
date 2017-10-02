#1/use/bin/python3
import sqlite3
def main():
    db = sqlite3.connect('son.db')
    db.row_factory = sqlite3.Row
    db.execute('DROP TABLE IF EXISTS TEST')
    db.execute('CREATE TABLE TEST(ID INT, NOME TEXT)')
    db.execute('INSERT INTO TEST (ID, NOME) VALUES (?,?)', (1, 'Rodrigo'))
    db.commit()
    cursor = db.execute('SELECT ID, NOME FROM TEST ORDER BY NOME')
    for row in cursor:
        print(dict(row))
if __name__ == "__main__" : main()
