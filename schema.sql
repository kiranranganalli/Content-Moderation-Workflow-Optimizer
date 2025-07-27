CREATE TABLE moderation_routing (
    content_id INT PRIMARY KEY,
    assigned_to VARCHAR(50),
    cost DECIMAL(5,4),
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);