def get_astrology_details(name, dob, tob, place, lang):
    if lang == "हिन्दी":
        return f"नाम: {name}\nजन्म तिथि: {dob}\nसमय: {tob}\nस्थान: {place}\n(यह एक डेमो ज्योतिष विवरण है।)"
    else:
        return f"Name: {name}\nDOB: {dob}\nTime: {tob}\nPlace: {place}\n(This is a demo astrology summary.)"
