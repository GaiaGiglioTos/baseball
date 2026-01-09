from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.`year` as y
from teams t
where t.year>= "1980" """

        cursor.execute(query)

        for row in cursor:
            result.append(row["y"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSquadreAnno(y):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.*
from teams t
where t.year = %s """

        cursor.execute(query,(y,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalari(y,idMap):
        conn = DBConnect.get_connection()

        res = {}

        cursor = conn.cursor(dictionary=True)
        query = """select t.ID as id, sum(s.salary) as s
from salaries s, teams t
where s.`year` = %s
and t.ID = s.teamID 
and t.`year` = s.`year` 
group by t.ID"""
        cursor.execute(query,(y,))

        for row in cursor:
                res[idMap[row["id"]]] = row["s"]

        cursor.close()
        conn.close()
        return res
