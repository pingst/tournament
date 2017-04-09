#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
# I left a lot of comments in the code where I had printed values
# to see how the tournament_test.py was proceeding through the code.
#
# I also included a list of references/browser tabs I had open while I
# was working through the process of writing the code in the README

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    c.execute("TRUNCATE TABLE matches RESTART IDENTITY;")
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("DELETE FROM players;")
    c.execute("TRUNCATE TABLE players RESTART IDENTITY CASCADE")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT count(id) FROM players")
    pc = int(c.fetchone()[0])
    DB.commit()
    DB.close()
    #print '\n' + 'PLAYER COUNT = ' + str(pc) + '\n'
    return pc

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT * FROM standings;")
    stand = c.fetchall()
    DB.close()
    return stand

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser,))
    # To see the id of player who won, player who lost
    #c.execute("SELECT match_id FROM matches;")
    #match_num = c.fetchall()
    #print 'Match #' + str(match_num[-1]) + ' Winner: ' + str(winner) + ' Loser: ' + str(loser)
    DB.commit()
    DB.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    #n = 1

    s = playerStandings()
    tp = len(s)
    # To see the number of players
    #print 'Total Players: ' + str(tp)
    paring = []

    for p in range(0, tp, 2):
        pair = ((s[p][0], s[p][1],
                 s[p + 1][0], s[p + 1][1]))
        # To see the list of tuples (id1, name1, id2, name2)
        #print '** Pairing ' + str(n) + ': '+ str(pair)
        paring.append(pair)
        #n += 1

    return paring
