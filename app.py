import streamlit as st
import google.generativeai as genai

# إعداد واجهة التطبيق
st.set_page_config(page_title="أمان للأرشفة الذكية", layout="centered")

# إعداد مفتاح API (تم وضعه بناءً على صورتك السابقة)
genai.configure(api_key="AIzaSyDh3Tf7a69lpWdlfd2KZ2FKF2cCwmdyUrQ")

st.title("📂 نظام الأرشفة الذكي - أمان هولدنج")
st.write("مرحباً بك، ابدأ برفع الملف أو الصورة لتحليلها وتصنيفها فوراً.")

# خانة رفع الملفات
uploaded_file = st.file_uploader("ارفع وثيقة أو صورة للأرشفة", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='جاري المعالجة...', use_column_width=True)
    
    if st.button('بدء الأرشفة الذكية'):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            bytes_data = uploaded_file.getvalue()
            image_parts = [{"mime_type": "image/jpeg", "data": bytes_data}]
            
            response = model.generate_content(["قم بتحليل هذه الوثيقة واستخراج البيانات الهامة للأرشفة.", image_parts[0]])
            
            st.subheader("نتائج التحليل:")
            st.write(response.text)
            st.success("تمت الأرشفة بنجاح!")
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
