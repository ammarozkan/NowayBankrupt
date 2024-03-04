CREATE TABLE activities (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	head TEXT NOT NULL,
	explanation TEXT,
	money FLOAT,
	date TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime'))
);