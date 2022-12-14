import mysql.connector

class UserDatabase:
    def __init__(self) -> None:
        #constructor used for connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Zeeshan@123",
            database="cafe_management")
        
        self.cursor = self.conn.cursor()

    def get_user(self, id):
        query = f"select * from users where id = {id}"
        self.cursor.execute(query)
        user_dict = {}
        result = self.cursor.fetchone()
        if result is not None:
            user_dict["id"], user_dict["username"], user_dict["password"] = result
            return user_dict

    def add_user(self, username, password):
        query = f"insert into users(username, password) values ('{username}', '{password}')"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False

    def delete_user(self, id):
        query = f"delete from users where id = {id}"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True