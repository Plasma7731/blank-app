import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.let_it_rain import rain
def dumbbell_rain():
    rain(
        emoji="🏋️‍♂️",
        font_size=53,
        falling_speed=4,
        animation_length=1.3,
    )
# Set page config
st.set_page_config(page_title="Bicep Strength Study", layout="wide", page_icon="💪")
GITHUB_IMAGE_URL = "https://raw.githubusercontent.com/Plasma7731/image/6d2c854ac3945a0ef57982188d7644c26e907211/Gemini_Generated_Image_cvf9w3cvf9w3cvf9.png"
GITHUB_IMAGE_URL2 = "https://raw.githubusercontent.com/Plasma7731/image/caa1c71656bf8258306aa9e96aa8e2b66c21c5c6/cssf2.png"
# 1. DATA LOADING (Based on your provided dataset)
def load_data():
    raw_data = [
        {'subject_id': 1, 'subject_name': 'Chuck', 'side': 'Right', 'angle_deg': 180, 'measurement': 3.0},
        {'subject_id': 2, 'subject_name': 'Klemens', 'side': 'Right', 'angle_deg': 180, 'measurement': 10.0},
        {'subject_id': 3, 'subject_name': 'Louis', 'side': 'Right', 'angle_deg': 180, 'measurement': 20.0},
        {'subject_id': 4, 'subject_name': 'Gaspard', 'side': 'Right', 'angle_deg': 180, 'measurement': 3.0},
        {'subject_id': 5, 'subject_name': 'Leon', 'side': 'Right', 'angle_deg': 180, 'measurement': 13.0},
        {'subject_id': 6, 'subject_name': 'Quan', 'side': 'Right', 'angle_deg': 180, 'measurement': 5.0},
        {'subject_id': 1, 'subject_name': 'Chuck', 'side': 'Right', 'angle_deg': 135, 'measurement': 6.0},
        {'subject_id': 2, 'subject_name': 'Klemens', 'side': 'Right', 'angle_deg': 135, 'measurement': 15.0},
        {'subject_id': 3, 'subject_name': 'Louis', 'side': 'Right', 'angle_deg': 135, 'measurement': 21.0},
        {'subject_id': 4, 'subject_name': 'Gaspard', 'side': 'Right', 'angle_deg': 135, 'measurement': 2.0},
        {'subject_id': 5, 'subject_name': 'Leon', 'side': 'Right', 'angle_deg': 135, 'measurement': 18.0},
        {'subject_id': 6, 'subject_name': 'Quan', 'side': 'Right', 'angle_deg': 135, 'measurement': 13.0},
        {'subject_id': 1, 'subject_name': 'Chuck', 'side': 'Right', 'angle_deg': 90, 'measurement': 21.0},
        {'subject_id': 2, 'subject_name': 'Klemens', 'side': 'Right', 'angle_deg': 90, 'measurement': 25.0},
        {'subject_id': 3, 'subject_name': 'Louis', 'side': 'Right', 'angle_deg': 90, 'measurement': 23.0},
        {'subject_id': 4, 'subject_name': 'Gaspard', 'side': 'Right', 'angle_deg': 90, 'measurement': 3.0},
        {'subject_id': 5, 'subject_name': 'Leon', 'side': 'Right', 'angle_deg': 90, 'measurement': 17.0},
        {'subject_id': 6, 'subject_name': 'Quan', 'side': 'Right', 'angle_deg': 90, 'measurement': 17.0},
        {'subject_id': 1, 'subject_name': 'Chuck', 'side': 'Left', 'angle_deg': 180, 'measurement': 3.0},
        {'subject_id': 2, 'subject_name': 'Klemens', 'side': 'Left', 'angle_deg': 180, 'measurement': 8.0},
        {'subject_id': 3, 'subject_name': 'Louis', 'side': 'Left', 'angle_deg': 180, 'measurement': 20.0},
        {'subject_id': 4, 'subject_name': 'Gaspard', 'side': 'Left', 'angle_deg': 180, 'measurement': 1.0},
        {'subject_id': 5, 'subject_name': 'Leon', 'side': 'Left', 'angle_deg': 180, 'measurement': 8.0},
        {'subject_id': 6, 'subject_name': 'Quan', 'side': 'Left', 'angle_deg': 180, 'measurement': 3.0},
        {'subject_id': 1, 'subject_name': 'Chuck', 'side': 'Left', 'angle_deg': 135, 'measurement': 0.0},
        {'subject_id': 2, 'subject_name': 'Klemens', 'side': 'Left', 'angle_deg': 135, 'measurement': 15.0},
        {'subject_id': 3, 'subject_name': 'Louis', 'side': 'Left', 'angle_deg': 135, 'measurement': 21.0},
        {'subject_id': 4, 'subject_name': 'Gaspard', 'side': 'Left', 'angle_deg': 135, 'measurement': 1.0},
        {'subject_id': 5, 'subject_name': 'Leon', 'side': 'Left', 'angle_deg': 135, 'measurement': 9.0},
        {'subject_id': 6, 'subject_name': 'Quan', 'side': 'Left', 'angle_deg': 135, 'measurement': 10.0},
        {'subject_id': 2, 'subject_name': 'Klemens', 'side': 'Left', 'angle_deg': 90, 'measurement': 18.0},
        {'subject_id': 3, 'subject_name': 'Louis', 'side': 'Left', 'angle_deg': 90, 'measurement': 23.0},
        {'subject_id': 4, 'subject_name': 'Gaspard', 'side': 'Left', 'angle_deg': 90, 'measurement': 2.0},
        {'subject_id': 5, 'subject_name': 'Leon', 'side': 'Left', 'angle_deg': 90, 'measurement': 19.0},
        {'subject_id': 6, 'subject_name': 'Quan', 'side': 'Left', 'angle_deg': 90, 'measurement': 23.0}
    ]
    return pd.DataFrame(raw_data).dropna(subset=['measurement'])

