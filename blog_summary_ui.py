# Import required libraries
import streamlit as st  # Alias for Streamlit
import helpers
import llm
from prompts import blog_prompts

# Set the title of the Streamlit web app
st.title("Blog Summary Generator")

# Add a description below the title
st.write("This application summarizes a blog article for you.")

# UI: Text Input for Blog URL
# A text input box where users can input the blog URL they wish to summarize.
# st.text_input(label, value, ...) displays a text input widget with a label and an optional default value.
blog_url = st.text_input("Enter the Blog URL:", "https://")

# UI: Selectbox for Model
# A dropdown box allowing the user to select the language model they wish to use for generating the summary.
# st.selectbox(label, options, ...) displays a select box with a label and a list of options.
selected_model = st.selectbox(
    "Select the Language Model:", ["gpt-3.5-turbo", "text-davinci-002"]
)

# UI: Slider for Number of Points
# A slider to set the range for the minimum and maximum points to include in the summary.
# st.slider(label, min_value, max_value, value, ...) displays a slider with a label and specified min, max, and initial values.
min_points = st.slider(
    "Minimum number of points in summary:", min_value=3, max_value=10, value=5
)
max_points = st.slider(
    "Maximum number of points in summary:", min_value=min_points, max_value=20, value=10
)

# Button to Execute Summarization
# When this button is pressed, the code in the following block will execute.
# st.button(label) displays a button with the given label.
if st.button("Generate Summary"):
    # Fetch the blog article using the 'get_article_from_url' function from helpers
    blog_article = helpers.get_article_from_url(blog_url)

    # Check if the fetched article is empty or not
    if not blog_article:
        st.write("Could not fetch the article. Please check the URL.")
        # Stop execution if the article is empty
        st.stop()

    # Prepare the prompt using the 'blog_bullet_summary_prompt' template from prompts
    prompt = blog_prompts.blog_bullet_summary_prompt.format(
        MaxPoints=max_points, MinPoints=min_points, InputText=blog_article
    )

    # Generate the text summary using the 'llm_generate_text' function from llm
    response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

    # Display the generated summary on the UI
    # st.write(text) writes the text on the UI
    st.write("## Generated Summary:")
    st.write(response)