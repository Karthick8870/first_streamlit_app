import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥪 Dosa')
streamlit.text('🥫 Masal Dosa')
streamlit.text('🥗 Idli')
streamlit.text('🥙 Poori')
streamlit.text('🌮 Pongal')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
