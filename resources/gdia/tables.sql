DROP SCHEMA greedy CASCADE;
CREATE SCHEMA greedy;
SET search_path TO greedy;

-----------------
-- Locations
-----------------
CREATE TABLE locs (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(20) NOT NULL,
  route_name INT NOT NULL,
  lon float NOT NULL,
  lat float NOT NULL
);

\copy locs FROM './data/Brickell_Downtown_OD_LatLongs.csv' WITH csv HEADER;

-----------------
-- Data
-----------------
CREATE TABLE data (
  id INT NOT NULL,
  name VARCHAR(40) NOT NULL,
  orig_id INT NOT NULL,
  dest_id INT NOT NULL,
  dest_rank INT NOT NULL,
  travel_time float NOT NULL,
  total_miles float NOT NULL,
  total_mins float NOT NULL,
  FOREIGN KEY (orig_id) REFERENCES locs (id),
  FOREIGN KEY (dest_id) REFERENCES locs (id)
);

\copy data FROM './data/ODCM_Brickell_Downtown_AVConstraints.csv' WITH csv HEADER;


-------------------
-- Solution
-------------------
CREATE TABLE solution (
  id BIGSERIAL PRIMARY KEY
);

\copy solution FROM './data/solution.csv' WITH csv HEADER;


--------------
-- Queries
--------------

-- (stop_id, lat, lon)

\copy ( SELECT id, lat, lon FROM locs ) TO './data/locations.csv' csv HEADER;

-- (orig, dest, travel_time)
\copy ( SELECT orig_id, dest_id, travel_time FROM data dt WHERE orig_id IN (SELECT id FROM solution sl) AND dest_id IN (SELECT id FROM solution sl) AND orig_id!=dest_id ) TO './data/durations.csv' csv HEADER;
