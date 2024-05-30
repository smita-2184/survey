import random
from collections import Counter
import streamlit as st
st.set_page_config(page_title="Survey Assignment", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
import streamlit.components.v1 as components

# Function to read survey links from a file
def get_survey_links():
    try:
        with open("survey_links.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        st.error("Error: survey_links.txt file not found!")
        return []  # Return empty list if file not found


# Function to pick a random link with usage tracking
def get_random_link(links, link_counts):
    # Shuffle the links to randomize selection order
    random.shuffle(links)

    # Count the occurrences of each link
    counts = link_counts.copy()

    for link in links:
        if counts[link] < 10:
            return link.strip()  # Return first available link

    return None  # No links available


# Function to update link usage counts
def update_link_counts(link, link_counts):
    link_counts[link] += 1

with st.popover("Contact us 📧"):
    st.markdown("Email us @ studium-eduai@gmail.com")
survey = st.button("Start Survey")
if survey:
    # Initialize link usage counts (dictionary)
    link_counts = Counter()

    # Example usage
    links = get_survey_links()

    # Simulate assigning a random link with usage tracking
    assigned_link = get_random_link(links, link_counts)
    if assigned_link:
        # Update usage count after assigning the link
        update_link_counts(assigned_link, link_counts)
        st.write("Start your survey here using this link: ", assigned_link , " or directly complete it below 👇")
        components.iframe(assigned_link, height=700)
        
    else:
        st.write("No surveys available (all links used 10 times)")
