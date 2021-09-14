DATABASE = "urls.db"

TABLE = "URLS"

COLUMN = "downloaded"

COLUMNS = [
  "item",
  "downloaded",
]

CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS """+TABLE+''' (item text NOT NULL, downloaded text NOT NULL);'''


