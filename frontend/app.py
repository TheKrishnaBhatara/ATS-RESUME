# import streamlit as st
# import requests

# st.title("AI ATS Resume Screening System")

# uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# resume_text = ""

# if uploaded_file is not None:
#     files = {"file": uploaded_file.getvalue()}
#     res = requests.post("http://127.0.0.1:8000/upload", files=files)

#     if res.status_code == 200:
#         resume_text = res.json().get("resume_text", "")
#         st.text_area("Extracted Resume", resume_text, height=200)
#     else:
#         st.error("Error extracting resume")

# jd_text = st.text_area("Paste Job Description")

# if st.button("Analyze"):

#     if resume_text.strip() == "" or jd_text.strip() == "":
#         st.error("Please upload resume and provide job description")
#     else:
#         response = requests.post(
#             "http://127.0.0.1:8000/rank",
#             params={
#                 "resume_text": resume_text,
#                 "jd_text": jd_text
#             }
#         )

#         if response.status_code == 200:
#             result = response.json()
#         else:
#             st.error("Backend Error: " + response.text)
#             st.stop()

#         score = result.get("final_score", 0)

#         st.markdown(f"<h1 style='text-align:center;color:green;'>{score}%</h1>", unsafe_allow_html=True)
#         st.progress(int(score))

#         st.subheader("📊 Results")
#         st.write("Similarity:", result.get("similarity", 0), "%")
#         st.write("Skill Score:", result.get("skill_score", 0), "%")

#         st.subheader("❗ Missing Skills")
#         for skill in result.get("missing_skills", []):
#             st.write("•", skill)

#         st.subheader("🤖 AI Feedback")
#         st.write(result.get("ai_feedback", "No feedback"))

# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # ---------------- PROFESSIONAL CSS (React-Style) ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     /* Background Gradient */
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Professional Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
#     .nav-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

#     /* Glassmorphism Card */
#     .main-card {
#         background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px);
#         border-radius: 30px; padding: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#         box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
#     }

#     /* Labels & Inputs */
#     .custom-label { font-size: 16px; font-weight: 600; color: #000000; margin-bottom: 10px; display: block; }
    
#     div[data-testid="stFileUploadDropzone"] {
#         background: white !important; border-radius: 12px !important;
#         border: 2px dashed #22c55e !important; color: black !important;
#     }
#     div[data-testid="stFileUploadDropzone"] button { color: black !important; }

#     .stTextArea textarea { 
#         background-color: white !important; color: black !important; 
#         border-radius: 12px !important; border: none !important;
#     }

#     /* Analyze Button with Yellow Hover */
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#         border: none !important; transition: 0.4s all ease;
#     }
#     div.stButton > button:hover {
#         background: #facc15 !important; color: black !important;
#         box-shadow: 0 0 30px rgba(250, 204, 21, 0.7); transform: translateY(-2px);
#     }

#     /* Results Styling */
#     .result-score { font-size: 60px; font-weight: 800; color: #22c55e; text-align: center; }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- NAVBAR ----------------
# st.markdown("""
#     <div class="nav-container">
#         <div class="nav-logo">AI ATS PRO</div>
#         <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 15px;">
#             <span>Dashboard</span><span>History</span><span>Pro Plan</span>
#         </div>
#         <div class="nav-btn">Sign Out</div>
#     </div>
# """, unsafe_allow_html=True)

# # ---------------- MAIN APP LAYOUT ----------------
# col_l, col_mid, col_r = st.columns([1, 2, 1])

# with col_mid:
#     st.markdown('<div class="main-card">', unsafe_allow_html=True)
#     st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h2>", unsafe_allow_html=True)

#     # 1. UPLOAD SECTION
#     st.markdown('<span class="custom-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

#     resume_text = ""
#     if uploaded_file is not None:
#         files = {"file": uploaded_file.getvalue()}
#         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#         if res.status_code == 200:
#             resume_text = res.json().get("resume_text", "")
#             st.success("Resume Extracted Successfully!")
#         else:
#             st.error("Error extracting resume")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # 2. JD SECTION
#     st.markdown('<span class="custom-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#     jd_text = st.text_area("", placeholder="Enter the job requirements...", height=150, label_visibility="collapsed")

#     # 3. ANALYZE BUTTON
#     if st.button("Analyze"):
#         if resume_text.strip() == "" or jd_text.strip() == "":
#             st.error("Please upload resume and provide job description")
#         else:
#             with st.spinner("AI is calculating your score..."):
#                 response = requests.post(
#                     "http://127.0.0.1:8000/rank",
#                     params={"resume_text": resume_text, "jd_text": jd_text}
#                 )

#                 if response.status_code == 200:
#                     result = response.json()
#                     score = result.get("final_score", 0)

#                     # PROFESSIONAL RESULTS DISPLAY
#                     st.markdown(f"<div class='result-score'>{score}%</div>", unsafe_allow_html=True)
#                     st.progress(int(score))

#                     st.markdown("### 📊 Metrics")
#                     c1, c2 = st.columns(2)
#                     c1.metric("Similarity", f"{result.get('similarity', 0)}%")
#                     c2.metric("Skill Score", f"{result.get('skill_score', 0)}%")

#                     st.markdown("### ❗ Missing Skills")
#                     skills = result.get("missing_skills", [])
#                     if skills:
#                         st.write(", ".join([f"**{s}**" for s in skills]))
#                     else:
#                         st.write("No major skills missing!")

#                     st.markdown("### 🤖 AI Feedback")
#                     st.info(result.get("ai_feedback", "No feedback"))
#                 else:
#                     st.error("Backend Error: " + response.text)

#     st.markdown("<p style='text-align:center; color:#94a3b8; font-size:12px; margin-top:20px;'>🔒 256-bit Encrypted. Your data is secure.</p>", unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- FOOTER STEPS ----------------
# st.markdown("""
#     <div style="display: flex; gap: 20px; margin-top: 50px; padding: 0 20px;">
#         <div style="flex: 1; background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1);">
#             <div style="background: #22c55e; color: white; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; margin-bottom: 15px;">01</div>
#             <h3 style="margin:0;">Semantic Analysis</h3>
#             <p style="color:#94a3b8; font-size:14px;">We use AI to understand the context of your experience.</p>
#         </div>
#         <div style="flex: 1; background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1);">
#             <div style="background: #22c55e; color: white; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; margin-bottom: 15px;">02</div>
#             <h3 style="margin:0;">Keyword Matching</h3>
#             <p style="color:#94a3b8; font-size:14px;">We find industry-specific keywords that you're missing.</p>
#         </div>
#     </div>
# """, unsafe_allow_html=True)
# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener. All rights reserved.</p>", unsafe_allow_html=True)









# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
#     .nav-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

#     /* Glassmorphism Card */
#     .main-card {
#         background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px);
        
#     }

#     /* Labels */
#     .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }
    
#     /* Inputs */
#     div[data-testid="stFileUploadDropzone"] {
#         background: white !important; border-radius: 12px !important;
#         border: 2px dashed #22c55e !important;
#     }
#     div[data-testid="stFileUploadDropzone"] button { color: black !important; }
#     div[data-testid="stFileUploadDropzone"] i { display: none !important; }

#     .stTextArea textarea { 
#         background-color: white !important; color: black !important; 
#         border-radius: 12px !important; border: none !important;
#     }

#     /* Extracted Text Box Styling */
#     .extracted-box {
#         background: rgba(255, 255, 255, 0.05);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 15px;
#         padding: 15px;
#         color: #94a3b8;
#         font-size: 14px;
#         max-height: 200px;
#         overflow-y: auto;
#         margin-top: 10px;
#     }

#     /* Analyze Button with Yellow Hover */
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#         border: none !important; margin-top: 20px; transition: 0.4s all ease;
#     }
#     div.stButton > button:hover {
#         background: #facc15 !important; color: black !important;
#         box-shadow: 0 0 30px rgba(250, 204, 21, 0.7); transform: translateY(-2px);
#     }

#     .result-score { font-size: 60px; font-weight: 800; color: #22c55e; text-align: center; margin-top: 20px; }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- NAVBAR ----------------
# st.markdown("""
#     <div class="nav-container">
#         <div class="nav-logo">AI ATS PRO</div>
#         <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 15px;">
#             <span>Dashboard</span><span>Features</span><span>Pricing</span>
#         </div>
#         <div class="nav-btn">Get Started</div>
#     </div>
# """, unsafe_allow_html=True)

# # ---------------- MAIN APP ----------------
# col_l, col_mid, col_r = st.columns([1, 2, 1])

# with col_mid:
#     st.markdown('<div class="main-card">', unsafe_allow_html=True)
#     st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1>", unsafe_allow_html=True)

#     # 1. UPLOAD SECTION
#     st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

#     resume_text = ""
#     if uploaded_file is not None:
#         files = {"file": uploaded_file.getvalue()}
#         res = requests.post("http://127.0.0.1:8000/upload", files=files)
        
#         if res.status_code == 200:
#             resume_text = res.json().get("resume_text", "")
#             # 🔥 Show Extracted Text in a nice React-style box
#             st.markdown('<span class="yellow-label">📄 Extracted Content</span>', unsafe_allow_html=True)
#             st.markdown(f'<div class="extracted-box">{resume_text[:1000]}...</div>', unsafe_allow_html=True)
#             st.caption("✅ Data parsed successfully")
#         else:
#             st.error("Error extracting resume")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # 2. JD SECTION
#     st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#     jd_text = st.text_area("", placeholder="Paste job requirements here...", height=150, label_visibility="collapsed")

#     # 3. ANALYZE BUTTON
#     if st.button("Analyze"):
#         if resume_text.strip() == "" or jd_text.strip() == "":
#             st.warning("Please upload a resume and provide a job description first.")
#         else:
#             with st.spinner("AI is analyzing your profile..."):
#                 response = requests.post(
#                     "http://127.0.0.1:8000/rank",
#                     params={"resume_text": resume_text, "jd_text": jd_text}
#                 )

#                 if response.status_code == 200:
#                     result = response.json()
#                     score = result.get("final_score", 0)

#                     # Display Score
#                     st.markdown(f"<div class='result-score'>{score}%</div>", unsafe_allow_html=True)
#                     st.progress(int(score))

#                     # Results Detail
#                     st.markdown("### 📊 Analysis Breakdown")
#                     c1, c2 = st.columns(2)
#                     c1.metric("Similarity", f"{result.get('similarity', 0)}%")
#                     c2.metric("Skill Match", f"{result.get('skill_score', 0)}%")

#                     st.markdown("### 🤖 AI Recommendation")
#                     st.info(result.get("ai_feedback", "Everything looks good!"))
#                 else:
#                     st.error("Backend connection failed.")

#     st.markdown("<p style='text-align:center; color:#94a3b8; font-size:12px; margin-top:20px;'>🔒 100% Privacy Guaranteed</p>", unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- FOOTER ----------------
# st.markdown("""
#     <div style="display: flex; gap: 20px; margin-top: 50px; padding: 0 20px;">
#         <div style="flex: 1; background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.08);">
#             <div style="background: #22c55e; color: white; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; margin-bottom: 15px;">01</div>
#             <h3 style="margin:0;">Instant Scan</h3>
#             <p style="color:#94a3b8; font-size:14px;">We process your data using high-speed AI inference.</p>
#         </div>
#         <div style="flex: 1; background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.08);">
#             <div style="background: #22c55e; color: white; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; margin-bottom: 15px;">02</div>
#             <h3 style="margin:0;">Detailed Insights</h3>
#             <p style="color:#94a3b8; font-size:14px;">Get specific feedback on what keywords you are missing.</p>
#         </div>
#     </div>
# """, unsafe_allow_html=True)
# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener. All rights reserved.</p>", unsafe_allow_html=True)






# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
#     .nav-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

#     /* Glassmorphism Card */
#     .main-card {
#         background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px);
        
#     }

#     /* Labels */
#     .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }
    
#     /* 🔥 UPLOADER BUTTON LOGIC CHANGE 🔥 */
#     div[data-testid="stFileUploadDropzone"] {
#         background: white !important; border-radius: 12px !important;
#         border: 2px dashed #22c55e !important;
#     }
    
#     /* Browse files button: White background & Black text */
#     button[data-testid="stBaseButton-secondary"] { 
#         background-color: white !important; 
#         color: black !important; 
#         border: 1px solid black !important;
#         font-weight: 700 !important;
#     }
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1);
#         color: #22c55e;
#         padding: 5px 15px;
#         border-radius: 50px;
#         font-size: 11px;
#         font-weight: 800;
#         letter-spacing: 1.5px;
#         border: 1px solid rgba(34, 197, 94, 0.3);
#         display: inline-block;
#         margin-bottom: 15px;
#         margin-left:200px;
#         text-transform: uppercase;
#     }
#     /* Drag & drop text to black for visibility on white bg */
#     div[data-testid="stFileUploadDropzone"] section div {
#         color: black !important;
#     }
    
#     div[data-testid="stFileUploadDropzone"] i { display: none !important; }

