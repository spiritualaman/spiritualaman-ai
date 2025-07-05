def get_mantra_by_purpose(purpose):
    mantras = {
        "ध्यान": "ॐ शांतिः शांतिः शांतिः",
        "सफलता": "ॐ श्रीं ह्रीं श्रीं नमः",
        "संकट मुक्ति": "ॐ नमः शिवाय"
    }
    return mantras.get(purpose, "मंत्र उपलब्ध नहीं")