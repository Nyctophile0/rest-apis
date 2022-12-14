import mysql.connector

class ItemDatabase:
    def __init__(self) -> None:
        #constructor used for connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Zeeshan@123",
            database="cafe_management")
        
        self.cursor = self.conn.cursor()

    def get_items(self):
        result = []
        query = "SELECT * FROM item" 
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"], item_dict["name"], item_dict["price"] = row
            result.append(item_dict)
        return result

    def get_item(self, item_id):
        query = f"select * from item where id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["id"], item_dict["name"], item_dict["price"] = row
            return [item_dict]


    def add_item(self, id, body):
        query = f"insert into item(id, name, price) values ('{id}', '{body['name']}', {body['price']})" 
        self.cursor.execute(query)
        self.conn.commit()

    def update_item(self, id, body):
        query = f"UPDATE item SET name = '{body['name']}', price = {body['price']} where id = '{id}'" 
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True

    def delete_item(self, id):
        query = f"delete from item where id = '{id}'"
        #print(query)
        self.cursor.execute(query)
        #print(self.cursor.rowcount)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True

#obj = ItemDatabase()
#obj.put_item(id="fc8e6c4a1bdf468d970908ff6e566fef", body_object={'name':"test", 'price':35})