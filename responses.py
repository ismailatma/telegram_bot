from datetime import datetime

def message_responses(text: str):
    if 'jam' in text.lower():
        response =  str(datetime.now())
    else:
        response = "Else Condition"

    return response