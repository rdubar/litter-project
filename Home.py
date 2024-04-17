import streamlit as st

st.set_page_config(page_title="Partick Litter Plan", page_icon="🌿")

if 'sbstate' not in st.session_state:
    st.session_state.sbstate = 'collapsed'

# Main heading
st.title('Partick Litter Plan 🌿')
st.write("Partick is our home. It's dirty. You can help clean it up!")

# Poster Section
with st.expander("🌿 Get Your Free Poster"):
    st.write("Download and share the Partick Litter Plan poster!")
    st.image('images/Partick_Litter_Plan.jpg', width=200)
    with open('images/Partick_Litter_Plan.pdf', "rb") as file:
        btn = st.download_button(
                label="Download Poster PDF",
                data=file,
                file_name="Partick_litter_Plsn.pdf",
                mime="image/pdf"
              )   
    
# Hints section
with st.expander("🛍️ How you can help"):
    """
    * Always carry reusable shopping bags. Use them every time you shop.
    * Ask Glasgow City Council to add more recycling and rubbish bins in key areas.
    * Never drop litter. Teach kids the importance of keeping our community clean.
    * Join a litter-picking event. They're fun and you will make a real difference.
    """
        
# Links Section
with st.expander("🔗 Handy Links"):
    """
    * [Glasgow City Council: Bins and Recycling](https://www.glasgow.gov.uk/index.aspx?articleid=15893)
    * Partick Action On Litter Facebook Group](https://www.facebook.com/PartickActiononLitter)
    """
    st.page_link("pages/5_Links.py", label = "Find more on our links page", icon="🔗")

# Supermarket Recycling section
with st.expander("🛒 Supermarket Action"):
    """
    * Currently only **Morrisons** and **Marks & Spencer** currently accept plastic packaging for recycling.
    * Ask your supermarket to collect plastic packaging for recycling.
    * Encourage them to use less plastic in food packaging.
    """ 

# Join Litter-Picking Events section
with st.expander("🧹 Litter-Picking Events"):
    """
    * Go on a litter-picking event. They're fun and great for the community. Get involved!
    * [Join the Partick Action on Litter group on Facebook!](https://www.facebook.com/PartickActiononLitter/)
    """
    
# Spread the Word section
with st.expander("💬 Spread the Word"):
    """
    * Be vocal! Share your efforts with hashtags: #PartickLitterPlan #LessPlasticMorePartick
    * [Email the Partick Litter Plan team](mailto:partick@dubar.com)
    """
    
# Chatbot Section
with st.expander("🤖 Partick Litter Plan Chatbot"):
    """
    Do you have questions about:
    * Plastics and recycling
    * Wildlife in the River Kelvin
    * The history of Partick
    * Anything else?
    """
    st.page_link("pages/2_Chatbot.py", label = "Ask the Partick Litter Chatbot!", icon="🤖")
