#libery files------
import json
import streamlit as st
from keras.models import load_model
from PIL import Image
import tensorflow.compat.v2 as tf
from util import classify
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#set page set-up
st.set_page_config(page_title="Disease Detector",page_icon="./bgs/doc.ico", layout="wide")

#load assets----
def load_lottiefiles(filepath:str):
      with open(filepath,"r") as f:
            return json.load(f)
my_logo = Image.open("bgs/pneumonia.ico")

#use CSS----
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#create sidebar
with st.sidebar:   
    selected = option_menu(
            menu_title="Main-Menu",
            options=["Home","Pneumonia Detector","Brain Tumour Detector"],
            icons=["house","lungs","people"],
            menu_icon="cast",
            default_index=0,
            orientation="Vertical",
            styles={
            "container":{"padding": "2!important", "background-color" :"#6C757D"},
            "icon":{"color":"#BCC6CC","font-size":"30px"},
            "nav-link":{
                "font-size":"15px",
                "text-align":"left",
                "margin":"4px",
                "--hover-color":"#ADB5BD",
            },
            "nav-link-selected":{"background-color":"#495057"}
            }
    )
#make home page
if selected=="Home":
        st.title("A Pnumonia Detection Web-App :desktop_computer:")
        st.subheader("Hi! Welcome to our page... :wave:")
        st.write(
              """
              Pneumonia is a common and pottentially life-threading respiratory infection that affects
              million of people worldwide each year.Timely detection and accurate diagnosis are crucial for effective 
              treatement and improves patients outcomes.That's why our pneumonia detection webapp comes in.
               """)
        with st.container():
              st.write("---")
              left_colmun, right_column = st.columns(2)
              with left_colmun:
                    st.subheader("Here's why our pneumonia detection webapp stands out:")
                    st.write("##")
                    st.write(
                          """
                            :red_circle: **ADVANCED ARTIFICIAL INTELLIGENCE**: Our WebApp utilizes cutting-edge artificial
                            intelligence technology, specically deep learning algorithm, to analyze chest X-rey images.
                            This Sophisticated technology enables our system to learn and recognize intricate patterns and
                            anomalies associated with pneumonia, providing accurate and detailed assesments."""
                    )
                    st.write(
                          """
                            :red_circle: **SPEED AND EFFICIANCY**: Time plays a crucial role in Pneumonia diagnosis and treatment.
                            With our WebApp, you can receive rapid resuits,allowing heaithcare professionals to make timely decisions
                            regardig patient care.By streamilning the diagnostic process,we aim to
                            minimize delays and expedite appropriate treatment interventions."""
                    )
                    st.write(
                          """
                            :red_circle: **ENHANCED ACCURACY**: Accuracy is paramount when it comes to diagnosing pneumonia.Our Web App has 
                            been trained on extensive datasets of diverse chest X-ray images,ensuring a robust understanding of the disease.
                          """
                    )
                    st.write(
                         """
                            :red_circle: **USER-FRIENDLY INTERFACE**: We believe that technology should be accessible to everyone.Our WebApp features
                            a user-friendly interface that makes it easy healthcare professionals and individuals to upload and analyze chest X-ray
                            images.The intuitive design ensures a seamless user experience,even for those with limited thechnical experties.

                          """
                    ) 
                    st.write(
                          """
                          :red_circle: **SUPPORT FOR HEALTHCARE PROFESSIONALS**: By providing reliable and accessible pneumonia detection,we aim to support
                          both medical practitioners and individuals in making informed decisions about their health.

                          """
                    )
              with right_column:
                 lottie_coding = load_lottiefiles("json/coding_dark.json")
                 st_lottie(
                    lottie_coding,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",
                    height="600px",
                    width="700px",
                    key=None,
                )

