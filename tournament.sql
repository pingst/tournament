-- Table definitions for the tournament project.
--
--------------------------------------
-- TABLES CREATED
-- Only need 2 tables, rest can be views
--------------------------------------

-- Players
CREATE TABLE players(
  id serial PRIMARY KEY,
  name text
);

-- Matches
CREATE TABLE matches(
  match_id serial PRIMARY KEY,
  winner integer REFERENCES players (id) NOT NULL,
  loser integer REFERENCES players (id) NOT NULL
);

--------------------------------------
-- VIEWS CREATED
--------------------------------------

-- TOTAL MATCHES
CREATE VIEW tm as (
  SELECT players.id, players.name, count(matches) as matches_played from players LEFT JOIN matches ON players.id = matches.winner or players.id = matches.loser GROUP BY players.id ORDER BY matches_played desc
);

-- TOTAL WINS
CREATE VIEW tw as (
  SELECT players.id, count(matches.winner) as matches_won from players LEFT JOIN matches ON players.id = matches.winner GROUP BY players.id ORDER BY matches_won desc
);

-- STANDINGS
-- Needs to be in order id, name, wins, matches_played OR line 87 from tournament_test thows an error
CREATE VIEW standings as (
  SELECT players.id, players.name, COALESCE(tw.matches_won, 0) AS wins, tm.matches_played from players, tm, tw where players.id = tm.id and players.id = tw.id ORDER BY tw.matches_won desc
);
