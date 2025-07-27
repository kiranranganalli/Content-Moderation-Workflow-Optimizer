-- Table for storing processed moderation review data
CREATE TABLE IF NOT EXISTS moderation_reviews (
    timestamp TIMESTAMP,
    content_id VARCHAR(64),
    routed_to VARCHAR(32),
    review_latency INT,
    review_accuracy FLOAT,
    review_cost INT,
    is_accurate BOOLEAN,
    cost_bucket VARCHAR(16)
);

-- Indexes to improve query performance
CREATE INDEX idx_routed_to ON moderation_reviews (routed_to);
CREATE INDEX idx_accuracy ON moderation_reviews (is_accurate);
