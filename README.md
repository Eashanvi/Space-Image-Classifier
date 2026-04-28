# AI-Powered Space Image Classifier

A deep learning-based web application that classifies astronomical images into **Stars** or **Galaxies** using Convolutional Neural Networks (CNN).

---

## Live Demo

Coming Soon, Deployment in Progress

---

## Features

* Classifies space images into **Star** or **Galaxy**
* Deep learning model using CNN
* Real-time prediction via web interface
* Displays prediction confidence
* Clean and interactive UI
* Supports both **Streamlit (local)** and **Gradio (deployment)**

---

## Tech Stack

* Python
* TensorFlow / Keras
* Streamlit
* Gradio
* NumPy
* PIL (Image Processing)

---

## Demo

### Upload Interface

![UI Screenshot 1](screenshots/ui1.png)

### Prediction Output

![UI Screenshot 2](screenshots/ui2.png)

---

## How to Run

### Run Streamlit (Local)

```bash
streamlit run streamlit_app.py
```

---

### Run Gradio (Local)

```bash
python app.py
```

---

## Model Details

* Input size: 128 × 128 images
* Architecture: Convolutional Neural Network (CNN)
* Data Augmentation: Applied (flip, rotation, zoom)
* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy

---

## Limitations

* Dataset is imbalanced (more stars than galaxies)
* Model may misclassify faint galaxies as stars
* Performance depends on image quality

---

## Future Improvements

* Use Transfer Learning (MobileNet / ResNet)
* Improve dataset balance
* Add more space object categories
* Deploy with GPU support

---

## App Versions

* **Gradio App (Hugging Face Deployment):** `app.py`
* **Streamlit App (Local UI):** `streamlit_app.py`

---

## Author

**Eashanvi**
