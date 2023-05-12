import streamlit as st
from websocket import create_connection
import base64, json

from utils import get_mask

def func(image, text):
    # Replace this with your function code
    b64 = base64.b64encode(image.read()).decode()
    html = f'data:image/{image.name.split(".")[-1]};base64,{b64}'


    resp = get_mask(html, text)
    return json.loads(resp)

def main():
    st.title("Image and Text Input App")
    image = st.file_uploader("Upload an image")
    # show the image once uploaded
    if image is not None:
        st.image(image, caption="Uploaded Image")

    text = st.text_input("Enter some text")
    if st.button("Submit"):
        print("Button clicked!")
        if image is not None and text != "":
            # show a spinner
            with st.spinner("Running your function..."):
                resp = func(image, text)
                image = resp["output"]["data"][0]
                image = image.split(",")[1]
                # image is a base64 encoded image, convert it to bytes
                image = base64.b64decode(image)
                st.image(image, caption="Output Image")
        else:
            st.write("Please upload an image and enter some text.")

if __name__ == "__main__":
    main()
