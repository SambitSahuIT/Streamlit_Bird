from bardapi import Bard 
import streamlit as st
from streamlit_chat import message

import os
os.environ['_BARD_API_KEY']="YAhi70m7MPPMduUaCkgkJaN_wt4qrPWFi7iVZhWCqt7JMWSsuUly43Q296UtRM8cQcMskQ."
bard = Bard(timeout = 100)

# Define a function to generate tweets
def generate_tweet(prompt):
    # prompt = f"Content: {content}\nType: {tweet_type}\nTweet:"
    # cannot set hyper-parameters
    response = bard.get_answer(prompt)
    tweet = response['content']
    return tweet

# Streamlit web app
def main():
    st.title(" Text Generator")
    content=st.text_input("Enter the content you want to generate!")
    mood_of_content=st.text_input("Enter the type of content:")
    platform=st.selectbox("Enter the platform you want to post the generated text:",
                        ('Instagram', 'LinkedIn Post', 'Notion Article', 'Tweet'))
    length=st.slider("Enter the length of the content you want to generate:",min_value=50,max_value=700)
    fprompt = f"Write a {mood_of_content} {platform} post about {content} within {length} character"
    fprompt  


    # Generate button  
    if st.button("Generate"):
            # Generate tweet
        tweet = generate_tweet(fprompt)
        # Display generated tweet
        st.success(tweet)

if __name__ == "__main__":
    main()