#     .stTextArea textarea { 
#         background-color: white !important; color: black !important; 
#         border-radius: 12px !important; border: none !important;
#     }

#     /* Extracted Text Box Styling */
#     .extracted-box {
#         background: rgba(255, 255, 255, 0.05);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 15px;
#         padding: 15px;
#         color: #94a3b8;
#         font-size: 14px;
#         max-height: 200px;
#         overflow-y: auto;
#         margin-top: 10px;
#     }

#     /* Analyze Button with Yellow Hover */
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#         border: none !important; margin-top: 20px; transition: 0.4s all ease;
#     }
#     div.stButton > button:hover {
#         background: #facc15 !important; color: black !important;
#         box-shadow: 0 0 30px rgba(250, 204, 21, 0.7); transform: translateY(-2px);
#     }

#     .result-score { font-size: 60px; font-weight: 800; color: #22c55e; text-align: center; margin-top: 20px; }
# </style>
# """, unsafe_allow_html=True)

# # # ---------------- NAVBAR ----------------
# st.markdown("""
#     <div class="nav-container">
#         <div class="nav-logo">AI ATS PRO</div>
#         <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 15px;">
#             <span>Resume Builder</span>Dashboard</span><span>Features</span><span>Pricing</span>
#         </div>
#         <div class="nav-btn">Get Started</div>
#     </div>
# """, unsafe_allow_html=True)

# # # ---------------- MAIN APP ----------------
# col_l, col_mid, col_r = st.columns([1, 2, 1])


# with col_mid:
#     st.markdown('<div class="ai-badge">✨ AI POWERED TECHNOLOGY</div>', unsafe_allow_html=True)
#     st.markdown('<div class="main-card">', unsafe_allow_html=True)
#     st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1>", unsafe_allow_html=True)

#     # 1. UPLOAD SECTION
#     st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

#     resume_text = ""
#     if uploaded_file is not None:
#         files = {"file": uploaded_file.getvalue()}
#         res = requests.post("http://127.0.0.1:8000/upload", files=files)
        
#         if res.status_code == 200:
#             resume_text = res.json().get("resume_text", "")
#             st.markdown('<span class="yellow-label">📄 Extracted Content</span>', unsafe_allow_html=True)
#             st.markdown(f'<div class="extracted-box">{resume_text[:1000]}...</div>', unsafe_allow_html=True)
#             st.caption("✅ Data parsed successfully")
#         else:
#             st.error("Error extracting resume")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # 2. JD SECTION
#     st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#     jd_text = st.text_area("", placeholder="Paste job requirements here...", height=150, label_visibility="collapsed")

#     # 3. ANALYZE BUTTON
#     if st.button("Analyze"):
#         if resume_text.strip() == "" or jd_text.strip() == "":
#             st.warning("Please upload a resume and provide a job description first.")
#         else:
#             with st.spinner("AI is analyzing your profile..."):
#                 response = requests.post(
#                     "http://127.0.0.1:8000/rank",
#                     params={"resume_text": resume_text, "jd_text": jd_text}
#                 )

#                 if response.status_code == 200:
#                     result = response.json()
#                     score = result.get("final_score", 0)

#                     st.markdown(f"<div class='result-score'>{score}%</div>", unsafe_allow_html=True)
#                     st.progress(int(score))

#                     st.markdown("### 📊 Analysis Breakdown")
#                     c1, c2 = st.columns(2)
#                     c1.metric("Similarity", f"{result.get('similarity', 0)}%")
#                     c2.metric("Skill Match", f"{result.get('skill_score', 0)}%")

#                     st.markdown("### 🤖 AI Recommendation")
#                     st.info(result.get("ai_feedback", "Everything looks good!"))
#                 else:
#                     st.error("Backend connection failed.")

#     st.markdown("<p style='text-align:center; color:#94a3b8; font-size:12px; margin-top:20px;'>🔒 100% Privacy Guaranteed</p>", unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # # ---------------- FOOTER ----------------
# st.markdown("""
#     <div style="display: flex; gap: 20px; margin-top: 50px; padding: 0 20px;">
#         <div style="flex: 1; background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.08);">
#             <div style="background: #22c55e; color: white; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; margin-bottom: 15px;">01</div>
#             <h3 style="margin:0;">Instant Scan</h3>
#             <p style="color:#94a3b8; font-size:14px;">We process your data using high-speed AI inference.</p>
#         </div>
#         <div style="flex: 1; background: rgba(255, 255, 255, 0.03); padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.08);">
#             <div style="background: #22c55e; color: white; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; margin-bottom: 15px;">02</div>
#             <h3 style="margin:0;">Detailed Insights</h3>
#             <p style="color:#94a3b8; font-size:14px;">Get specific feedback on what keywords you are missing.</p>
#         </div>
#     </div>
# """, unsafe_allow_html=True)
# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener. All rights reserved.</p>", unsafe_allow_html=True)





#correct
# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
#     .nav-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

#     /* Glassmorphism Card */
#     .main-card {
#         background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px);
        
#     }

#     /* AI Badge */
#     .ai-badge-container { text-align: center; width: 100%; margin-bottom: 10px; }
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1);
#         color: #22c55e;
#         padding: 5px 15px;
#         border-radius: 50px;
#         font-size: 11px;
#         font-weight: 800;
#         letter-spacing: 1.5px;
#         margin-right:50px;
#         border: 1px solid rgba(34, 197, 94, 0.3);
#         display: inline-block;
#         text-transform: uppercase;
#     }

#     .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }
    
#     /* Uploader */
#     div[data-testid="stFileUploadDropzone"] {
#         background: white !important; border-radius: 12px !important;
#         border: 2px dashed #22c55e !important;
#     }
#     button[data-testid="stBaseButton-secondary"] { 
#         background-color: white !important; color: black !important; 
#         border: 1px solid black !important; font-weight: 700 !important;
#     }
#     div[data-testid="stFileUploadDropzone"] section div { color: black !important; }
#     div[data-testid="stFileUploadDropzone"] i { display: none !important; }

#     .stTextArea textarea { 
#         background-color: white !important; color: black !important; 
#         border-radius: 12px !important; border: none !important;
#     }

#     .extracted-box {
#         background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 15px; padding: 15px; color: #94a3b8; font-size: 14px;
#         max-height: 200px; overflow-y: auto; margin-top: 10px;
#     }

#     /* Analyze Button */
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#         border: none !important; margin-top: 20px; transition: 0.4s all ease;
#     }
#     div.stButton > button:hover {
#         background: #facc15 !important; color: black !important;
#         box-shadow: 0 0 30px rgba(250, 204, 21, 0.7); transform: translateY(-2px);
#     }

#     .result-score { font-size: 60px; font-weight: 800; color: #22c55e; text-align: center; margin-top: 20px; }

#     /* Footer Cards 01 & 02 */
#     .footer-card {
#         background: rgba(255, 255, 255, 0.03); 
#         padding: 30px; 
#         border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.08);
#         height: 100%;
#     }
#     .footer-number {
#         background: #22c55e; color: white; width: 35px; height: 35px; 
#         display: flex; align-items: center; justify-content: center; 
#         border-radius: 50%; font-weight: 800; margin-bottom: 15px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- NAVBAR ----------------
# st.markdown("""
#     <div class="nav-container">
#         <div class="nav-logo">AI ATS PRO</div>
#         <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 15px;">
#             <span>Resume Builder</span><span>Dashboard</span><span>Features</span><span>Pricing</span>
#         </div>
#         <div class="nav-btn">Get Started</div>
#     </div>
# """, unsafe_allow_html=True)

# # ---------------- MAIN APP ----------------
# col_l, col_mid, col_r = st.columns([1, 2, 1])

# with col_mid:
#     st.markdown('<div class="ai-badge-container"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div>', unsafe_allow_html=True)
#     st.markdown('<div class="main-card">', unsafe_allow_html=True)
#     st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1>", unsafe_allow_html=True)

#     # 1. UPLOAD SECTION
#     st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

#     resume_text = ""
#     if uploaded_file is not None:
#         files = {"file": uploaded_file.getvalue()}
#         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#         if res.status_code == 200:
#             resume_text = res.json().get("resume_text", "")
#             st.markdown('<span class="yellow-label">📄 Extracted Content</span>', unsafe_allow_html=True)
#             st.markdown(f'<div class="extracted-box">{resume_text[:1000]}...</div>', unsafe_allow_html=True)
#             st.caption("✅ Data parsed successfully")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # 2. JD SECTION
#     st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#     jd_text = st.text_area("", placeholder="Paste job requirements here...", height=150, label_visibility="collapsed")

#     # 3. ANALYZE BUTTON
#     if st.button("Analyze"):
#         if resume_text.strip() == "" or jd_text.strip() == "":
#             st.warning("Please upload a resume and provide a job description first.")
#         else:
#             with st.spinner("AI is analyzing..."):
#                 response = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                 if response.status_code == 200:
#                     result = response.json()
#                     score = result.get("final_score", 0)
#                     st.markdown(f"<div class='result-score'>{score}%</div>", unsafe_allow_html=True)
#                     st.progress(int(score))
                    
#                     st.markdown("### 📊 Results")
#                     c1, c2 = st.columns(2)
#                     c1.metric("Similarity", f"{result.get('similarity', 0)}%")
#                     c2.metric("Skill Match", f"{result.get('skill_score', 0)}%")

#                     st.subheader("❗ Missing Skills")
#                     missing = result.get("missing_skills", [])
#                     if missing:
#                         for s in missing: st.write(f"• {s}")
#                     else: st.write("✅ All skills found!")

#                     st.markdown("### 🤖 AI Recommendation")
#                     st.info(result.get("ai_feedback", "No feedback available."))

#     st.markdown("<p style='text-align:center; color:#94a3b8; font-size:12px; margin-top:20px;'>🔒 100% Privacy Guaranteed</p>", unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- FOOTER (01 & 02 Fixed) ----------------
# st.markdown("<br><br>", unsafe_allow_html=True)
# f_col1, f_col2,f_col3 = st.columns(3)

# with f_col1:
#     st.markdown("""
#         <div class="footer-card">
#             <div class="footer-number">01</div>
#             <h3 style="margin:0;">Instant Scan</h3>
#             <p style="color:#94a3b8; font-size:14px;">We process your data using high-speed AI inference.</p>
#         </div>
#     """, unsafe_allow_html=True)

# with f_col2:
#     st.markdown("""
#         <div class="footer-card">
#             <div class="footer-number">02</div>
#             <h3 style="margin:0;">Detailed Insights</h3>
#             <p style="color:#94a3b8; font-size:14px;">Get specific feedback on what keywords you are missing.</p>
#         </div>
#     """, unsafe_allow_html=True)

# with f_col3:
#     st.markdown("""
#         <div class="footer-card">
#             <div class="footer-number">03</div>
#             <h3 style="margin:0;">JD Matching</h3>
#             <p style="color:#94a3b8; font-size:14px;">Smart semantic matching beyond simple keyword counts.</p>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # Second Row: 04, 05, 06
# f_col4, f_col5, f_col6 = st.columns(3)

# with f_col4:
#     st.markdown("""
#         <div class="footer-card">
#             <div class="footer-number">04</div>
#             <h3 style="margin:0;">Privacy First</h3>
#             <p style="color:#94a3b8; font-size:14px;">Your resume data is processed securely and never stored.</p>
#         </div>
#     """, unsafe_allow_html=True)

# with f_col5:
#     st.markdown("""
#         <div class="footer-card">
#             <div class="footer-number">05</div>
#             <h3 style="margin:0;">AI Feedback</h3>
#             <p style="color:#94a3b8; font-size:14px;">Get personalized LLM-powered tips to improve ranking.</p>
#         </div>
#     """, unsafe_allow_html=True)

# with f_col6:
#     st.markdown("""
#         <div class="footer-card">
#             <div class="footer-number">06</div>
#             <h3 style="margin:0;">ATS Optimized</h3>
#             <p style="color:#94a3b8; font-size:14px;">Built to mimic top-tier Applicant Tracking Systems.</p>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener. All rights reserved.</p>", unsafe_allow_html=True)



# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Initialize Session State for Login
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
#     .nav-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

#     /* Login Card Styling (Matches your screenshot) */
#     .login-container {
        
#         color: white; text-align: center; max-width: 450px; margin: auto;
#         box-shadow: 0 10px 40px rgba(0,0,0,0.4);
#     }
#     .login-header { font-weight: 800; font-size: 28px; margin-bottom: 25px; color: white; }

#     /* Main Glassmorphism Card */
#     .main-card {
#         background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px);
#         border-radius: 30px; padding: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }

#     /* Labels & Badges */
#     .ai-badge-container { text-align: center; width: 100%; margin-bottom: 10px; }
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e; padding: 5px 15px;
#         border-radius: 50px; font-size: 11px; font-weight: 800; letter-spacing: 1.5px;
#         border: 1px solid rgba(34, 197, 94, 0.3); display: inline-block; text-transform: uppercase;
#     }
#     .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }

