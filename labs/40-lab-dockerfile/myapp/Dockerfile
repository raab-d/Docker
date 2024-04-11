# Create image with you nodejs image
# (replace zbbfufu by your docker id)
FROM micka98/python:3.10.14-bookworm
# Declare ports listening in the container
EXPOSE 9090
# Define variables
ENV appDir=/app
# Define current working directory (build & run)
WORKDIR ${appDir}
# Specify the maintainer
LABEL maintainer="Mickael <mickael.padonou2@gmail.com>"
# Specify the version of the Dockerfile
LABEL version="1.0"
# Copy all files from “build context” to /app folder
COPY requirement.txt /app
# Build the application
RUN pip install -r requirement.txt
# Declare container startup command and options
CMD ["python", "app.py"]