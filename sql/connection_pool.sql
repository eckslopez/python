CREATE TABLE connection_pool_metrics (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100),
    timestamp TIMESTAMP,
    active_connections INTEGER,
    max_connections INTEGER,
    wait_time_ms INTEGER
);

INSERT INTO connection_pool_metrics (service_name, timestamp, active_connections, max_connections, wait_time_ms) VALUES
('auth-service', '2024-01-15 10:00:00', 8, 10, 250),
('api-gateway', '2024-01-15 10:00:00', 45, 50, 1200),
('db-primary', '2024-01-15 10:00:00', 90, 100, 500),
('cache-redis', '2024-01-15 10:00:00', 15, 100, 100),
('worker-queue', '2024-01-15 10:00:00', 30, 100, 2000);

SELECT
    service_name,
    timestamp,
    active_connections,
    max_connections,
    wait_time_ms
FROM connection_pool_metrics
WHERE (active_connections * 100.0 / max_connections) >= 80
OR wait_time_ms >= 1000
ORDER BY timestamp DESC;