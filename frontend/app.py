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
import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI ATS Pro", layout="wide")

# Initialize Session State
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ---------------- PROFESSIONAL CSS ----------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
        font-family: 'Inter', sans-serif;
        color: white;
    }

    /* Navbar */
    .nav-container {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 40px; background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px); border-radius: 100px;
        margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
    }
            
    /* Username te Password de labels nu white karan layi */
label[data-testid="stWidgetLabel"] p {
    color: white !important; 
    font-weight: 700 !important; 
    font-size: 16px !important;
}
    .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }
            
    .nav-admin-btn { background: white; color: black; padding: 8px 20px; border-radius: 10px; font-weight: 800; }

    /* Login Card (White Inputs) */
    .login-card {
        
    }
    .stTextInput input {
        color: black !important; background: white !important;
        border-radius: 10px !important; padding: 12px !important;
            
    }
   .nav-logout-btn button {
        background: white !important; 
        color: black !important; 
        border-radius: 50px !important;
        padding: 5px 25px !important;
        font-weight: 700 !important;
    }


    

    /* Main Content */
    .main-card {
        b
    }
    .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }
    
    /* White Uploader & Area */
    div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
    .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }

    /* --- FULL 6 SECTIONS FOOTER --- */
    .footer-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 50px; }
    .footer-card {
        background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
    }
    .footer-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.08); border-color: #22c55e; }
    .footer-num { 
        background: #22c55e; color: white; width: 35px; height: 35px; 
        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
        font-weight: 800; margin-bottom: 15px; 
    }
            
            /* NAVBAR BUTTON FIX */
.nav-container button {
    background: transparent !important;
    color: #94a3b8 !important;
    border: none !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    cursor: pointer;
}
            
            /* AI Badge */
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1);
#         color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3);
#         padding: 6px 15px; border-radius: 50px;
#         font-size: 11px; font-weight: 800; letter-spacing: 1.2px;
#         display: inline-block; margin-bottom: 10px;
#         box-shadow: 0 0 15px rgba(34, 197, 94, 0.1);
#     }

