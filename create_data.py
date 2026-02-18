import pandas as pd
import os

# ساخت پوشه data اگر نباشد
if not os.path.exists('data'):
    os.makedirs('data')

data = {
    'url': [
        'http://secure-login.com',      # امن
        'https://google.com',           # امن
        'http://192.168.1.1/login',     # فیشینگ (آی‌پی دارد)
        'http://verify-account.com',    # فیشینگ (نام مشکوک)
        'https://yahoo.com',            # امن
        'http://secure..verify.com',    # فیشینگ (دو نقطه)
        'https://github.com',           # امن
        'http://123.45.67.89/bank',     # فیشینگ (آی‌پی)
    ],
    'label': [0, 0, 1, 1, 0, 1, 0, 1] # 0 امن، 1 فیشینگ
}

df = pd.DataFrame(data)
df.to_csv('data/dataset.csv', index=False)
print("Dataset created successfully.")