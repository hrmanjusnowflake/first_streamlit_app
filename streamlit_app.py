import streamlit

streamlit.title('my light is here') 
streamlit.header('it''s a headed') 
streamlit.text('it''s a text') 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
