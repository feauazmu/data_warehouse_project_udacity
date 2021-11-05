import configparser


# CONFIG
config = configparser.ConfigParser()
config.read("dwh.cfg")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create = """
CREATE TABLE IF NOT EXISTS staging_events (
  artist        VARCHAR(250),
  auth          VARCHAR(20),
  firstName     VARCHAR(50),
  gender        CHAR(1),
  itemInSession INTEGER,
  lastName      VARCHAR(50),
  length        DECIMAL(9, 5),
  level         CHAR(4),
  location      VARCHAR(80),
  method        CHAR(3),
  page          VARCHAR(20),
  registration  BIGINT,
  sessionId     INTEGER,
  song          VARCHAR(500),
  status        SMALLINT,
  ts            BIGINT,
  userAgent     VARCHAR(250),
  userId        INTEGER
);
"""

staging_songs_table_create = """
CREATE TABLE IF NOT EXISTS staging_songs (
  artist_id         CHAR(18)        NOT NULL,
  artist_latitude   DECIMAL(7,5),
  artist_location   VARCHAR(256),
  artist_longitude  DECIMAL(8,5),
  artist_name       VARCHAR(250)    NOT NULL,
  duration          DECIMAL(9,5),
  num_songs         INTEGER         NOT NULL,
  song_id           CHAR(18)        NOT NULL,
  title             VARCHAR(500)    NOT NULL,
  year              INTEGER
);
"""

songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplay (
  songplay_id   INTEGER IDENTITY(0,1) PRIMARY KEY   NOT NULL,
  start_time    TIMESTAMP                           NOT NULL,
  user_id       INTEGER                             NOT NULL    DISTKEY,
  level         VARCHAR(4)                          NOT NULL,
  song_id       CHAR(18)                            NOT NULL,
  artist_id     CHAR(18)                            NOT NULL,
  session_id    INTEGER                             NOT NULL    SORTKEY,
  location      VARCHAR(80)                         NOT NULL,
  user_agent    VARCHAR(250)                        NOT NULL,
  
  FOREIGN KEY(user_id)
    REFERENCES users(user_id),

  FOREIGN KEY(song_id)
    REFERENCES song(song_id),

  FOREIGN KEY(artist_id)
    REFERENCES artist(artist_id)
);
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
  user_id       INTEGER PRIMARY KEY NOT NULL    SORTKEY DISTKEY,
  first_name    VARCHAR(50)         NOT NULL,
  last_name     VARCHAR(50)         NOT NULL,
  gender        CHAR(1)             NOT NULL,
  level         CHAR(4)             NOT NULL
);
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS song (
  song_id   VARCHAR(18) PRIMARY KEY NOT NULL    SORTKEY,
  title     VARCHAR(80)             NOT NULL,
  artist_id VARCHAR(80)             NOT NULL,
  year      INTEGER                 NOT NULL,
  duration  DECIMAL(9, 5)           NOT NULL
);
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artist (
  artist_id VARCHAR(18) PRIMARY KEY NOT NULL    SORTKEY,
  name      VARCHAR(80)             NOT NULL,
  location  VARCHAR(80)             NOT NULL,
  latitude  DECIMAL(7,5)            NOT NULL,
  longitude DECIMAL(8,5)            NOT NULL
);
"""

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
  start_time    TIMESTAMP PRIMARY KEY   NOT NULL    SORTKEY,
  hour          SMALLINT                NOT NULL,
  day           SMALLINT                NOT NULL,
  week          SMALLINT                NOT NULL,
  month         SMALLINT                NOT NULL,
  year          SMALLINT                NOT NULL,
  weekday       SMALLINT                NOT NULL
);
"""

# STAGING TABLES

staging_events_copy = (
    """
"""
).format()

staging_songs_copy = (
    """
"""
).format()

# FINAL TABLES

songplay_table_insert = """
"""

user_table_insert = """
"""

song_table_insert = """
"""

artist_table_insert = """
"""

time_table_insert = """
"""

# QUERY LISTS

create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create,
]
drop_table_queries = [
    staging_events_table_drop,
    staging_songs_table_drop,
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [
    songplay_table_insert,
    user_table_insert,
    song_table_insert,
    artist_table_insert,
    time_table_insert,
]
