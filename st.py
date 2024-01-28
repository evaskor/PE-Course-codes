import streamlit as st

st.title('My First Streamlit App')

# User input
user_name = st.text_input("Enter your name", "Type Here")

# Displaying input
if st.button("Greet"):
    st.write(f"Hello, {user_name}!")

# Chart
chart_data = {
    'Days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    'Productivity': [50, 60, 55, 67, 80]
}
st.bar_chart(chart_data)

st.title('Your Title Here')
st.header('Your Header Here')
st.subheader('Your Subheader Here')
st.text('Some text here')
st.write('This can display text, dataframes, etc.')
st.image('https://gitano.org/wp-content/uploads/2022/08/cropped-gitano-coaching.jpg', caption='GitanoWeb', use_column_width=False)