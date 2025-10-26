import streamlit as st
from teen_patti import RANKS, SUITS, win_probability

st.set_page_config(page_title="Teen Patti Odds Simulator", page_icon="🃏", layout="centered")

st.title("🃏 Teen Patti Odds Simulator")
st.write("Estimate your probability of winning based on your hand and number of players.")

# --- Sidebar Inputs ---
st.sidebar.header("Game Settings")
num_players = st.sidebar.slider("Number of players", min_value=2, max_value=10, value=5)

st.sidebar.header("Select Your Hand")
col1, col2, col3 = st.sidebar.columns(3)
rank1, suit1 = col1.selectbox("Card 1 Rank", RANKS), col1.selectbox("Suit for Card 1", SUITS)
rank2, suit2 = col2.selectbox("Card 2 Rank", RANKS), col2.selectbox("Suit for Card 2", SUITS)
rank3, suit3 = col3.selectbox("Card 3 Rank", RANKS), col3.selectbox("Suit for Card 3", SUITS)

your_hand = [f"{rank1} of {suit1}", f"{rank2} of {suit2}", f"{rank3} of {suit3}"]

if len(set(your_hand)) < 3:
    st.error("⚠️ Each card must be unique.")
else:
    if st.button("🎲 Calculate Win Probability"):
        with st.spinner("Simulating rounds..."):
            prob = win_probability(your_hand, num_players=num_players, trials=50000)
        st.success(f"✅ Estimated Win Probability: **{prob*100:.2f}%**")

        st.caption("Simulation based on 50,000 random trials.")