df = load_data()

# 2. SIDEBAR
from streamlit_option_menu import option_menu

with st.sidebar:
    page = option_menu(
        menu_title=None, 
        options=["Background Research", "Experiment Method", "Data", "Conclusion"],
        icons=["book", "clipboard-check", "graph-up", "check2-circle"], # Optional icons
        menu_icon="cast", 
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#262730"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {
                "font-size": "20px",        # Bigger font
                "text-align": "left", 
                "margin": "10px",           # Further apart
                "--hover-color": "#444"
            },
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )
# --- PAGE 1: RESEARCH ---
if page == "Background Research":
    st.title("💪 How Angle Affects Bicep Performance")
    st.image(GITHUB_IMAGE_URL, width='stretch')
    st.markdown("### The Length-Tension Relationship")
    

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("The Theory")
        st.info("""
        "As a muscle elongates so streaches out, the overlap between actin and myosin decreases which is the fibers in your muscle, reducing the effort" (Brookbush Institute). 
        Theoretically, the higher the angle (more stretched), the lower the performance.
        """)
    with col2:
        st.subheader("The Adaptation")
        st.warning("""
        Past training can change results! Some studies show that training in a specific position can lead 
        to adapting and getting used to that position(Rhea 43).
        """)

    st.divider()
    st.header("🧠 Make Your Prediction!")
    user_guess = st.select_slider("Based on the research, which angle will allow for the MOST repetitions?", options=[180, 135, 90])
    if st.button("Lock in Prediction"):
        st.session_state['guess'] = user_guess
        st.balloons()
# --- PAGE 2: METHOD ---
elif page == "Experiment Method":
    st.title("Materials & Procedure")
    st.image(GITHUB_IMAGE_URL2, width='stretch')
    with st.expander("Materials List"):
        st.write("* 2x 10kg dumbbells")
        st.write("* Joint angle measurement tool (Goniometer)")
        st.write("* Reference table for consistent angles")

    st.subheader("The Method")
    st.write("The 14 steps used in our study:")
    
    # Checkbox style for students to 'follow along'
    steps = [
        "1. Subject stands straight, knees slightly bent at shoulder level.",
        "2. Elbows kept touching the side; back must not move.",
        "3. Assistant ensures form criteria are followed.",
        "4. Subject puts hand down to a straight, stretched-out position.",
        "5. Measurement tool checks that the arm is exactly 180 degrees.",
        "6. Subject contracts arm up to the shoulder while keeping elbow stuck to side.",
        "7. Retract to the same starting position.",
        "8. One rep is counted.",
        "9. Repeat until the subject is not able to contract the bicep.",
        "10. Final result is recorded; subject takes a break.",
        "11. Repeat experiment starting from 135 degrees.",
        "12. Assistant puts hand under the subject's hand at 135° to ensure consistent range.",
        "13. Repeat reps, returning only to the 135-degree mark.",
        "14. Repeat all points at 90 degrees."
    ]
    
    for step in steps:
        st.checkbox(step)

