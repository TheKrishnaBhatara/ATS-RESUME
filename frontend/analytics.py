# import streamlit as st
# import plotly.graph_objects as go

# def show_analytics():
#     st.markdown("<h2 style='color:#22c55e; text-align:center; font-weight:800;'>📊 Matching Analytics</h2>", unsafe_allow_html=True)

#     if not st.session_state.get('scan_history'):
#         st.warning("Analytics dekhan layi pehla resume scan karo.")
#         return

#     # Get the latest scan data
#     latest = st.session_state.scan_history[-1]

#     # --- GAUGE CHART ---
#     fig = go.Figure(go.Indicator(
#         mode = "gauge+number",
#         value = latest['score'],
#         domain = {'x': [0, 1], 'y': [0, 1]},
#         title = {'text': f"Latest Result: {latest['name']}", 'font': {'color': "white", 'size': 20}},
#         gauge = {
#             'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
#             'bar': {'color': "#22c55e"},
#             'bgcolor': "rgba(0,0,0,0)",
#             'borderwidth': 2,
#             'bordercolor': "#444",
#             'steps': [
#                 {'range': [0, 40], 'color': 'rgba(255, 0, 0, 0.3)'},
#                 {'range': [40, 75], 'color': 'rgba(255, 165, 0, 0.3)'},
#                 {'range': [75, 100], 'color': 'rgba(34, 197, 94, 0.3)'}
#             ],
#             'threshold': {
#                 'line': {'color': "white", 'width': 4},
#                 'thickness': 0.75,
#                 'value': 80
#             }
#         }
#     ))

#     fig.update_layout(
#         paper_bgcolor='rgba(0,0,0,0)', 
#         plot_bgcolor='rgba(0,0,0,0)', 
#         font={'color': "white", 'family': "Inter"}
#     )

#     # Display Gauge in a Glass Card
#     st.markdown('<div style="background:rgba(255,255,255,0.03); padding:20px; border-radius:20px; border:1px solid rgba(255,255,255,0.1);">', unsafe_allow_html=True)
#     st.plotly_chart(fig, use_container_width=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     # --- COMPARISON TABLE ---
#     if len(st.session_state.scan_history) > 1:
#         st.markdown("<br><h3 style='color:white;'>🔄 Recent Comparisons</h3>", unsafe_allow_html=True)
#         # Create a clean data table for comparison
#         comp_data = []
#         for x in st.session_state.scan_history[-5:]: # Last 5 records
#             comp_data.append({
#                 "Resume Name": x['name'],
#                 "ATS Score": f"{x['score']}%",
#                 "Status": "✅ Strong" if x['score'] > 70 else "⚠️ Needs Work"
#             })
#         st.table(comp_data)




import streamlit as st
import plotly.graph_objects as go

def show_analytics():
    # --- DELETE ALL SECTION ---
    col_title, col_del = st.columns([3, 1])
    with col_title:
        st.markdown("<h2 style='color:#22c55e; font-weight:800;'>📊 Matching Analytics</h2>", unsafe_allow_html=True)
    
    if not st.session_state.get('scan_history'):
        st.warning("Firstly Scan Resume then See Resume Analytics")
        return

    # Get the latest scan data
    latest = st.session_state.scan_history[-1]

    # --- GAUGE CHART (Your exact logic) ---
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = latest['score'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Latest Result: {latest['name']}", 'font': {'color': "white", 'size': 20}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#22c55e"},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "#444",
            'steps': [
                {'range': [0, 40], 'color': 'rgba(255, 0, 0, 0.3)'},
                {'range': [40, 75], 'color': 'rgba(255, 165, 0, 0.3)'},
                {'range': [75, 100], 'color': 'rgba(34, 197, 94, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        font={'color': "white", 'family': "Inter"}
    )

    # Display Gauge in a Glass Card (Your exact CSS)
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- COMPARISON TABLE ---
    if len(st.session_state.scan_history) > 1:
        st.markdown("<br><h3 style='color:white;'>🔄 Recent Comparisons</h3>", unsafe_allow_html=True)
        comp_data = []
        for x in st.session_state.scan_history[-5:]: # Last 5 records
            comp_data.append({
                "Resume Name": x['name'],
                "ATS Score": f"{x['score']}%",
                "Status": "✅ Strong" if x['score'] > 70 else "⚠️ Needs Work"
            })
        st.table(comp_data)