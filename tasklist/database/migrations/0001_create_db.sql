DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    uuid BINARY(16) PRIMARY KEY,
    nome NVARCHAR(1024)
);

CREATE TABLE tasks (
    uuid BINARY(16) PRIMARY KEY,
    description NVARCHAR(1024),
    completed BOOLEAN,
    user_id BINARY(16) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(uuid)
);