/* Hover effect (React wali feel 🔥) */
.nav-container button:hover {
    color: #22c55e !important;
}

    .footer-card h3 { font-size: 18px; margin-bottom: 10px; color: white; }
    .footer-card p { font-size: 14px; color: #94a3b8; line-height: 1.5; }

    /* Analyze Button */
    div.stButton > button {
        width: 100%; background: #22c55e !important; color: white !important;
        font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
    }
            
    div.nav_container.nav_logo>button{
            background:radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;

    .nav-admin-btn > button {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
if not st.session_state.logged_in:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, l_col, _ = st.columns([1, 1.5, 1])
    with l_col:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<h2 style="color:#22c55e;">Admin Login</h2><br>', unsafe_allow_html=True)
        u = st.text_input("Username", placeholder="admin")
        p = st.text_input("Password", type="password", placeholder="admin123")
        if st.button("Launch System 🚀"):
            if u == "admin" and p == "admin123":
                st.session_state.logged_in = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MAIN APP ----------------
else:
    # NAVBAR
    st.markdown("""
        <div class="nav-container">
            <div class="nav-logo">AI ATS PRO</div>
            <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 14px; font-weight: 600;">
                <span><button>Resume Builder</button></span><span><button>Dashboard</button></span><span><button>Features</button></span><span><button>Pricing</button></span>
            </div>
            <div class="nav-admin-btn"><button>Logout🔓</button></div>

        </div>
    """, unsafe_allow_html=True)

    

    # SCANNER
    _, mid, _ = st.columns([0.5, 2, 0.5])
    _, mid, _ = st.columns([0.5, 2, 0.5])
    with mid:
        st.markdown("""
            <div style="text-align: center;">
                <div class="ai-badge">✨ AI POWERED TECHNOLOGY</div>
                
            </div><br>
        """, unsafe_allow_html=True)
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1><br>", unsafe_allow_html=True)
        
        st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
        st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
        st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
        
        if st.button("Analyze Now ✨"):
            st.info("Analysis in progress...")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- THE 6 SECTIONS (FOOTER) ---
    st.markdown("<br><br><h2 style='text-align:center;'>Core Project Features</h2><br>", unsafe_allow_html=True)
    
    f_row1 = st.columns(3)
    features = [
        ("01", "Instant Scan", "Deep text extraction from PDFs using advanced parsing algorithms."),
        ("02", "Deep Insights", "Identifies the gap between your skills and the recruiter's expectations."),
        ("03", "JD Matching", "Uses AI vector embeddings to check semantic similarity with the job role."),
        ("04", "Privacy First", "Your data is processed in-memory and is never stored on our servers."),
        ("05", "AI Feedback", "Actionable tips to improve your bullet points and keyword density."),
        ("06", "ATS Optimized", "Calibrated to pass through filters of top ATS systems like Workday.")
    ]

    # Row 1
    for i in range(3):
        with f_row1[i]:
            st.markdown(f'''<div class="footer-card"><div class="footer-number">{features[i][0]}</div><h3>{features[i][1]}</h3><p>{features[i][2]}</p></div>''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Row 2
    f_row2 = st.columns(3)
    for i in range(3, 6):
        with f_row2[i-3]:
            st.markdown(f'''<div class="footer-card"><div class="footer-number">{features[i][0]}</div><h3>{features[i][1]}</h3><p>{features[i][2]}</p></div>''', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)




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
            
#     label[data-testid="stWidgetLabel"] p {
#         color: white !important; 
#         font-weight: 700 !important; 
#         font-size: 16px !important;
#     }

#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; }

#     .stTextInput input {
#         color: black !important; background: white !important;
#         border-radius: 10px !important; padding: 12px !important;
#     }

#     .yellow-label { font-size: 16px; font-weight: 700; color: yellow; margin-bottom: 10px; display: block; }
    
#     div[data-testid="stFileUploadDropzone"] { background: white !important; border-radius: 12px !important; }
#     .stTextArea textarea { background-color: white !important; color: black !important; border-radius: 12px !important; }

#     .footer-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 50px; }
#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 25px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); height: 100%; transition: 0.3s;
#     }
#     .footer-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.08); border-color: #22c55e; }
#     .footer-number { 
#         background: #22c55e; color: white; width: 35px; height: 35px; 
#         border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#         font-weight: 800; margin-bottom: 15px; 
#     }
#     .footer-card h3 { font-size: 18px; margin-bottom: 10px; color: white; }
#     .footer-card p { font-size: 14px; color: #94a3b8; line-height: 1.5; }

#     div.stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#     }
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
#     # NAVBAR WITH WORKING LOGOUT
#     col1, col2, col3 = st.columns([6, 3, 1])

#     with col1:
#         st.markdown('<div class="nav-logo">AI ATS PRO</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#             <div style="display: flex; gap: 30px; color: #94a3b8; font-size: 14px; font-weight: 600; margin-top:10px;">
#                 <span>Resume Builder</span>
#                 <span>Dashboard</span>
#                 <span>Features</span>
#                 <span>Pricing</span>
#             </div>
#         """, unsafe_allow_html=True)

#     with col3:
#         if st.button("Logout 🔓"):
#             st.session_state.logged_in = False
#             st.rerun()

#     # SCANNER
#     _, mid, _ = st.columns([0.5, 2, 0.5])

#     with mid:
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

#     # FEATURES
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

#     for i in range(3):
#         with f_row1[i]:
#             st.markdown(f'''<div class="footer-card"><div class="footer-number">{features[i][0]}</div><h3>{features[i][1]}</h3><p>{features[i][2]}</p></div>''', unsafe_allow_html=True)
    
#     st.markdown("<br>", unsafe_allow_html=True)
    
#     f_row2 = st.columns(3)
#     for i in range(3, 6):
#         with f_row2[i-3]:
#             st.markdown(f'''<div class="footer-card"><div class="footer-number">{features[i][0]}</div><h3>{features[i][1]}</h3><p>{features[i][2]}</p></div>''', unsafe_allow_html=True)

# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)


# import streamlit as st
# import requests

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI ATS Pro", layout="wide")

# # Initialize Session State
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'analysis_result' not in st.session_state:
#     st.session_state.analysis_result = None

# # ---------------- PROFESSIONAL CSS ----------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
#     .stApp {
#         background: radial-gradient(circle at 20% 30%, #062d24 0%, #020617 50%, #1e1b4b 100%) !important;
#         font-family: 'Inter', sans-serif;
#         color: white;
#     }

#     /* Navbar Container */
#     .nav-container {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 10px 40px; background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(15px); border-radius: 100px;
#         margin-bottom: 40px; border: 1px solid rgba(255, 255, 255, 0.1);
#     }
    
#     .nav-logo { font-weight: 800; font-size: 24px; color: #22c55e; letter-spacing: 1px; }
    
#     /* Navigation Links */
#     .nav-links { display: flex; gap: 25px; align-items: center; }
#     .nav-links a { color: #94a3b8; text-decoration: none; font-weight: 600; font-size: 14px; transition: 0.3s; }
#     .nav-links a:hover { color: #22c55e; }

#     /* AI Badge */
#     .ai-badge {
#         background: rgba(34, 197, 94, 0.1);
#         color: #22c55e;
#         border: 1px solid rgba(34, 197, 94, 0.3);
#         padding: 6px 15px; border-radius: 50px;
#         font-size: 11px; font-weight: 800; letter-spacing: 1.2px;
#         display: inline-block; margin-bottom: 10px;
#         box-shadow: 0 0 15px rgba(34, 197, 94, 0.1);
#     }

#     /* --- SPECIFIC UPLOADER BUTTON FIX --- */
#     /* Target the button inside the file uploader */
#     [data-testid="stFileUploadDropzone"] button {
#         background-color: white !important;
#         color: black !important;
#         border: 2px solid black !important;
#         font-weight: 700 !important;
#         border-radius: 8px !important;
#         padding: 0.5rem 1rem !important;
#     }
    
#     [data-testid="stFileUploadDropzone"] button:hover {
#         border-color: #22c55e !important;
#         color: #22c55e !important;
#     }

#     /* Ensure the zone background is white */
#     div[data-testid="stFileUploadDropzone"] {
#         background-color: white !important;
#         border-radius: 12px !important;
#     }

#     /* Logout Button Styling */
#     .logout-btn {
#         background: white !important;
#         color: #1e293b !important;
#         padding: 8px 18px !important;
#         border-radius: 10px !important;
#         font-weight: 800 !important;
#         font-size: 14px !important;
#         border: none !important;
#         display: flex; align-items: center; gap: 5px;
#     }

#     /* Yellow Labels */
#     .yellow-label { font-size: 15px; font-weight: 700; color: yellow; margin-bottom: 8px; display: block; }

#     /* Analyze Button */
#     .stButton > button {
#         width: 100%; background: #22c55e !important; color: white !important;
#         font-weight: 800 !important; border-radius: 12px !important; padding: 12px !important;
#         border: none !important; margin-top: 10px;
#     }
            
#             /* Footer Sections */
#     .footer-section-header {
#         margin-top: 80px !important;
#         margin-bottom: 40px !important;
#     }

#     .footer-card {
#         background: rgba(255, 255, 255, 0.04); padding: 30px; border-radius: 20px; 
#         border: 1px solid rgba(255, 255, 255, 0.1); min-height: 200px; transition: 0.3s;
#         display: flex; flex-direction: column; justify-content: center;
#         margin-bottom: 25px;
#     }
#     .footer-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.08); border-color: #22c55e; }
    
#     .footer-card h3 { font-size: 20px; margin-bottom: 12px; color: #22c55e; font-weight: 700; }
#     .footer-card p { font-size: 15px; color: #94a3b8; line-height: 1.6; }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- MAIN APP ----------------
# if not st.session_state.logged_in:
#     # (Simple login remains same for brevity)
#     st.session_state.logged_in = True 
#     st.rerun()
# else:
#     # NAVBAR (Updated as per screenshot)
#     st.markdown("""
#         <div class="nav-container">
#             <div class="nav-logo">AI ATS PRO</div>
#             <div class="nav-links">
#                 <a href="abc.html">Resume Builder</a>
#                 <a href="#">Dashboard</a>
#                 <a href="#">Features</a>
#                 <a href="#">Pricing</a>
#             </div>
#             <button class="logout-btn">Logout 🔓</button>
#         </div>
#     """, unsafe_allow_html=True)

#     # SCANNER SECTION
#     _, mid, _ = st.columns([0.5, 2, 0.5])
#     with mid:
#         st.markdown("""
#             <div style="text-align: center;">
#                 <div class="ai-badge">✨ AI POWERED TECHNOLOGY</div>
#                 <h1 style='font-size: 40px; margin-top: 5px;'>Is your Resume <span style='color:#22c55e;'>good enough?</span></h1>
#             </div><br>
#         """, unsafe_allow_html=True)
        
#         st.markdown('<span class="yellow-label">📤 Upload Resume (PDF)</span>', unsafe_allow_html=True)
#         # The internal Streamlit logic will now be targeted by the CSS above
#         st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown('<span class="yellow-label">📝 Paste Job Description</span>', unsafe_allow_html=True)
#         st.text_area("", placeholder="Paste JD here...", height=150, label_visibility="collapsed")
        
#         st.button("Analyze Now ✨")

# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>100% Data Secured 🔒</p>", unsafe_allow_html=True)


# st.markdown('<div class="footer-section-header"><h2 style="text-align:center;">Core Project Features</h2></div>', unsafe_allow_html=True)
    
# features = [
#         ("01", "Instant Scan", "Deep text extraction from PDFs using advanced parsing algorithms and high-speed processing."),
#         ("02", "Deep Insights", "Identifies the critical gap between your current skills and the recruiter's specific expectations."),
#         ("03", "JD Matching", "Uses AI vector embeddings to check semantic similarity, ensuring context-aware matching."),
#         ("04", "Privacy First", "Your data is processed strictly in-memory and is never stored on our servers."),
#         ("05", "AI Feedback", "Actionable, real-time tips to improve your resume's bullet points and keyword density."),
#         ("06", "ATS Optimized", "Calibrated to pass through the filtering logic of top ATS systems like Workday.")
#     ]

# for i in range(0, 6, 3):
#         cols = st.columns(3, gap="large")
#         for j in range(3):
#             idx = i + j
#             with cols[j]:
#                 st.markdown(f'''
#                     <div class="footer-card">
#                         <h3>{features[idx][0]}. {features[idx][1]}</h3>
#                         <p>{features[idx][2]}</p>
#                     </div>
#                 ''', unsafe_allow_html=True)

# st.markdown("<br><br><p style='text-align:center; color:#4b5563;'>© 2026 AI ATS Screener Pro</p>", unsafe_allow_html=True)