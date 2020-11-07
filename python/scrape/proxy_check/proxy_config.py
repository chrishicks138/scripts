DATABASE = "./proxy_check/proxies.db"

TABLE = "PROXIES"

COLUMN = "ip"

COLUMNS = [
  "ip",
  "port",
]

CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS """+TABLE+''' (ip text NOT NULL, port text NOT NULL);'''


