# Use the official PostgreSQL image from the Docker Hub
FROM postgres:13-alpine

# Set environment variables
ENV POSTGRES_DB=blogdb
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=secret

# Copy initialization scripts
COPY init /docker-entrypoint-initdb.d/
