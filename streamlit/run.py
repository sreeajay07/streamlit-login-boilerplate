from enum import unique
import time
import streamlit as st
import hashlib
import streamlit as st




             




def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


def is_authenticated(username, password):
    # with open('user_login.json') as json_file:
    #     user_login = json.load(json_file)
    if username == "admin" and password == "admin":
        return True, True
    else:
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            return True, False

def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()
    return block1, block2
    
def generate_signin_block():
	block6=st.empty()
	block7=st.empty()	

def generate_title_block(title):
    block0 = st.title(title)
    
    return block0

def generate_empty_block():
    block3 = st.empty()
    return block3

def generate_success_block():
    block5 = st.success('Successfully Logged in')
    return block5

def clean_blocks(blocks):
    for block in blocks:
        block.empty()
        
def clean_block(block):
    block.empty()

def user_login(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input('Username')

def password_login(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input('Password')


def button_click(block):
    if st.button=='login' : 
        return block.button('Login')
    else :
        return block.button('signin')
# @st.cache(suppress_st_warning=True)
# @st.cache(persist=True)
    
def main():
    title_blocks = generate_title_block('basic login')
    username_login_blocks = generate_login_block()
    username = user_login(username_login_blocks)
    password_login_blocks = generate_login_block()
    password = password_login(password_login_blocks)
    left, right =  st.columns(2)
    with left:
        a= st.button('login')
    with right:
        b= st.button('sign in')    
    if a:
       
        st.info("sucess")
        authentication , admin_flag = is_authenticated(username, password)
        if authentication:
            clean_blocks(username_login_blocks)
            clean_blocks(password_login_blocks)
            clean_block(title_blocks)
            success_block = generate_success_block()
            time.sleep(2)
            clean_block(success_block)
            st.session_state['login'] = "True"
            return username
            # if admin_flag:
            #     login_dict = {"status": "True", "admin": "True"}
            # else:
            #     login_dict = {"status": "True", "admin": "False"}
            # json_file = ""
            # with open('login_status.json', 'w') as json_file:
            #     json.dump(login_dict , json_file)
            # new_page()
            
            
    elif b:
        st.error('This is an error', icon="🚨")
              
            

if __name__ == '__main__':
	main()


