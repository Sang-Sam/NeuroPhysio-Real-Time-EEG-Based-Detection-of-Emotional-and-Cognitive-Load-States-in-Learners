<!-- ⚠️ Note: The complete implementation is currently under review for a publication and will be made public after acceptance.
 -->


# NeuroPhysio: Real-Time EEG-Based Detection of Emotional and Cognitive Load States in Learners

## Project Overview
This research project develops an innovative system for real-time monitoring and classification of learners' emotional(Anxiety, Confusion, Frustration) and cognitive states(Low, Medium, High) using EEG signals. The system aims to enhance educational experiences by providing insights into students' mental states during learning activities.

## Key Components

### 1. Data Collection & Processing
- Custom EEG dataset collected from college students
- Multiple EEG channels processed for feature extraction
- Signal preprocessing including noise reduction and artifact removal
- Temporal and frequency domain feature extraction

### 2. Machine Learning Models
#### Emotion Detection
- CNN architecture for spatial feature learning
- LSTM networks for temporal dependencies
- Conformer model combining transformer and convolution capabilities
- XGBoost implementation for comparative analysis

#### Cognitive Load Detection
- Specialized neural networks for cognitive load classification
- Gender-specific model variations
- Real-time processing capabilities

### 3. Feature Analysis
- Comprehensive feature extraction pipeline
- Data augmentation techniques
- Normalized feature sets for improved model performance
- Gender-specific feature analysis

### 4. Implementation Details
- Python-based backend implementation
- Web interface using Gradio for demonstrations
- Real-time signal processing capabilities
- Support for EDF file format processing

## Technical Specifications
### Dependencies
- Python 3.8+
- TensorFlow/Keras for deep learning models
- XGBoost for gradient boosting
- MNE-Python for EEG signal processing
- Gradio for web interface

### Architecture
- Modular design for easy integration
- Separate modules for:
  - Signal preprocessing
  - Feature extraction
  - Model training
  - Real-time prediction
  - Web visualization

## Research Context
This work was conducted as part of a BTech Final Year Project at [NIT Trichy]. The project demonstrates:
- Novel approaches to EEG-based emotion recognition
- Real-time cognitive load assessment
- Gender-specific variations in EEG patterns
- Integration of multiple deep learning architectures

## Future Integration
While currently implemented with a web interface for demonstration purposes, the system is designed for:
- Integration with commercial EEG devices
- Real-time monitoring in classroom settings
- Adaptive learning systems
- Educational technology platforms

## Data Privacy Notice
The EEG dataset used in this project contains sensitive biometric information and was collected with proper consent for research purposes. To maintain privacy and ethical considerations:
- Raw EEG data is not included in the repository
- Data collection protocols followed institutional guidelines
- All personal information has been anonymized

## Publication & Usage Rights
- This research work is protected under academic guidelines
- Implementation details may be subject to future publication
- Commercial use requires explicit permission


## Contact
For research collaboration inquiries, please contact through appropriate institutional channels.

## Overview
This project implements a real-time system for detecting emotional and cognitive load states in learners using EEG signals. The system utilizes various deep learning models (CNN, LSTM, Conformer) and machine learning techniques to classify emotional states and cognitive load levels from EEG data.

## Features
- Real-time EEG signal processing and feature extraction
- Multiple neural network architectures for classification:
  - CNN (Convolutional Neural Network)
  - LSTM (Long Short-Term Memory)
  - Conformer (Transformer-based architecture)
- Gender-specific analysis and modeling
- Web interface for demonstration and visualization
- Support for both emotional state and cognitive load detection

## Project Structure
- `Cognition_code/`: Implementation of cognitive load detection models
- `Emotion_code/`: Implementation of emotion detection models
- `Feature wise/`: Feature extraction and analysis
- `GenderWise/`: Gender-specific model implementations
- `website/`: Web interface for demonstration

## Important Note
The EEG dataset used in this project was collected privately for research purposes and contains sensitive information. Therefore, the raw EEG data files are not included in this repository. The models and code are shared for research and educational purposes only.

## Research Context
This work was conducted as part of a Final Year Project (FYP) in collaboration with academic research initiatives. The system is designed for future integration with EEG hardware devices for real-time monitoring and analysis in learning environments.

## Technical Implementation
- Python-based implementation using modern deep learning frameworks
- Feature extraction using advanced signal processing techniques
- Real-time signal processing capabilities
- Modular architecture for easy integration with EEG hardware

## Purpose
This project demonstrates the potential of using EEG signals for understanding and improving learning experiences through real-time emotional and cognitive load monitoring. The web interface serves as a proof-of-concept demonstration for academic review purposes.

## License
This project is for research and educational purposes only. All rights reserved.