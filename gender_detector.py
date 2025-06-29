# gender_detector.py

female_names = [
    "Aisha", "Hauwa", "Zainab", "Fatima", "Hadiza", "Maryam", "Rukayya",
    "Asma'u", "Khadija", "Safiya", "Sadiya", "Hajara", "Jamila", "Bilkisu",
    "Habiba", "Rabi", "Ladidi", "Maimuna", "Lami", "Rahil", "Rabi'at", "Maroofat"
]

male_names = [
    "Abubakar", "Usman", "Musa", "Muhammad", "Aliyu", "Bashir", "Kabiru", "Shehu",
    "Sulaiman", "Yahaya", "Tijjani", "Umar", "Ismail", "Aminu", "Ibrahim", "Nasir",
    "Haruna", "Lawan", "Habibu", "Ahmad", "Danladi", "Bello", "Shamsuddeen"
]

def detect_gender(name):
    name = name.strip().split(" ")[0].capitalize()
    if name in female_names:
        return "female"
    elif name in male_names:
        return "male"
    else:
        return "male"  # default fallback
