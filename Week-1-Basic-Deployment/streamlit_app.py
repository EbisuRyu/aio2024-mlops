import pickle
import streamlit as st 
LATITUDE = 40.71422708323266
LONGITUDE = -73.94160121297645

st.title('New York Housing Price Prediction')
st.write('This is a simple web app to predict the price of a house in New York City based on its size in square feet and the number of bedrooms')

@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)

def predict_price(model, bedrooms, bathrooms, size):
    x = [[bedrooms, bathrooms, size, LATITUDE, LONGITUDE]]
    return model.predict(x)

model = load_model('./notebooks/rf_regressor.pkl')
bedrooms = st.number_input('Bedrooms', min_value=1, max_value=50, value=1, step=1)
bathrooms = st.number_input('Bathrooms', min_value=0, max_value=50, value=0, step=1)
size = st.number_input('Size (sqft)', min_value=230.0, max_value=65535.0, value=230.0, step=10.0)

if st.button('Predict'):
    price = predict_price(model, bedrooms, bathrooms, size).item()
    st.write(f'The estimated price of this house is ${price:,.2f}')