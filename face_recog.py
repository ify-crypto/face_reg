import cv2
import streamlit as st 

st.markdown("<h1 style = 'color: #FFACAC'>FACE DETECTION APP</h1> ", unsafe_allow_html = True)
st.markdown("<h6 style = 'top_margin: 0rem; color: #F2921D'>Built by IfyOkafor</h6>", unsafe_allow_html = True)

st.image('pngwing.com.png',caption = 'Built by Ifeyinwa',width=400)

#Create a line and a space underneath
st.markdown('<hr>,<hr><br>',unsafe_allow_html=True)

# Add instructions to the Streamlit app interface to guide the user on how to use the app.
if st.button('Read the usage Instructions below'): 
    st.success ('Hello User,these are the guidelines for the app usage')
    st.write('Press the camera button for our model to detect your face')
    st.write('Use the MinNeighbour slider to adjust how many neighbors each candidate rectangle should have to retain it')
    st.write('Use the Scaler slider to specify how much the image size is reduced at each image scale.')


st.markdown('<br>',unsafe_allow_html=True)
# Start the face detection 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default .xml')
camera = cv2.VideoCapture(0)        #.........opens the web cam

#set the minNeighbours abd Scale Factor buttons
min_Neighbours = st.slider('Adjust Min Neighbour',1, 0, 5) 
Scale_Factor = st.slider('Adjust Scale_Factor',0.0, 3.0, 1.3)


st.markdown('<br>',unsafe_allow_html=True)

if st.button('FACE DETECT'):
# Initialize the webcam
    while True:
        _, camera_view = camera.read()   #....................................... Initiate the camera
        gray = cv2.cvtColor(camera_view, cv2.COLOR_BGR2GRAY) #.................. Grayscale it using the cv grayscale library
    #   Detect the faces using the face cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor= Scale_Factor, minNeighbors= min_Neighbours, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    #   Draw rectangles around the detected faces
        for (x, y, width, height) in faces:
            cv2.rectangle(camera_view, (x, y), (x + width, y + height), (225, 255, 0), 2)
    # Display the camera_views
        cv2.imshow('Face Detection using Viola-Jones Algorithm', camera_view)
    # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
    # Release the webcam and close all windows
    camera.release()
    cv2.destroyAllWindows()