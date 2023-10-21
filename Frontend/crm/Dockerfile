# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN npm install

# Build the Vue.js app
RUN npm run build

# Expose the port the app runs on
EXPOSE 8080

# Define the command to run your application
CMD ["npm", "run", "serve"]
