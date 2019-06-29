DROP TABLE IF EXISTS members;


CREATE TABLE members (
    name TEXT
);
--初期データの投入
INSERT INTO members
    (name)
VALUES
    ('Bob'),
    ('Tom'),
    ('Ken')
;