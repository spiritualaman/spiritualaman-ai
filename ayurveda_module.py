def get_herbs_for_disease(disease):
    herbs_dict = {
        "जुकाम": ["तुलसी", "अदरक", "शहद"],
        "सिरदर्द": ["ब्रह्मी", "जटामांसी"],
        "पेट दर्द": ["अजवाइन", "हींग"]
    }
    return herbs_dict.get(disease, ["कोई सुझाव नहीं मिला"])
