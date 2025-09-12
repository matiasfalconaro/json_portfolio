#!/bin/bash

# Variables
IMAGE_NAME="mlfalconaro/portfolio-reflex"
VERSION="1.2.1"  # Incrementa la versión
LATEST_TAG="latest"

# Build de la imagen
echo "Building Docker image..."
docker build -t $IMAGE_NAME:$VERSION -t $IMAGE_NAME:$LATEST_TAG .

# Push de las tags
echo "Pushing version $VERSION..."
docker push $IMAGE_NAME:$VERSION

echo "Pushing latest tag..."
docker push $IMAGE_NAME:$LATEST_TAG

echo "Build and push completed successfully!"
echo "Image: $IMAGE_NAME:$VERSION"
echo "Image: $IMAGE_NAME:$LATEST_TAG"