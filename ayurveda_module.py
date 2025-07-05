def get_herbs_for_disease(disease_name):
    remedies = {
        "जुकाम": ["तुलसी", "अदरक", "शहद"],
        "पेट दर्द": ["अजवाइन", "हींग", "सौंफ"],
        "खांसी": ["मुलेठी", "गिलोय", "काली मिर्च"]
    }
    return remedies.get(disease_name, ["कोई सुझाव नहीं मिला"])