#     /* Uploader & Textarea overrides */
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; border: 2px dashed #22c55e !important; }
#     button[data-testid="stBaseButton-secondary"] { background-color: white !important; color: black !important; border: 1px solid black !important; font-weight: 700 !important; }
#     div[data-testid="stFileUploadDropzone"] section div { color: black !important; }
#     .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }

#     .extracted-box {
#         background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 15px; padding: 15px; color: #94a3b8; font-size: 14px;
#         max-height: 150px; overflow-y: auto; margin-top: 10px;
#     }

#     /* Analyze Button */
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#         border: none !important; margin-top: 20px; transition: 0.4s all ease;
#     }
#     div.stButton > button:hover { background: #facc15 !important; color: black !important; box-shadow: 0 0 30px rgba(250, 204, 21, 0.7); }

#     .result-score { font-size: 60px; font-weight: 800; color: #22c55e; text-align: center; margin-top: 20px; }

#     /* Footer Cards */
#     .footer-card {
#         background: rgba(255, 255, 255, 0.03); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.08); height: 100%;
#     }
#     .footer-number {
#         background: #22c55e; color: white; width: 35px; height: 35px; 
#         display: flex; align-items: center; justify-content: center; 
#         border-radius: 50%; font-weight: 800; margin-bottom: 12px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- LOGIN LOGIC ----------------
# if not st.session_state.logged_in:
#     st.markdown("<br><br><br>", unsafe_allow_html=True)
#     col1, col2, col3 = st.columns([1, 1.5, 1])
#     with col2:
#         st.markdown('<div class="login-container">', unsafe_allow_html=True)
#         st.markdown('<div class="login-header">Admin Login</div>', unsafe_allow_html=True)
#         user_input = st.text_input("Username", placeholder="Enter admin username")
#         pass_input = st.text_input("Password", type="password", placeholder="Enter password")
        
#         if st.button("Login"):
#             if user_input == "admin" and pass_input == "admin123":
#                 st.session_state.logged_in = True
#                 st.rerun()
#             else:
#                 st.error("Invalid username or password")
#         st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- MAIN APP (Only if logged in) ----------------
# else:
#     # --- NAVBAR ---
#     st.markdown("""
#         <div class="nav-container">
#             <div class="nav-logo">AI ATS PRO</div>
#             <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 15px;">
#                 <span>Resume Builder</span><span>Dashboard</span><span>Features</span><span>Pricing</span>
#             </div>
#             <div class="nav-btn">Admin Dashboard</div>
#         </div>
#     """, unsafe_allow_html=True)

#     col_l, col_mid, col_r = st.columns([1, 2, 1])

#     with col_mid:
#         st.markdown('<div class="ai-badge-container"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div>', unsafe_allow_html=True)
#         st.markdown('<div class="main-card">', unsafe_allow_html=True)
#         st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1>", unsafe_allow_html=True)

#         # 1. UPLOAD SECTION
#         st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#         uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

#         resume_text = ""
#         if uploaded_file is not None:
#             files = {"file": uploaded_file.getvalue()}
#             res = requests.post("http://127.0.0.1:8000/upload", files=files)
#             if res.status_code == 200:
#                 resume_text = res.json().get("resume_text", "")
#                 st.markdown('<span class="yellow-label">📄 Extracted Content</span>', unsafe_allow_html=True)
#                 st.markdown(f'<div class="extracted-box">{resume_text[:1000]}...</div>', unsafe_allow_html=True)
#                 st.caption("✅ Resume parsed successfully")

#         st.markdown("<br>", unsafe_allow_html=True)

#         # 2. JD SECTION
#         st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#         jd_text = st.text_area("", placeholder="Paste job requirements here...", height=150, label_visibility="collapsed")

#         # 3. ANALYZE LOGIC
#         if st.button("Analyze"):
#             if resume_text.strip() == "" or jd_text.strip() == "":
#                 st.warning("Please upload a resume and provide a job description first.")
#             else:
#                 with st.spinner("AI is calculating your ATS score..."):
#                     response = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                     if response.status_code == 200:
#                         result = response.json()
#                         score = result.get("final_score", 0)
                        
#                         st.markdown(f"<div class='result-score'>{score}%</div>", unsafe_allow_html=True)
#                         st.progress(int(score))
                        
#                         st.markdown("### 📊 Analysis Breakdown")
#                         c1, c2 = st.columns(2)
#                         c1.metric("Similarity", f"{result.get('similarity', 0)}%")
#                         c2.metric("Skill Match", f"{result.get('skill_score', 0)}%")

#                         # 🔥 MISSING SKILLS 🔥
#                         st.subheader("❗ Missing Skills")
#                         missing = result.get("missing_skills", [])
#                         if missing:
#                             for s in missing: st.write(f"• {s}")
#                         else: st.write("✅ All critical skills found!")

#                         st.markdown("### 🤖 AI Recommendation")
#                         st.info(result.get("ai_feedback", "Everything looks solid."))
#                     else:
#                         st.error("Backend connection failed.")

#         st.markdown("<p style='text-align:center; color:#94a3b8; font-size:12px; margin-top:20px;'>🔒 100% Privacy Guaranteed</p>", unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     # ---------------- FOOTER (01 to 06) ----------------
#     st.markdown("<br><br>", unsafe_allow_html=True)
    
#     # Row 1
#     f1, f2, f3 = st.columns(3)
#     with f1:
#         st.markdown('<div class="footer-card"><div class="footer-number">01</div><h3>Instant Scan</h3><p style="color:#94a3b8; font-size:14px;">High-speed AI inference for results.</p></div>', unsafe_allow_html=True)
#     with f2:
#         st.markdown('<div class="footer-card"><div class="footer-number">02</div><h3>Deep Insights</h3><p style="color:#94a3b8; font-size:14px;">Identify missing keywords easily.</p></div>', unsafe_allow_html=True)
#     with f3:
#         st.markdown('<div class="footer-card"><div class="footer-number">03</div><h3>JD Matching</h3><p style="color:#94a3b8; font-size:14px;">Smart semantic matching tech.</p></div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Row 2
#     f4, f5, f6 = st.columns(3)
#     with f4:
#         st.markdown('<div class="footer-card"><div class="footer-number">04</div><h3>Privacy First</h3><p style="color:#94a3b8; font-size:14px;">Your data is never stored.</p></div>', unsafe_allow_html=True)
#     with f5:
#         st.markdown('<div class="footer-card"><div class="footer-number">05</div><h3>AI Feedback</h3><p style="color:#94a3b8; font-size:14px;">Personalized tips for ranking.</p></div>', unsafe_allow_html=True)
#     with f6:
#         st.markdown('<div class="footer-card"><div class="footer-number">06</div><h3>ATS Optimized</h3><p style="color:#94a3b8; font-size:14px;">Mimics real-world screening.</p></div>', unsafe_allow_html=True)

#     st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener. All rights reserved.</p>", unsafe_allow_html=True)








##correct
# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Initialize Session State
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
            
#     /* Username te Password de labels nu white karan layi */
# label[data-testid="stWidgetLabel"] p {
#     color: white !important; 
#     font-weight: 700 !important; 
#     font-size: 16px !important;
# }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
            
#     .nav-admin-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

#     /* Login Card (White Inputs) */
#     .login-card {
        
#     }
#     .stTextInput input {
#         color: black !important; background: white !important;
#         border-radius: 10px !important; padding: 12px !important;
            
#     }
#    .nav-logout-btn button {
#         background: white !important; 
#         color: black !important; 
#         border-radius: 50px !important;
#         padding: 5px 25px !important;
#         font-weight: 700 !important;
#     }


    

#     /* Main Content */
#     .main-card {
#         b
#     }
#     .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }
    
#     /* White Uploader & Area */
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
#     .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }

#     /* --- FULL 6 SECTIONS FOOTER --- */
#     .footer-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 50px; }
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#     }
#     .footer-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.08); border-color: #22c55e; }
#     .footer-num { 
#         background: #22c55e; color: white; width: 35px; height: 35px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 15px; 
#     }
            
#             /* NAVBAR BUTTON FIX */
# .nav-container button {
#     background: transparent !important;
#     color: #94a3b8 !important;
#     border: none !important;
#     font-size: 14px !important;
#     font-weight: 600 !important;
#     cursor: pointer;
# }
            
#             /* AI Badge */
# #     .ai-badge {
# #         background: rgba(34, 197, 94, 0.1);
# #         color: #22c55e;
# #         border: 1px solid rgba(34, 197, 94, 0.3);
# #         padding: 6px 15px; border-radius: 50px;
# #         font-size: 11px; font-weight: 800; letter-spacing: 1.2px;
# #         display: inline-block; margin-bottom: 10px;
# #         box-shadow: 0 0 15px rgba(34, 197, 94, 0.1);
# #     }

# /* Hover effect (React wali feel 🔥) */
# .nav-container button:hover {
#     color: #22c55e !important;
# }

#     .footer-card h3 { font-size: 18px; margin-bottom: 10px; color: white; }
#     .footer-card p { font-size: 14px; color: #94a3b8; line-height: 1.5; }

#     /* Analyze Button */
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#     }
            
#     div.nav_container.nav_logo>button{
#             background:radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;

#     .nav-admin-btn > button {
#     color: black !important;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- LOGIN ----------------
# if not st.session_state.logged_in:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<div class="login-card">', unsafe_allow_html=True)
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀"):
#             if u == "admin" and p == "admin123":
#                 st.session_state.logged_in = True
#                 st.rerun()
#         st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- MAIN APP ----------------
# else:
#     # NAVBAR
#     st.markdown("""
#         <div class="nav-container">
#             <div class="nav-logo">AI ATS PRO</div>
#             <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 14px; font-weight: 600;">
#                 <span><button>Resume Builder</button></span><span><button>Dashboard</button></span><span><button>Features</button></span><span><button>Pricing</button></span>
#             </div>
#             <div class="nav-admin-btn"><button>Logout🔓</button></div>

#         </div>
#     """, unsafe_allow_html=True)

    

#     # SCANNER
#     _, mid, _ = st.columns([0.5, 2, 0.5])
#     _, mid, _ = st.columns([0.5, 2, 0.5])
#     with mid:
#         st.markdown("""
#             <div style="text-align: center;">
#                 <div class="ai-badge">✨ AI POWERED TECHNOLOGY</div>
                
#             </div><br>
#         """, unsafe_allow_html=True)
#         st.markdown('<div class="main-card">', unsafe_allow_html=True)
#         st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
        
#         st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#         st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#         st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
        
#         if st.button("Analyze Now ✨"):
#             st.info("Analysis in progress...")
#         st.markdown('</div>', unsafe_allow_html=True)

#     # --- THE 6 SECTIONS (FOOTER) ---
#     st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
    
#     f_row1 = st.columns(3)
#     features = [
#         ("01", "Instant Scan", "Deep text extraction from PDFs using advanced parsing algorithms."),
#         ("02", "Deep Insights", "Identifies the gap between your skills and the recruiter's expectations."),
#         ("03", "JD Matching", "Uses AI vector embeddings to check semantic similarity with the job role."),
#         ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers."),
#         ("05", "AI Feedback", "Actionable tips to improve your bullet points and keyword density."),
#         ("06", "ATS Optimized", "Calibrated to pass through filters of top ATS systems like Workday.")
#     ]

#     # Row 1
#     for i in range(3):
#         with f_row1[i]:
#             st.markdown(f'''<div class="footer-card"><div class="footer-number">{features[i][0]}</div><h3>{features[i][1]}</h3><p>{features[i][2]}</p></div>''', unsafe_allow_html=True)
    
#     st.markdown("<br>", unsafe_allow_html=True)
    
#     # Row 2
#     f_row2 = st.columns(3)
#     for i in range(3, 6):
#         with f_row2[i-3]:
#             st.markdown(f'''<div class="footer-card"><div class="footer-number">{features[i][0]}</div><h3>{features[i][1]}</h3><p>{features[i][2]}</p></div>''', unsafe_allow_html=True)

# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)




# # # import streamlit as st

# # # # ---------------- PAGE CONFIG ----------------
# # # st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # # # Initialize Session State
# # # if 'logged_in' not in st.session_state:
# # #     st.session_state.logged_in = False

# # # # ---------------- PROFESSIONAL CSS ----------------
# # # st.markdown("""
# # # <style>
# # #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
# # #     .stApp {
# # #         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
# # #         font-family: 'Inter', sans-serif;
# # #         color: white;
# # #     }

# # #     /* --- Navbar Styling (Hollow Tube) --- */
# # #     .nav-container {
# # #         display: flex; justify-content: space-between; align-items: center;
# # #         padding: 12px 40px; background: rgba(255, 255, 255, 0.03);
# # #         backdrop-filter: blur(15px); border-radius: 100px;
# # #         margin: 10px 0px 40px 0px; border: 1px solid rgba(255, 255, 255, 0.1);
# # #     }
# # #     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }

