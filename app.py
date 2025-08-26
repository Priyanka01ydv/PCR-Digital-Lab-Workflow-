import streamlit as st
import pandas as pd

st.set_page_config(page_title="Digital Lab Workflow - OneLab Style", layout="centered")

st.title("🧪 Digital Lab Workflow Simulator")
st.write("A OneLab-style tool for digitizing wet-lab experiments.")

# Experiment selection
experiment = st.selectbox("Choose Experiment:", ["PCR"])

# PCR Workflow
if experiment == "PCR":
    st.header("PCR Protocol")
    samples = st.number_input("Number of samples:", min_value=1, value=5)
    reaction_volume = st.number_input("Reaction volume per sample (µL):", min_value=10, value=25)

    # Define reagents (per reaction, µL)
    reagents = {
        "DNA template": 2,
        "Forward primer": 1,
        "Reverse primer": 1,
        "dNTPs": 0.5,
        "Buffer": 5,
        "Taq polymerase": 0.5,
        "Water": reaction_volume - (2 + 1 + 1 + 0.5 + 5 + 0.5)
    }

    # Calculate total reagent needs
    reagent_data = []
    for reagent, vol in reagents.items():
        total = vol * samples
        reagent_data.append([reagent, vol, total])

    df = pd.DataFrame(reagent_data, columns=["Reagent", "Per Sample (µL)", f"Total for {samples} samples (µL)"])

    st.subheader("📊 Reagent Requirements")
    st.dataframe(df, use_container_width=True)

    # Workflow steps
    st.subheader("🧾 Workflow Steps")
    steps = [
        "1. Thaw all reagents on ice.",
        "2. Mix reagents according to calculated volumes.",
        "3. Aliquot into PCR tubes.",
        "4. Load into thermocycler and run program:",
        "   - Denaturation: 95°C for 30 sec",
        "   - Annealing: 55°C for 30 sec",
        "   - Extension: 72°C for 1 min",
        "   - Repeat for 30 cycles",
        "5. Store amplified DNA at -20°C."
    ]
    for step in steps:
        st.markdown(f"- {step}")

    # Download protocol
    st.download_button(
        label="📥 Download Protocol (CSV)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="PCR_Protocol.csv",
        mime="text/csv"
    )