# --- PAGE 3: DATA ---
elif page == "Data":
    st.title("Results")
    st.write("We calculated the average dumbbell curl at each joint angle degree. Use the filters to explore.")

    subjects = st.multiselect("Select Subjects:", options=df['subject_name'].unique(), default=df['subject_name'].unique())
    filtered_df = df[df['subject_name'].isin(subjects)]

    # Graph 1: The Main Curve
    # Graph 1: Individual Participant Performance
    st.subheader("Individual Participant Curves")
    
    show_avg = st.toggle("Show Group Average Line", value=False)

    if st.button("🚀 Reveal Strength Lines"):
        dumbbell_rain()
        
        # 1. Create the figure with a line for each person
        fig = px.line(
            filtered_df, 
            x='angle_deg', 
            y='measurement', 
            color='subject_name',  # This creates one line per person in different colors
            markers=True,
            title="Performance by Participant",
            labels={'angle_deg': 'Joint Angle', 'measurement': 'Reps', 'subject_name': 'Participant'}
        )

        # 2. Optional: Add a thick black dashed line for the average
        if show_avg:
            avg_data = filtered_df.groupby('angle_deg')['measurement'].mean().reset_index()
            fig.add_scatter(
                x=avg_data['angle_deg'], 
                y=avg_data['measurement'], 
                mode='lines+markers',
                name='AVERAGE',
                line=dict(color='black', width=4, dash='dash')
            )

        # Ensure the X-axis only shows your specific test angles
        fig.update_layout(xaxis=dict(tickmode='array', tickvals=[90, 135, 180]))
        
        st.plotly_chart(fig, use_container_width=True)
    # Graphs 2 and 3: Side-by-Side Comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Left vs Right Arm")
        if st.button("📊 Show Side Comparison"):
            dumbbell_rain()
            side_data = filtered_df.groupby(['side', 'angle_deg'])['measurement'].mean().reset_index()
            fig2 = px.bar(side_data, x='angle_deg', y='measurement', color='side', barmode='group', 
                          title="Performance by Arm Side")
            st.plotly_chart(fig2, use_container_width=True)
            
    with col2:
        st.subheader("Data Consistency")
        if st.button("📦 Show Data Spread (Box Plot)"):
            dumbbell_rain()
            fig3 = px.box(filtered_df, x='angle_deg', y='measurement', 
                          title="Consistency Check per Angle")
            st.plotly_chart(fig3, use_container_width=True)
# --- PAGE 4: CONCLUSION ---
elif page == "Conclusion":
    st.title("Conclusion")
    
    st.header("Summary of Findings")
    st.success("""
    Based on the data collected, the smaller the angle of the joint, the easier it is for the bicep to 
    move, leading to more repetitions. 
    """)
    
    st.subheader("Interesting Observations")
    st.write("""
    * **Training Adaptation:** We saw that training at a specific angle (like 90°) can mean that 
    muscles adapt to that position, leading to minimal changes between angles.
    * **Outliers:** One subject scored high on every angle but showed a very weak pattern change. 
    Another experienced a limit of 3 reps across the board.
    * **Isometric Effect:** The 90-degree pull resembles an isometric exercise(it doesnt move and stays in one position) more than larger angles, 
    providing more muscle stimulation but sustained tension.
    """)

    st.subheader("Points of Improvement")
    st.info("""
    Next time, we could use more monitoring for form. Hands of helpers sometimes moved, and subjects 
    occasionally 'cheated' unknowingly by making smaller movements to get higher numbers!
    """)
    
    if st.button("View Bibliography"):
        st.markdown("""
        1. **Brookbush Institute.** "Length-Tension Relationship."
        2. **Rhea, M. R.** "Human Movement 17 (1) 2016."
        3. **Lee, Sabrina Eun Kyung.** "Isometric strength training outcomes."
        """)
