import streamlit as st
from ayurveda_module import get_herbs_for_disease
from spiritual_module import get_mantra_by_purpose
from astrology_module import get_astrology_details

st.set_page_config(page_title="SpiritualAman AI", page_icon="🧘")
st.title("🧘‍♂️ SpiritualAman AI")

lang = st.selectbox("Language / भाषा चुनें", ["English", "हिन्दी"])
tab1, tab2, tab3 = st.tabs(["🌿 Ayurveda", "🔮 Astrology", "🧘 Mantra AI"])

with tab1:
    disease = st.text_input("Enter disease / रोग दर्ज करें:")
    if disease:
        herbs = get_herbs_for_disease(disease, lang)
        st.write("🌿 Herbs / औषधियाँ:")
        st.write(herbs)

with tab2:
    name = st.text_input("Name / नाम:")
    dob = st.date_input("Date of Birth / जन्म तिथि:")
    time = st.time_input("Time of Birth / जन्म समय:")
    place = st.text_input("Place of Birth / जन्म स्थान:")
    if name and dob and time and place:
        astro = get_astrology_details(name, dob, time, place, lang)
        st.write("🔮 Astrology Details / ज्योतिष विवरण:")
        st.write(astro)

with tab3:
    purpose = st.selectbox("Select purpose / उद्देश्य चुनें", ["Meditation / ध्यान", "Success / सफलता", "Protection / संकट मुक्ति"])
    mantra = get_mantra_by_purpose(purpose, lang)
    st.write("📿 Mantra / मंत्र:")
    st.write(mantra)
