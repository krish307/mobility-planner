import streamlit as st

# -------------------------------
# DATA & CONSTANTS
# -------------------------------

EMISSION_FACTORS = {
    "walking": 0,
    "cycling": 0,
    "bus": 82,
    "car": 192,
    "ev": 50
}

TRAFFIC_PENALTY = {
    "low": 1.0,
    "medium": 1.2,
    "high": 1.5
}

# -------------------------------
# MODEL LOGIC
# -------------------------------

def sustainability_score(distance, mode, traffic):
    emission = distance * EMISSION_FACTORS[mode]
    traffic_impact = TRAFFIC_PENALTY[traffic]
    return emission * traffic_impact


def recommend_mode(distance, traffic):
    modes = ["walking", "cycling", "bus", "ev", "car"]
    scores = {}

    for mode in modes:
        scores[mode] = sustainability_score(distance, mode, traffic)

    best_mode = min(scores, key=scores.get)
    return best_mode, scores

# -------------------------------
# STREAMLIT UI
# -------------------------------

st.set_page_config(page_title="Sustainable Mobility Planner")

st.title("🌱 Sustainable Mobility Planner")
st.write("Find the most eco-friendly transport option based on distance and traffic.")

distance = st.number_input(
    "Enter Distance (km)",
    min_value=0.1,
    step=0.1
)

traffic = st.selectbox(
    "Select Traffic Level",
    ["low", "medium", "high"]
)

if st.button("Find Best Eco-Friendly Mode"):

    best_mode, scores = recommend_mode(distance, traffic)

    st.subheader("📊 Sustainability Scores (Lower is Better)")
    for mode, score in scores.items():
        st.write(f"{mode.capitalize()} → {score:.2f}")

    st.success(f"✅ Recommended Transport Mode: {best_mode.upper()}")

    st.info("This recommendation minimizes carbon emissions and traffic impact.")
