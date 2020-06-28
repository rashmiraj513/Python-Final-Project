import sqlite3
connectionObject = sqlite3.connect('CricketGame.db')
cursorObject = connectionObject.cursor()
sql_Match = '''CREATE TABLE IF NOT EXISTS Match (
Player STRING NOT NULL PRIMARY KEY, 
Scored INTEGER,
Faced INTEGER,
Fours INTEGER,
Sixes INTEGER,
Bowled INTEGER,
Maiden INTEGER,
Given INTEGER,
Wickets INTEGER,
Catches INTEGER,
Stumping INTEGER,
RO INTEGER);'''

sq1_Teams = ''' CREATE TABLE IF NOT EXISTS Teams (
Name STRING NOT NULL,
Players STRING NOT NULL,
Value INTEGER NOT NULL);'''

sql_Stats = ''' CREATE TABLE IF NOT EXISTS Stats (
Player STRING NOT NULL PRIMARY KEY,
Matches STRING NOT NULL,
Run INTEGER NOT NULL,
Centuries INTEGER,
HalfCenturies INTEGER,
Value INTEGER NOT NULL,
Category STRING NOT NULL);'''

sql_TeamsData = ''' INSERT INTO Match (Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RO) VALUES
("Virat Kohli",102,98,8,2,0,0,0,0,0,0,1),
("Yuvraj Singh",12,20,1,0,48,0,36,1,0,0,0),
("Ajinkya Rahane",49,75,3,0,0,0,0,0,1,0,0),
("Shikhar Dhawan",32,35,4,0,0,0,0,0,0,0,0),
("M. S. Dhoni",56,45,3,1,0,0,0,0,3,2,0),
("Axar Patel",8,4,2,0,48,2,35,1,0,0,0),
("Hardik Pandya",42,36,3,3,30,0,25,0,1,0,0),
("Sir Jadeja",18,10,1,1,60,3,50,2,1,0,1),
("Kedar Jadhav",65,60,7,0,24,0,24,0,0,0,0),
("R. Ashwin",23,42,3,0,60,2,45,6,0,0,0),
("Umesh Yadav",0,0,0,0,54,0,50,4,1,0,0),
("Jasprit Bumrah",0,0,0,0,60,2,49,1,0,0,0),
("Bhuwaneshwar Kumar",15,12,2,0,60,1,46,2,0,0,0),
("Rohit Sharma",46,65,5,1,0,0,0,0,1,0,0),
("Dinesh Kartik",29,42,3,0,0,0,0,0,2,0,1);'''

sql_StatsData = ''' INSERT INTO Stats (Player,Matches,Run,Centuries,HalfCenturies,Value,Category) VALUES
("Virat Kohli",189,8257,28,43,120,"BAT"),
("Yuvraj Singh",86,3689,10,21,100,"BAT"),
("Ajinkya Rahane",158,5435,11,31,100,"BAT"),
("Shikhar Dhawan",25,565,2,1,85,"AR"),
("M. S. Dhoni",78,2573,3,19,75,"BAT"),
("Axar Patel",67,208,0,0,100,"BWL"),
("Hardik Pandya",70,77,0,0,75,"BWL"),
("Sir Jadeja",16,1,0,0,85,"BWL"),
("Kedar Jadhav",111,675,0,1,90,"BWL"),
("R. Ashwin",136,1914,0,10,100,"AR"),
("Umesh Yadav",296,9496,10,64,110,"WK"),
("Jasprit Bumrah",73,1365,0,8,60,"WK"),
("Bhuwaneshwar Kumar",17,289,0,2,75,"AR"),
("Rohit Sharma",304,8701,14,52,85,"BAT"),
("Dinesh Kartik",11,111,0,0,75,"AR");'''

try:
    cursorObject.execute(sql_Match)
    cursorObject.execute(sq1_Teams)
    cursorObject.execute(sql_Stats)

    cursorObject.execute(sql_TeamsData)
    cursorObject.execute(sql_StatsData)
    connectionObject.commit()

except:
    print("Error in creating table.")
    print("Please debug the code!!!")
    connectionObject.rollback()

connectionObject.close()
