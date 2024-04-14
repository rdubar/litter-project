import streamlit as st

st.set_page_config(page_title="The Partick Litter Project", page_icon=":robot:")

if 'sbstate' not in st.session_state:
    st.session_state.sbstate = 'collapsed'

# Main heading
st.title('The Partick Litter Manifesto 🌿')
st.write("Partick is our home. It's under siege from litter. Together, we can restore its glow.")

# Supermarket Recycling section
with st.expander("🛒 Supermarket Recycling"):
    st.write("**Recycling at Supermarkets:**")
    st.write("Only **Morrisons** and **Marks & Spencer** currently accept plastic packaging for recycling.")
    st.write('**Action:**')
    st.write('Ask your supermarket to start recycling plastic packaging.')
    st.write('Encourage them to use less plastic in food packaging.')

# Ask for More Bins section
with st.expander("🚮 Ask for More Bins"):
    st.write('**Need More Bins:**')
    st.write('Partick needs more bins!')
    st.write('Ask **Glasgow City Council** to add more recycling and rubbish bins in key areas.')

# Bring Your Own Bag section
with st.expander("🛍️ Bring Your Own Bag"):
    st.write('**Reusable Bags:**')
    st.write('Always carry reusable shopping bags. Use them every time you shop.')

# Join Litter-Picking Events section
with st.expander("🧹 Join Litter-Picking Events"):
    st.write('**Community Clean-Up:***')
    st.write('Join a litter-picking event. It’s fun and great for the community. Get involved!')
    st.markdown('[Join the Partick Action on Litter group on Facebook!](https://www.facebook.com/PartickActiononLitter/)')


# Teach and Practice section
with st.expander("🚯 Teach and Practice"):
    st.write('**No Littering:**')
    st.write('Never drop litter. Teach kids the importance of keeping our community clean.')

# Spread the Word section
with st.expander("💬 Spread the Word"):
    st.write('**Be Vocal:**')
    st.write('Make Partick a dear clean place. Share your efforts with hashtags:')
    st.write('#DearCleanPlace #LessPlasticMorePartick')

st.page_link("pages/Chatbot.py", label = "Questions? Ask the PARTICK LITTER CHATBOT!", icon="🤖")

st.write('#DearCleanPlace #LessPlasticMorePartick')