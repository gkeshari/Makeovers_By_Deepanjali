
import streamlit as st
from PIL import Image
import time

# Set page config
st.set_page_config(page_title="Makeovers_By_Deepanjali", page_icon="💄", layout="wide")

# Custom CSS for enhanced aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #FFF0F5;
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        color: #FF69B4;
        border-color: #FF69B4;
        border-radius: 30px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }
    h1, h2, h3 {
        color: #C71585;
    }
    .st-expander {
        border-radius: 20px;
        border: 1px solid #FF69B4;
        background-color: #ffe6f7;
    }
    .st-expander:hover {
        background-color: #fdd7e4;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #FF69B4;
    }
    .stSelectbox, .stDateInput {
        border-radius: 10px;
        border: 2px solid #FF69B4;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("💄 Makeovers_By_Deepanjali")
st.subheader("Professional Makeup Artist")

# About section with a Carousel
st.header("About Me")

# Moved about section to below the images
st.write("""
**Welcome. I'm Deepanjali, your personal beauty alchemist !**  
Let's create your most radiant self together. As a seasoned makeup artist, I specialize in transforming looks for every occasion. My passion lies in enhancing your natural beauty and boosting your confidence. Book your appointment today and let's make your special day unforgettable!
""")

# Initialize session state to avoid infinite loop
if 'carousel_index' not in st.session_state:
    st.session_state.carousel_index = 0

# Carousel Logic
image_files = ['Bridal_1.jpeg', 'Bridal_3.jpeg', 'Bridal_4.jpeg', 'Bridal_5.jpeg', 'Bridal_2.jpeg']

# Get dimensions of Bridal_1.jpeg to use as reference
reference_image = Image.open('Bridal_1.jpeg')
reference_size = reference_image.size  # Get (width, height) of Bridal_1.jpeg

# Resize images to match the reference image size
def resize_to_reference(image, reference_size):
    return image.resize(reference_size)

# Display images horizontally in a moving manner
st.markdown("<h3 style='text-align: center; color: #C71585;'>Happy Clients, Happy Faces</h3>", unsafe_allow_html=True)

# Create 5 columns for displaying images
cols = st.columns(5)

# Display resized images with same dimensions as Bridal_1.jpeg
for i, img_col in enumerate(cols):
    img_index = (st.session_state.carousel_index + i) % len(image_files)  # Loop through images
    image = Image.open(image_files[img_index])
    resized_image = resize_to_reference(image, reference_size)  # Resize image to reference size
    img_col.image(resized_image, use_column_width=True)  # Display resized image

# Update index to shift images for the next cycle
st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(image_files)

# Introduce a time delay before re-rendering
time.sleep(2)  # Adjust delay for smooth carousel effect

# Services section with icons and a grid layout
st.header("Services")
services = {
    "Bridal Makeup": "$250",
    "Special Event Makeup": "$150",
    "Photoshoot Makeup": "$200",
    "Makeup Lesson": "$100/hour"
}



# Create three columns
col1, col2, col3 = st.columns(3)

# Column 1: Bridal, Photoshoot, Party Makeup
with col1:
    st.write("👰 **Bridal Makeup**")
    st.write("📸 **Photoshoot Makeup**")
    st.write("🎉 **Party Makeup**")

# Column 2: Fantasy, SFX, Reception Makeup
with col2:
    st.write("🦄 **Fantasy Makeup**")
    st.write("🎭 **SFX Makeup**")
    st.write("💍 **Reception Makeup**")

# Column 3: Hairstyle, Saree Draping, Mehendi
with col3:
    st.write("💇 **Hairstyle**")
    st.write("👗 **Saree Draping**")
    st.write("🌿 **Mehendi**")


# Contact details with icons
st.header("Contact Me")
st.write("📞 **Phone:** +91-8528048822")
st.write("📧 **Email:** deepanjali.keshari@gmail.com")
st.write("🏠 **Address:** Chinnapanhalli Main Road, Doddanekkundi Ext, Bangalore, 560037")

# FAQ section with expanders
st.header("Frequently Asked Questions")
faq = {
    "What brands do you use?": "I use a variety of high-end brands including PAC, Krylon, Forever52 and MAC.",
    "Do you travel to clients?": "Yes, I offer on-location services to clients",
    "How long does a typical makeup session take?": "A full face of makeup typically takes 60-90 minutes.",
    "Do you offer group discounts?": "Yes, I offer discounts for bridal parties and other group bookings."
}

for question, answer in faq.items():
    with st.expander(f"❓ {question}"):
        st.write(answer)


st.header("Check out my Social Media Handles & Please follow :")
col1, col2 = st.columns(2)
with col1:
    youtube_link = "https://www.youtube.com/@makeovers_by_deepanjali"
    st.markdown(f'<a href="{youtube_link}" target="_blank"><button style="color: #FF69B4; border-color: #FF69B4; border-radius: 30px; padding: 10px 20px; font-size: 16px; font-weight: bold;">🎥 YouTube Channel</button></a>', unsafe_allow_html=True)

with col2:
    instagram_link = "https://www.instagram.com/makeovers_by_deepanjali?igsh=MTNwaW94aWMzbmw1Yg=="
    st.markdown(f'<a href="{instagram_link}" target="_blank"><button style="color: #FF69B4; border-color: #FF69B4; border-radius: 30px; padding: 10px 20px; font-size: 16px; font-weight: bold;">📷 Instagram Profile</button></a>', unsafe_allow_html=True)


# # Booking section with enhanced input fields
# st.header("Book an Appointment")
# name = st.text_input("Name")
# email = st.text_input("Email")
# date = st.date_input("Preferred Date")
# service = st.selectbox("Service", list(services.keys()))

# if st.button("Submit Booking Request"):
#     st.success("Thank you for your booking request. I'll get back to you soon!")

# Create three columns
col1, col2, col3 = st.columns(3)

# Ratings and Feedback Section
st.header("Ratings and Feedback")

# Initialize session state for ratings and feedback if not already present
if 'ratings' not in st.session_state:
    st.session_state.ratings = []
if 'feedback' not in st.session_state:
    st.session_state.feedback = []

# Ratings
rating = st.select_slider("Rate your experience", options=[1, 2, 3, 4, 5], value=5)
if st.button("Submit Rating"):
    st.session_state.ratings.append(rating)
    st.success(f"Thank you for your rating of {rating} stars!")

# Display average rating
if st.session_state.ratings:
    avg_rating = sum(st.session_state.ratings) / len(st.session_state.ratings)
    st.write(f"Average Rating: {avg_rating:.1f} stars")

# Feedback
feedback = st.text_area("Leave your feedback")
if st.button("Submit Feedback"):
    if feedback:
        st.session_state.feedback.append(feedback)
        st.success("Thank you for your feedback!")
    else:
        st.warning("Please enter your feedback before submitting.")

# Display feedback
if st.session_state.feedback:
    st.subheader("Recent Feedback")
    for i, fb in enumerate(reversed(st.session_state.feedback[-5:])):  # Show last 5 feedback entries
        st.text(f"{i+1}. {fb}")

# Footer
st.markdown("---")
st.write("© 2024 Glamour by Deepanjali. All rights reserved.")



