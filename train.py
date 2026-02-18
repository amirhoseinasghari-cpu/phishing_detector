import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from utils import extract_features

# ۱. لود کردن دیتاست
print("Loading dataset...")
# فرض می‌کنیم فایل csv ستون‌های 'url' و 'label' دارد
df = pd.read_csv('data/dataset.csv')

# ۲. تبدیل URLها به اعداد (ویژگی‌ها) با استفاده از تابعی که قبلا نوشتیم
print("Extracting features...")
X = df['url'].apply(lambda x: extract_features(x)).tolist()
y = df['label']

# ۳. تقسیم داده‌ها به بخش آموزش و تست (۲۰٪ تست)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ۴. ساخت و آموزش مدل
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ۵. بررسی دقت مدل
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# ۶. ذخیره مدل آموزش دیده برای استفاده بعدی
joblib.dump(model, 'model.pkl')
print("Model saved to model.pkl")