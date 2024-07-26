import streamlit as st
import streamlit_authenticator as stauth

import random

import yaml
from yaml.loader import SafeLoader

import json

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Hello Mainframer')
    st.write('## All The Best For Job Search')
    st.warning('Please remember, this data is help you to get job. "DON NOT MISSUSE".')
        # Data submission form
    st.write('## Submit HR Data')
    with st.form(key='hr_form'):
        #======================================
        #Get the data
        #======================================
        value1 = st.text_input('Name')
        value2 = st.text_input('Company name')
        value3 = st.text_input('Phone Number')
        value4 = st.text_input('Email')
        value6 = str(st.date_input('Enter Date you got the call'))
        value5 = st.selectbox("Is it 3rd party or Direct",("yes","no"))
        submit_button = st.form_submit_button(label='Submit')
        
        # Store the data in Dict
        y = {"hr_name":value1,"company": value2,"phno": value3,"email": value4,"3rd_party": value5,'date': value6}

        #=======================================
        # Put the data
        #=======================================
        def write_json(new_data, filename='hrdata.json'):
        		with open(filename,'r+') as file:
			        file_data = json.load(file)
			        file_data["hrdetail"].append(new_data)
			        file.seek(0)
			        json.dump(file_data, file, indent = 4)
        if submit_button:
        	
        	if len(value1) < 2 or (len(value3) < 2 or len(value3) > 10):
        		st.warning('Name & Phno is importent')
        	else:
        		with open('hrdata.json','r+') as file:
        			file_data = json.load(file)
        		data = str(file_data['hrdetail'])
        		pos=data.find(str(value3))
        		if pos >= 0:
        			st.warning('Data already exist')
        		else:
        			write_json(y)
        			x = len(file_data['hrdetail'])
				st.write('Currently we have' x 'Number of HR data in our database')
        			get_data = random.sample(range(x), 5)
        			for i in get_data:
        				st.write(file_data['hrdetail'][i])
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')




#my_dict["hrdetail"][0].update({"remarks": "Your remarks here"})
