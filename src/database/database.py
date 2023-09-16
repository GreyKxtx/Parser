import sqlite3


class DB:
    connection = None

    def __init__(self):
        try:
            self.connection = sqlite3.connect("database19.06.db", timeout=10)
            cursor = self.connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Posts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                source TEXT,
                                title TEXT,
                                text TEXT,
                                date TEXT,
                                link TEXT UNIQUE
                            )''')
            self.connection.commit()
        except Exception as e:
            self.connection.close()
            raise ValueError('DB cannot be connected:', str(e))

    def find_many(self):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM Posts ''')
        return cursor.fetchall()

    def insert(self, source, post_data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                '''INSERT INTO Posts (source, title, text, date, link) VALUES (?, ?, ?, ?, ?)''',
                (
                    source,
                    post_data.get('title'),
                    post_data.get('text'),
                    post_data.get('date'),
                    post_data.get('link'),
                )
            )

            self.connection.commit()
            print('Inserted')
        except sqlite3.IntegrityError:
            print('Passed')
            pass


dbService = DB()
