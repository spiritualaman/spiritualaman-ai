def get_mantra_by_purpose(purpose):
    mantra_dict = {
        "ध्यान": "ॐ शान्तिः शान्तिः शान्तिः",
        "सफलता": "ॐ श्रीं ह्रीं क्लीं नमः",
        "संकट मुक्ति": "ॐ नमः भगवते वासुदेवाय"
    }
    return mantra_dict.get(purpose, "कोई मंत्र नहीं मिला")

