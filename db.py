# db.py

entries = []

def has_entered(user_id):
    return any(e['user_id'] == user_id for e in entries)

def add_entry(user_id, account_number, bank_name, holder_name, gender):
    entries.append({
        "user_id": user_id,
        "account_number": account_number,
        "bank_name": bank_name,
        "holder_name": holder_name,
        "gender": gender
    })

def count_gender(gender):
    return sum(1 for e in entries if e['gender'] == gender)

def is_full(gender, male_limit, female_limit):
    if gender == "male":
        return count_gender("male") >= male_limit
    else:
        return count_gender("female") >= female_limit

def get_all_entries():
    return entries
