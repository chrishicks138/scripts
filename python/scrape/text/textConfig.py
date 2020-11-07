DATABASE = "./text/text.db"

TABLE = "TEXT"

COLUMN = "url"

COLUMNS = [
  "url",
  "ptag",
]

CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS """+TABLE+''' (url text NOT NULL, ptag text NOT NULL);'''


