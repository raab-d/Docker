-- Create a basic table for posts in the blog application
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL
);

-- Insert a sample post
INSERT INTO posts (title, content) VALUES ('First Post', 'This is the first post content.');
