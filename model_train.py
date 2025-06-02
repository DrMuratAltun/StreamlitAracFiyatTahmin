import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

#veri setini yükle
df=pd.read_excel("cars.xls")
print (df.info())

#özellikleri ve hedef değişkeni ayır
X= df.drop("Price", axis=1)
y= df["Price"]

#Veri setini eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

#Preprocessor oluştur
preprocessor =ColumnTransformer(transformers=[('num',StandardScaler(),
                                               ['Mileage','Cylinder','Liter','Doors']),
                                               ('cat',OneHotEncoder(),
                                               ['Make','Model','Trim','Type'])])
model=LinearRegression()

#pipelie oluştur
pipe = Pipeline(steps=[('preprocessor', preprocessor),
                             ('model', model)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

#Model performansını değerlendir
mse= mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)
#print("Ortalama Araç fiyatı : ", y.mean())
#print(f"Ortalama Kare hata karekökü : {mse**.5}")
#print(f"R^2 Skor: {r2}")

#Pipeline ı kaydet
import joblib
joblib.dump(pipe, 'car_price_model.pkl')