# import streamlit as st

# def show_history():
#     st.markdown("<h2 style='color:#22c55e; text-align:center; font-weight:800;'>📜 Scan History</h2>", unsafe_allow_html=True)
    
#     # Check if history exists
#     if not st.session_state.get('scan_history'):
#         st.info("Paji, halle tak koi resume scan nahi kita. Dashboard te ja ke scan karo!")
#         return

#     # Display records in Reverse (Latest first)
#     for idx, item in enumerate(reversed(st.session_state.scan_history)):
#         st.markdown(f"""
#         <div style="
#             background: rgba(255, 255, 255, 0.05); 
#             backdrop-filter: blur(10px); 
#             padding: 20px; 
#             border-radius: 15px; 
#             border-left: 6px solid #22c55e; 
#             border-top: 1px solid rgba(255, 255, 255, 0.1);
#             margin-bottom: 20px;
#         ">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <h4 style="margin: 0; color: white;">📄 {item['name']}</h4>
#                 <span style="background: #22c55e; color: white; padding: 5px 15px; border-radius: 20px; font-weight: 800;">
#                     {item['score']}% Match
#                 </span>
#             </div>
#             <p style="color: #94a3b8; font-size: 14px; margin-top: 10px;">
#                 <b>Keywords Found:</b> {item.get('date', 'Today')} | ATS Optimization Active
#             </p>
#         </div>
#         """, unsafe_allow_html=True)



# import streamlit as st

# def show_history():
#      st.markdown("""
#         <style>
#         /* Expander Hover Fix: Mouse hatan te white nahi hoyega */
#         div[data-testid="stExpander"] details summary {
#             background-color: rgba(255, 255, 255, 0.05) !important;
#             color: white !important;
#             transition: none !important;
#         }
#         div[data-testid="stExpander"] details summary:hover {
#             background-color: rgba(255, 255, 255, 0.1) !important;
#             color: white !important;
#         }

#         /* Button Hover Fix: Mouse piche karan te white background khatam */
#         div.stButton > button {
#             background-color: #1e293b !important;
#             color: white !important;
#             border: 1px solid rgba(255, 255, 255, 0.1) !important;
#             transition: none !important;
#         }
#         div.stButton > button:hover {
#             background-color: #ef4444 !important; /* Delete button red highlight */
#             color: white !important;
#             border: 1px solid #ef4444 !important;
#         }
#         div.stButton > button:active, div.stButton > button:focus {
#             background-color: #1e293b !important;
#             color: white !important;
#         }
#         </style>
#     """, unsafe_allow_html=True) 
#      st.markdown("<h2 style='color:#22c55e; text-align:center; font-weight:800;'>📜 Scan History</h2>", unsafe_allow_html=True)
    
#      if not st.session_state.get('scan_history'):
#         st.info("Paji, halle tak koi resume scan nahi kita. Dashboard te ja ke scan karo!")
#         return

#     # Display records in Reverse (Latest first)
#     # We use a copy of the list to handle index correctly during deletion
#      history_list = list(reversed(st.session_state.scan_history))
    
#      for idx, item in enumerate(history_list):
#         # Original index in the actual session_state list
#         original_idx = len(st.session_state.scan_history) - 1 - idx
        
#         # CARD START (Your exact CSS)
#         st.markdown(f"""
#         <div style="
#             background: rgba(255, 255, 255, 0.05); 
#             backdrop-filter: blur(10px); 
#             padding: 20px; 
#             border-radius: 15px; 
#             border-left: 6px solid #22c55e; 
#             border-top: 1px solid rgba(255, 255, 255, 0.1);
#             margin-bottom: 5px;
#         ">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <h4 style="margin: 0; color: white;">📄 {item['name']}</h4>
#                 <span style="background: #22c55e; color: white; padding: 5px 15px; border-radius: 20px; font-weight: 800;">
#                     {item['score']}% Match
#                 </span>
#             </div>
#             <p style="color: #94a3b8; font-size: 14px; margin-top: 10px;">
#                 <b>Keywords Found:</b> {item.get('date', 'Today')} | ATS Optimization Active
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # DELETE BUTTON (Placed just below the glass card)
#         if st.button(f"🗑️ Delete {item['name']}", key=f"del_{original_idx}"):
#             st.session_state.scan_history.pop(original_idx)
#             st.rerun()
        
#         st.markdown("<br>", unsafe_allow_html=True)



import streamlit as st

def show_history():
    
    st.markdown("<h2 style='color:#22c55e; text-align:center; font-weight:800;'>📜 Scan History</h2>", 
                unsafe_allow_html=True)
    
    if not st.session_state.get('scan_history'):
        st.info("Firstly! Scan Your Resume Then History Appears")
        return

    # Display records in Reverse (Latest first)
    history_list = list(reversed(st.session_state.scan_history))
    
    for idx, item in enumerate(history_list):
        # Original index logic
        original_idx = len(st.session_state.scan_history) - 1 - idx
        
        # CARD START (Glassmorphism CSS)
        st.markdown(f"""
        <div style="
            background: rgba(255, 255, 255, 0.05); 
            backdrop-filter: blur(10px); 
            padding: 20px; 
            border-radius: 15px; 
            border-left: 6px solid #22c55e; 
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 5px;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin: 0; color: white;">📄 {item['name']}</h4>
                <span style="background: #22c55e; color: white; padding: 5px 15px; border-radius: 20px; font-weight: 800;">
                    {item['score']}% Match
                </span>
            </div>
            <p style="color: #94a3b8; font-size: 14px; margin-top: 10px;">
                <b>Keywords Found:</b> {item.get('date', 'Today')} | ATS Optimization Active
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- NEW: AI FEEDBACK TOGGLE (Expander) ---
        # Je feedback save kitta hoya hai, taan hi dikhayega
        if "feedback" in item and item["feedback"]:
            with st.expander(f"💡 View AI Feedback for {item['name']}"):
                st.markdown(f"""
                    <div style="background: rgba(34, 197, 94, 0.1); padding: 15px; border-radius: 10px; border: 1px solid #22c55e;">
                        <p style="color: white; line-height: 1.6;">{item['feedback']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No detailed feedback saved for this scan.")

        # DELETE BUTTON
        if st.button(f"🗑️ Delete {item['name']}", key=f"del_{original_idx}"):
            st.session_state.scan_history.pop(original_idx)
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)

