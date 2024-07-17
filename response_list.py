import requests
import json 

"""
requests and json module is used to send requests to the Endpoint and Parse the response

"""
def request_server():
    """
    Returns:
        list: A  list containing the response from the server.
    """
    response = requests.get('https://email-sev.onrender.com/fetch_usernames')
    if response.status_code == 200:
    # Get the response text
        intermediate_mail = response.text
        
        # Parse the string into a list (assuming it's a JSON string)
        try:
            email_list = json.loads(intermediate_mail)
            
            # Ensure the data is a list
            if isinstance(email_list, list):
                set_of_user_replied = set(email_list)
                
                # Print the original list and the set
                print("Set of unique emails:", set_of_user_replied)
                with open ("mail_replied.txt",'a') as f:
                    for email in set_of_user_replied:
                        f.write(f"{email}\n")
            else:
                print("Unexpected response format:", type(email_list))
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", str(e))
    else:
        print("Failed to fetch data:", response.status_code)
    return set_of_user_replied
request_server()