# # #     /* White Labels & Inputs */
# #     label[data-testid="stWidgetLabel"] p {
# #         color: white !important; font-weight: 700 !important; font-size: 16px !important;
# #     }
# #     .stTextInput input, .stTextArea textarea {
# #         color: black !important; background: white !important;
# #         border-radius: 10px !important; padding: 12px !important;
# #     }

# #     /* --- Footer 6 Sections (Same Height & Circle Num) --- */
# #     .footer-card {
# #         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
# #         border: 1px solid rgba(255, 255, 255, 0.1); 
# #         min-height: 230px; display: flex; flex-direction: column;
# #         transition: 0.3s;
# #     }
# #     .footer-num-circle { 
# #         background: #22c55e; color: white; width: 35px; height: 35px; 
# #         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
# #         font-weight: 800; margin-bottom: 15px;
# #     }
# #     .footer-card h3 { font-size: 19px; margin-bottom: 10px; color: white; }
# #     .footer-card p { font-size: 14px; color: #94a3b8; line-height: 1.5; }

# #     /* Buttons */
# #     div.stButton > button {
# #         width: 100%; background: #22c55e !important; color: white !important;
# #         font-weight: 800 !important; border-radius: 10px !important;
# #     }
# #     /* Inner Nav Logout Button Styling */
# #     .nav-logout-btn button {
# #         background: white !important; color: black !important; width: auto !important;
# #         padding: 5px 25px !important; font-size: 14px !important;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # ---------------- LOGIN PAGE ----------------
# # if not st.session_state.logged_in:
# #     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.2, 1])
#     with l_col:
#         st.markdown('<h2 style="text-align:center; color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u_input = st.text_input("Username", placeholder="admin")
#         p_input = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀"):
#             if u_input == "admin" and p_input == "admin123":
#                 st.session_state.logged_in = True
#                 st.rerun()

# # ---------------- DASHBOARD ----------------
# else:
#     # NAVBAR (Logout Inside the Tube)
#     st.markdown('<div class="nav-container">', unsafe_allow_html=True)
#     nc1, nc2, nc3 = st.columns([1.5, 3, 1])
#     with nc1:
#         st.markdown('<div class="nav-logo">AI ATS PRO</div>', unsafe_allow_html=True)
#     with nc2:
#         st.markdown('<div style="display:flex; gap:30px; color:#94a3b8; font-size:14px; font-weight:600; padding-top:8px;"><span>Resume Builder</span><span>Dashboard</span><span>Features</span><span>Pricing</span></div>', unsafe_allow_html=True)
#     with nc3:
#         # Logout button hun Tube de andar hi hai
#         st.markdown('<div class="nav-logout-btn">', unsafe_allow_html=True)
#         if st.button("Logout 🔓"):
#             st.session_state.logged_in = False
#             st.rerun()
#         st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     # MAIN SCANNER
#     _, mid, _ = st.columns([0.5, 2, 0.5])
#     with mid:
#         st.markdown('<div style="background:rgba(255,255,255,0.02); padding:40px; border-radius:30px; border:1px solid rgba(255,255,255,0.1);">', unsafe_allow_html=True)
#         st.markdown("<h1 style='text-align:center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
        
#         st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#         st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
#         st.markdown("<br><span style='color:yellow; font-weight:700;'>📝 Paste Job Description</span>", unsafe_allow_html=True)
#         st.text_area("", placeholder="Paste requirements here...", height=150, label_visibility="collapsed")
        
#         if st.button("Analyze Now ✨"):
#             st.info("Analysis in progress...")
#         st.markdown('</div>', unsafe_allow_html=True)

#     # FOOTER 6 SECTIONS
#     st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
    
#     features_list = [
#         ("01", "Instant Scan", "Deep text extraction from PDFs using advanced parsing algorithms for fast results."),
#         ("02", "Deep Insights", "Identifies the gap between your skills and recruiter's technical expectations."),
#         ("03", "JD Matching", "Uses AI vector embeddings to check semantic similarity with the target role."),
#         ("04", "Privacy First", "Your data is processed in-memory and is never stored on our secure servers."),
#         ("05", "AI Feedback", "Actionable tips to improve your bullet points and technical keyword density."),
#         ("06", "ATS Optimized", "Calibrated to pass through the filters of top ATS systems like Workday.")
#     ]

#     # Uniform Row Layout
#     r1 = st.columns(3)
#     for i in range(3):
#         with r1[i]:
#             st.markdown(f'''<div class="footer-card"><div class="footer-num-circle">{features_list[i][0]}</div><h3>{features_list[i][1]}</h3><p>{features_list[i][2]}</p></div>''', unsafe_allow_html=True)
    
#     st.markdown("<br>", unsafe_allow_html=True)
#     r2 = st.columns(3)
#     for i in range(3, 6):
#         with r2[i-3]:
#             st.markdown(f'''<div class="footer-card"><div class="footer-num-circle">{features_list[i][0]}</div><h3>{features_list[i][1]}</h3><p>{features_list[i][2]}</p></div>''', unsafe_allow_html=True)

# st.markdown("<br><br><p style='text-align:center; color:#4b5563; font-size:12px;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)









#correct hai

# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# import time

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # Tuhada Lottie Link
# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'show_loader' not in st.session_state:
#     st.session_state.show_loader = False

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#             .nav-container button {
#     background: transparent !important;
#     color: #94a3b8 !important;
#     border: none !important;
#     font-size: 14px !important;
#     font-weight: 600 !important;
#     cursor: pointer;
#             }
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#     }
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
            
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN SCREEN ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀",use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True # Loader state on karo
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")

# # ---------------- 2. LOADING ANIMATION (After Login) ----------------
# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         st.markdown("<br><br>", unsafe_allow_html=True)
#         st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         st.markdown("<p style='text-align:center; color:#94a3b8;'>Setting up secure environment for analysis</p>", unsafe_allow_html=True)
        
#         time.sleep(4) # Animation 4 second lyi dikhegi
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False # Loader band karo
#         st.rerun()

# # ---------------- 3. MAIN DASHBOARD ----------------
# else:
#     # NAVBAR
#     st.markdown("""
#         <div class="nav-container">
#             <div class="nav-logo">AI ATS PRO</div>
#             <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 14px; font-weight: 600;">
#                 <button><span>Resume Builder</span></button><button><span>Dashboard</span></button><button><span>History</span></button><button><span>Analytics</span></button>
#             </div>
#             <div class="nav-logout-btn">
#                 <a href="/" style="text-decoration:none;"><button style="background:white; color:black; border-radius:50px; padding:5px 20px; font-weight:700;">Logout 🔓</button></a>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

#     # SCANNER SECTION
#     _, mid, _ = st.columns([0.5, 2, 0.5])
#     with mid:
#         st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#         st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
        
#         st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#         res_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#         jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
        
#         if st.button("Analyze Now ✨"):
#             if res_file and jd_text:
#                 st.info("Analysis logic goes here (RapidAPI)...")
#             else:
#                 st.error("Paji, pehla file te JD fill karo!")

#     # FEATURES (FOOTER)
#     st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
#     features = [
#         ("01", "Instant Scan", "Deep text extraction from PDFs using advanced parsing algorithms."),
#         ("02", "Deep Insights", "Identifies the gap between your skills and the recruiter's expectations."),
#         ("03", "JD Matching", "Uses AI vector embeddings to check semantic similarity with the job role."),
#         ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers."),
#         ("05", "AI Feedback", "Actionable tips to improve your bullet points and keyword density."),
#         ("06", "ATS Optimized", "Calibrated to pass through filters of top ATS systems like Workday.")
#     ]

#     f_cols = st.columns(3)
#     for idx, (num, title, desc) in enumerate(features):
#         with f_cols[idx % 3]:
#             st.markdown(f'''
#                 <div class="footer-card">
#                     <div class="footer-number">{num}</div>
#                     <h3>{title}</h3>
#                     <p>{desc}</p>
#                 </div><br>
#             ''', unsafe_allow_html=True)

# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)


# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# import streamlit.components.v1 as components
# import time

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro | Futuristic", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         return r.json()
#     except: return None

# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"

# # ---------------- 1. MOVING STONES / PARTICLES BACKGROUND (HTML/JS) ----------------
# # Eh code poore background vich floating stones te particles chalaega
# particles_js = """
# <div id="tsparticles"></div>
# <script src="https://cdn.jsdelivr.net/npm/tsparticles-confetti@2.12.0/tsparticles.confetti.bundle.min.js"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/tsparticles/2.12.0/tsparticles.bundle.min.js"></script>
# <script>
# tsParticles.load("tsparticles", {
#   particles: {
#     number: { value: 60, density: { enable: true, value_area: 800 } },
#     color: { value: "#22c55e" },
#     shape: { type: "polygon", polygon: { nb_sides: 6 } }, // Hexagon stones
#     opacity: { value: 0.3, random: true },
#     size: { value: 5, random: true },
#     move: {
#       enable: true,
#       speed: 1.5,
#       direction: "none",
#       random: true,
#       straight: false,
#       out_mode: "out",
#       bounce: false,
#     },
#     line_linked: {
#       enable: true,
#       distance: 150,
#       color: "#22c55e",
#       opacity: 0.2,
#       width: 1
#     }
#   },
#   interactivity: {
#     detect_on: "canvas",
#     events: {
#       onhover: { enable: true, mode: "grab" },
#       onclick: { enable: true, mode: "push" }
#     }
#   },
#   retina_detect: true
# });
# </script>
# <style>
# #tsparticles {
#   position: fixed;
#   width: 100vw;
#   height: 100vh;
#   top: 0;
#   left: 0;
#   z-index: -1; /* Background de piche */
# }
# </style>
# """

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: #020617 !important; /* Dark theme for particles visibility */
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Glassmorphism Cards */
#     .glass-card {
#         background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px);
#         border-radius: 20px;
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         padding: 30px;
#         margin-bottom: 20px;
#     }

#     /* Navbar */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 10px 40px; background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(20px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }

#     div.stButton > button {
#         background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%) !important;
#         color: white !important; font-weight: 800 !important;
#         border-radius: 12px !important; border: none !important;
#         padding: 12px !important; transition: 0.4s;
#     }
#     div.stButton > button:hover {
#         box-shadow: 0 0 20px rgba(34, 197, 94, 0.5);
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Background Particles Chalao
# components.html(particles_js, height=0)

# # ---------------- 1. LOGIN SCREEN ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     # Adding extra space to center vertically
#     for _ in range(5): st.markdown("<br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.2, 1])
#     with l_col:
#         st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
#         st.markdown("<h1 style='color:#22c55e;'>AI ATS PRO</h1>", unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="••••••••")
#         if st.button("Access Dashboard ⚡", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else: st.error("Invalid Credentials!")
#         st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- 2. LOADER ----------------
# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         st.markdown("<br><br>", unsafe_allow_html=True)
#         st_lottie(lottie_scan, height=450, key="loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>CONNECTING TO NEURAL NETWORK...</h2>", unsafe_allow_html=True)
#         time.sleep(3)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 3. MAIN DASHBOARD ----------------
# else:
#     # NAVBAR
#     n1, n2, n3, n4, n5 = st.columns([2.5, 1, 1, 1, 1.2])
#     with n1: st.markdown("<h2 style='color:#22c55e; margin:0;'>AI ATS PRO</h2>", unsafe_allow_html=True)
#     with n2: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"
#     with n3:
#         if st.button("Builder"): st.session_state.page = "Builder"
#     with n4:
#         if st.button("History"): st.session_state.page = "History"
#     with n5:
#         if st.button("Logout 🔓"):
#             st.session_state.logged_in = False
#             st.rerun()
    
#     st.markdown("<br>", unsafe_allow_html=True)

#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.5, 2, 0.5])
#         with mid:
#             st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align:center;'>Analyze Your <span style='color:#22c55e;'>Potential</span></h1>", unsafe_allow_html=True)
            
#             st.markdown("<br><b style='color:yellow;'>📤 Resume Upload (PDF)</b>", unsafe_allow_html=True)
#             res_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
            
#             st.markdown("<br><b style='color:yellow;'>📝 Job Requirements</b>", unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             if st.button("Run AI Diagnostics ✨"):
#                 if res_file and jd_text:
#                     st.success("Particles Analysis Complete! Score: 92%")
#                 else: st.warning("Paji, data te pao pehla!")
#             st.markdown('</div>', unsafe_allow_html=True)

#         # Footer Stats
#         s1, s2, s3 = st.columns(3)
#         with s1: st.markdown('<div class="glass-card"><h3>Live Nodes</h3><p>60 Active Particles</p></div>', unsafe_allow_html=True)
#         with s2: st.markdown('<div class="glass-card"><h3>AI Core</h3><p>V3.2 Neural Engine</p></div>', unsafe_allow_html=True)
#         with s3: st.markdown('<div class="glass-card"><h3>Latency</h3><p>0.4ms Response</p></div>', unsafe_allow_html=True)

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro - Particle Edition</p>", unsafe_allow_html=True)



# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# import streamlit.components.v1 as components
# import time

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         return r.json()
#     except: return None

# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"

