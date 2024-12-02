# 🔥 Fire Detection Using AI

This project leverages Artificial Intelligence (AI) to detect fires in real-time using image processing and deep learning. Designed to assist in early fire detection, this solution can help mitigate damage and improve emergency response times.

# 📝 Features

### Real-Time Fire Detection: 
Processes live video streams or images to identify fire occurrences.
### High Accuracy: 
 Uses state-of-the-art AI models for precise fire detection.
### Scalable Deployment: 
Suitable for implementation on drones, surveillance systems, and IoT devices.
### Alerts & Notifications:
Configurable to send real-time alerts via email or SMS.

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

Webcam:  
bash  
Copy code  
python src/detection/detect_realtime.py  
Video File:  
bash  
Copy code  
python src/detection/detect_video.py --video_path /path/to/video.mp4  
Image:  
bash  
Copy code  
python src/detection/detect_image.py --image_path /path/to/image.jpg  


# 🛠️ Technologies Used

Deep Learning Frameworks: TensorFlow, PyTorch  
Image Processing: OpenCV  
Alert System: Twilio API / SMTP  


# 📊 Dataset

This project uses a curated dataset of fire and non-fire images from open-source repositories.

# 📈 Performance Metrics

Accuracy: 95%  
Precision: 94%  
Recall: 96%  


# 🛡️ License

This project is licensed under the MIT License.

# 🤝 Contributing

Contributions are welcome! Please see our CONTRIBUTING.md for guidelines.

# 🌐 Connect

For inquiries, suggestions, or collaborations:

Email: harshsaini00025@gmail.com

LinkedIn: https://www.linkedin.com/in/harsh-saini-bb5583238/
