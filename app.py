import streamlit as st
from ayurveda_module import get_herbs_for_disease
from spiritual_module import get_mantra_by_purpose

st.title("🌿 SpiritualAman AI")

choice = st.selectbox("सेवा चुनें:", ["Ayurveda", "Spiritual"])

if choice == "Ayurveda":
    disease = st.text_input("रोग का नाम:")
    if disease:
        herbs = get_herbs_for_disease(disease)
        st.write("सुझावित औषधियाँ:", herbs)

elif choice == "Spiritual":
    purpose = st.selectbox("आपका उद्देश्य:", ["ध्यान", "सफलता", "संकट मुक्ति"])
    st.write("मंत्र:", get_mantra_by_purpose(purpose))