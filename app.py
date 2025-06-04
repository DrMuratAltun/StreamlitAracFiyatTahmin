#pkl modelini yükle
import pandas as pd
import joblib
pipe= joblib.load('car_price_model.pkl')
#Load data
df=pd.read_excel('cars.xls')
def predict_price(make, model,trim, mileage, car_type, cylinder, liter, doors, cruise, sound, leather):
    # Kullanıcıdan alınan verileri DataFrame'e dönüştür
    input_data=pd.DataFrame({
        'Make':[make],
        'Model':[model],
        'Trim':[trim],
        'Mileage':[mileage],
        'Type':[car_type],
        'Cylinder':[cylinder],
        'Liter':[liter],
        'Doors':[doors],
        'Cruise':[cruise],
        'Sound':[sound],
        'Leather':[leather]
    })
    prediction = pipe.predict(input_data)[0]
    return prediction

#Streamlit arayüzü
import streamlit as st
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(":red_car: Fiyat Tahmin Uygulaması @drmurataltun")
st.write("Araba fiyatı tahmini için aşağıdaki bilgileri giriniz:")
make=st.selectbox("Marka", df['Make'].unique())
model=st.selectbox("Model", df[df['Make'] == make]['Model'].unique())
trim=st.selectbox("Trim", df[(df['Make'] == make) & (df['Model'] == model)]['Trim'].unique())
mileage=st.number_input("Kilometre",200, 600000, step=1000)
car_type=st.selectbox("Araç tipi",df[(df['Make'] == make) & (df['Model'] == model) & (df['Trim'] == trim)]['Type'].unique())
cylinder=st.selectbox("Silindir",df['Cylinder'].unique())
liter=st.number_input("Motor hacmi (Litre)",1,6)
doors=st.selectbox("Kapı:",df['Doors'].unique())
cruise=st.radio("Hız Sabitleme",[True, False])
sound=st.radio("Ses Sistemi",[True, False])
leather=st.radio("Koltuk",[True, False])
if st.button("Fiyat Tahmini"):
    pred=predict_price(make, model,trim, mileage, car_type, cylinder, liter, doors, cruise, sound, leather)
    st.success(f"Tahmini Fiyat: ${int(pred):}")
