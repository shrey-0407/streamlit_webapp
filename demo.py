from doctest import Example
import streamlit as st
from pymongo import MongoClient

# import logging
# from streamlit.server.server import Server
# import httpx

# def handle_balloons(args):
#     return f"🎈 BALLOONS: {args}"

# Server.get_current().add_api_route('balloons', handle_balloons)

# result = httpx.get('http://localhost:8501/api/balloons')
# st.write(result)
# st.write(result.text)






##########LOGGING PART###############
# logging.basicConfig(filename='example.log')
# logging.debug('This message should go to the log file')

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Get user input
num1 = st.number_input("Enter a number: ")
num2 = st.number_input("Enter another number: ")



# Save data to MongoDB and doing particular operations
col1, col2, col3,col4 = st.columns(4)
with col1:
    if st.button("ADD"):
        
            try:
                if num1!=0 and num2!=0:
                    sum=num1+num2
                    st.info(sum)
                    data = {"num1": num1, "num2": num2,"res":sum}
                    collection.insert_one(data)
                    st.success("Data saved to MongoDB")
                else:
                    st.error('Input should be greater than zero!')

            except ValueError:
                # st.error('This is an error', icon="🚨")
                # raise st.error(TypeError("{0} is invalid This is an error".format(num1 or num2)),icon="🚨")
                e = RuntimeError('This is an exception of type RuntimeError')
                st.error(e)

with col2:
    if st.button("Subtract"):
        try:
            if num1!=0 and num2!=0:
                subtract=num1-num2
                st.info(subtract)
                data = {"num1": num1, "num2": num2,"res":subtract}
                collection.insert_one(data)
                st.success("Data saved to MongoDB")
            else:
                    st.error('Input should be greater than zero!')

        except ValueError:
            # st.error('This is an error', icon="🚨")
            # raise st.error(TypeError("{0} is invalid This is an error".format(num1 or num2)),icon="🚨")
            e = RuntimeError('This is an exception of type RuntimeError')
            st.error(e)

with col3:
    if st.button("Multiply"):
        try:
            if num1!=0 and num2!=0:    
                multiply=num1*num2
                st.info(multiply)
                data = {"num1": num1, "num2": num2,"res":multiply}
                collection.insert_one(data)
                st.success("Data saved to MongoDB")
            else:
                st.error('Input should be greater than zero!')

        except ValueError:
            # st.error('This is an error', icon="🚨")
            # raise st.error(TypeError("{0} is invalid This is an error".format(num1 or num2)),icon="🚨")
            e = RuntimeError('This is an exception of type RuntimeError')
            st.error(e)

with col4:
    if st.button("Division"):
        try:
            if num1!=0 and num2!=0:    
                division=num1+num2
                st.info(division)
                data = {"num1": num1, "num2": num2,"res":division}
                collection.insert_one(data)
                st.success("Data saved to MongoDB")

            else:
                st.error('Input should be greater than zero!')

        except ValueError:
            # st.error('This is an error', icon="🚨")
            # raise st.error(TypeError("{0} is invalid This is an error".format(num1 or num2)),icon="🚨")
            e = RuntimeError('This is an exception of type RuntimeError')
            st.error(e)



# Retrieve data from MongoDB
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Retrieve"):
        data = list(collection.find({}))
        st.write(data)

# logging.basicConfig(filename='example.log')
# logging.debug('This message should go to the log file')

# if st.button("LOGS"):
#         #data = list(collection.find({}))
#         st.info(example.txt)
