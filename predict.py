import joblib
from utils import extract_features

# ۱. لود کردن مدل آموزش دیده
model = joblib.load('model.pkl')

def check_url(url):
    # ۲. تبدیل URL جدید به ویژگی‌های عددی
    features = [extract_features(url)] # مدل ورودی را لیستی از لیست‌ها می‌خواهد
    
    # ۳. پیش‌بینی (0 یعنی امن، 1 یعنی فیشینگ)
    prediction = model.predict(features)[0]
    
    # ۴. نمایش نتیجه
    if prediction == 1:
        return "⚠️ این سایت فیشینگ است (خطرناک)"
    else:
        return "✅ این سایت امن است"

# --- نحوه استفاده ---
target_url = input("آدرس سایت را وارد کنید: ")
result = check_url(target_url)
print(result)