#make pneumonia detector page
if selected=="Pneumonia Detector":
        #set background
        #..........blank........#
        #set title

        st.title('Pneumonia Classification Webapp')

        #set subheader
        with st.container():
             left_column,right_column = st.columns(2)
             with left_column:
                  st.write("##")
                  st.write("##")
                  st.subheader("Step by Step process:-")
                  st.write(
                       """
                       :red_circle: **STEP 1:-** Click the "Browse file" button and choose the Chest X-rey
                       """
                  )
                  st.write(
                       """
                       :red_circle: **STEP 2:-** Click on "Open" and wait for few moment.
                       """
                  )
                  st.subheader("Now add your Chest X-rey")
             with right_column:
                  lottie_coding = load_lottiefiles("json/upload.json")
                  st_lottie(
                    lottie_coding,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",
                    height="300px",
                    width="400px",
                    key=None,
                )
        #upload file

        file = st.file_uploader('',type=['jpeg','jpg','png'])

        #load classifier

        model = load_model('./model/Pneumonia_detect.h5')

        #load class name

        with open('./model/label.txt','r') as f:
            class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
            f.close()

        #display image

        if file is not None:
            image = Image.open(file).convert('RGB')
            st.image(image, use_column_width=True)

        #classify image

            class_name, conf_score = classify(image, model, class_names)

        #write classification

            st.write("## {}".format(class_name))
            st.write("### score: {}".format(conf_score))

        #ADDITIONAL DESIGN 
        with st.container():
             st.write("---")
             st.write("##")
             image_column,text_column = st.columns((1,2))
             with image_column:
                st.image(my_logo) 
             with text_column:
                  st.subheader("Thank You...")
                  st.write(
                       """
                       We believe that our Pneumonia detection WebApp will be a valuable tool in the fight against this
                       widespread respiratory infection.Whether you are a healthcare professional seeking an additional resource
                       for diagnosis or an individual concerned about your rspiratory health,our WebApp is here to provide reliable
                       and accessible assistance
                       """
                     )
                  st.write(
                       """
                        We are dedicated to continuously improving our WebApp's performance and expanding
                        its capabilities to contribute to the early detection and effective management of pneumonia.
                        Your feedback and suggestions are always welcome as we strive to make a positive impact on respiratory healthcare.
                       """
                  )
                  st.write(
                       """
                       Thank you for choosing our Pneumonia Detection WebApp. 
                        We hope it proves to be a valuable resource in your journey towards better respiratory health.
                        """
                  )                  
        #feedback
        with st.container():
             st.write("---")
             st.header("Get In Touch With Us :handshake:")
             st.write("##")
             contact_form = """
             <form action="https://formsubmit.co/anupampal.ind@gmail.com" method="POST">
               <input type="hidden" name="_captcha" value="false">
               <input type="text" name="name" placeholder="Your name" required>
               <input type="email" name="email" placeholder="Your E-mail" required><br>
               <textarea name="message" placeholder="Enter your message" required></textarea><br>
               <button type="submit">SEND</button>
             </form>
             """
             left_colmun, right_column = st.columns(2)
             with left_colmun:
                  st.markdown(contact_form, unsafe_allow_html=True)
             with right_column:
                     lottie_coding = load_lottiefiles("json/welcome_dark.json")
                     st_lottie(
                        lottie_coding,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality="low",
                        height=250,
                        width=650,
                        key=None,
                    )

#make brain tumor detector
if selected=="Brain Tumour Detector":
        #set background
        #..........blank........#
        #set title

        st.title('Brain Tumour Detector')

        #set subheader
        with st.container():
             left_column,right_column = st.columns(2)
             with left_column:
                  st.write("##")
                  st.write("##")
                  st.subheader("Step by Step process:-")
                  st.write(
                       """
                       :red_circle: **STEP 1:-** Click the "Browse file" button and choose the Chest X-rey
                       """
                  )
                  st.write(
                       """
                       :red_circle: **STEP 2:-** Click on "Open" and wait for few moment.
                       """
                  )
                  st.subheader("Now add your Brain MRI")
             with right_column:
                  lottie_coding = load_lottiefiles("json/upload.json")
                  st_lottie(
                    lottie_coding,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",
                    height="300px",
                    width="400px",
                    key=None,
                )
        #upload file

        file = st.file_uploader('',type=['jpeg','jpg','png'])

        #load classifier

        model = load_model('./model/Brain_tumor.h5')

        #load class name

        with open('./model/label2.txt','r') as f:
            class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
            f.close()

        #display image

        if file is not None:
            image = Image.open(file).convert('RGB')
            st.image(image, use_column_width=True)

        #classify image

            class_name, conf_score = classify(image, model, class_names)

        #write classification

            st.write("## {}".format(class_name))
            st.write("### score: {}".format(conf_score))

        #ADDITIONAL DESIGN 
        with st.container():
             st.write("---")
             st.write("##")
             image_column,text_column = st.columns((1,2))
             with image_column:
                st.image(my_logo) 
             with text_column:
                  st.subheader("Thank You...")
                  st.write(
                       """
                       We believe that our Pneumonia detection WebApp will be a valuable tool in the fight against this
                       widespread respiratory infection.Whether you are a healthcare professional seeking an additional resource
                       for diagnosis or an individual concerned about your rspiratory health,our WebApp is here to provide reliable
                       and accessible assistance
                       """
                     )
                  st.write(
                       """
                        We are dedicated to continuously improving our WebApp's performance and expanding
                        its capabilities to contribute to the early detection and effective management of pneumonia.
                        Your feedback and suggestions are always welcome as we strive to make a positive impact on respiratory healthcare.
                       """
                  )
                  st.write(
                       """
                       Thank you for choosing our Pneumonia Detection WebApp. 
                        We hope it proves to be a valuable resource in your journey towards better respiratory health.
                        """
                  )                  
        #feedback
        with st.container():
             st.write("---")
             st.header("Get In Touch With Us :handshake:")
             st.write("##")
             contact_form = """
             <form action="https://formsubmit.co/anupampal.ind@gmail.com" method="POST">
               <input type="hidden" name="_captcha" value="false">
               <input type="text" name="name" placeholder="Your name" required>
               <input type="email" name="email" placeholder="Your E-mail" required><br>
               <textarea name="message" placeholder="Enter your message" required></textarea><br>
               <button type="submit">SEND</button>
             </form>
             """
             left_colmun, right_column = st.columns(2)
             with left_colmun:
                  st.markdown(contact_form, unsafe_allow_html=True)
             with right_column:
                     lottie_coding = load_lottiefiles("json/welcome_dark.json")
                     st_lottie(
                        lottie_coding,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality="low",
                        height=250,
                        width=650,
                        key=None,
                    )
