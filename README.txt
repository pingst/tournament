Implementation of a Swiss-style tournament

--------------------------------------------------------

Files included:
tournament.py
tournament.sql
tournament_test.py

--------------------------------------------------------

Software needed:
Install Vagrant https://www.vagrantup.com/
and VirtualBox https://www.virtualbox.org/

--------------------------------------------------------

Instructions:
1. Start Vagrant
2. Run GitBash
3. Navigate to the correct folder
4. Run $ vagrant ssh
5. Open psql => psql
6. Create the tournament db => CREATE DATABASE tournament;
7. Connect to the tournament db => \c tournament
8. Import the contents of tournament.sql => \i tournament.sql
9. Exit psql => \q
10. Run tournament_test.py $ python tournament_test.py

tournament_test.py file should run 10 tests, and give these outcomes:
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!

--------------------------------------------------------

RESOURCES USED
Truncate
http://stackoverflow.com/questions/5342440/reset-auto-increment-counter-in-postgres
Coalesce
https://www.postgresql.org/docs/9.5/static/functions-conditional.html
Left join
https://www.postgresql.org/docs/9.4/static/tutorial-join.html
https://discussions.udacity.com/t/playerstandings-and-views/39255/7
Not null
http://stackoverflow.com/questions/2326813/how-to-make-a-view-column-not-null
Alter table
https://www.postgresql.org/docs/9.1/static/sql-altertable.html
.fetchall()
https://discussions.udacity.com/t/playerstandings-output-is-confusing-l-appended-to-wins-and-matches-count/33111/5
Primary and foreign keys
http://stackoverflow.com/questions/27159951/there-is-no-unique-constraint-matching-given-keys-for-referenced-table
Guidance on swiss pairings method
https://github.com/mrosata/fullstack-tournament/blob/master/tournament/tournament.py
https://github.com/anuragsoni/udacity-fsnd-tournament-results/blob/master/tournament.py
https://github.com/joshuashoemaker/swiss-pairing-tournament/blob/master/tournament.py