# # ---------------- 1. MOVING PARTICLES BACKGROUND ----------------
# particles_js = """
# <div id="tsparticles"></div>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/tsparticles/2.12.0/tsparticles.bundle.min.js"></script>
# <script>
# tsParticles.load("tsparticles", {
#   particles: {
#     number: { value: 50 },
#     color: { value: "#22c55e" },
#     shape: { type: "polygon", polygon: { nb_sides: 6 } },
#     opacity: { value: 0.2 },
#     size: { value: 3 },
#     move: { enable: true, speed: 1 },
#     line_linked: { enable: true, distance: 150, color: "#22c55e", opacity: 0.1 }
#   },
#   interactivity: { events: { onhover: { enable: true, mode: "grab" } } }
# });
# </script>
# <style> #tsparticles { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; } </style>
# """

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
#     .stApp { background: #020617 !important; font-family: 'Inter', sans-serif; color: white; }
#     .glass-card {
#         background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px);
#         border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); padding: 30px; margin-bottom: 20px;
#     }
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 10px 40px; background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(20px); border-radius: 100px; margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div.stButton > button {
#         background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%) !important;
#         color: white !important; font-weight: 800 !important; border-radius: 12px !important; border: none !important; transition: 0.4s;
#     }
#     .result-score { font-size: 50px; font-weight: 800; color: #22c55e; text-align: center; }
# </style>
# """, unsafe_allow_html=True)
# components.html(particles_js, height=0)

# # ---------------- 1. LOGIN SCREEN ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     for _ in range(5): st.markdown("<br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.2, 1])
#     with l_col:
#         st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
#         st.markdown("<h2 style='color:#22c55e;'>Admin Login</h2>", unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Access AI Dashboard 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else: st.error("Galti hai paji! Credentials check karo.")
#         st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- 2. LOADER ----------------
# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         st.markdown("<br><br>", unsafe_allow_html=True)
#         st_lottie(lottie_scan, height=450, key="loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Synchronizing Backend...</h2>", unsafe_allow_html=True)
#         time.sleep(3)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 3. MAIN DASHBOARD ----------------
# else:
#     # NAVBAR
#     st.markdown(f"""
#         <div class="nav-container">
#             <div style="font-weight: 800; font-size: 24px; color: #22c55e;">AI ATS PRO</div>
#             <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 14px; font-weight: 600;">
#                 <span>Dashboard</span><span>History</span><span>Reports</span>
#             </div>
#             <a href="/" style="text-decoration:none;"><button style="background:white; color:black; border-radius:50px; padding:5px 20px; font-weight:700; border:none;">Logout 🔓</button></a>
#         </div>
#     """, unsafe_allow_html=True)

#     _, mid, _ = st.columns([0.5, 2, 0.5])
#     with mid:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.markdown("<h2 style='text-align:center;'>Analyze Your Resume</h2><br>", unsafe_allow_html=True)
        
#         # INPUTS
#         st.markdown('<b style="color:yellow;">📤 Upload Resume (PDF)</b>', unsafe_allow_html=True)
#         uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
#         st.markdown("<br><b style='color:yellow;'>📝 Paste Job Description</b>", unsafe_allow_html=True)
#         jd_text = st.text_area("", placeholder="Paste JD requirements here...", height=150, label_visibility="collapsed")
        
#         if st.button("Run AI Diagnostics ✨", use_container_width=True):
#             if uploaded_file and jd_text:
#                 with st.spinner("Processing through Backend API..."):
#                     try:
#                         # 1. Upload & Extract Text
#                         files = {"file": uploaded_file.getvalue()}
#                         res_upload = requests.post("http://127.0.0.1:8000/upload", files=files)
                        
#                         if res_upload.status_code == 200:
#                             resume_text = res_upload.json().get("resume_text", "")
                            
#                             # 2. Analyze & Rank
#                             response = requests.post(
#                                 "http://127.0.0.1:8000/rank",
#                                 params={"resume_text": resume_text, "jd_text": jd_text}
#                             )
                            
#                             if response.status_code == 200:
#                                 result = response.json()
#                                 score = result.get("final_score", 0)
                                
#                                 # --- DISPLAY RESULTS ---
#                                 st.markdown("---")
#                                 st.markdown(f'<div class="result-score">{score}%</div>', unsafe_allow_html=True)
#                                 st.markdown("<p style='text-align:center;'>Overall Match Score</p>", unsafe_allow_html=True)
#                                 st.progress(int(score))
                                
#                                 r1, r2 = st.columns(2)
#                                 with r1:
#                                     st.markdown(f'<div class="glass-card"><h4>📊 Similarity</h4><h3>{result.get("similarity", 0)}%</h3></div>', unsafe_allow_html=True)
#                                 with r2:
#                                     st.markdown(f'<div class="glass-card"><h4>🎯 Skill Match</h4><h3>{result.get("skill_score", 0)}%</h3></div>', unsafe_allow_html=True)
                                
#                                 # Missing Skills & AI Feedback
#                                 st.subheader("❗ Missing Skills")
#                                 skills = result.get("missing_skills", [])
#                                 if skills:
#                                     st.write(", ".join([f"`{s}`" for s in skills]))
#                                 else:
#                                     st.success("Sira! No missing skills found.")
                                
#                                 st.subheader("🤖 AI Smart Feedback")
#                                 st.info(result.get("ai_feedback", "No specific feedback provided."))
                                
#                             else: st.error("Backend Ranking Error!")
#                         else: st.error("File Extraction Failed!")
#                     except Exception as e:
#                         st.error(f"Connection Error: {e}. Check if FastAPI is running on port 8000!")
#             else:
#                 st.warning("Paji, Resume te JD dono zaroori ne!")
#         st.markdown('</div>', unsafe_allow_html=True)

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro - Integrated Edition</p>", unsafe_allow_html=True)

# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from builder import show_builder_ui
# from analytics import show_analytics  # Eh import check karo
# from history import show_history
# import time

# # ---------------- 0. PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200: return None
#         return r.json()
#     except:
#         return None

# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"
# if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# # ---------------- PROFESSIONAL CSS (UNTOUCHED) ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif; color: white;
#     }

#     .nav-logo { 
#         font-weight: 800; 
#         font-size: 26px; 
#         color: #22c55e; 
#         line-height: 65px; 
#         white-space: nowrap;
#     }

#     div[data-testid="stHorizontalBlock"] button {
#         background: transparent !important;
#         color: #94a3b8 !important;
#         border: none !important;
#         font-size: 14px !important;
#         font-weight: 600 !important;
#         box-shadow: none !important;
#         height: 65px !important; 
#         margin: 0 !important;
#         padding: 0 !important;
#     }
    
#     div[data-testid="stHorizontalBlock"] button:hover {
#         color: #22c55e !important;
#     }

#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#         padding-bottom:10px;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
    
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
#     .footer-card:hover {
#         transform: translateY(-15px) scale(1.02); /* Card moves up and slightly grows */
#         background: rgba(34, 197, 94, 0.1); /* Subtle Green Glow */
#         border: 1px solid rgba(34, 197, 94, 0.5);
#         box-shadow: 0px 20px 30px rgba(0, 0, 0, 0.5);
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN & LOADER ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")

# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         if lottie_scan:
#             st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         time.sleep(2)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 2. MAIN APP ----------------
# else:
#     # --- NAVBAR ---
#     n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
#     with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
#     with n_col2: 
#         if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
#     with n_col3: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
#     with n_col4: 
#         if st.button("History"): st.session_state.page = "History"; st.rerun()
#     with n_col5: 
#         if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
#     with n_col6: 
#         if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

#     # --- DASHBOARD PAGE ---
#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.2, 2, 0.2])
#         with mid:
#             st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
#             # PDF UPLOAD
#             st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
#             res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
#             # EXTRACTED TEXT PREVIEW (Appears immediately after upload)
#             extracted_data = {} 
#             if res_files:
#                 for res_file in res_files:
#                     files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
#                     try:
#                         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#                         if res.status_code == 200:
#                             text = res.json().get("resume_text", "")
#                             extracted_data[res_file.name] = text
#                             st.text_area(f"Extracted Text: {res_file.name}", text, height=100)
#                     except: st.error("Backend offline paji!")

#             # JD INPUT
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             # ANALYZE ACTION
#             if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
#                 if extracted_data and jd_text.strip():
#                     for name, resume_text in extracted_data.items():
#                         with st.expander(f"📊 Results for: {name}", expanded=True):
#                             try:
#                                 rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                                 if rank_res.status_code == 200:
#                                     data = rank_res.json()
#                                     score = data.get("final_score", 0)
                                    
#                                     # Result Display
#                                     st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
#                                     st.progress(int(score))
                                    
#                                     col1, col2 = st.columns(2)
#                                     col1.write(f"**Similarity:** {data.get('similarity', 0)}%")
#                                     col2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
#                                     st.markdown("**❗ Missing Skills:**")
#                                     st.write(", ".join(data.get("missing_skills", [])))
                                    
#                                     st.markdown("**🔑 Keywords:**")
#                                     st.write(", ".join(data.get("keywords", [])))
                                    
#                                     st.info(f"🤖 AI Feedback: {data.get('ai_feedback', '')}")
                                    
#                                     st.session_state.scan_history.append({"name": name, "score": score, "date": time.strftime("%Y-%m-%d")})
#                                 else: st.error("Ranking error")
#                             except: st.error("Connection failed")
#                 else: st.error("Paji, files te JD dono check karo!")

#         # Features Section (Unchanged)
#         # --- UPDATED 6 FEATURES SECTION (WITH HOVER LIFT) ---
#         st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
        
#         # Extended 6 features with more descriptive text
#         features = [
#             ("01", "Instant Scan", "Advanced parsing engine extracts deep text from any PDF format instantly with 99.9% precision and speed."),
#             ("02", "Deep Insights", "Go beyond simple matching; identify the exact technical and soft skill gaps between you and the recruiter."),
#             ("03", "JD Matching", "Leverage state-of-the-art AI vector embeddings to check semantic similarity and contextual relevance for the role."),
#             ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers, ensuring 100% professional confidentiality."),
#             ("05", "AI Feedback", "Get actionable, AI-driven tips to improve your impact verbs, bullet points, and industry-keyword density."),
#             ("06", "ATS Optimized", "Specifically calibrated to bypass complex algorithmic filters used by top-tier ATS systems like Workday")
#         ]
        
#         # CSS for Hover Effect (Make sure this is in your <style> block)
#         # .footer-card { transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
#         # .footer-card:hover { transform: translateY(-15px) scale(1.03); background: rgba(34, 197, 94, 0.15) !important; border: 1px solid #22c55e !important; }

#         # Logic to display 6 cards in 2 rows (3 columns each)
#         rows = [features[0:3], features[3:6]]
        
#         for row in rows:
#             f_cols = st.columns(3)
#             for idx, (num, title, desc) in enumerate(row):
#                 with f_cols[idx]:
#                     st.markdown(f'''
#                         <div class="footer-card">
#                             <div class="footer-number">{num}</div>
#                             <h3>{title}</h3>
#                             <p>{desc}</p>
#                         </div><br>
#                     ''', unsafe_allow_html=True)

#     elif st.session_state.page == "Builder": show_builder_ui()
#     elif st.session_state.page == "History": show_history()
#     elif st.session_state.page == "Analytics": show_analytics()
    

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)











# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from builder import show_builder_ui
# from analytics import show_analytics  # Eh import check karo
# from history import show_history
# import time

# # ---------------- 0. PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200: return None
#         return r.json()
#     except:
#         return None

# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"
# if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# # ---------------- PROFESSIONAL CSS (UNTOUCHED) ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif; color: white;
#     }

#     .nav-logo { 
#         font-weight: 800; 
#         font-size: 26px; 
#         color: #22c55e; 
#         line-height: 65px; 
#         white-space: nowrap;
#     }

#     div[data-testid="stHorizontalBlock"] button {
#         background: transparent !important;
#         color: #94a3b8 !important;
#         border: none !important;
#         font-size: 14px !important;
#         font-weight: 600 !important;
#         box-shadow: none !important;
#         height: 65px !important; 
#         margin: 0 !important;
#         padding: 0 !important;
#     }
    
#     div[data-testid="stHorizontalBlock"] button:hover {
#         color: #22c55e !important;
#     }

#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
    
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN & LOADER ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")

# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         if lottie_scan:
#             st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         time.sleep(2)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 2. MAIN APP ----------------
# else:
#     # --- NAVBAR ---
#     n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
#     with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
#     with n_col2: 
#         if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
#     with n_col3: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
#     with n_col4: 
#         if st.button("History"): st.session_state.page = "History"; st.rerun()
#     with n_col5: 
#         if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
#     with n_col6: 
#         if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

#     # --- DASHBOARD PAGE ---
#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.2, 2, 0.2])
#         with mid:
#             st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
#             # PDF UPLOAD
#             st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
#             res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
#             # EXTRACTED TEXT PREVIEW (Appears immediately after upload)
#             extracted_data = {} 
#             if res_files:
#                 for res_file in res_files:
#                     files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
#                     try:
#                         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#                         if res.status_code == 200:
#                             text = res.json().get("resume_text", "")
#                             extracted_data[res_file.name] = text
#                             st.text_area(f"Extracted Text: {res_file.name}", text, height=100)
#                     except: st.error("Backend offline paji!")

