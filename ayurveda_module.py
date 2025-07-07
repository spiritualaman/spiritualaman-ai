def get_herbs_for_disease(disease, lang):
    data = {
        "सिरदर्द": {"hi": ["ब्रह्मी", "जटामांसी"], "en": ["Brahmi", "Jatamansi"]},
        "headache": {"hi": ["ब्रह्मी", "जटामांसी"], "en": ["Brahmi", "Jatamansi"]},
        "जुकाम": {"hi": ["तुलसी", "अदरक", "शहद"], "en": ["Tulsi", "Ginger", "Honey"]},
        "cold": {"hi": ["तुलसी", "अदरक", "शहद"], "en": ["Tulsi", "Ginger", "Honey"]},
    }
    entry = data.get(disease.lower())
    if entry:
        return entry["hi"] if lang == "हिन्दी" else entry["en"]
    return ["कोई सुझाव नहीं / No suggestions found"]
