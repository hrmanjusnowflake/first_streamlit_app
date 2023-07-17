import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my light is here') 
streamlit.header('it''s a headed') 
streamlit.text('it''s a text') 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.

# Create repeateable code block(called function)
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


streamlit.dataframe(fruits_to_show) 
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_fuction = get_fruitvice_data(fruit_choice)  
    streamlit.dataframe(back_from_fuction)

except URLError as e:
  streamlit.error()
  
# streamlit.write('The user entered ', fruit_choice)



# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 

# write your own comment - what does this do?

# streamlit.stop()


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:-")
#snowflake-releted functions
#def get_fruits_load_list():
 #   with my_cnx.cursor() as my_cur:
  #       my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
   #      return my_cur.fetchall()
        
# Add button to load fruits 
if streamlit.button('Get the Fruits load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruits_load_list()
    streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
         return "Thanks for adding " + new_fruit

Add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to a list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_funtion = insert_row_snowflake(Add_my_fruit)
    streamlit.text(back_from_funtion)

# my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