#             # JD INPUT
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             # ANALYZE ACTION
#             if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
#                 if extracted_data and jd_text.strip():
#                     for name, resume_text in extracted_data.items():
#                         with st.expander(f"📊 Results for: {name}", expanded=True):
#                             try:
#                                 rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                                 if rank_res.status_code == 200:
#                                     data = rank_res.json()
#                                     score = data.get("final_score", 0)
                                    
#                                     # Result Display
#                                     st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
#                                     st.progress(int(score))
                                    
#                                     col1, col2 = st.columns(2)
#                                     col1.write(f"**Similarity:** {data.get('similarity', 0)}%")
#                                     col2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
#                                     st.markdown("**❗ Missing Skills:**")
#                                     st.write(", ".join(data.get("missing_skills", [])))
                                    
#                                     st.markdown("**🔑 Keywords:**")
#                                     st.write(", ".join(data.get("keywords", [])))
                                    
#                                     st.info(f"🤖 AI Feedback: {data.get('ai_feedback', '')}")
                                    
#                                     st.session_state.scan_history.append({"name": name, "score": score, "date": time.strftime("%Y-%m-%d")})
#                                 else: st.error("Ranking error")
#                             except: st.error("Connection failed")
#                 else: st.error("Paji, files te JD dono check karo!")

#         # Features Section (Unchanged)
#         st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
#         f_cols = st.columns(3)
#         features = [("01", "Instant Scan", "Deep text extraction..."), ("02", "Deep Insights", "Identifies the gap..."), ("03", "JD Matching", "Uses AI vector...")]
#         for idx, (num, title, desc) in enumerate(features):
#             with f_cols[idx]:
#                 st.markdown(f'<div class="footer-card"><div class="footer-number">{num}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

#     elif st.session_state.page == "Builder": show_builder_ui()
#     elif st.session_state.page == "History": show_history()
#     elif st.session_state.page == "Analytics": show_analytics()
    

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)



# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from builder import show_builder_ui
# from analytics import show_analytics 
# from history import show_history
# import time

# # ---------------- 0. PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200: return None
#         return r.json()
#     except:
#         return None

# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"
# if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# # ---------------- PROFESSIONAL CSS (UNTOUCHED + WHITE LABELS) ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif; color: white;
#     }

#     /* LOGIN LABELS TO WHITE */
#     .stTextInput label {
#         color: white !important;
#         font-weight: 600 !important;
#     }

#     .nav-logo { 
#         font-weight: 800; 
#         font-size: 26px; 
#         color: #22c55e; 
#         line-height: 65px; 
#         white-space: nowrap;
#     }

#     div[data-testid="stHorizontalBlock"] button {
#         background: transparent !important;
#         color: #94a3b8 !important;
#         border: none !important;
#         font-size: 14px !important;
#         font-weight: 600 !important;
#         box-shadow: none !important;
#         height: 65px !important; 
#         margin: 0 !important;
#         padding: 0 !important;
#     }
    
#     div[data-testid="stHorizontalBlock"] button:hover {
#         color: #22c55e !important;
#     }

#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#         padding-bottom:10px;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
    
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
#     .footer-card:hover {
#         transform: translateY(-15px) scale(1.02); 
#         background: rgba(34, 197, 94, 0.1); 
#         border: 1px solid rgba(34, 197, 94, 0.5);
#         box-shadow: 0px 20px 30px rgba(0, 0, 0, 0.5);
#     }
   
#     div[data-testid="stTextInput"] button {
#         display: flex !important;
#         align-items: center !important;
#         justify-content: center !important;
#         padding-top: 5px !important; /* Ehnu thoda adjust karke dekhlo centre de layi */
#         height: 100% !important;
#     }

#     /* Container nu proper height den layi */
#     div[data-testid="stTextInput"] > div > div {
#         display: flex !important;
#         align-items: center !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN & LOADER ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="Enter Your Username")
#         p = st.text_input("Password", type="password", placeholder="Enter Your Password")
#         if st.button("Launch System 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")

# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         if lottie_scan:
#             st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         time.sleep(2)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 2. MAIN APP ----------------
# else:
#     # --- NAVBAR ---
#     n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
#     with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
#     with n_col2: 
#         if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
#     with n_col3: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
#     with n_col4: 
#         if st.button("History"): st.session_state.page = "History"; st.rerun()
#     with n_col5: 
#         if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
#     with n_col6: 
#         if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

#     # --- ROUTING LOGIC ---
#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.2, 2, 0.2])
#         with mid:
#             st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
#             # PDF UPLOAD
#             st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
#             res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
#             # EXTRACTED TEXT PREVIEW
#             extracted_data = {} 
#             if res_files:
#                 for res_file in res_files:
#                     files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
#                     try:
#                         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#                         if res.status_code == 200:
#                             text = res.json().get("resume_text", "")
#                             extracted_data[res_file.name] = text
#                             st.text_area(f"Extracted Text: {res_file.name}", text, height=100)
#                     except: st.error("Backend offline paji!")

#             # JD INPUT
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             # ANALYZE ACTION
#             if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
#                 if extracted_data and jd_text.strip():
#                     for name, resume_text in extracted_data.items():
#                         with st.expander(f"📊 Results for: {name}", expanded=True):
#                             try:
#                                 rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                                 if rank_res.status_code == 200:
#                                     data = rank_res.json()
#                                     score = data.get("final_score", 0)
#                                     st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
#                                     st.progress(int(score))
                                    
#                                     col1, col2 = st.columns(2)
#                                     col1.write(f"**Similarity:** {data.get('similarity', 0)}%")
#                                     col2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
#                                     st.markdown("**❗ Missing Skills:**")
#                                     st.write(", ".join(data.get("missing_skills", [])))
                                    
#                                     st.info(f"🤖 AI Feedback: {data.get('ai_feedback', '')}")
#                                     st.session_state.scan_history.append({"name": name, "score": score, "date": time.strftime("%Y-%m-%d")})
#                                 else: st.error("Ranking error")
#                             except: st.error("Connection failed")
#                 else: st.error("Check Both File And JD")

#         # Features Section
#         st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
#         features = [
#             ("01", "Instant Scan", "Advanced parsing engine extracts deep text from any PDF format instantly with 99.9% precision and speed."),
#             ("02", "Deep Insights", "Go beyond simple matching; identify the exact technical and soft skill gaps between you and the recruiter."),
#             ("03", "JD Matching", "Leverage state-of-the-art AI vector embeddings to check semantic similarity and contextual relevance for the role."),
#             ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers, ensuring 100% professional confidentiality."),
#             ("05", "AI Feedback", "Get actionable, AI-driven tips to improve your impact verbs, bullet points, and industry-keyword density."),
#             ("06", "ATS Optimized", "Specifically calibrated to bypass complex algorithmic filters used by top-tier ATS systems like Workday")
#         ]
        
#         rows = [features[0:3], features[3:6]]
#         for row in rows:
#             f_cols = st.columns(3)
#             for idx, (num, title, desc) in enumerate(row):
#                 with f_cols[idx]:
#                     st.markdown(f'''
#                         <div class="footer-card">
#                             <div class="footer-number">{num}</div>
#                             <h3>{title}</h3>
#                             <p>{desc}</p>
#                         </div><br>
#                     ''', unsafe_allow_html=True)

#     elif st.session_state.page == "Builder": show_builder_ui()
#     elif st.session_state.page == "History": show_history()
#     elif st.session_state.page == "Analytics": show_analytics()

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)
#correct above

# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from builder import show_builder_ui
# from analytics import show_analytics 
# from history import show_history
# import time

# # ---------------- 0. PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200: return None
#         return r.json()
#     except:
#         return None

# # Load Lottie Animations
# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")
# lottie_analyze = load_lottieurl("https://lottie.host/9853763a-e430-40c3-9146-057a304d559c/8dFcWvf3nD.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"
# if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# # ---------------- PROFESSIONAL CSS (WITH EYE-ICON & WHITE LABELS) ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif; color: white;
#     }

#     /* LOGIN LABELS TO WHITE */
#     .stTextInput label {
#         color: white !important;
#         font-weight: 600 !important;
#     }

#     /* Password Eye Icon Centering */
#     div[data-testid="stTextInput"] button {
#         display: flex !important;
#         align-items: center !important;
#         justify-content: center !important;
#         height: 100% !important;
#     }

#     .nav-logo { 
#         font-weight: 800; 
#         font-size: 26px; 
#         color: #22c55e; 
#         line-height: 65px; 
#         white-space: nowrap;
#     }

#     div[data-testid="stHorizontalBlock"] button {
#         background: transparent !important;
#         color: #94a3b8 !important;
#         border: none !important;
#         font-size: 14px !important;
#         font-weight: 600 !important;
#         box-shadow: none !important;
#         height: 65px !important; 
#         margin: 0 !important;
#         padding: 0 !important;
#     }
    
#     div[data-testid="stHorizontalBlock"] button:hover { color: #22c55e !important; }

#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#         padding-bottom:10px;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
    
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
#     .footer-card:hover {
#         transform: translateY(-15px) scale(1.02); 
#         background: rgba(34, 197, 94, 0.1); 
#         border: 1px solid rgba(34, 197, 94, 0.5);
#         box-shadow: 0px 20px 30px rgba(0, 0, 0, 0.5);
#     }
#               div[data-testid="stTextInput"] button {
#         display: flex !important;
#         align-items: center !important;
#         justify-content: center !important;
#         padding-top: 5px !important; /* Ehnu thoda adjust karke dekhlo centre de layi */
#         height: 100% !important;
#     }

#     /* Container nu proper height den layi */
#     div[data-testid="stTextInput"] > div > div {
#         display: flex !important;
#         align-items: center !important;
# #     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN & LOADER ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else: st.error("Invalid Credentials")

# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         if lottie_scan: st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         time.sleep(2)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 2. MAIN APP ----------------
# else:
#     # --- NAVBAR ---
#     n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
#     with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
#     with n_col2: 
#         if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
#     with n_col3: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
#     with n_col4: 
#         if st.button("History"): st.session_state.page = "History"; st.rerun()
#     with n_col5: 
#         if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
#     with n_col6: 
#         if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

#     # --- DASHBOARD PAGE ---
#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.2, 2, 0.2])
#         with mid:
#             st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
#             st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
#             res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
#             extracted_data = {} 
#             if res_files:
#                 for res_file in res_files:
#                     files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
#                     try:
#                         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#                         if res.status_code == 200:
#                             text = res.json().get("resume_text", "")
#                             extracted_data[res_file.name] = text
#                             st.text_area(f"Extracted Text: {res_file.name}", text, height=100)
#                     except: st.error("Backend offline paji!")

#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             # --- UPDATED ANALYZE ACTION WITH NEW LOTTIE ---
#             if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
#                 if extracted_data and jd_text.strip():
#                     # Show naya Lottie animation during analysis
#                     with st.empty():
#                         if lottie_analyze:
#                             st_lottie(lottie_analyze, height=300, key="analyze_loader")
#                         st.markdown("<h3 style='text-align:center; color:#22c55e;'>AI is deep-scanning your resume...</h3>", unsafe_allow_html=True)
#                         time.sleep(3) # Short delay to show animation
#                         st.write("") # Clear animation before showing results

#                     for name, resume_text in extracted_data.items():
#                         with st.expander(f"📊 Results for: {name}", expanded=True):
#                             try:
#                                 rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                                 if rank_res.status_code == 200:
#                                     data = rank_res.json()
#                                     score = data.get("final_score", 0)
#                                     st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
#                                     st.progress(int(score))
                                    
#                                     c1, c2 = st.columns(2)
#                                     c1.write(f"**Similarity:** {data.get('similarity', 0)}%")
#                                     c2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
#                                     st.markdown("**❗ Missing Skills:**")
#                                     st.write(", ".join(data.get("missing_skills", [])))
#                                     st.info(f"🤖 AI Feedback: {data.get('ai_feedback', '')}")
#                                     st.session_state.scan_history.append({"name": name, "score": score, "date": time.strftime("%Y-%m-%d")})
#                                 else: st.error("Ranking error")
#                             except: st.error("Connection failed")
#                 else: st.error("Paji, files te JD dono check karo!")

#         # Features Section
#         st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
#         features = [
#             ("01", "Instant Scan", "Advanced parsing engine extracts deep text from any PDF format instantly with 99.9% precision and speed."),
#             ("02", "Deep Insights", "Go beyond simple matching; identify the exact technical and soft skill gaps between you and the recruiter."),
#             ("03", "JD Matching", "Leverage state-of-the-art AI vector embeddings to check semantic similarity and contextual relevance for the role."),
#             ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers, ensuring 100% professional confidentiality."),
#             ("05", "AI Feedback", "Get actionable, AI-driven tips to improve your impact verbs, bullet points, and industry-keyword density."),
#             ("06", "ATS Optimized", "Specifically calibrated to bypass complex algorithmic filters used by top-tier ATS systems like Workday")
#         ]
        
