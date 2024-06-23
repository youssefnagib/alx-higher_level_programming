USE `hbtn_0c_0`;

-- Create the temperatures table
CREATE TABLE IF NOT EXISTS temperatures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    temperature FLOAT NOT NULL,
    recorded_at DATE NOT NULL
);

-- Insert sample data into the temperatures table
INSERT INTO temperatures (city, temperature, recorded_at) VALUES
('Chandler', 72.9, '2024-01-01'),
('Gilbert', 71.8, '2024-01-01'),
('Pismo beach', 71.5, '2024-01-01'),
('San Francisco', 71.5, '2024-01-01'),
('Sedona', 70.8, '2024-01-01'),
('Phoenix', 70.6, '2024-01-01'),
('Oakland', 70.6, '2024-01-01'),
('Sunnyvale', 70.5, '2024-01-01'),
('Chicago', 70.4, '2024-01-01'),
('San Diego', 70.1, '2024-01-01'),
('Glendale', 70.1, '2024-01-01'),
('Sonoma', 70.0, '2024-01-01'),
('Yuma', 69.4, '2024-01-01'),
('San Jose', 69.3, '2024-01-01'),
('Tucson', 69.0, '2024-01-01'),
('Joliet', 68.7, '2024-01-01'),
('Naperville', 68.1, '2024-01-01'),
('Tempe', 67.0, '2024-01-01'),
('Peoria', 66.5, '2024-01-01');