## Project Overview

Sign Language Detection is a deep learning-based project that aims to recognize and interpret sign language gestures. The system processes images and live camera feeds to identify hand signs using a YOLOv5 object detection model.

### 📌 Features

✅ **Data Collection & Annotation**

- Image collection using a custom data collector module.
- Annotation with `labelImg`.

✅ **Pipeline**

1. **Data Ingestion**: Retrieve data from GitHub or Google Drive.
2. **Data Validation**: Ensure proper format and structure.
3. **Model Training**: Train a YOLOv5 model on labeled images.
4. **Deployment**:
   - **CI/CD automation** using **GitHub Actions**.
   - Deploy to **AWS EC2** using **Docker** and **AWS ECR**.

### 📂 Workflows :

1. **constants**
2. **config_entity**
3. **artifact_entity**
4. **components**
5. **pipeline**
6. **app.py**

### 🛠️ Technologies Used

- **Deep Learning**: YOLOv5
- **Frameworks**: Flask, OpenCV, PyTorch
- **Cloud**: AWS EC2, AWS ECR
- **DevOps**: Docker, GitHub Actions
