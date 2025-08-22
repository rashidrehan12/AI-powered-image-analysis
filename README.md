# Gemini Vision Pro 🔮

An advanced AI-powered image analysis application that leverages Google's Gemini multimodal AI to understand and describe image content through conversational interactions.

![GitHub last commit](https://img.shields.io/github/last-commit/your-username/gemini-vision-pro)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0%2B-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **Multimodal AI Analysis**: Utilizes Google's Gemini AI to process and understand both images and text prompts
- **Interactive Q&A**: Ask specific questions about uploaded images and receive detailed, contextual answers
- **Premium UI/UX**: Sophisticated dark theme with glassmorphism effects and smooth animations
- **Real-time Processing**: Visual feedback with animated progress indicators during analysis
- **Response Export**: Download AI-generated analysis as text files
- **Fully Responsive**: Works seamlessly across desktop and mobile devices

## 🚀 Demo

[![Live Demo](https://img.shields.io/badge/Streamlit-Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit)](https://ai-powered-image-analysis.streamlit.app/)

Check out the live application to experience Gemini Vision Pro in action!


## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/AI-powered-image-analysis.git
cd AI-powered-image-analysis
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your Google API key: `GOOGLE_API_KEY=your_api_key_here`

4. Run the application:
```bash
streamlit run app.py
```

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key
- Streamlit

## 🔧 Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Google Gemini API** - Multimodal AI processing
- **Pillow (PIL)** - Image processing
- **Custom CSS** - Premium UI styling and animations

## 🎯 How to Use

1. **Upload an Image**: Click on the uploader to select a JPG, JPEG, or PNG file
2. **Ask a Question** (Optional): Type your question about the image in the text area
3. **Analyze**: Click the "Analyze Image" button to process your request
4. **Review Results**: View the AI-generated analysis and download if desired

## 💡 Use Cases

- **Accessibility**: Help visually impaired users understand image content
- **Education**: Learn about objects, scenes, or artistic elements within images
- **Content Analysis**: Extract information from complex images or documents
- **Research**: Quickly analyze visual data and receive contextual information
- **Creative Inspiration**: Generate descriptive narratives from visual content

## 🔍 Project Structure

```
AI-powered-image-analysis/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── assets/               # Static assets (optional)
└── README.md             # Project documentation
```

## 🚀 Deployment

### Streamlit Cloud Deployment

1. Fork this repository
2. Create a new app at [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to `app.py`
5. Add your `GOOGLE_API_KEY` as a secret in the advanced settings

### Local Deployment

Follow the installation steps above to run the application locally.

## 📝 API Key Setup

To use Gemini Vision Pro, you need a Google Gemini API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add the key to your `.env` file as `GOOGLE_API_KEY=your_actual_key_here`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini team for the powerful multimodal AI
- Streamlit team for the excellent web framework
- Contributors and testers who helped refine the application

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact me at rashidrehan122000@gmail.com.

---

<div align="center">
Made with ❤️ and ☕ by Md Rashid
</div>
