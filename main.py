import streamlit as st
from few_shots import FewShotPosts
from genrated_posts import genrateposts
import base64
import json


def Streamlit_app():
    
    # Set the background image
    set_background("assets\R.jpg")  # Make sure this path is correct
    
    st.title("Customized Post Generator🔥") 
    
    # Add a container with semi-transparent background
    col1,col2,col3=st.columns(3)
    fs=FewShotPosts()
    with col1: 
            selected_tag = st.selectbox("Title",options=fs.get_tags())
    with col2:
            selected_language = st.selectbox("Language", options=["English","Hinglish"])
    with col3:
            selected_length = st.selectbox("Length", options=["short","Medium","Long"])
            
    if st.button("Generate"):
            try:
                # Load preprocessed posts to check combinations
                with open("data/preprocessed_posts.json", "r") as f:
                    preprocessed_posts = json.load(f)
                
                # Check if combination exists
                valid_combination = any(
                    post.get('tag') == selected_tag or
                    post.get('language') == selected_language or
                    post.get('length') == selected_length
                    
                    for post in preprocessed_posts
                )
                
                if valid_combination:
                    post = genrateposts(selected_length, selected_language, selected_tag)
                    # print(post)
                    st.markdown(
                        f"""
                        <div style="background-color: black; 
                                    padding:20px;
                                    border-radius: 10px; 
                                    margin: 10px 0;">
                            {post}
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("Please select a valid combination of tag, language, and length")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                
def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-
    }}
    

    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
if __name__ == "__main__":
    st.set_page_config(page_title="Post Generator", page_icon="📢")
    Streamlit_app()