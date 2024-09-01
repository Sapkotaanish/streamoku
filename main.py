import streamlit as st

def main():
    st.title("Hello World App")
    
    st.write("Hello, World!")
    
    if st.button("Say Hello and Go to Google"):
        st.write("Hello from the button!")

if __name__ == "__main__":
    main()