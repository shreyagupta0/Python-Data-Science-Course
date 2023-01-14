import streamlit as st

st.image('https://www.bing.com/th?id=OAIP.81cb434682db8d1aba5e87dc7ab53ba5&pid=AdsNative&w=300&h=157&c=4&dynsize=1')
st.title("String App")
message = st.text_area("enter some text")
button = st.button("Process text")

if button:
    st.write(message)
if st.sidebar.checkbox("show words"):
    words = message.split()
    st.write(words)
if st.sidebar.checkbox("character count"):
    for char in massege:
        st.write(f'{char} : {message.count(char)}')
    
