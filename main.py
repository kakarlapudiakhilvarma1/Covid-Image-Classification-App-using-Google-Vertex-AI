import base64
import streamlit as st
from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")


# Set page configuration
st.set_page_config(
    page_title="Covid Image Classification",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding: 0rem 1rem;
}
.block-container {
    padding: 2rem;
}
.prediction-card {
    background-color: white;
    padding: 1rem;
    border-radius: 5px;
    margin: 0.5rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.stButton>button {
    width: 100%;
    padding: 0.5rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# This function sends an image to Google Vertex AI Endpoint for classification.
def predict_image_classification(
    project: str,
    endpoint_id: str,
    file_content: bytes,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    ## Creates a connection to Google Cloud's AI prediction service.
    client_options = {"api_endpoint": api_endpoint}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    
    # Encodes the image to Base64 format for API compatibility.
    encoded_content = base64.b64encode(file_content).decode("utf-8")
    
    # Creates an instance with the encoded image and Wraps it inside a list to match API format
    instance = predict.instance.ImageClassificationPredictionInstance(
        content=encoded_content,
    ).to_value()    # to_value() → Converts it into a dictionary format for the API.
    instances = [instance]
    
    # Setting Prediction Parameters
    parameters = predict.params.ImageClassificationPredictionParams(
        confidence_threshold=0.5,   # Only return predictions with ≥50% confidence.
        max_predictions=5,          # Limits predictions to 5.
    ).to_value()
    
    # Generates the API URL using the provided Project ID & Endpoint ID.
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    
    # Sending the Request - Sends the image to Google Vertex AI for classification.
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    
    # Returning the Prediction Response
    return response

# Sidebar content
with st.sidebar:
    st.title("🖼️ Covid Dection")
    st.write("Upload an image to see what's in it!")
    
    uploaded_file = st.file_uploader(
        "Choose an image file...", 
        type=['png', 'jpg', 'jpeg'],
        help="Supported formats: PNG, JPG, JPEG"
    )
    
    analyze_button = st.button("🔍 Analyze Image", use_container_width=True)
    
    st.markdown("---")
    st.markdown("Made with ❤️ using Google Cloud AI Platform")

# Main window content
if uploaded_file is not None:
    # Create two columns for the main window
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Display the uploaded image
        st.image(
            uploaded_file,
            caption="Uploaded Image",
            width=300
        )
    
    with col2:
        if analyze_button:
            try:
                with st.spinner("Analyzing..."):
                    file_content = uploaded_file.getvalue()
                    response = predict_image_classification(
                        project=PROJECT_ID,
                        endpoint_id=ENDPOINT_ID,
                        file_content=file_content
                    )
                    
                    # Display predictions
                    st.subheader("Results:")
                    for prediction in response.predictions:
                        pred_dict = dict(prediction)
                        if 'displayNames' in pred_dict and 'confidences' in pred_dict:
                            for name, confidence in zip(
                                pred_dict['displayNames'],
                                pred_dict['confidences']
                            ):
                                confidence_percentage = confidence * 100
                                if confidence_percentage >= 50:
                                    st.markdown(f"""
                                    <div class="prediction-card">
                                        <h3 style='margin: 0; color: #1f77b4;'>🎯 {name}</h3>
                                        <p style='margin: 0.5rem 0 0 0; color: #666;'>
                                            Confidence: {confidence_percentage:.1f}%
                                        </p>
                                    </div>
                                    """, unsafe_allow_html=True)
            
            except Exception as e:
                st.error("😕 Oops! Something went wrong. Please try again.")
else:
    # Show placeholder in main window
    st.markdown("""
    <div style='
        text-align: center;
        padding: 3rem;
        background-color: #f8f9fa;
        border-radius: 10px;
        margin: 2rem 0;
    '>
        <h3 style='color: #666;'>👈 Use the sidebar to upload an image</h3>
    </div>
    """, unsafe_allow_html=True)
