import streamlit as st

st.set_page_config(page_title="Partick Litter Plan", page_icon="🌿")

if 'sbstate' not in st.session_state:
    st.session_state.sbstate = 'collapsed'

# Main heading
st.title('Partick Litter Plan 🌿')
st.write("Partick is our home. It's dirty. Let's clean it up together!")

# Poster Section
with st.expander("🌿 Free Poster"):
    st.write("Please download and share the Partick Litter Plan poster!")
    st.image('images/Partick_Litter_Plan.jpg', width=200)
    with open('images/Partick_Litter_Plan.pdf', "rb") as file:
        btn = st.download_button(
                label="Download Poster PDF",
                data=file,
                file_name="Partick_litter_Plsn.pdf",
                mime="image/pdf"
              )
        
# Links Section
with st.expander("🔗 Useful Links"):
    """
    [Glasgow City Council: Bins and Recycling](https://www.glasgow.gov.uk/index.aspx?articleid=15893)
    Partick Action On Litter Facebook Group](https://www.facebook.com/PartickActiononLitter)
    """
    st.page_link("pages/Links.py", label = "Find more on our links page", icon="🔗")

# Supermarket Recycling section
with st.expander("🛒 Supermarket Recycling"):
    st.write("**Recycling at Supermarkets:**")
    st.write("Only **Morrisons** and **Marks & Spencer** currently accept plastic packaging for recycling.")
    st.write('**Action:**')
    st.write('Ask your supermarket to start recycling plastic packaging.')
    st.write('Encourage them to use less plastic in food packaging.')

# Hints section
with st.expander("🛍️ Hints & Tips"):
    st.write('Always carry reusable shopping bags. Use them every time you shop.')
    st.write('Ask **Glasgow City Council** to add more recycling and rubbish bins in key areas.')
    st.write('Never drop litter. Teach kids the importance of keeping our community clean.')

# Join Litter-Picking Events section
with st.expander("🧹 Join Litter-Picking Events"):
    st.write('**Community Clean-Up:***')
    st.write('Join a litter-picking event. It’s fun and great for the community. Get involved!')
    st.markdown('[Join the Partick Action on Litter group on Facebook!](https://www.facebook.com/PartickActiononLitter/)')
    
# Spread the Word section
with st.expander("💬 Spread the Word"):
    st.write('**Be Vocal:**')
    st.write('Make Partick a dear clean place. Share your efforts with hashtags:')
    st.write('#PartickLitterPlan #LessPlasticMorePartick')

st.page_link("pages/Chatbot.py", label = "Questions? Ask the PARTICK LITTER CHATBOT!", icon="🤖")

st.write('#PartickLitterPlan #LessPlasticMorePartick')
