import streamlit as st
import google.generativeai as genai

# 1. إعداد الصفحة (عشان تظهر كأنها موقع رسمي)
st.set_page_config(page_title="AI Archive System", layout="centered")

# 2. كود لإخفاء أي حاجة تدل على جوجل أو ستريم ليت
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #0e1117; color: white; }
    /* تنسيق صندوق الرفع */
    .stFileUploader { border: 2px dashed #00ffaa; border-radius: 10px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. الربط بمحرك الذكاء الاصطناعي (مخفي)
genai.configure(api_key="AIzaSyDh3Tf7a69lpWdlfd2KZ2FKF2cCwmdyUrQ")

# 4. واجهة الموقع
st.title("نظام المعالجة الذكي")
st.write("ارفع الملف وسيقوم النظام بتحليله فوراً")

uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    # عرض الصورة بشكل شيك
    st.image(uploaded_file, caption="المستند المرفوع", use_container_width=True)
    
    if st.button("تحليل المستند"):
        with st.spinner('جاري التحليل...'):
            # استدعاء المحرك من غير ما المستخدم يشوف جوجل
            model = genai.GenerativeModel("gemini-1.5-flash")
            img = uploaded_file.getvalue()
            response = model.generate_content([
                "حلل المستند واستخرج البيانات بدقة", 
                {"mime_type": "image/jpeg", "data": img}
            ])
            
            st.success("تم التحليل")
            st.write(response.text)
