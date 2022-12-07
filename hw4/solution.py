import json

def question01(text):
    # The argument of this function is a JSON string.
    # Return the corresponding JSON object.
    # If the input text is not a legitimate JSON string, return the following object:
    # {
    #   "error": true
    # }
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "error": True
        }
    
