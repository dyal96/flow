# Use a lightweight Nginx image
FROM nginx:alpine

# Copy the HTML file to the Nginx default directory
COPY index.html /usr/share/nginx/html/index.html

# Copy local assets if they exist (for the offline version)
# If using index - online.html, you can rename it to index.html before building
COPY assets /usr/share/nginx/html/assets

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
