import sqlite3

class FoodNotFoundError(Exception):
    pass

class DatabaseModel:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def close_connection(self):
        self.conn.close()

    def get_CategoryList(self):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute('SELECT * FROM Food_Category')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_foodList(self, category_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM FoodInfo WHERE category_id = {category_id}')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_CategoryName(self, category_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Food_Category WHERE id = {category_id}')
        rows = self.cursor.fetchall()
        return rows[0]['name']
    
    def get_food(self, food_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM FoodInfo WHERE id = {food_id}')
        rows = self.cursor.fetchall()
        return rows[0]
    
    def get_commonIllnessList(self):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Common_Illness')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_IllnessByID(self, illness_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Common_Illness WHERE id = {illness_id}')
        rows = self.cursor.fetchall()
        return rows[0]
    
    def get_LifeStagesList(self):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Life_Stages')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_LifeStagesByID(self, stage_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Life_Stages WHERE id = {stage_id}')
        rows = self.cursor.fetchall()
        return rows[0]
    
    def get_DeficiencyList(self):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Deficiency')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_DeficiencyByID(self, deficiency_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Deficiency WHERE id = {deficiency_id}')
        rows = self.cursor.fetchall()
        return rows[0]
    
    def get_SeasonsList(self):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Season')
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_SeasonByID(self, season_id):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f'SELECT * FROM Season WHERE id = {season_id}')
        rows = self.cursor.fetchall()
        return rows[0]
    
    def searchText (self, search_query):
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(f"""
            SELECT 
                    FoodInfo.id AS FoodInfo_id,
                    Common_Illness.id AS Common_Illness_id,
                    Life_Stages.id AS Life_Stages_id,
                    Deficiency.id AS Deficiency_id,
                    Season.id AS Season_id,
                    FoodInfo.name As FoodInfo_name,
                    Common_Illness.name AS Common_Illness_name,
                    Life_Stages.name AS Life_Stages_name,
                    Life_Stages.description  AS Life_Stages_description,
                    Life_Stages.principles  AS Life_Stages_principles,
                    Life_Stages.suitable_foods  AS Life_Stages_suitable_foods,
                    Life_Stages.nonsuitable_foods AS Life_Stages_nonsuitable_foods,
                    Deficiency.name AS Deficiency_name,
                    Deficiency.description AS Deficiency_description,
                    Deficiency.principles AS Deficiency_principles,
                    Deficiency.suitable_foods AS Deficiency_suitable_foods,
                    Deficiency.nonsuitable_foods AS Deficiency_nonsuitable_foods,
                    Season.name AS Season_name,
                    Season.description AS Season_description,
                    Season.principles AS Season_principles,
                    Season.suitable_foods AS Season_suitable_foods,
                    Season.nonsuitable_foods AS Season_nonsuitable_foods,     
                    * 
            FROM FoodInfo
            FULL JOIN Common_Illness ON FoodInfo.name = Common_Illness.name
            FULL JOIN Life_Stages ON FoodInfo.name = Life_Stages.name
            FULL JOIN Deficiency ON FoodInfo.name = Deficiency.name
            FULL JOIN Season ON FoodInfo.name = Season.name
            WHERE (FoodInfo.name LIKE '%' || '{search_query}' || '%' 
                OR FoodInfo.nickname LIKE '%' || '{search_query}' || '%' 
                OR FoodInfo.efficacy LIKE '%' || '{search_query}' || '%' 
                OR FoodInfo.suitable_for LIKE '%' || '{search_query}' || '%' 
                OR FoodInfo.not_suitable_for LIKE '%' || '{search_query}' || '%' 
                OR FoodInfo.note LIKE '%' || '{search_query}' || '%'
                OR Common_Illness.name LIKE '%' || '{search_query}' || '%' 
                OR Common_Illness.description LIKE '%' || '{search_query}' || '%' 
                OR Common_Illness.principles LIKE '%' || '{search_query}' || '%' 
                OR Common_Illness.suitable_foods LIKE '%' || '{search_query}' || '%' 
                OR Common_Illness.nonsuitable_foods LIKE '%' || '{search_query}' || '%'
                OR Life_Stages.name LIKE '%' || '{search_query}' || '%' 
                OR Life_Stages.description LIKE '%' || '{search_query}' || '%' 
                OR Life_Stages.principles LIKE '%' || '{search_query}' || '%' 
                OR Life_Stages.suitable_foods LIKE '%' || '{search_query}' || '%' 
                OR Life_Stages.nonsuitable_foods LIKE '%' || '{search_query}' || '%'
                OR Deficiency.name LIKE '%' || '{search_query}' || '%' 
                OR Deficiency.description LIKE '%' || '{search_query}' || '%' 
                OR Deficiency.principles LIKE '%' || '{search_query}' || '%' 
                OR Deficiency.suitable_foods LIKE '%' || '{search_query}' || '%' 
                OR Deficiency.nonsuitable_foods LIKE '%' || '{search_query}' || '%'
                OR Season.name LIKE '%' || '{search_query}' || '%' 
                OR Season.description LIKE '%' || '{search_query}' || '%' 
                OR Season.principles LIKE '%' || '{search_query}' || '%' 
                OR Season.suitable_foods LIKE '%' || '{search_query}' || '%' 
                OR Season.nonsuitable_foods LIKE '%' || '{search_query}' || '%')
            COLLATE NOCASE""")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
