DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;
CREATE TABLE tasks (
    uuid BINARY(16) PRIMARY KEY,
    description NVARCHAR(1024),
    completed BOOLEAN
);
CREATE TABLE users (
    uuid BINARY(16) PRIMARY KEY,
    name NVARCHAR(1024)
);
