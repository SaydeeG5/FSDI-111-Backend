-- Create task table 

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

--Dummy data

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash the car",
    "Take the car to the car wash or DIY"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Make or buy dinner",
    "Prepare a mean for the family or order pizza"
);