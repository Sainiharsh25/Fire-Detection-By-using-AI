# 🔥 Fire Detection Using AI

This project leverages Artificial Intelligence (AI) to detect fires in real-time using image processing and deep learning. Designed to assist in early fire detection, this solution can help mitigate damage and improve emergency response times.

# 📝 Features
- Real-time fire detection from video feeds
- Fire detection from static images
- High accuracy using deep learning models
- Easy integration with IoT systems for alerts
- Scalable and customizable
## Technologies Used

### Frameworks and Libraries
- Python
- TensorFlow / PyTorch (Choose based on implementation)
- OpenCV (for image and video processing)
- NumPy
- Flask/Django (for web interface)

### Models
- Pre-trained Convolutional Neural Networks (CNN) such as:
  - ResNet
  - MobileNet
  - EfficientNet

### Optional Tools
- Docker (for containerization)
- AWS/GCP (for cloud deployment)

## Installation

### Prerequisites

Ensure the following are installed on your machine:

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fire-detection-ai.git
   cd fire-detection-ai
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download pre-trained model weights:
   - Place them in the `models/` directory.

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000` to access the interface.

# 📂 Project Structure

fire-detection-ai/  
├── data/              # Dataset for training and testing  
├── models/            # Pre-trained and custom AI models  
├── src/               # Source code for the application  
│   ├── preprocessing/ # Image processing utilities  
│   ├── training/      # Model training scripts  
│   └── detection/     # Fire detection algorithms  
├── requirements.txt   # Python dependencies  
├── README.md          # Project documentation  
└── LICENSE            # License information  


# 🚀 Getting Started

Prerequisites  
Python 3.8+  
Install dependencies:  
bash  
Copy code  
pip install -r requirements.txt  
Installation  
Clone the repository:  
bash  
Copy code  
git clone https://github.com/Sainiharsh25/fire-detection-ai.git  
cd fire-detection-ai  
Set up your environment:  
Configure your dataset path in config.py.  
(Optional) Update alert settings in alerts_config.json.  


# 🧠 Model Training

Place your dataset in the data/ directory.  
Start training:  
bash  
Copy code  
python src/training/train_model.py  
The trained model will be saved in the models/ directory.  


# ⚡ Real-Time Detection

Run the detection script with your preferred input source:  

- Webcam:  
-- bash  
-- Copy code  
-- python src/detection/detect_realtime.py  
- Video File:  
-- bash  
-- Copy code  
-- python src/detection/detect_video.py --video_path /path/to/video.mp4  
- Image:  
-- bash  
Copy code  
python src/detection/detect_image.py --image_path /path/to/image.jpg  


# 🛠️ Technologies Used

- Deep Learning Frameworks: TensorFlow, PyTorch  
- Image Processing: OpenCV  
- Alert System: Twilio API / SMTP  


# 📊 Dataset

This project uses a curated dataset of fire and non-fire images from open-source repositories.

# 📈 Performance Metrics

- Accuracy: 95%  
- Precision: 94%  
- Recall: 96%  

## Usage

### Detect Fire in Images
1. Upload an image through the web interface.
2. The system will analyze the image and highlight fire regions, if any.

### Real-time Video Detection
1. Connect your webcam or provide a video file.
2. The system will process the video frame-by-frame to detect fire.

## Screenshots

Include images of your application. Example:

![Image Fire Detection](https://via.placeholder.com/800x400)
![Real-time Detection](https://via.placeholder.com/800x400)

## Dataset

- Use public fire datasets like [Fire Dataset](https://www.kaggle.com/)
- Ensure proper preprocessing (resizing, normalization, etc.)

## Future Enhancements

- Integrate with IoT devices for automated alerts
- Implement smoke detection for early fire warnings
- Add multi-class classification (e.g., fire intensity levels)
- Deploy the system to cloud platforms for scalability

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

# 🛡️ License

This project is licensed under the MIT License.

# 🤝 Contributing

Contributions are welcome! Please see our CONTRIBUTING.md for guidelines.

# 🌐 Connect

For inquiries, suggestions, or collaborations:

Email: harshsaini00025@gmail.com

LinkedIn: https://www.linkedin.com/in/harsh-saini-bb5583238/
