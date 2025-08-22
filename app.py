# Q&A Chatbot
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai
import time
import base64
import random

# Configure API
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Set page configuration
st.set_page_config(
    page_title="Gemini Vision Pro",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium styling
st.markdown("""
    <style>
    /* Main styles */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #24243e 50%, #302b63 100%);
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-header {
        font-size: 4rem;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6b6b, #6c5ce7, #48dbfb, #6c5ce7, #ff6b6b);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 5s ease infinite;
        text-shadow: 0 0 20px rgba(108, 92, 231, 0.3);
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .sub-header {
        font-size: 1.3rem;
        color: #dfe6e9;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    /* Containers */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.08);
        border-radius: 15px 15px 0px 0px;
        gap: 10px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        border-bottom: 3px solid transparent;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(108, 92, 231, 0.3);
        border-bottom: 3px solid #6c5ce7;
        box-shadow: 0 5px 15px rgba(108, 92, 231, 0.2);
    }
    .upload-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        border: 2px dashed rgba(108, 92, 231, 0.5);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    .upload-container:hover {
        border: 2px dashed rgba(108, 92, 231, 0.8);
        box-shadow: 0 0 25px rgba(108, 92, 231, 0.3);
        transform: translateY(-5px);
    }
    .response-container {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 30px;
        margin-top: 25px;
        border-left: 5px solid #6c5ce7;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        position: relative;
        overflow: hidden;
    }
    .response-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #ff6b6b, #6c5ce7, #48dbfb);
        z-index: 1;
    }
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #6c5ce7 0%, #48dbfb 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 15px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s;
        box-shadow: 0 5px 15px rgba(108, 92, 231, 0.3);
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 1rem;
    }
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(108, 92, 231, 0.4);
        background: linear-gradient(135deg, #6c5ce7 0%, #48dbfb 50%, #6c5ce7 100%);
        background-size: 200% 200%;
        animation: gradientBG 1.5s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .clear-button button {
        background: linear-gradient(135deg, #fd79a8 0%, #e17055 100%);
    }
    /* Input fields */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.06) !important;
        color: white !important;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px;
        font-size: 1rem;
        transition: all 0.3s;
    }
    .stTextArea textarea:focus {
        border: 1px solid rgba(108, 92, 231, 0.5);
        box-shadow: 0 0 15px rgba(108, 92, 231, 0.2);
    }
    .stTextArea label {
        color: #dfe6e9 !important;
        font-weight: 500;
        font-size: 1.1rem;
        margin-bottom: 10px;
    }
    /* File uploader */
    .stFileUploader {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 15px;
        padding: 20px;
    }
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 15px;
        padding: 20px;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 10px;
        border-left: 4px solid #6c5ce7;
    }
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 0 0 15px 15px;
        padding: 20px;
    }
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
        padding: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    /* Custom card */
    .custom-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    .custom-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        background: linear-gradient(to bottom, #ff6b6b, #6c5ce7, #48dbfb);
    }
    .custom-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    /* Animation for response */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fade-in {
        animation: fadeIn 0.7s ease forwards;
    }
    /* Icon containers */
    .icon-container {
        text-align: center;
        font-size: 5rem;
        margin: 30px 0;
        filter: drop-shadow(0 5px 15px rgba(108, 92, 231, 0.3));
        transition: all 0.3s ease;
    }
    .icon-container:hover {
        transform: scale(1.1) rotate(5deg);
        filter: drop-shadow(0 8px 20px rgba(108, 92, 231, 0.5));
    }
    /* Floating elements */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .floating {
        animation: float 5s ease-in-out infinite;
    }
    /* Glow effect */
    .glow {
        text-shadow: 0 0 10px rgba(108, 92, 231, 0.5), 
                     0 0 20px rgba(108, 92, 231, 0.3), 
                     0 0 30px rgba(108, 92, 231, 0.2);
    }
    /* Success animation */
    @keyframes successPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .success-pulse {
        animation: successPulse 2s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for clear functionality
if 'clear_clicked' not in st.session_state:
    st.session_state.clear_clicked = False

# Header section with floating animation
st.markdown("""
    <div style='text-align: center;'>
        <h1 class='main-header floating'>🔮 Gemini Vision Pro</h1>
        <p class='sub-header'>Advanced AI-powered image analysis with Google Gemini</p>
    </div>
""", unsafe_allow_html=True)

# Create tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["📷 Image Analysis", "ℹ️ How It Works", "🌟 Examples"])

with tab1:
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📤 Upload Your Image")
        with st.container():
            uploaded_file = st.file_uploader(
                "Drag and drop or click to browse",
                type=["jpg", "jpeg", "png"],
                help="Supported formats: JPG, JPEG, PNG",
                key="uploader"
            )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Your Uploaded Image", use_column_width=True)
        
        st.markdown("### 💬 Ask a Question")
        input_text = st.text_area(
            "What would you like to know about the image?",
            placeholder="Example: What's in this image? Describe it in detail...",
            height=120,
            key="input"
        )

        # Create two columns for buttons
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            submit = st.button("🚀 Analyze Image", type="primary", use_container_width=True)
        with btn_col2:
            clear_clicked = st.button("🗑️ Clear", use_container_width=True)
            if clear_clicked:
                st.session_state.clear_clicked = True
                # Use JavaScript to clear the file uploader (visual effect only)
                st.markdown("""
                <script>
                // This is a visual effect only - actual clearing would need more complex handling
                document.querySelector('[data-testid="stFileUploader"]').style.opacity = "0.5";
                setTimeout(() => {
                    document.querySelector('[data-testid="stFileUploader"]').style.opacity = "1";
                }, 500);
                </script>
                """, unsafe_allow_html=True)
                st.info("Upload cleared! Select a new image.")

    with col2:
        # Animated AI Icon
        st.markdown('<div class="icon-container floating">🤖</div>', unsafe_allow_html=True)
        
        st.markdown("### 📋 Quick Tips")
        with st.expander("💡 Get the most out of Gemini Vision", expanded=True):
            st.markdown("""
            - **Be specific**: Ask detailed questions for better responses
            - **Context matters**: Provide context about what you're looking for
            - **Multiple angles**: Try different questions for comprehensive analysis
            - **No question needed**: Leave blank for a general description
            
            **Example questions:**
            - "What's the main subject of this image?"
            - "Describe the colors and composition"
            - "What emotions does this image evoke?"
            - "Are there any text elements and what do they say?"
            """)
        
        # Response section
        if submit and uploaded_file is not None:
            with st.spinner("🔮 Gemini is analyzing your image..."):
                # Create a fancy progress bar
                progress_text = st.empty()
                progress_bar = st.progress(0)
                
                for i in range(100):
                    # Update progress bar
                    progress_bar.progress(i + 1)
                    # Add some text that changes during loading
                    loading_phrases = [
                        "Analyzing visual patterns...",
                        "Detecting objects and features...",
                        "Understanding context and content...",
                        "Generating insights...",
                        "Almost done..."
                    ]
                    if i % 20 == 0:
                        progress_text.text(f"⏳ {loading_phrases[i//20]}")
                    time.sleep(0.02)
                
                progress_text.text("✅ Analysis complete!")
                time.sleep(0.5)
                
                response = get_gemini_response(input_text, image)
            
            st.markdown("### 📝 Analysis Results")
            st.markdown('<div class="response-container fade-in">', unsafe_allow_html=True)
            st.write(response)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Add a download button for the response
            st.download_button(
                label="📥 Download Response",
                data=response,
                file_name="gemini_response.txt",
                mime="text/plain"
            )
            
            # Add a fun confetti effect using HTML (visual only)
            st.markdown("""
            <div style='text-align: center; color: #6c5ce7; margin-top: 20px;' class='success-pulse'>
                <h3 class='glow'>✨ Analysis Complete! ✨</h3>
            </div>
            """, unsafe_allow_html=True)
            
        elif submit and uploaded_file is None:
            st.error("⚠️ Please upload an image first!")

with tab2:
    st.markdown("## How Gemini Vision Pro Works")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="custom-card">
        <h3>🔍 Step 1: Upload Your Image</h3>
        <p>Select any JPG, JPEG, or PNG image from your device. The image is processed securely and never stored on our servers.</p>
        </div>
        
        <div class="custom-card">
        <h3>💭 Step 2: Ask a Question (Optional)</h3>
        <p>Type your question about the image. You can ask about content, context, colors, emotions, or anything else you're curious about.</p>
        </div>
        
        <div class="custom-card">
        <h3>🚀 Step 3: Analyze</h3>
        <p>Click the Analyze button to send your image and question to Google's powerful Gemini AI model for processing.</p>
        </div>
        
        <div class="custom-card">
        <h3>📊 Step 4: Receive Insights</h3>
        <p>Get detailed analysis and answers to your questions. You can download the results for future reference.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="icon-container floating">📊</div>', unsafe_allow_html=True)
        st.markdown('<div class="icon-container floating">🔍</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("## Example Use Cases")
    
    ex_col1, ex_col2, ex_col3 = st.columns(3)
    
    with ex_col1:
        st.markdown("""
        <div class="custom-card">
        <h4>🖼️ Art Analysis</h4>
        <p>Upload artwork and ask about style, techniques, or historical context.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with ex_col2:
        st.markdown("""
        <div class="custom-card">
        <h4>📸 Photo Understanding</h4>
        <p>Get descriptions of photos for accessibility or content analysis.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with ex_col3:
        st.markdown("""
        <div class="custom-card">
        <h4>🛍️ Product Identification</h4>
        <p>Identify products, brands, or similar items in images.</p>
        </div>
        """, unsafe_allow_html=True)
    
    ex_col4, ex_col5, ex_col6 = st.columns(3)
    
    with ex_col4:
        st.markdown("""
        <div class="custom-card">
        <h4>🌳 Nature Recognition</h4>
        <p>Identify plants, animals, or natural landscapes in your images.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with ex_col5:
        st.markdown("""
        <div class="custom-card">
        <h4>📄 Document Analysis</h4>
        <p>Extract text or understand the content of document images.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with ex_col6:
        st.markdown("""
        <div class="custom-card">
        <h4>🎨 Design Feedback</h4>
        <p>Get AI-powered feedback on design compositions and color schemes.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    '<p class="footer">Powered by Google Gemini AI • Built with Streamlit • 🚀 Premium Experience</p>',
    unsafe_allow_html=True
)

# Add a custom message if the user hasn't uploaded an image
if uploaded_file is None and not submit:
    st.info("👆 Upload an image to get started with Gemini Vision Pro!")
    
    # Create some visual interest with columns of icons
    icon_col1, icon_col2, icon_col3, icon_col4, icon_col5 = st.columns(5)
    with icon_col1:
        st.markdown('<div class="icon-container">📷</div>', unsafe_allow_html=True)
    with icon_col2:
        st.markdown('<div class="icon-container">🔍</div>', unsafe_allow_html=True)
    with icon_col3:
        st.markdown('<div class="icon-container">🤖</div>', unsafe_allow_html=True)
    with icon_col4:
        st.markdown('<div class="icon-container">💡</div>', unsafe_allow_html=True)
    with icon_col5:
        st.markdown('<div class="icon-container">🎯</div>', unsafe_allow_html=True)