#         rows = [features[0:3], features[3:6]]
#         for row in rows:
#             f_cols = st.columns(3)
#             for idx, (num, title, desc) in enumerate(row):
#                 with f_cols[idx]:
#                     st.markdown(f'''<div class="footer-card"><div class="footer-number">{num}</div><h3>{title}</h3><p>{desc}</p></div><br>''', unsafe_allow_html=True)

#     elif st.session_state.page == "Builder": show_builder_ui()
#     elif st.session_state.page == "History": show_history()
#     elif st.session_state.page == "Analytics": show_analytics()

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)


# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from builder import show_builder_ui
# from analytics import show_analytics 
# from history import show_history
# import time
# import re

# # ---------------- 0. PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200: return None
#         return r.json()
#     except:
#         return None

# # Load Lottie Animations
# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")
# # Updated Mixing Animation
# lottie_analyze = load_lottieurl("https://lottie.host/9853763a-e430-40c3-9146-057a304d559c/8dFcWvf3nD.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"
# if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif; color: white;
#     }

#     .stTextInput label { color: white !important; font-weight: 600 !important; }

#     /* Password Eye Icon Centering */
#     div[data-testid="stTextInput"] button {
#         display: flex !important; align-items: center !important;
#         justify-content: center !important; padding-top: 5px !important; height: 100% !important;
#     }
#     div[data-testid="stTextInput"] > div > div { display: flex !important; align-items: center !important; }

#     .nav-logo { font-weight: 800; font-size: 26px; color: #22c55e; line-height: 65px; white-space: nowrap; }

#     div[data-testid="stHorizontalBlock"] button {
#         background: transparent !important; color: #94a3b8 !important; border: none !important;
#         font-size: 14px !important; font-weight: 600 !important; box-shadow: none !important;
#         height: 65px !important; margin: 0 !important; padding: 0 !important;
#     }
#     div[data-testid="stHorizontalBlock"] button:hover { color: #22c55e !important; }

#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     /* AI FEEDBACK CARDS (YELLOW-BLUE GRADIENT) */
#     .feedback-card {
#         background: linear-gradient(135deg, rgba(255, 235, 59, 0.1) 0%, rgba(33, 150, 243, 0.1) 100%);
#         border-left: 5px solid #ffeb3b;
#         padding: 18px;
#         margin: 12px 0px;
#         border-radius: 12px;
#         border: 1px solid rgba(255, 255, 255, 0.15);
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2);
#     }

#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
    
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN & INITIAL LOADER ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else: st.error("Invalid Credentials")

# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         if lottie_scan: st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         time.sleep(2)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 2. MAIN APP ----------------
# else:
#     # --- NAVBAR ---
#     n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
#     with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
#     with n_col2: 
#         if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
#     with n_col3: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
#     with n_col4: 
#         if st.button("History"): st.session_state.page = "History"; st.rerun()
#     with n_col5: 
#         if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
#     with n_col6: 
#         if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

#     # --- DASHBOARD PAGE ---
#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.2, 2, 0.2])
#         with mid:
#             st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
#             st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
#             res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
#             extracted_data = {} 
#             if res_files:
#                 for res_file in res_files:
#                     files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
#                     try:
#                         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#                         if res.status_code == 200:
#                             text = res.json().get("resume_text", "")
#                             extracted_data[res_file.name] = text
#                             st.text_area(f"Extracted Text: {res_file.name}", text, height=100)
#                     except: st.error("Backend offline paji!")

#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             # --- ANALYZE ACTION WITH MIXING ANIMATION ---
#             if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
#                 if extracted_data and jd_text.strip():
#                     # Mixing Animation State
#                     with st.empty():
#                         if lottie_analyze: 
#                             st_lottie(lottie_analyze, height=350, key="mixing_loader")
#                         st.markdown("<h3 style='text-align:center; color:#22c55e;'>Mixing Data & Benchmarking Skills...</h3>", unsafe_allow_html=True)
#                         time.sleep(3.5)
#                         st.write("") 

#                     for name, resume_text in extracted_data.items():
#                         with st.expander(f"📊 Results for: {name}", expanded=True):
#                             try:
#                                 rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                                 if rank_res.status_code == 200:
#                                     data = rank_res.json()
#                                     score = data.get("final_score", 0)
#                                     st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
#                                     st.progress(int(score))
                                    
#                                     c1, c2 = st.columns(2)
#                                     c1.write(f"**Similarity:** {data.get('similarity', 0)}%")
#                                     c2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
#                                     st.markdown("**❗ Missing Skills:**")
#                                     st.write(", ".join(data.get("missing_skills", [])))
                                    
#                                     # --- PART BY PART AI FEEDBACK (YELLOW-BLUE CARDS) ---
#                                     st.markdown("<br><b>🤖 AI Detailed Feedback:</b>", unsafe_allow_html=True)
#                                     raw_feedback = data.get('ai_feedback', '')
                                    
#                                     # Split feedback by numbers (1., 2., etc.)
#                                     feedback_points = re.split(r'\d+\.', raw_feedback)
#                                     for point in feedback_points:
#                                         if point.strip():
#                                             st.markdown(f'''
#                                                 <div class="feedback-card">
#                                                     <span style="color:#ffeb3b; font-weight:bold;">💡 Insight:</span> {point.strip()}
#                                                 </div>
#                                             ''', unsafe_allow_html=True)

#                                     st.session_state.scan_history.append({"name": name, "score": score, "date": time.strftime("%Y-%m-%d")})
#                                 else: st.error("Ranking error")
#                             except: st.error("Connection failed")
#                 else: st.error("Paji, files te JD dono check karo!")

#         # Features Section
#         st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
#         features = [
#             ("01", "Instant Scan", "Advanced parsing engine extracts deep text from any PDF format instantly with 99.9% precision and speed."),
#             ("02", "Deep Insights", "Go beyond simple matching; identify the exact technical and soft skill gaps between you and the recruiter."),
#             ("03", "JD Matching", "Leverage state-of-the-art AI vector embeddings to check semantic similarity and contextual relevance for the role."),
#             ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers, ensuring 100% professional confidentiality."),
#             ("05", "AI Feedback", "Get actionable, AI-driven tips to improve your impact verbs, bullet points, and industry-keyword density."),
#             ("06", "ATS Optimized", "Specifically calibrated to bypass complex algorithmic filters used by top-tier ATS systems like Workday")
#         ]
        
#         rows = [features[0:3], features[3:6]]
#         for row in rows:
#             f_cols = st.columns(3)
#             for idx, (num, title, desc) in enumerate(row):
#                 with f_cols[idx]:
#                     st.markdown(f'''<div class="footer-card"><div class="footer-number">{num}</div><h3>{title}</h3><p>{desc}</p></div><br>''', unsafe_allow_html=True)

#     elif st.session_state.page == "Builder": show_builder_ui()
#     elif st.session_state.page == "History": show_history()
#     elif st.session_state.page == "Analytics": show_analytics()

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)



# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from builder import show_builder_ui
# from analytics import show_analytics 
# from history import show_history
# import time
# import re
# import json

# # ---------------- 0. PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Lottie Loader Function
# def load_lottieurl(url: str):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200: return None
#         return r.json()
#     except:
#         return None

# # Load Lottie Animations
# lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")
# lottie_analyze = load_lottieurl("https://lottie.host/9853763a-e430-40c3-9146-057a304d559c/8dFcWvf3nD.json")

# # Initialize Session States
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'show_loader' not in st.session_state: st.session_state.show_loader = False
# if 'page' not in st.session_state: st.session_state.page = "Dashboard"
# if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# # ---------------- PROFESSIONAL CSS (NO CHANGES 😠) ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif; color: white;
#     }

#     .stTextInput label { color: white !important; font-weight: 600 !important; }

#     /* Password Eye Icon Centering */
#     div[data-testid="stTextInput"] button {
#         display: flex !important; align-items: center !important;
#         justify-content: center !important; padding-top: 5px !important; height: 100% !important;
#     }
#     div[data-testid="stTextInput"] > div > div { display: flex !important; align-items: center !important; }

#     .nav-logo { font-weight: 800; font-size: 26px; color: #22c55e; line-height: 65px; white-space: nowrap; }

#     div[data-testid="stHorizontalBlock"] button {
#         background: transparent !important; color: #94a3b8 !important; border: none !important;
#         font-size: 14px !important; font-weight: 600 !important; box-shadow: none !important;
#         height: 65px !important; margin: 0 !important; padding: 0 !important;
#     }
#     div[data-testid="stHorizontalBlock"] button:hover { color: #22c55e !important; }

#     .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
#     /* AI FEEDBACK CARDS (YELLOW-BLUE GRADIENT) */
#     .feedback-card {
#         background: linear-gradient(135deg, rgba(255, 235, 59, 0.1) 0%, rgba(33, 150, 243, 0.1) 100%);
#         border-left: 5px solid #ffeb3b;
#         padding: 18px;
#         margin: 12px 0px;
#         border-radius: 12px;
#         border: 1px solid rgba(255, 255, 255, 0.15);
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2);
#     }

#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#     }
#     .footer-number { 
#         background: #22c55e; color: white; width: 30px; height: 30px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 10px; 
#     }
    
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1); color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
#         font-size: 15px; font-weight: 800; display: inline-block;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- 1. LOGIN & INITIAL LOADER ----------------
# if not st.session_state.logged_in and not st.session_state.show_loader:
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     _, l_col, _ = st.columns([1, 1.5, 1])
#     with l_col:
#         st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
#         u = st.text_input("Username", placeholder="admin")
#         p = st.text_input("Password", type="password", placeholder="admin123")
#         if st.button("Launch System 🚀", use_container_width=True):
#             if u == "admin" and p == "admin123":
#                 st.session_state.show_loader = True
#                 st.rerun()
#             else: st.error("Invalid Credentials")

# elif st.session_state.show_loader:
#     _, center_col, _ = st.columns([1, 2, 1])
#     with center_col:
#         if lottie_scan: st_lottie(lottie_scan, height=400, key="login_loader")
#         st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
#         time.sleep(2)
#         st.session_state.logged_in = True
#         st.session_state.show_loader = False
#         st.rerun()

# # ---------------- 2. MAIN APP ----------------
# else:
#     # --- NAVBAR ---
#     n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
#     with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
#     with n_col2: 
#         if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
#     with n_col3: 
#         if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
#     with n_col4: 
#         if st.button("History"): st.session_state.page = "History"; st.rerun()
#     with n_col5: 
#         if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
#     with n_col6: 
#         if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

#     # --- DASHBOARD PAGE ---
#     if st.session_state.page == "Dashboard":
#         _, mid, _ = st.columns([0.2, 2, 0.2])
#         with mid:
#             st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
#             st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
#             st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
#             res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
#             extracted_data = {} 
#             if res_files:
#                 for res_file in res_files:
#                     files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
#                     try:
#                         res = requests.post("http://127.0.0.1:8000/upload", files=files)
#                         if res.status_code == 200:
#                             text = res.json().get("resume_text", "")
#                             extracted_data[res_file.name] = text
#                             st.text_area(f"Extracted Text: {res_file.name}", text, height=100)
#                     except: st.error("Backend offline paji!")

#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
#             jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
#             # --- ANALYZE ACTION ---
#             if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
#                 if extracted_data and jd_text.strip():
#                     # 1. Show Mixing Animation
#                     with st.empty():
#                         if lottie_analyze: 
#                             st_lottie(lottie_analyze, height=350, key="mixing_loader")
#                         st.markdown("<h3 style='text-align:center; color:#22c55e;'>Mixing Data & Benchmarking Skills...</h3>", unsafe_allow_html=True)
#                         time.sleep(3.5)
#                         st.write("") 

#                     # 2. Process Each Resume
#                     for name, resume_text in extracted_data.items():
#                         with st.expander(f"📊 Results for: {name}", expanded=True):
#                             try:
#                                 # Update this URL to your backend endpoint
#                                 rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
#                                 if rank_res.status_code == 200:
#                                     data = rank_res.json()
#                                     score = data.get("final_score", 0)
#                                     st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
#                                     st.progress(int(score))
                                    
#                                     c1, c2 = st.columns(2)
#                                     c1.write(f"**Similarity:** {data.get('similarity', 0)}%")
#                                     c2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
#                                     st.markdown("**❗ Missing Skills:**")
#                                     st.write(", ".join(data.get("missing_skills", [])))
                                    
#                                     # --- CLEAN AI FEEDBACK LOGIC ---
#                                     st.markdown("<br><b>🤖 AI Detailed Feedback:</b>", unsafe_allow_html=True)
#                                     raw_feedback = data.get('ai_feedback', '')

#                                     # Clean Markdown symbols and rogue tags
#                                     clean_feedback = raw_feedback.replace("###", "").replace("</div>", "").replace("<div>", "").replace("---", "")

#                                     # Split by numbered points
#                                     feedback_points = re.split(r'\d+\.', clean_feedback)

