# Object-Detection-Service




---

## Overview

This project focuses on object detection using the YOLOv8 model. The project is structured into two main components:

1. **AI Backend**: Handles AI-related tasks, such as image processing or model inference using **YOLOv8**.
2. **UI Backend**: Manages the user interface or API endpoints for interacting with the AI backend.

The project is containerized using Docker, and the services are orchestrated with `docker-compose`.

---

## Project Structure

```
├── ai_backend/
│   ├── app.py               # AI backend code (YOLOv8 inference)
│   ├── requirements.txt     # Python dependencies for AI backend
│   ├── Dockerfile           # Dockerfile for AI backend
│
├── ui_backend/
│   ├── app.py               # UI backend code
│   ├── requirements.txt     # Python dependencies for UI backend
│   ├── Dockerfile           # Dockerfile for UI backend
│
├── temp/                    # Folder to store input images
├── output/                  # Folder to store output images and JSON files
├── docker-compose.yml       # Orchestrates the two services
├── Documenation.pdf         # Documentation with references 
└── README.md                # Documentation
```

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Python**: Version **3.9** (for local development if not using Docker)

---

## Setup and Running the Project

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Build and Run with Docker Compose

To build and run the project, use the following command:

```bash
docker-compose up --build
```

This will:
- Build the Docker images for the `ai_backend` and `ui_backend`.
- Start the services as defined in `docker-compose.yml`.

### 3. Access the Service



After running the `docker-compose up --build` command, you can access the services via:
- `http://localhost:5000`
  

---

## Folder Descriptions

### `ai_backend/`
- Contains the code for the AI backend, which uses **YOLOv8** for object detection or image processing.
- `app.py`: Entry point for the AI backend.
- `requirements.txt`: Lists the Python dependencies required for the AI backend, including `ultralytics` for YOLOv8.
- `Dockerfile`: Defines the Docker image for the AI backend.

### `ui_backend/`
- Contains the code for the UI backend.
- `app.py`: Entry point for the UI backend.
- `requirements.txt`: Lists the Python dependencies required for the UI backend.
- `Dockerfile`: Defines the Docker image for the UI backend.

### `temp/`
- Storage for input images or files.

### `output/`
- Stores the processed output images with bounding boxes.

### `docker-compose.yml`
- Orchestrates the `ai_backend` and `ui_backend` services.
- Defines how the services interact and which ports to expose.

---

## Python Version

The project is built using **Python 3.9**. Ensure you have the correct version installed if you plan to run the services locally without Docker.

---

## YOLOv8 Integration

The **AI Backend** uses **YOLOv8** for object detection or image processing. Here are some key points about YOLOv8:

### 1. Model File
1. Model Download
The YOLOv8 model (yolov8n.pt) is automatically downloaded when the model is first used.

2. Dependencies
The ultralytics package is required for YOLOv8. It is listed in the `ai_backend/requirements.txt` file.

