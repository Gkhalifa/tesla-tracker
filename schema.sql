CREATE TABLE charging_sessions (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    kwh_added REAL NOT NULL,
    cost REAL NOT NULL,
    odometer INTEGER NOT NULL
);

CREATE TABLE repairs (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    cost REAL NOT NULL,
    odometer INTEGER,
    category TEXT NOT NULL
);
