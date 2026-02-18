import re
from urllib.parse import urlparse

def extract_features(url):
    """
    دریافت URL و برگرداندن لیستی از ویژگی‌های عددی
    """
    features = []
    parsed = urlparse(url)

    # ویژگی ۱: طول URL
    features.append(len(url))

    # ویژگی ۲: آیا IP آدرس دارد؟ (مثلا: 127.0.0.1)
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    has_ip = 1 if re.search(ip_pattern, url) else 0
    features.append(has_ip)

    # ویژگی ۳: آیا پروتکل HTTPS است؟
    is_https = 1 if parsed.scheme == 'https' else 0
    features.append(is_https)

    # ویژگی ۴: تعداد نقاط (.) در آدرس
    features.append(url.count('.'))

    return features