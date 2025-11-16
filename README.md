## 🧠 Concrete Crack Detection Using InceptionV3

Crack Detection in Concrete Surfaces Using Deep Learning
This repository contains the clean and optimized TensorFlow/Keras implementation of a crack detection system for concrete structures using the InceptionV3 convolutional neural network. The model is trained to classify high-resolution images of concrete surfaces as Crack or No-Crack, enabling accurate structural health monitoring for bridges, buildings, and civil infrastructure.

The system is based on concepts from
“Deep Learning-Based Crack Damage Detection Using Convolutional Neural Networks”,
but upgraded with transfer learning, improved preprocessing, and a lightweight inference pipeline suitable for Jetson Nano ,Raspberry Pi, Edge devices, and real-time monitoring systems.

---

## 📌 Features

- ✔ Transfer learning with *InceptionV3*
- ✔ High accuracy crack / no-crack classification
- ✔ Preprocessed dataset with data augmentation
- ✔ Exportable model (.h5 and TFLite)
- ✔ Ready for *real-time deployment*
- ✔ Lightweight inference script included

---

## 📦 Dependencies required

TensorFlow/Keras, SimpleITK, Dataset - The dataset can be downloaded or use the dataset using Kaggle api keys from this link- https://www.kaggle.com/datasets/arunrk7/surface-crack-detection

---

## 📊 Dataset

Surface Crack Detection Dataset

Context
Concrete surface cracks are major defect in civil structures. Building Inspection which is done for the evaluation of rigidity and tensile strength of the building. Crack detection plays a major role in the building inspection, finding the cracks and determining the building health.

Content
The datasets contains images of various concrete surfaces with and without crack. The image data are divided into two as negative (without crack) and positive (with crack) in separate folder for image classification. Each class has 20000images with a total of 40000 images with 227 x 227 pixels with RGB channels. The dataset is generated from 458 high-resolution images (4032x3024 pixel) with the method proposed by Zhang et al (2016). High resolution images found out to have high variance in terms of surface finish and illumination condition. No data augmentation in terms of random rotation or flipping or tilting is applied.

Acknowledgements
This dataset is taken from the website Mendeley Data - Crack Detection, contributed by Çağlar Fırat Özgenel.

---
## 🔖 How to download the model

Download and Use the Model

The crack detection model (crack_detection.h5) is a large file stored on Hugging Face.

How to download the model

Run the Python script (download_model.py) in Colab or any Python environment you prefer.
This script will automatically download the model file from Hugging Face.

The download_model.py script also shows how to load the model after downloading.





