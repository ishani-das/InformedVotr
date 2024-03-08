import requests
import base64

api_key = "YOUR_API_KEY"
bill_id = "US123456"  # Replace with the actual bill ID

selected_bill_id = ""

# LegiScan API endpoint for bill details
#endpoint = f"https://api.legiscan.com/?key={api_key}&op=getBill&id={bill_id}"
endpoint = "https://api.legiscan.com/?key=6ef4e9b53f820698d5d6a447dc7499c7&op=getBillText&id=1167968"
state_list_endpoint = "https://api.legiscan.com/?key=6ef4e9b53f820698d5d6a447dc7499c7&op=getMasterList&state=CA"

to_display = ""
num_bills = 0

resp2 = requests.get(state_list_endpoint)
if resp2.status_code == 200:
    list_data = resp2.json()
    to_display = "Bill " + list_data['masterlist']['0']['number'] + ": " + list_data['masterlist']['0']['title']
    #print(to_display)
    #print("# OF BILLS: " + str(len(list_data['masterlist'])))
    num_bills = len(list_data['masterlist'])




# Make the request
response = requests.get(endpoint)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    bill_data = response.json()
    #print(bill_data)

    # Extract the text of the bill
    bill_text = bill_data['text']['doc']

    # Do something with the bill text
    #print(bill_text)
    # UNCOMMENT LATER - print(base64.b64decode(bill_text))
else:
    print(f"Error: {response.status_code} - {response.text}")

import streamlit as st
#st.markdown(base64.b64decode(bill_text), unsafe_allow_html=True)


#def remove_text_before_phrase(input_string, target_phrase):
    #index = input_string.find(target_phrase)
    #if index != -1:
        #return input_string[index:]
    #else:
        #return input_string

def remove_text_before(input_string, flag_phrase):
    index = input.string.find(flag_phrase)
    if index != -1:
        return input_string.split(flag_phrase)

# Example usage:
input_text = base64.b64decode(bill_text)
#st.write(type(input_text))
input_text_str = str(input_text, encoding='utf-8')
#st.write(type(input_text_str))
# st.markdown(input_text_str, unsafe_allow_html=True) #VERY IMPORTANT -- UNCOMMENT LATER - 

#opts2 = []
#opts2_ids = []
bills_dict = {"id": "title"}

for i in range(10): # change 10 to num_bills later
    print( "Bill " + list_data['masterlist'][str(i)]['number'] + ": " + list_data['masterlist'][str(i)]['title'])
    #opts2.append("Bill " + list_data['masterlist'][str(i)]['number'] + ": " + list_data['masterlist'][str(i)]['title'])
    current_title = "Bill " + list_data['masterlist'][str(i)]['number'] + ": " + list_data['masterlist'][str(i)]['title']
    #opts2_ids.append(list_data['masterlist'][str(i)]['bill_id'])
    current_id = list_data['masterlist'][str(i)]['bill_id']
    bills_dict.update({current_id: current_title})
#print(opts2)
#print(opts2_ids)
print(bills_dict)
#print("https://api.legiscan.com/?key=6ef4e9b53f820698d5d6a447dc7499c7&op=getBillText&id=" + str(opts2_ids[0]))


def update_text_summary(c_e):

    response = requests.get(c_e)
    st.write("GETTING " + c_e)
    if response.status_code == 200:
        bill_data = response.json()
        bill_text = bill_data['text']['doc']
    else:
        print(f"Error: {response.status_code} - {response.text}")
    #st.write("TEXT :  " + bill_text)
    decoded_bytes = base64.b64decode(bill_text)
    # Handle the decoded bytes appropriately
    try:
        # Attempt to decode the bytes using UTF-8
        decoded_string = decoded_bytes.decode("utf-8")
        print("Decoded string:", decoded_string)
    except UnicodeDecodeError:
        # Handle the case where decoding as UTF-8 fails
        print("Decoding as UTF-8 failed. Do something else with the bytes.")
    #st.write(input_text)
    input_text_str = str(input_text, encoding='utf-8')
    #st.write(input_text_str)
    #st.markdown(input_text_str, unsafe_allow_html=True)
    return input_text_str



option = st.selectbox(
    'Which bill would you like to learn more about?',
    bills_dict.values()) #, index=None, placeholder="Select one below...")

st.write('You selected:', option)
position = list(bills_dict.values()).index(option)
#print(list(bills_dict.keys())[position])

clicked_endpoint = "https://api.legiscan.com/?key=6ef4e9b53f820698d5d6a447dc7499c7&op=getBillText&id=" + str(list(bills_dict.keys())[position])
st.markdown(update_text_summary(clicked_endpoint), unsafe_allow_html=True)
#st.write(clicked_endpoint)

# --------------

# --------------




def show_summary():
    update_text_summary()
    #st.write(input_text)
    st.markdown(input_text_str, unsafe_allow_html=True)


# IF MUTLI BUTTON ROW:
#col1, col2 = st.columns([1,1])
#with col1:
    #if st.button('Summarize'):
        #show_summary()
#with col2:
    #st.button('Read Official Document')

#if st.button('Summarize'):
    #show_summary()
    #update_text_summary()




#if st.button("Summarize"):
#    st.markdown(input_text_str, unsafe_allow_html=True)


#st.write(type("the type of this is"))
target_phrase = "AN ACT CONCERNING"

#result = remove_text_before_phrase(input_text, target_phrase)
#print(result)
#st.markdown(result, unsafe_allow_html=True)