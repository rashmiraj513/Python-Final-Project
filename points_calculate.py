import sqlite3
# connecting to 'CricketGame.db' dataase.
connectionObject = sqlite3.connect('CricketGame.db')
# Creating Cursor Object.
cursorObject = connectionObject.cursor()
# String which selects all data from the table Match.
sql = "SELECT * FROM Match;"
try:
    cursorObject.execute(sql)
    connectionObject.commit()
except:
    connectionObject.rollback()
#cursorObject.execute(sql)

# Fetching all the data and storing in row.
row = cursorObject.fetchall()

connectionObject.close()

# Function that calculates points for players.
def pointsCalculator(data):
    points = 0
    score = data[1]
    try:
        strike_rate = data[1] / data[2] * 100   # strike rate = runs / balls.
    except:
        strike_rate = 0
    
    fours, sixes = data[3], data[4]
    wickets = data[8]
    try:
        economy_rate = (data[7] / data[5] / 6)
    except:
        economy_rate = 0
    
    fielding = (data[9] + data[10] + data[11])

    # 1 points for every 2 runs scored.
    points = score / 2

    # 5 points for half centuries.
    if score > 50:
        points += 5
    
    # 10 points for centuries.
    if score > 100:
        points += 10
    
    # 4 points for strike rate greater than 100.
    if strike_rate > 100:
        points += 4
    # 2 points for strike rate between 80 and 100.
    elif strike_rate > 80:
        points += 2
    
    # 1 point for a boundary and 2 points for an over boundary.
    points += (fours + (2 * sixes))
    # 10 points for a wicket.
    points += (wickets * 10)
    # 10 points if taken wickets are greater than or equal to 5.
    if wickets >= 5:
        points += 10
    # 5 points if taken wickets are greater than or equal to 3.
    elif wickets >= 3:
        points += 5
    
    # 4 points if economy rate lies between 3.5 and 4.5
    if economy_rate >= 3.5 and economy_rate <= 4.5:
        points += 4
    # 7 points if economy rate lies between 2 and 3.5
    elif economy_rate >= 2 and economy_rate < 3.5:
        points += 7
    # 10 points if economy rate is less than 2
    elif economy_rate < 2 and data[7] > 0:
        points += 10
    
    # 10 points for each catch/stumping/run out.
    points = points + (fielding * 10)
    return points       # returning the points.

player_dict = {}        # Creating empty dictionary.

def returnPoint():
    player_points = {}
    for i in row:
        player_points[i[0]] = pointsCalculator(i)
    return player_points

#print(returnPoint())
