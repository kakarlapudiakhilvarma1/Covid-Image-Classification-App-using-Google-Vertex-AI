# Covid-Image-Classification-App-using-Google-Vertex-AI

A Streamlit web application that uses Google Cloud Vertex AI to classify chest X-ray images for COVID-19 detection. The application provides a user-friendly interface for medical professionals to upload X-ray images and get instant predictions with confidence scores.

## Features

- Simple and intuitive user interface
- Real-time image classification
- Confidence score display for predictions
- Support for multiple image formats (PNG, JPG, JPEG)
- Responsive design that works on both desktop and mobile devices

## Prerequisites

Before running this application, you need to:

1. Have a Google Cloud Platform (GCP) account
2. Set up Google Cloud CLI and authentication:
   - Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
   - Run `gcloud init` to initialize the SDK
   - Run `gcloud auth application-default login` to set up local authentication
3. Have Python 3.7+ installed
4. Enable the following Google Cloud APIs:
   - Vertex AI API
   - Cloud Storage API

## Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/kakarlapudiakhilvarma1/Covid-Image-Classification-App-using-Google-Vertex-AI.git
cd covid-image-classification-app-using-google-vertex-ai
```

2. Create and activate a virtual environment:
```bash
conda create -p myenv python==3.10 -y
conda activate myenv/   
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Google Cloud credentials:
```
PROJECT_ID=your-project-id    # Google Cloud project ID
ENDPOINT_ID=your-endpoint-id  # The unique ID of the Vertex AI endpoint
```

## Running the Application

1. Start the Streamlit server:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Screenshots

Covid
![image](https://github.com/user-attachments/assets/ec5131e5-2a86-4c2e-b8d0-fa9e003d26f2)
--
![image](https://github.com/user-attachments/assets/3337dba3-d6c0-4119-8b70-179a5a3a3fcd)

Normal
![image](https://github.com/user-attachments/assets/ebadf2ca-8759-43b0-989f-0642bea982f6)
---
![image](https://github.com/user-attachments/assets/68038a45-ec1b-4fa5-b5a6-41833ab94aa8)


## Project Structure

```
covid-xray-classifier/
├── app.py                  # Main Streamlit application
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Requirements

```
streamlit==1.x.x
google-cloud-aiplatform==x.x.x
python-dotenv==x.x.x
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Cloud Platform for providing the Vertex AI services
- Streamlit for the awesome web application framework
- The Kaggle community for providing the training data

## Support

If you encounter any problems or have suggestions, please open an issue in the GitHub repository.