#                                     for point in feedback_points:
#                                         point_text = point.strip()
#                                         if point_text:
#                                             # Separate Title from Description if possible
#                                             if ":" in point_text:
#                                                 parts = point_text.split(":", 1)
#                                                 title_tag = parts[0].strip()
#                                                 desc_tag = parts[1].strip()
#                                             else:
#                                                 title_tag = "Insight"
#                                                 desc_tag = point_text

#                                             st.markdown(f'''
#                                                 <div class="feedback-card">
#                                                     <span style="color:#ffeb3b; font-weight:bold;">💡 {title_tag}:</span> 
#                                                     <div style="margin-top:5px; line-height:1.5;">{desc_tag}</div>
#                                                 </div>
#                                             ''', unsafe_allow_html=True)

#                                     st.session_state.scan_history.append({"name": name, "score": score, "date": time.strftime("%Y-%m-%d")})
#                                 else: st.error("Ranking error")
#                             except Exception as e: st.error(f"Backend Error: {str(e)}")
#                 else: st.error("Paji, files te JD dono check karo!")

#         # Features Section
#         st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
#         features = [
#             ("01", "Instant Scan", "Advanced parsing engine extracts deep text from any PDF format instantly with 99.9% precision and speed."),
#             ("02", "Deep Insights", "Go beyond simple matching; identify the exact technical and soft skill gaps between you and the recruiter."),
#             ("03", "JD Matching", "Leverage state-of-the-art AI vector embeddings to check semantic similarity and contextual relevance for the role."),
#             ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers, ensuring 100% professional confidentiality."),
#             ("05", "AI Feedback", "Get actionable, AI-driven tips to improve your impact verbs, bullet points, and industry-keyword density."),
#             ("06", "ATS Optimized", "Specifically calibrated to bypass complex algorithmic filters used by top-tier ATS systems like Workday")
#         ]
        
#         rows = [features[0:3], features[3:6]]
#         for row in rows:
#             f_cols = st.columns(3)
#             for idx, (num, title, desc) in enumerate(row):
#                 with f_cols[idx]:
#                     st.markdown(f'''<div class="footer-card"><div class="footer-number">{num}</div><h3>{title}</h3><p>{desc}</p></div><br>''', unsafe_allow_html=True)

#     elif st.session_state.page == "Builder": show_builder_ui()
#     elif st.session_state.page == "History": show_history()
#     elif st.session_state.page == "Analytics": show_analytics()

# st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from builder import show_builder_ui
from analytics import show_analytics 
from history import show_history
import time
import re
import json

# ---------------- 0. PAGE CONFIG ----------------
st.set_page_config(page_title="AI ATS Pro", layout="wide")

# Lottie Loader Function
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except:
        return None

# Load Lottie Animations
lottie_scan = load_lottieurl("https://lottie.host/3167a94b-8115-4d5e-98ce-e116526660d8/auhgJOyov3.json")
lottie_analyze = load_lottieurl("https://lottie.host/9853763a-e430-40c3-9146-057a304d559c/8dFcWvf3nD.json")

# Initialize Session States
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'show_loader' not in st.session_state: st.session_state.show_loader = False
if 'page' not in st.session_state: st.session_state.page = "Dashboard"
if 'scan_history' not in st.session_state: st.session_state.scan_history = []

# ---------------- PROFESSIONAL CSS ----------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
        font-family: 'Inter', sans-serif; color: white;
    }

    .stTextInput label { color: white !important; font-weight: 600 !important; }

    div[data-testid="stTextInput"] button {
        display: flex !important; align-items: center !important;
        justify-content: center !important; padding-top: 5px !important; height: 100% !important;
    }
    div[data-testid="stTextInput"] > div > div { display: flex !important; align-items: center !important; }

    .nav-logo { font-weight: 800; font-size: 26px; color: #22c55e; line-height: 65px; white-space: nowrap; }

    div[data-testid="stHorizontalBlock"] button {
        background: transparent !important; color: #94a3b8 !important; border: none !important;
        font-size: 14px !important; font-weight: 600 !important; box-shadow: none !important;
        height: 65px !important; margin: 0 !important; padding: 0 !important;
    }
    div[data-testid="stHorizontalBlock"] button:hover { color: #22c55e !important; }

    .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }
    div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
    }
    div[data-testid="stExpander"] > details {
        background-color: transparent !important;
    }
    div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p {
        color: white !important;
    }

    .footer-card {
        background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: all 0.4s ease;
    }
    .footer-card:hover {
        background: rgba(34, 197, 94, 0.15) !important;
        border: 1px solid #22c55e !important;
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 10px 25px rgba(34, 197, 94, 0.2);
    }

    .feedback-card {
        background: linear-gradient(135deg, rgba(255, 235, 59, 0.1) 0%, rgba(33, 150, 243, 0.1) 100%);
        border-left: 5px solid #ffeb3b;
        padding: 18px;
        margin: 12px 0px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    /* ADD THIS NEW SECTION */
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }

    div[data-testid="stExpander"] details summary {
        background-color: transparent !important;
        color: white !important;
    }

    /* Eh line mouse hatan te white hon ton rokegi */
    div[data-testid="stExpander"] details summary:hover, 
    div[data-testid="stExpander"] details[open] summary {
        background-color: rgba(255, 255, 255, 0.08) !important;
        color: white !important;
    }
    div[data-testid="stExpander"] details summary {
    transition: none !important;
}

    .footer-number { 
        background: #22c55e; color: white; width: 30px; height: 30px; 
        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
        font-weight: 800; margin-bottom: 10px; 
    }
    
    .ai-badge {
        background: rgba(34, 197, 94, 0.1); color: #22c55e;
        border: 1px solid rgba(34, 197, 94, 0.3); padding: 10px 30px; border-radius: 50px;
        font-size: 15px; font-weight: 800; display: inline-block;
    }
    
</style>
""", unsafe_allow_html=True)

# ---------------- 1. LOGIN & INITIAL LOADER ----------------
if not st.session_state.logged_in and not st.session_state.show_loader:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, l_col, _ = st.columns([1, 1.5, 1])
    with l_col:
        st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
        u = st.text_input("Username", placeholder="Enter Your Username")
        p = st.text_input("Password", type="password", placeholder="Enter Your Password")
        if st.button("Launch System 🚀", use_container_width=True):
            if u == "admin" and p == "admin123":
                st.session_state.show_loader = True
                st.rerun()
            else: st.error("Invalid Credentials")

elif st.session_state.show_loader:
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        if lottie_scan: st_lottie(lottie_scan, height=400, key="login_loader")
        st.markdown("<h2 style='text-align:center; color:#22c55e;'>Initializing AI Engine...</h2>", unsafe_allow_html=True)
        time.sleep(7)
        st.session_state.logged_in = True
        st.session_state.show_loader = False
        st.rerun()

# ---------------- 2. MAIN APP ----------------
else:
    n_col1, n_col2, n_col3, n_col4, n_col5, n_col6 = st.columns([1.8, 1.2, 1, 0.8, 1, 0.8])
    with n_col1: st.markdown('<div class="nav-logo" style="margin-left:30px;">AI ATS PRO</div>', unsafe_allow_html=True)
    with n_col2: 
        if st.button("Resume Builder"): st.session_state.page = "Builder"; st.rerun()
    with n_col3: 
        if st.button("Dashboard"): st.session_state.page = "Dashboard"; st.rerun()
    with n_col4: 
        if st.button("History"): st.session_state.page = "History"; st.rerun()
    with n_col5: 
        if st.button("Analytics"): st.session_state.page = "Analytics"; st.rerun()
    with n_col6: 
        if st.button("Logout 🔓"): st.session_state.logged_in = False; st.rerun()

    if st.session_state.page == "Dashboard":
        _, mid, _ = st.columns([0.2, 2, 0.2])
        with mid:
            st.markdown('<div style="text-align: center;"><div class="ai-badge">✨ AI POWERED TECHNOLOGY</div></div><br>', unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
            
            st.markdown('<span style="color:yellow; font-weight:700;">📤 Upload Resumes (PDF)</span>', unsafe_allow_html=True)
            res_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
            
            extracted_data = {} 
            if res_files:
                for res_file in res_files:
                    files = {"file": (res_file.name, res_file.getvalue(), "application/pdf")}
                    try:
                        res = requests.post("http://127.0.0.1:8000/upload", files=files)
                        if res.status_code == 200:
                            text = res.json().get("resume_text", "")
                            extracted_data[res_file.name] = text
                            # Changed label color to yellow here
                            st.markdown(f'<span style="color:yellow; font-weight:700;">📄 Extracted Text: {res_file.name}</span>', unsafe_allow_html=True)
                            st.text_area("", text, height=100, label_visibility="collapsed", key=f"area_{res_file.name}")
                    except: st.error("Backend offline paji!")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<span style="color:yellow; font-weight:700;">📝 Paste Job Description</span>', unsafe_allow_html=True)
            jd_text = st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
            
            if st.button("Analyze Now ✨", key="main_analyze", use_container_width=True):
                if extracted_data and jd_text.strip():
                    with st.empty():
                        if lottie_analyze: st_lottie(lottie_analyze, height=350, key="mixing_loader")
                        st.markdown("<h3 style='text-align:center; color:#22c55e;'>Mixing Data & Benchmarking Skills...</h3>", unsafe_allow_html=True)
                        time.sleep(3.5)
                        st.write("") 

                    for name, resume_text in extracted_data.items():
                        # ADDED EXPANDER BACK
                        with st.expander(f"📊 Results for: {name}", expanded=True):
                            
                            try:
                                rank_res = requests.post("http://127.0.0.1:8000/rank", params={"resume_text": resume_text, "jd_text": jd_text})
                                if rank_res.status_code == 200:
                                    data = rank_res.json()
                                    score = data.get("final_score", 0)
                                    st.markdown(f"### Score: <span style='color:#22c55e;'>{score}%</span>", unsafe_allow_html=True)
                                    st.progress(int(score))
                                    
                                    c1, c2 = st.columns(2)
                                    c1.write(f"**Similarity:** {data.get('similarity', 0)}%")
                                    c2.write(f"**Skill Score:** {data.get('skill_score', 0)}%")
                                    
                                    st.markdown("**❗ Missing Skills:**")
                                    st.write(", ".join(data.get("missing_skills", [])))
                                    
                                    st.markdown("<br><b>🤖 AI Detailed Feedback:</b>", unsafe_allow_html=True)
                                    raw_feedback = data.get('ai_feedback', '')
                                    clean_feedback = raw_feedback.replace("###", "").replace("</div>", "").replace("<div>", "").replace("---", "")
                                    feedback_points = re.split(r'\d+\.', clean_feedback)

                                    for point in feedback_points:
                                        point_text = point.strip()
                                        if point_text:
                                            if ":" in point_text:
                                                parts = point_text.split(":", 1)
                                                title_tag, desc_tag = parts[0].strip(), parts[1].strip()
                                            else:
                                                title_tag, desc_tag = "Insight", point_text

                                            st.markdown(f'''
                                                <div class="feedback-card">
                                                    <span style="color:#ffeb3b; font-weight:bold;">💡 {title_tag}:</span> 
                                                    <div style="margin-top:5px; line-height:1.5;">{desc_tag}</div>
                                                </div>
                                            ''', unsafe_allow_html=True)

                                    # CRITICAL UPDATE: Saving clean_feedback for History.py
                                    st.session_state.scan_history.append({
                                        "name": name, 
                                        "score": score, 
                                        "date": time.strftime("%Y-%m-%d"),
                                        "feedback": clean_feedback 
                                    })
                                else: st.error("Ranking error")
                            except: st.error("Connection failed")
                else: st.error("Paji, files te JD dono check karo!")

        st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
        features = [
            ("01", "Instant Scan", "Advanced parsing engine extracts deep text from any PDF format instantly with 99.9% precision and speed."),
            ("02", "Deep Insights", "Go beyond simple matching; identify the exact technical and soft skill gaps between you and the recruiter."),
            ("03", "JD Matching", "Leverage state-of-the-art AI vector embeddings to check semantic similarity and contextual relevance for the role."),
            ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers, ensuring 100% professional confidentiality."),
            ("05", "AI Feedback", "Get actionable, AI-driven tips to improve your impact verbs, bullet points, and industry-keyword density."),
            ("06", "ATS Optimized", "Specifically calibrated to bypass complex algorithmic filters used by top-tier ATS systems like Workday")
        ]
        
        rows = [features[0:3], features[3:6]]
        for row in rows:
            f_cols = st.columns(3)
            for idx, (num, title, desc) in enumerate(row):
                with f_cols[idx]:
                    st.markdown(f'''<div class="footer-card"><div class="footer-number">{num}</div><h3>{title}</h3><p>{desc}</p></div><br>''', unsafe_allow_html=True)

    elif st.session_state.page == "Builder": show_builder_ui()
    elif st.session_state.page == "History": show_history()
    elif st.session_state.page == "Analytics": show_analytics()

st.markdown("<br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)