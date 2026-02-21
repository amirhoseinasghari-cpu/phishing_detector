document.getElementById("checkBtn").addEventListener("click", async () => {
  const resultDiv = document.getElementById("result");
  resultDiv.innerText = "در حال بررسی...";

  // دریافت آدرس تب فعلی
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  let url = tab.url;

  // ارسال به سرور پایتون
  fetch(`http://127.0.0.1:5000/predict?url=${encodeURIComponent(url)}`)
    .then(response => response.json())
    .then(data => {
      if (data.prediction === "Phishing") {
        resultDiv.innerText = "⚠️ فیشینگ (خطرناک)";
        resultDiv.style.color = "red";
      } else {
        resultDiv.innerText = "✅ امن است";
        resultDiv.style.color = "green";
      }
    })
    .catch(err => {
      resultDiv.innerText = "خطا: ارتباط با سرور برقرار نشد (آیا api.py در حال اجراست؟)";
      resultDiv.style.color = "orange";
    });
});