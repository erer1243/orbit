PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	id integer primary key,
	username string UNIQUE NOT NULL,
	pwdhash string NOT NULL,
	lfx boolean NOT NULL,
	student_id integer
);
CREATE TABLE sessions (
        token string PRIMARY KEY,
        username string UNIQUE NOT NULL,
        expiry string NOT NULL);
CREATE TABLE submissions (
	sub_id string PRIMARY KEY,
	username string NOT NULL,
	time string NOT NULL,
	_to string NOT NULL,
	_from string NOT NULL,
	email_ids string NOT NULL,
	subjects string NOT NULL);
CREATE TABLE assignments (
	web_id string PRIMARY KEY,
	email_id string NOT NULL);
INSERT INTO assignments (web_id, email_id) VALUES ('setup', 'introductions');
INSERT INTO assignments (web_id, email_id) VALUES ('E0', 'exercise0');
INSERT INTO assignments (web_id, email_id) VALUES ('E1', 'exercise1');
INSERT INTO assignments (web_id, email_id) VALUES ('E2', 'exercise2');
INSERT INTO assignments (web_id, email_id) VALUES ('P0', 'programming0');
INSERT INTO assignments (web_id, email_id) VALUES ('P1', 'programming1');
INSERT INTO assignments (web_id, email_id) VALUES ('P2', 'programming2');
INSERT INTO assignments (web_id, email_id) VALUES ('F0', 'final0');
INSERT INTO assignments (web_id, email_id) VALUES ('F1', 'final1');
COMMIT;
