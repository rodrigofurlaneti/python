#1/use/bin/python3
import sqlite3
def insert(db, row):
    db.execute('INSERT INTO TEST (ID, NOME) VALUES (?,?)', (row['ID'], row['NOME']))
    db.commit()

def retrieve(db , ID):
    cursor = db.execute('SELECT * FROM TEST WHERE ID = ?', (ID,))
    return cursor.fetchone()

def update(db, row):
    db.execute('UPDATE TEST SET NOME = ? WHERE ID=?' , (row['NOME'], row['ID']))
    db.commit()

def delete(db,ID):
    db.execute('DELETE FROM TEST WHERE ID = ?', (ID,))
    db.commit()

def display(db):
    cursor = db.execute('SELECT * FROM TEST ORDER BY ID')
    for row in cursor:
        print(' {}:{}'. format(row['ID'], row['NOME']))

def main():
    db = sqlite3.connect('son.db')
    db.row_factory = sqlite3.Row
    db.execute('DROP TABLE IF EXISTS TEST')
    db.execute('CREATE TABLE TEST(ID INT, NOME TEXT)')
    print("Criar")
    insert(db, dict(ID=1, NOME='Rodrigo'))
    insert(db, dict(ID=2, NOME='Joaquim'))
    insert(db, dict(ID=3, NOME='Jose'))
    insert(db, dict(ID=4, NOME='Maria'))
    display(db)

    print("Recuperar")
    print(dict(retrieve(db, 1)), dict(retrieve(db, 2)), dict(retrieve(db, 3)), dict(retrieve(db, 4)))

    print("Atualizar")
    update(db, dict (ID='1', NOME='MARIA JOSE'))
    display(db)

    print ("Excluir")
    delete(db, 1)
    display(db)

if __name__ == "__main__" : main()
