from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model

# Download the model file and get the local path
model_path = hf_hub_download(
    repo_id="vikram-47/crack_detection",
    filename="crack_detection.h5"
)

# Load the model
model = load_model(model_path)

print("Model loaded successfully!")
