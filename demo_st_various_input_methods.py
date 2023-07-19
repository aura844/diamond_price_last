import streamlit as st
import pickle

st.title("Streamlit Demo: Input Data")

with open ('model_pickle','rb') as f:
    model =pickle.load(f)

# Text Field carat
st.subheader("carat")
carat = st.text_input("Enter some text",key=1)
st.write("Text input:", carat)


st.subheader("Cut")
cut = st.radio("Select Cut value", ["Fair","Good","Very Good","Premium","Ideal"])
st.write("Cut value:", cut)
if cut=="Fair": 
    cut=1
elif cut=="Good":
    cut=2
elif cut=="Very Good":
    cut=3
elif cut=="Premium":
    cut=4
elif cut=="Ideal":
    cut=5
st.subheader("Color")
color = st.radio("Select color", ["D","E","F","G","H","I","J"])
st.write("Color:", color)
if color=="J": 
    color=1
elif color=="I":
    color=2
elif color=="H":
    color=3
elif color=="G":
    color=4
elif color=="F":
    color=5
elif color=="E":
    color=6
elif color=="D":
    color=7

st.subheader("Clarity")
clarity = st.radio("Select Clarity", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])
st.write("Clarity Level:", clarity)
if clarity=="I1": 
    clarity=1
elif clarity=="SI2":
    clarity=2
elif clarity=="SI1":
    clarity=3
elif clarity=="VS2":
    clarity=4
elif clarity=="VS1":
    clarity=5
elif clarity=="VVS2":
    clarity=6
elif clarity=="VVS1":
    clarity=7
elif clarity=="IF":
    clarity=8


# Text Field depth
st.subheader("Depth")
depth = st.text_input("Enter some text",key=5)
st.write("Text input:", depth)


# Text Field table
st.subheader("Table")
table = st.text_input("Enter some text",key=6)
st.write("Text input:", table)































# Button
st.subheader("For Price")
if st.button("Click Me"):
    st.write("Button was clicked!")
    yhat_test=model.predict([[carat, cut,color,clarity,depth,table]])
    st.write("Predicted Price",yhat_test )

