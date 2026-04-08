# import streamlit as st

# # --- 1. TEMPLATE FUNCTIONS ---

# def get_simple_template(data):
#     return f"""
#     <div style="font-family: 'Inter', sans-serif; color: #333; padding: 40px; background: white; border: 1px solid #eee; border-radius:10px;">
#         <h1 style="text-align: center; text-transform: uppercase; margin-bottom: 5px; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px; color: #666;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['education']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">WORK EXPERIENCE</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['experience']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">PROJECTS</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['projects']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">SKILLS</h3>
#             <p style="padding-left: 10px;">{data['skills']}</p>
#         </div>
#     </div>
#     """

# def get_modern_template(data):
#     img_url = "https://via.placeholder.com/150" 
#     return f"""
#     <div style="font-family: 'Inter', sans-serif; display: flex; min-height: 850px; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
#         <div style="width: 35%; background: #062d24; color: white; padding: 40px; text-align: center;">
#             <img src="{img_url}" style="width: 140px; height: 140px; border-radius: 50%; object-fit: cover; border: 4px solid #22c55e; margin: 0 auto 20px; display: block;" alt="User">
#             <h2 style="margin-bottom: 10px;">{data['name']}</h2>
#             <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 20px 0;">
#             <p style="font-size: 14px; line-height: 1.8; text-align: left;"><b>📧</b> {data['email']}<br><b>📞</b> {data['phone']}<br><b>📍</b> {data['address']}</p>
#             <h4 style="margin-top: 40px; color: #22c55e; letter-spacing: 2px; text-align: left;">SKILLS</h4>
#             <p style="font-size: 14px; opacity: 0.9; text-align: left;">{data['skills']}</p>
#         </div>
#         <div style="width: 65%; background: white; padding: 50px; color: #1e293b;">
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; padding-bottom: 5px;">WORK EXPERIENCE</h3>
#             <p style="white-space: pre-wrap; font-size: 15px; color: #475569;">{data['experience']}</p>
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; padding-bottom: 5px; margin-top: 40px;">PROJECTS</h3>
#             <p style="white-space: pre-wrap; font-size: 15px; color: #475569;">{data['projects']}</p>
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; padding-bottom: 5px; margin-top: 40px;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; font-size: 15px; color: #475569;">{data['education']}</p>
#         </div>
#     </div>
#     """

# def get_advanced_template(data):
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 60px; background: #fff; color: #000; line-height: 1.5; border: 1px solid #ddd;">
#         <div style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px;">
#             <h1 style="margin: 0; font-size: 32px; letter-spacing: 1px;">{data['name']}</h1>
#             <p style="margin: 5px 0; font-style: italic;">{data['address']} | {data['phone']} | {data['email']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Professional Experience</h3>
#             <p style="white-space: pre-wrap;">{data['experience']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Technical Projects</h3>
#             <p style="white-space: pre-wrap;">{data['projects']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Education</h3>
#             <p style="white-space: pre-wrap;">{data['education']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Skills & Certifications</h3>
#             <p>{data['skills']}</p>
#         </div>
#     </div>
#     """

# # --- 2. MAIN UI FUNCTION ---

# def show_builder_ui():
#     st.markdown("""
#         <style>
#         /* Background */
#         .stApp {
#             background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important;
#             background-attachment: fixed !important;
#         }

#         label { color: #f8fafc !important; font-weight: 600 !important; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 28px; margin: 30px 0; }

#         /* Template Cards */
#         .template-card {
#             background: rgba(255, 255, 255, 0.05) !important;
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(255, 255, 255, 0.1) !important;
#             border-radius: 25px;
#             padding: 20px;
#             text-align: center;
#             min-height: 480px;
#             transition: transform 0.3s ease;
#         }
        
#         .template-card:hover { transform: translateY(-5px); }

#         .template-img {
#             width: 100%;
#             height: 350px;
#             object-fit: cover;
#             border-radius: 18px;
#             margin-bottom: 15px;
#             background: rgba(255,255,255,0.1);
#         }

#         /* --- BUTTON WITH HOVER --- */
#         div.stButton > button {
#             background: linear-gradient(135deg, #15803d 0%, #166534 100%) !important;
#             color: white !important;
#             border-radius: 12px !important;
#             font-weight: 700 !important;
#             height: 50px;
#             border: none !important;
#             width: 100% !important;
#             text-transform: uppercase;
#             transition: all 0.3s ease !important;
#         }

#         div.stButton > button:hover {
#             background: #22c55e !important;
#             transform: scale(1.02) !important;
#             box-shadow: 0 8px 20px rgba(34, 197, 94, 0.4) !important;
#         }

#         /* Input styling with Placeholder color fix */
#         .stTextInput input, .stTextArea textarea {
#             background: #ffffff !important; 
#             color: #000000 !important; 
#             border-radius: 10px !important;
#             font-weight: 500 !important;
#         }

#         /* Placeholder color (Light Grey) */
#         ::placeholder { color: #6b7280 !important; opacity: 1; }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-weight:800; font-size: 45px;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'selected_template' not in st.session_state: st.session_state.selected_template = None
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     # --- STEP 1 ---
#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         col1, col2, col3 = st.columns(3)
        
#         # Paji ethe apni photos la deo
#         templates = [
#             (col1, "Simple","simple.jpg"),   
#             (col2, "Modern", ""),   
#             (col3, "Advanced", "")  
#         ]

#         for col, name, img_url in templates:
#             with col:
#                 st.markdown(f'''
#                     <div class="template-card">
#                         <img src="{img_url}" class="template-img" alt="Layout Preview">
#                         <h3 style="color:white;">{name} Layout</h3>
#                     </div>
#                 ''', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=f"btn_{name}"):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     # --- STEP 2: WITH PLACEHOLDERS ---
#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="e.g. Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="e.g. aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="e.g. +91 98765-43210")
#             address = c2.text_input("Location", placeholder="e.g. Chandigarh, Punjab")
            
#             education = st.text_area("Education Details", placeholder="B.Tech in CSE - PU (2022-2026)")
#             skills = st.text_input("Technical Skills", placeholder="Python, React, Streamlit, SQL")
#             experience = st.text_area("Work Experience", placeholder="Intern at Google (3 months) - Python Developer")
#             projects = st.text_area("Key Projects", placeholder="AI Resume Builder using Python and React")
            
#             submit = st.form_submit_button("COMPILE RESUME ✨")
#             if submit:
#                 if name and email:
#                     st.session_state.resume_data = {"name": name, "email": email, "phone": phone, "address": address, "education": education, "skills": skills, "experience": experience, "projects": projects}
#                     st.session_state.builder_step = 3
#                     st.rerun()

#         if st.button("⬅️ BACK TO DESIGN"):
#             st.session_state.builder_step = 1
#             st.rerun()

#     # --- STEP 3 ---
#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Export</div>', unsafe_allow_html=True)
#         data = st.session_state.resume_data
#         temp = st.session_state.selected_template
#         final_html = get_simple_template(data) if temp == "Simple" else get_modern_template(data) if temp == "Modern" else get_advanced_template(data)
            
#         st.markdown('<div style="background: white; border-radius: 20px; padding: 10px;">', unsafe_allow_html=True)
#         st.components.v1.html(final_html, height=800, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         st.download_button("EXPORT HTML 📥", final_html, file_name=f"Resume_{temp}.html")
#         if st.button("🔄 NEW RESUME"):
#             st.session_state.builder_step = 1
#             st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()

# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from PIL import Image

# # --- 1. HELPER: PHOTO & LOCAL IMAGE PROCESSING ---
# def get_local_img_base64(image_path):
#     """Binary ton Base64 convert karda hai local cards layi"""
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Image+Found"

# def process_image(uploaded_file):
#     """User di profile photo process karda hai"""
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()
#         base64_image = base64.b64encode(bytes_data).decode()
#         return f"data:image/png;base64,{base64_image}"
#     return "https://via.placeholder.com/150"

# # --- 2. TEMPLATES (HTML Layouts) ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: 'Inter', sans-serif; color: #333; padding: 40px; background: white; border-radius:10px; max-width: 800px; margin: auto;">
#         <h1 style="text-align: center; text-transform: uppercase; margin-bottom: 5px; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px; color: #666;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['education']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">SKILLS</h3>
#             <p style="padding-left: 10px;">{data['skills']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     photo_html = f'<img src="{data["photo"]}" style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; border: 4px solid #22c55e; margin: 0 auto 20px; display: block;">'
#     return f"""
#     <div style="font-family: 'Inter', sans-serif; display: flex; min-height: 850px; border-radius: 15px; overflow: hidden; max-width: 900px; margin: auto; background: white;">
#         <div style="width: 35%; background: #062d24; color: white; padding: 40px; text-align: center;">
#             {photo_html}
#             <h2 style="margin-bottom: 10px;">{data['name']}</h2>
#             <p style="font-size: 14px; text-align: left;">📧 {data['email']}<br>📞 {data['phone']}<br>📍 {data['address']}</p>
#             <h4 style="margin-top: 40px; color: #22c55e; text-align: left;">SKILLS</h4>
#             <p style="font-size: 14px; text-align: left;">{data['skills']}</p>
#         </div>
#         <div style="width: 65%; background: white; padding: 50px; color: #1e293b;">
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e;">WORK EXPERIENCE</h3>
#             <p style="white-space: pre-wrap;">{data['experience']}</p>
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; margin-top: 30px;">PROJECTS</h3>
#             <p style="white-space: pre-wrap;">{data['projects']}</p>
#         </div>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<img src="{data["photo"]}" style="width: 150px; height: 180px; object-fit: cover; border: 2px solid #000; float: right; margin-left: 20px;">'
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 50px; background: #fff; color: #000; border: 1px solid #ddd; max-width: 800px; margin: auto;">
#         {photo_html}
#         <h1 style="margin: 0; font-size: 32px;">{data['name']}</h1>
#         <p style="font-style: italic;">{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000;">
#         <h3 style="text-transform: uppercase; border-bottom: 1px solid #000;">Professional Experience</h3>
#         <p style="white-space: pre-wrap;">{data['experience']}</p>
#         <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; margin-top: 20px;">Education</h3>
#         <p style="white-space: pre-wrap;">{data['education']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""
#         <style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600 !important; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
        
#         /* Symmetrical Card Styling */
#         .template-card {
#             background: rgba(255,255,255,0.05);
#             padding: 20px;
#             border-radius: 20px;
#             border: 1px solid rgba(255,255,255,0.1);
#             height: 480px; /* Fixed height for symmetry */
#             display: flex;
#             flex-direction: column;
#             justify-content: space-between;
#             transition: 0.3s ease;
#         }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .template-img {
#             width: 100%;
#             height: 320px; /* Fixed image height */
#             object-fit: cover;
#             border-radius: 12px;
#         }
#         .stButton > button { margin-top: 15px !important; }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'selected_template' not in st.session_state: st.session_state.selected_template = None
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     # --- STEP 1: LAYOUT SELECTION ---
#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         col1, col2, col3 = st.columns(3)
        
#         # Config for Symmetry
#         layouts = [
#             ("Simple", col1, "simple.jpg"), 
#             ("Modern", col2, "modern.jpg"), 
#             ("Advanced", col3, "advanced.jpg")
#         ]

#         for name, col, img_path in layouts:
#             with col:
#                 img_data = get_local_img_base64(img_path)
#                 st.markdown(f'''
#                     <div class="template-card">
#                         <div>
#                             <img src="{img_data}" class="template-img">
#                             <h4 style="color:white; text-align:center; margin-top:15px;">{name} Layout</h4>
#                         </div>
#                     </div>
#                 ''', unsafe_allow_html=True)
                
#                 if st.button(f"USE {name.upper()}", key=f"btn_{name}", use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     # --- STEP 2: DATA ENTRY ---
#     elif st.session_state.builder_step == 2:
#         temp_name = st.session_state.get('selected_template', 'Layout')
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({temp_name})</div>', unsafe_allow_html=True)
        
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="e.g. Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="e.g. aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="e.g. +91 98765-43210")
#             address = c2.text_input("Location", placeholder="e.g. Chandigarh, Punjab")
            
#             user_photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 user_photo = st.file_uploader("Upload Profile Photo", type=['jpg', 'png', 'jpeg'])

#             edu = st.text_area("Education", placeholder="e.g. B.Tech in CSE - Punjab University (2024)")
#             skills = st.text_input("Skills", placeholder="e.g. Python, SQL, React, AI/ML")
#             exp = st.text_area("Experience", placeholder="e.g. Software Intern at XYZ Solutions (6 Months)")
#             proj = st.text_area("Projects", placeholder="e.g. AI Resume Builder using Python & Streamlit")
            
#             if st.form_submit_button("COMPILE RESUME ✨"):
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": address,
#                     "education": edu, "skills": skills, "experience": exp, "projects": proj,
#                     "photo": process_image(user_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#         if st.button("⬅️ BACK TO DESIGN"):
#             st.session_state.builder_step = 1
#             st.rerun()

#     # --- STEP 3: PREVIEW & DOWNLOAD ---
#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         data = st.session_state.resume_data
#         temp = st.session_state.selected_template
        
#         if temp == "Simple": html = get_simple_template(data)
#         elif temp == "Modern": html = get_modern_template(data)
#         else: html = get_advanced_template(data)
            
#         st.markdown('<div style="background:white; border-radius:20px; padding:20px; border:3px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=800, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         col_dl, col_back = st.columns(2)
#         with col_dl:
#             st.download_button("📥 SAVE AS HTML/PDF", html, file_name=f"Resume_{data['name']}.html", use_container_width=True)
#         with col_back:
#             if st.button("🎨 BACK TO DESIGN", use_container_width=True):
#                 st.session_state.builder_step = 1
#                 st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from xhtml2pdf import pisa  # Ensure you've run: pip install xhtml2pdf

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Image"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     """HTML nu PDF binary vich convert karda hai"""
#     pdf_buffer = BytesIO()
#     pisa_status = pisa.CreatePDF(html_string, dest=pdf_buffer)
#     if pisa_status.err:
#         return None
#     return pdf_buffer.getvalue()

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""<div style="font-family:sans-serif; padding:30px; background:white; color:#333;">
#         <h1 style="text-align:center; color:#1e1b4b;">{data['name']}</h1>
#         <p style="text-align:center; border-bottom:2px solid #22c55e; padding-bottom:10px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <h3>EDUCATION</h3><p>{data['education']}</p>
#         <h3>SKILLS</h3><p>{data['skills']}</p>
#         <h3>EXPERIENCE</h3><p>{data['experience']}</p>
#     </div>"""

# def get_modern_template(data):
#     return f"""<div style="font-family:sans-serif; display:flex; background:white; min-height:800px;">
#         <div style="width:35%; background:#062d24; color:white; padding:30px; text-align:center;">
#             <img src="{data['photo']}" style="width:120px; height:120px; border-radius:50%; border:3px solid #22c55e;">
#             <h2>{data['name']}</h2>
#             <p style="font-size:12px; text-align:left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width:65%; padding:40px; color:#1e293b;">
#             <h3 style="border-bottom:2px solid #22c55e;">EXPERIENCE</h3><p>{data['experience']}</p>
#             <h3 style="border-bottom:2px solid #22c55e;">PROJECTS</h3><p>{data['projects']}</p>
#         </div>
#     </div>"""

# def get_advanced_template(data):
#     return f"""<div style="font-family:serif; padding:50px; background:white; color:black;">
#         <h1 style="margin:0;">{data['name']}</h1>
#         <p>{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr>
#         <h3>PROFESSIONAL EXPERIENCE</h3><p>{data['experience']}</p>
#         <h3>EDUCATION</h3><p>{data['education']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""
#         <style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 30px; margin-bottom: 25px; text-align: center; }
        
#         /* Step 2 Label Color */
#         label { color: white !important; font-size: 1.1rem !important; }

#         /* Symmetrical Card Layout for Step 1 */
#         .template-card {
#             background: rgba(255,255,255,0.05); padding: 15px; border-radius: 20px;
#             border: 1px solid rgba(255,255,255,0.1); height: 480px;
            
#         }
#         .template-img { width: 100%; height: 320px; object-fit: cover; border-radius: 12px; }
#         div.stButton > button { height: 10px !important; }
#         </style>
#     """, unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'selected_template' not in st.session_state: st.session_state.selected_template = "Simple"
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     # --- STEP 1: SELECT DESIGN ---
#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         # Using columns ensures horizontal symmetry like in your photo
#         col1, col2, col3 = st.columns(3)
#         layouts = [("Simple", "simple.jpg", col1), ("Modern", "modern.jpg", col2), ("Advanced", "advanced.jpg", col3)]
        
#         for name, img_p, col in layouts:
#             with col:
#                 st.markdown(f'''<div class="template-card">
#                     <img src="{get_local_img_base64(img_p)}" class="template-img">
#                     <h4 style="color:white; text-align:center; margin-top:10px;">{name} Layout</h4>
#                 </div>''', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=f"btn_{name}", use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     # --- STEP 2: ENTER DETAILS ---
#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
        
#         d = st.session_state.resume_data 
        
#         with st.container():
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", value=d.get('name', ''), placeholder="Aman Deep Singh")
#             email = c2.text_input("Email ID", value=d.get('email', ''), placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", value=d.get('phone', ''), placeholder="+91 98765-43210")
#             addr = c2.text_input("Location", value=d.get('address', ''), placeholder="Chandigarh, Punjab")
            
#             photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 photo = st.file_uploader("Upload Profile Photo", type=['jpg', 'png'])

#             edu = st.text_area("Education", value=d.get('education', ''), placeholder="Degree, University, Year")
#             skl = st.text_input("Skills", value=d.get('skills', ''), placeholder="Python, React, etc.")
#             exp = st.text_area("Experience", value=d.get('experience', ''), placeholder="Your work history")
#             prj = st.text_area("Projects", value=d.get('projects', ''), placeholder="Major projects")
            
#             st.markdown("<br>", unsafe_allow_html=True)
            
#             # --- SYMMETRICAL BUTTONS IN STEP 2 ---
#             btn_step2_col1, btn_step2_col2 = st.columns(2)
            
#             with btn_step2_col1:
#                 if st.button("⬅️ BACK TO DESIGN", use_container_width=True):
#                     st.session_state.builder_step = 1
#                     st.rerun()
            
#             with btn_step2_col2:
#                 if st.button("COMPILE RESUME ✨", type="primary", use_container_width=True):
#                     st.session_state.resume_data = {
#                         "name": name, "email": email, "phone": phone, "address": addr,
#                         "education": edu, "skills": skl, "experience": exp, "projects": prj,
#                         "photo": process_image(photo) if photo else d.get('photo', "https://via.placeholder.com/150")
#                     }
#                     st.session_state.builder_step = 3
#                     st.rerun()

#     # --- STEP 3: PREVIEW & DOWNLOAD ---
#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Download</div>', unsafe_allow_html=True)
#         data = st.session_state.resume_data
        
#         if st.session_state.selected_template == "Simple": html_content = get_simple_template(data)
#         elif st.session_state.selected_template == "Modern": html_content = get_modern_template(data)
#         else: html_content = get_advanced_template(data)

#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html_content, height=600, scrolling=True)
#         st.markdown('</div><br>', unsafe_allow_html=True)

#         # Symmetrical Row for Final Actions
#         btn_col1, btn_col2, btn_col3 = st.columns(3)
#         pdf_bytes = convert_html_to_pdf(html_content)
        
#         with btn_col1:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD PDF", data=pdf_bytes, file_name="Resume.pdf", mime="application/pdf", use_container_width=True)
#         with btn_col2:
#             if st.button("✏️ RE-EDIT DETAILS", use_container_width=True):
#                 st.session_state.builder_step = 2
#                 st.rerun()
#         with btn_col3:
#             if st.button("🎨 BACK TO DESIGN", use_container_width=True):
#                 st.session_state.builder_step = 1
#                 st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from xhtml2pdf import pisa  # PDF conversion layi zaroori hai

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     """HTML nu PDF bytes vich convert karda hai"""
#     pdf_output = BytesIO()
#     pisa_status = pisa.CreatePDF(BytesIO(html_string.encode("UTF-8")), dest=pdf_output)
#     if pisa_status.err:
#         return None
#     return pdf_output.getvalue()

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3>EDUCATION</h3><p>{data['education']}</p>
#             <h3>SKILLS</h3><p>{data['skills']}</p>
#             <h3>EXPERIENCE</h3><p>{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; display: flex; background: white; min-height: 800px;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center;">
#             <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px;">
#             <h2>{data['name']}</h2>
#             <p style="font-size: 12px; text-align: left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width: 70%; padding: 40px; color: #1e293b;">
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p>{data['experience']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p>{data['projects']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EDUCATION</h3><p>{data['education']}</p>
#         </div>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right;"><img src="{data["photo"]}" style="width: 100px; height: 120px; border: 1px solid #000;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 50px; background: white; color: black;">
#         {photo_html}
#         <h1 style="margin: 0; text-transform: uppercase;">{data['name']}</h1>
#         <p>{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000; clear: both; margin-top: 15px;">
#         <h3>EXPERIENCE</h3><p>{data['experience']}</p>
#         <h3>PROJECTS</h3><p>{data['projects']}</p>
#         <h3>EDUCATION</h3><p>{data['education']}</p>
#         <h3>SKILLS</h3><p>{data['skills']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; }
#         .template-img { width: 100%; height: 300px; object-fit: cover; border-radius: 12px; }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "advanced.jpg")]
#         for i, (name, img) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><img src="{get_local_img_base64(img)}" class="template-img"><h4 style="color:white; margin-top:10px;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name")
#             email = c2.text_input("Email ID")
#             phone = c1.text_input("Phone Number")
#             addr = c2.text_input("Location")
#             u_photo = st.file_uploader("Upload Photo", type=['jpg','png']) if st.session_state.selected_template != "Simple" else None
#             edu = st.text_area("Education")
#             skl = st.text_input("Technical Skills")
#             exp = st.text_area("Experience")
#             prj = st.text_area("Key Projects")
#             if st.form_submit_button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {"name":name,"email":email,"phone":phone,"address":addr,"education":edu,"skills":skl,"experience":exp,"projects":prj,"photo":process_image(u_photo)}
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         st.components.v1.html(html, height=700, scrolling=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from xhtml2pdf import pisa  

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     # Added PDF specific styles to force proper sizing and margins
#     pdf_style = """
#     <style>
#         @page {
#             size: A4;
#             margin: 0mm;
#         }
#         body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
#         div { box-sizing: border-box; }
#     </style>
#     """
#     full_html = pdf_style + html_string
#     pdf_output = BytesIO()
#     pisa_status = pisa.CreatePDF(BytesIO(full_html.encode("UTF-8")), dest=pdf_output)
#     if pisa_status.err:
#         return None
#     return pdf_output.getvalue()

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="padding: 40px; background: white; color: #333; min-height: 1000px;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b; margin-bottom: 5px;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px; font-size: 12px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">PROFESSIONAL SUMMARY</h3>
#             <p style="white-space: pre-wrap; font-size: 13px;">{data['summary']}</p>
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; font-size: 13px;">{data['education']}</p>
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">SKILLS</h3>
#             <p style="font-size: 13px;">{data['skills']}</p>
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">EXPERIENCE</h3>
#             <p style="white-space: pre-wrap; font-size: 13px;">{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     return f"""
#     <div style="display: block; background: white; min-height: 1120px;">
#         <table style="width: 100%; border-collapse: collapse;">
#             <tr>
#                 <td style="width: 30%; background: #062d24; color: white; padding: 30px; vertical-align: top; text-align: center;">
#                     <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 60px; border: 3px solid #22c55e; margin-bottom: 20px;">
#                     <h2 style="margin-bottom: 10px;">{data['name']}</h2>
#                     <p style="font-size: 11px; text-align: left; line-height: 1.5;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#                 </td>
#                 <td style="width: 70%; padding: 40px; color: #1e293b; vertical-align: top;">
#                     <h3 style="border-bottom: 2px solid #22c55e; color: #062d24; margin-top: 0;">PROFESSIONAL SUMMARY</h3>
#                     <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 20px;">{data['summary']}</p>
#                     <h3 style="border-bottom: 2px solid #22c55e; color: #062d24;">EXPERIENCE</h3>
#                     <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 20px;">{data['experience']}</p>
#                     <h3 style="border-bottom: 2px solid #22c55e; color: #062d24;">PROJECTS</h3>
#                     <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 20px;">{data['projects']}</p>
#                     <h3 style="border-bottom: 2px solid #22c55e; color: #062d24;">EDUCATION</h3>
#                     <p style="white-space: pre-wrap; font-size: 12px;">{data['education']}</p>
#                 </td>
#             </tr>
#         </table>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right;"><img src="{data["photo"]}" style="width: 100px; height: 120px; border: 1px solid #000;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 40px; background: white; color: black; min-height: 1000px;">
#         {photo_html}
#         <h1 style="margin: 0; text-transform: uppercase; font-size: 24px;">{data['name']}</h1>
#         <p style="font-size: 13px; margin-top: 5px;">{data['address']} | {data['phone']} | {data['email']}</p>
#         <div style="border-top: 2px solid #000; clear: both; margin-top: 10px; padding-top: 10px;">
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 16px; margin-bottom: 5px;">Professional Summary</h3>
#             <p style="white-space: pre-wrap; font-size: 13px; margin-bottom: 15px;">{data['summary']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 16px; margin-bottom: 5px;">Professional Experience</h3>
#             <p style="white-space: pre-wrap; font-size: 13px; margin-bottom: 15px;">{data['experience']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 16px; margin-bottom: 5px;">Key Projects</h3>
#             <p style="white-space: pre-wrap; font-size: 13px; margin-bottom: 15px;">{data['projects']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 16px; margin-bottom: 5px;">Education</h3>
#             <p style="white-space: pre-wrap; font-size: 13px; margin-bottom: 15px;">{data['education']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 16px; margin-bottom: 5px;">Skills</h3>
#             <p style="font-size: 13px;">{data['skills']}</p>
#         </div>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .template-img { width: 100%; height: 300px; object-fit: cover; border-radius: 12px; }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "advanced.jpg")]
#         for i, (name, img) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><img src="{get_local_img_base64(img)}" class="template-img"><h4 style="color:white; margin-top:10px;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="+91 98765-43210")
#             addr = c2.text_input("Location", placeholder="Chandigarh, Punjab")
            
#             u_photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 u_photo = st.file_uploader("Upload Profile Photo", type=['jpg','png','jpeg'])
            
#             summary = st.text_area("Professional Summary")
#             edu = st.text_area("Education")
#             skl = st.text_input("Technical Skills")
#             exp = st.text_area("Experience")
#             prj = st.text_area("Key Projects")
            
#             if st.form_submit_button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": process_image(u_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=750, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64

# # --- 1. FUNCTION TO CONVERT IMAGE TO BASE64 (Optional but recommended) ---
# # Is naal image path di problem nahi aaundi
# def get_image_base64(path):
#     try:
#         with open(path, "rb") as image_file:
#             return base64.b64encode(image_file.read()).decode()
#     except:
#         return ""

# # --- 2. TEMPLATE FUNCTIONS ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: 'Inter', sans-serif; color: #333; padding: 40px; background: white; border: 1px solid #eee; border-radius:10px;">
#         <h1 style="text-align: center; text-transform: uppercase; margin-bottom: 5px; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px; color: #666;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['education']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">WORK EXPERIENCE</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['experience']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">PROJECTS</h3>
#             <p style="white-space: pre-wrap; padding-left: 10px;">{data['projects']}</p>
#         </div>
#         <div style="margin-top: 20px;">
#             <h3 style="background: #f8fafc; padding: 8px; color: #1e1b4b; border-left: 5px solid #22c55e;">SKILLS</h3>
#             <p style="padding-left: 10px;">{data['skills']}</p>
#         </div>
#     </div>
#     """

# def get_modern_template(data):
#     return f"""
#     <div style="font-family: 'Inter', sans-serif; display: flex; min-height: 850px; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
#         <div style="width: 35%; background: #062d24; color: white; padding: 40px; text-align: center;">
#             <h2 style="margin-bottom: 10px;">{data['name']}</h2>
#             <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 20px 0;">
#             <p style="font-size: 14px; line-height: 1.8; text-align: left;"><b>📧</b> {data['email']}<br><b>📞</b> {data['phone']}<br><b>📍</b> {data['address']}</p>
#             <h4 style="margin-top: 40px; color: #22c55e; letter-spacing: 2px; text-align: left;">SKILLS</h4>
#             <p style="font-size: 14px; opacity: 0.9; text-align: left;">{data['skills']}</p>
#         </div>
#         <div style="width: 65%; background: white; padding: 50px; color: #1e293b;">
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; padding-bottom: 5px;">WORK EXPERIENCE</h3>
#             <p style="white-space: pre-wrap; font-size: 15px; color: #475569;">{data['experience']}</p>
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; padding-bottom: 5px; margin-top: 40px;">PROJECTS</h3>
#             <p style="white-space: pre-wrap; font-size: 15px; color: #475569;">{data['projects']}</p>
#             <h3 style="color: #062d24; border-bottom: 2px solid #22c55e; padding-bottom: 5px; margin-top: 40px;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; font-size: 15px; color: #475569;">{data['education']}</p>
#         </div>
#     </div>
#     """

# def get_advanced_template(data):
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 60px; background: #fff; color: #000; line-height: 1.5; border: 1px solid #ddd;">
#         <div style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px;">
#             <h1 style="margin: 0; font-size: 32px; letter-spacing: 1px;">{data['name']}</h1>
#             <p style="margin: 5px 0; font-style: italic;">{data['address']} | {data['phone']} | {data['email']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Professional Experience</h3>
#             <p style="white-space: pre-wrap;">{data['experience']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Technical Projects</h3>
#             <p style="white-space: pre-wrap;">{data['projects']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Education</h3>
#             <p style="white-space: pre-wrap;">{data['education']}</p>
#         </div>
#         <div style="margin-top: 30px;">
#             <h3 style="text-transform: uppercase; border-bottom: 1px solid #000; font-size: 18px; margin-bottom: 10px;">Skills & Certifications</h3>
#             <p>{data['skills']}</p>
#         </div>
#     </div>
#     """

# # --- 3. MAIN UI FUNCTION ---
# def show_builder_ui():
#     st.markdown("""
#         <style>
#         .stApp {
#             background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important;
#             background-attachment: fixed !important;
#         }
#         label { color: #f8fafc !important; font-weight: 600 !important; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 28px; margin: 30px 0; }

#         .template-card {
#             background: rgba(255, 255, 255, 0.05) !important;
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(255, 255, 255, 0.1) !important;
#             border-radius: 25px;
#             padding: 20px;
#             text-align: center;
#             min-height: 480px;
#         }

#         .template-img {
#             width: 100%;
#             height: 350px;
#             object-fit: cover;
#             border-radius: 18px;
#             margin-bottom: 15px;
#             border: 1px solid rgba(255,255,255,0.1);
#         }

#         div.stButton > button {
#             background: linear-gradient(135deg, #15803d 0%, #166534 100%) !important;
#             color: white !important;
#             border-radius: 12px !important;
#             font-weight: 700 !important;
#             height: 50px;
#             border: none !important;
#             width: 100% !important;
#             transition: all 0.3s ease !important;
#         }
#         div.stButton > button:hover {
#             background: #22c55e !important;
#             transform: scale(1.02) !important;
#         }
#         .stTextInput input, .stTextArea textarea {
#             background: #ffffff !important; 
#             color: #000000 !important; 
#             border-radius: 10px !important;
#         }
#         ::placeholder { color: #6b7280 !important; }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-weight:800; font-size: 45px;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1

#     # --- STEP 1 ---
#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         col1, col2, col3 = st.columns(3)
        
#         # --- PHOTOS LAGON DA TAREEKA ---
#         # 1. Je photo folder ch hai: "assets/simple.png"
#         # 2. Je online hai: "https://example.com/photo.jpg"
        
#         # Local Image example (je tusi folder ch rakhi hai):
#         # simple_img = f"data:image/png;base64,{get_image_base64('simple.png')}"
        
#         templates = [
#             (col1, "Simple", "https://img.freepik.com/free-vector/professional-resume-template-minimalist-style_23-2148389020.jpg"),   
#             (col2, "Modern", "https://img.freepik.com/free-vector/modern-professional-resume-template_23-2148412496.jpg"),   
#             (col3, "Advanced", "https://img.freepik.com/free-vector/creative-business-resume-template_23-2148415178.jpg")  
#         ]

#         for col, name, img_url in templates:
#             with col:
#                 st.markdown(f'''
#                     <div class="template-card">
#                         <img src="{img_url}" class="template-img">
#                         <h3 style="color:white;">{name} Layout</h3>
#                     </div>
#                 ''', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=f"btn_{name}"):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     # --- STEP 2 ---
#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="Aman Deep")
#             email = c2.text_input("Email ID", placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="+91 98XXX-XXXXX")
#             address = c2.text_input("Location", placeholder="Chandigarh, IN")
#             education = st.text_area("Education", placeholder="B.Tech in CSE...")
#             skills = st.text_input("Skills", placeholder="Python, React...")
#             experience = st.text_area("Experience", placeholder="Describe your roles...")
#             projects = st.text_area("Projects", placeholder="Project details...")
            
#             if st.form_submit_button("COMPILE RESUME ✨"):
#                 st.session_state.resume_data = {"name": name, "email": email, "phone": phone, "address": address, "education": education, "skills": skills, "experience": experience, "projects": projects}
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     # --- STEP 3 ---
#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview</div>', unsafe_allow_html=True)
#         data = st.session_state.resume_data
#         temp = st.session_state.selected_template
#         html = get_simple_template(data) if temp == "Simple" else get_modern_template(data) if temp == "Modern" else get_advanced_template(data)
#         st.components.v1.html(html, height=800, scrolling=True)
#         st.download_button("EXPORT HTML 📥", html, file_name="Resume.html")

# if __name__ == "__main__":
#     show_builder_ui()

# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from xhtml2pdf import pisa  # PDF conversion layi zaroori hai

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     pdf_output = BytesIO()
#     pisa_status = pisa.CreatePDF(BytesIO(html_string.encode("UTF-8")), dest=pdf_output)
#     if pisa_status.err:
#         return None
#     return pdf_output.getvalue()

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3>PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3>EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#             <h3>SKILLS</h3><p>{data['skills']}</p>
#             <h3>EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; display: flex; background: white; min-height: 800px;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center;">
#             <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
#             <h2>{data['name']}</h2>
#             <p style="font-size: 12px; text-align: left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width: 70%; padding: 40px; color: #1e293b;">
#             <h3 style="border-bottom: 2px solid #22c55e;">PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p style="white-space: pre-wrap;">{data['projects']}</p>
#             <h3 style="border-bottom: 20px solid #fff; border-bottom: 2px solid #22c55e;">EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#         </div>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right; margin-left: 15px;"><img src="{data["photo"]}" style="width: 110px; height: 130px; border: 1px solid #000; object-fit: cover;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 50px; background: white; color: black; border: 1px solid #eee;">
#         {photo_html}
#         <h1 style="margin: 0; text-transform: uppercase; font-size: 26px;">{data['name']}</h1>
#         <p style="font-size: 14px;">{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000; clear: both; margin-top: 15px;">
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Summary</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['summary']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Experience</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['experience']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Key Projects</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['projects']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Education</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['education']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Skills</h3>
#         <p style="font-size: 14px;">{data['skills']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .template-img { width: 100%; height: 300px; object-fit: cover; border-radius: 12px; }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "advanced.jpg")]
#         for i, (name, img) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><img src="{get_local_img_base64(img)}" class="template-img"><h4 style="color:white; margin-top:10px;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="+91 98765-43210")
#             addr = c2.text_input("Location", placeholder="Chandigarh, Punjab")
            
#             u_photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 u_photo = st.file_uploader("Upload Profile Photo", type=['jpg','png','jpeg'])
            
#             summary = st.text_area("Professional Summary")
#             edu = st.text_area("Education")
#             skl = st.text_input("Technical Skills")
#             exp = st.text_area("Experience")
#             prj = st.text_area("Key Projects")
            
#             if st.form_submit_button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": process_image(u_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=750, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# # import streamlit as st
# # import base64
# # import os
# # from io import BytesIO
# # import pdfkit   # ✅ NEW (better than xhtml2pdf)

# # # ---------- CONFIG (IMPORTANT) ----------
# # # wkhtmltopdf path (change if needed)
# # config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")


# # # ---------- HELPER FUNCTIONS ----------
# # def get_local_img_base64(image_path):
# #     if os.path.exists(image_path):
# #         with open(image_path, "rb") as img_file:
# #             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
# #     return "https://via.placeholder.com/300x400?text=No+Preview"

# # def process_image(uploaded_file):
# #     if uploaded_file:
# #         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
# #     return "https://via.placeholder.com/150"

# # def convert_html_to_pdf(html_string):
# #     return pdfkit.from_string(html_string, False, configuration=config)


# # # ---------- TEMPLATES ----------
# # def get_simple_template(d):
# #     return f"""
# #     <div style="font-family: Arial; padding:40px;">
# #         <h1 style="text-align:center;">{d['name'] or "YOUR NAME"}</h1>
# #         <p style="text-align:center;">
# #             {d['email'] or "email@example.com"} | {d['phone'] or "+91 XXXXX"} | {d['address'] or "Your Address"}
# #         </p>

# #         <h3>SUMMARY</h3>
# #         <p>{d['summary'] or "Your professional summary..."}</p>

# #         <h3>EDUCATION</h3>
# #         <p>{d['education'] or "Your education..."}</p>

# #         <h3>SKILLS</h3>
# #         <p>{d['skills'] or "Your skills..."}</p>

# #         <h3>EXPERIENCE</h3>
# #         <p>{d['experience'] or "Your experience..."}</p>
# #     </div>
# #     """


# # def get_modern_template(d):
# #     return f"""
# #     <div style="display:flex; font-family:Arial;">
# #         <div style="width:30%; background:#062d24; color:white; padding:20px;">
# #             <img src="{d['photo']}" style="width:100px; border-radius:50%;">
# #             <h2>{d['name'] or "YOUR NAME"}</h2>
# #             <p>{d['email'] or "email"}<br>{d['phone'] or "phone"}</p>
# #         </div>

# #         <div style="width:70%; padding:30px;">
# #             <h3>SUMMARY</h3>
# #             <p>{d['summary'] or "Your summary..."}</p>

# #             <h3>EXPERIENCE</h3>
# #             <p>{d['experience'] or "Your experience..."}</p>

# #             <h3>PROJECTS</h3>
# #             <p>{d['projects'] or "Your projects..."}</p>

# #             <h3>EDUCATION</h3>
# #             <p>{d['education'] or "Your education..."}</p>
# #         </div>
# #     </div>
# #     """


# # def get_advanced_template(d):
# #     return f"""
# #     <div style="font-family: 'Times New Roman'; padding:40px;">
        
# #         <div style="text-align:right;">
# #             <img src="{d['photo']}" style="width:100px;">
# #         </div>

# #         <h1>{d['name'] or "YOUR NAME"}</h1>
# #         <p>{d['address'] or "Address"} | {d['phone'] or "Phone"} | {d['email'] or "Email"}</p>
# #         <hr>

# #         <h3>SUMMARY</h3>
# #         <p>{d['summary'] or "Your summary..."}</p>

# #         <h3>EXPERIENCE</h3>
# #         <p>{d['experience'] or "Your experience..."}</p>

# #         <h3>PROJECTS</h3>
# #         <p>{d['projects'] or "Your projects..."}</p>

# #         <h3>EDUCATION</h3>
# #         <p>{d['education'] or "Your education..."}</p>

# #         <h3>SKILLS</h3>
# #         <p>{d['skills'] or "Your skills..."}</p>
# #     </div>
# #     """


# # # ---------- MAIN UI ----------
# # def show_builder_ui():
# #     st.title("🔥 AI Resume Builder PRO")

# #     if 'step' not in st.session_state:
# #         st.session_state.step = 1
# #     if 'data' not in st.session_state:
# #         st.session_state.data = {}

# #     # STEP 1
# #     if st.session_state.step == 1:
# #         st.subheader("Select Template")

# #         if st.button("Simple"):
# #             st.session_state.template = "simple"
# #             st.session_state.step = 2
# #             st.rerun()

# #         if st.button("Modern"):
# #             st.session_state.template = "modern"
# #             st.session_state.step = 2
# #             st.rerun()

# #         if st.button("Advanced"):
# #             st.session_state.template = "advanced"
# #             st.session_state.step = 2
# #             st.rerun()

# #     # STEP 2
# #     elif st.session_state.step == 2:
# #         st.subheader("Enter Details")

# #         with st.form("form"):
# #             name = st.text_input("Name")
# #             email = st.text_input("Email")
# #             phone = st.text_input("Phone")
# #             address = st.text_input("Address")
# #             photo = st.file_uploader("Photo", type=["png", "jpg"])

# #             summary = st.text_area("Summary")
# #             education = st.text_area("Education")
# #             skills = st.text_input("Skills")
# #             experience = st.text_area("Experience")
# #             projects = st.text_area("Projects")

# #             if st.form_submit_button("Generate"):
# #                 st.session_state.data = {
# #                     "name": name,
# #                     "email": email,
# #                     "phone": phone,
# #                     "address": address,
# #                     "photo": process_image(photo),
# #                     "summary": summary,
# #                     "education": education,
# #                     "skills": skills,
# #                     "experience": experience,
# #                     "projects": projects
# #                 }
# #                 st.session_state.step = 3
# #                 st.rerun()

# #     # STEP 3
# #     elif st.session_state.step == 3:
# #         d = st.session_state.data
# #         t = st.session_state.template

# #         if t == "simple":
# #             html = get_simple_template(d)
# #         elif t == "modern":
# #             html = get_modern_template(d)
# #         else:
# #             html = get_advanced_template(d)

# #         st.subheader("Preview")

# #         # ✅ FIXED CENTERED PREVIEW
# #         st.components.v1.html(f"""
# #         <div style="display:flex; justify-content:center;">
# #             <div style="width:800px;">
# #                 {html}
# #             </div>
# #         </div>
# #         """, height=900, scrolling=True)

# #         # PDF
# #         pdf = convert_html_to_pdf(html)

# #         if pdf:
# #             st.download_button("📥 Download PDF", pdf, "resume.pdf")

# #         if st.button("Edit"):
# #             st.session_state.step = 2
# #             st.rerun()

# #         if st.button("New"):
# #             st.session_state.step = 1
# #             st.rerun()


# # if __name__ == "__main__":
# #     show_builder_ui()



#corrrect
# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from xhtml2pdf import pisa  # PDF conversion layi zaroori hai

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     pdf_output = BytesIO()
#     pisa_status = pisa.CreatePDF(BytesIO(html_string.encode("UTF-8")), dest=pdf_output)
#     if pisa_status.err:
#         return None
#     return pdf_output.getvalue()

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3>PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3>EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#             <h3>SKILLS</h3><p>{data['skills']}</p>
#             <h3>EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; display: flex; background: white; min-height: 800px;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center;">
#             <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
#             <h2>{data['name']}</h2>
#             <p style="font-size: 12px; text-align: left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width: 70%; padding: 40px; color: #1e293b;">
#             <h3 style="border-bottom: 2px solid #22c55e;">PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p style="white-space: pre-wrap;">{data['projects']}</p>
#             <h3 style="border-bottom: 20px solid #fff; border-bottom: 2px solid #22c55e;">EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#         </div>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right; margin-left: 15px;"><img src="{data["photo"]}" style="width: 110px; height: 130px; border: 1px solid #000; object-fit: cover;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 50px; background: white; color: black; border: 1px solid #eee;">
#         {photo_html}
#         <h1 style="margin: 0; text-transform: uppercase; font-size: 26px;">{data['name']}</h1>
#         <p style="font-size: 14px;">{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000; clear: both; margin-top: 15px;">
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Summary</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['summary']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Experience</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['experience']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Key Projects</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['projects']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Education</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['education']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Skills</h3>
#         <p style="font-size: 14px;">{data['skills']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .template-img { width: 100%; height: 300px; object-fit: cover; border-radius: 12px; }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "advanced.jpg")]
#         for i, (name, img) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><img src="{get_local_img_base64(img)}" class="template-img"><h4 style="color:white; margin-top:10px;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="+91 98765-43210")
#             addr = c2.text_input("Location", placeholder="Chandigarh, Punjab")
            
#             u_photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 u_photo = st.file_uploader("Upload Profile Photo", type=['jpg','png','jpeg'])
            
#             summary = st.text_area("Professional Summary")
#             edu = st.text_area("Education")
#             skl = st.text_input("Technical Skills")
#             exp = st.text_area("Experience")
#             prj = st.text_area("Key Projects")
            
#             if st.form_submit_button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": process_image(u_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=750, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64
# import os
# from io import BytesIO
# import pdfkit  # Nava engine

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     try:
#         # Tuhade screenshot de mutabik exact path:
#         path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#         config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        
#         options = {
#             'page-size': 'A4',
#             'margin-top': '0in',
#             'margin-right': '0in',
#             'margin-bottom': '0in',
#             'margin-left': '0in',
#             'encoding': "UTF-8",
#             'no-outline': None,
#             'enable-local-file-access': None,
#             'disable-smart-shrinking': None, # Layout size maintain karan layi
#         }
        
#         pdf_bytes = pdfkit.from_string(html_string, False, options=options, configuration=config)
#         return pdf_bytes
#     except Exception as e:
#         st.error(f"PDF Engine Error: {e}")
#         return None

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3>PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3>EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#             <h3>SKILLS</h3><p>{data['skills']}</p>
#             <h3>EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; display: flex; background: white; min-height: 1000px; width: 100%;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center; float: left;">
#             <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
#             <h2 style="color: white;">{data['name']}</h2>
#             <p style="font-size: 12px; text-align: left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width: 65%; padding: 40px; color: #1e293b; float: right;">
#             <h3 style="border-bottom: 2px solid #22c55e;">PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p style="white-space: pre-wrap;">{data['projects']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#         </div>
#         <div style="clear: both;"></div>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right; margin-left: 15px;"><img src="{data["photo"]}" style="width: 110px; height: 130px; border: 1px solid #000; object-fit: cover;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 50px; background: white; color: black; border: 1px solid #eee;">
#         {photo_html}
#         <h1 style="margin: 0; text-transform: uppercase; font-size: 26px;">{data['name']}</h1>
#         <p style="font-size: 14px;">{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000; clear: both; margin-top: 15px;">
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Summary</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['summary']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Experience</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['experience']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Key Projects</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['projects']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Education</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['education']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Skills</h3>
#         <p style="font-size: 14px;">{data['skills']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.set_page_config(page_title="AI Resume Builder Pro", layout="wide")
    
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "advanced.jpg")]
#         for i, (name, img) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><h4 style="color:white;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="+91 98765-43210")
#             addr = c2.text_input("Location", placeholder="Chandigarh, Punjab")
            
#             u_photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 u_photo = st.file_uploader("Upload Profile Photo", type=['jpg','png','jpeg'])
            
#             summary = st.text_area("Professional Summary")
#             edu = st.text_area("Education")
#             skl = st.text_input("Technical Skills")
#             exp = st.text_area("Experience")
#             prj = st.text_area("Key Projects")
            
#             if st.form_submit_button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": process_image(u_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         # Display Live Preview
#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=800, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         # PDF Generation
#         pdf_bytes = convert_html_to_pdf(html)
        
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()

# import streamlit as st
# import base64
# import os
# from io import BytesIO
# import pdfkit

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     try:
#         path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#         config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        
#         options = {
#             'page-size': 'A4',
#             'margin-top': '0in',
#             'margin-right': '0in',
#             'margin-bottom': '0in',
#             'margin-left': '0in',
#             'encoding': "UTF-8",
#             'no-outline': None,
#             'enable-local-file-access': None,
#             'disable-smart-shrinking': None,
#         }
        
#         pdf_bytes = pdfkit.from_string(html_string, False, options=options, configuration=config)
#         return pdf_bytes
#     except Exception as e:
#         st.error(f"PDF Engine Error: {e}")
#         return None

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 20px;">
#             <h3>PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3>EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#             <h3>SKILLS</h3><p>{data['skills']}</p>
#             <h3>EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     return f"""
#     <div style="font-family: Arial, sans-serif; display: flex; background: white; min-height: 1000px; width: 100%;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center; float: left;">
#             <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
#             <h2 style="color: white;">{data['name']}</h2>
#             <p style="font-size: 12px; text-align: left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width: 65%; padding: 40px; color: #1e293b; float: right;">
#             <h3 style="border-bottom: 2px solid #22c55e;">PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data['summary']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data['experience']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p style="white-space: pre-wrap;">{data['projects']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EDUCATION</h3><p style="white-space: pre-wrap;">{data['education']}</p>
#         </div>
#         <div style="clear: both;"></div>
#     </div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right; margin-left: 15px;"><img src="{data["photo"]}" style="width: 110px; height: 130px; border: 1px solid #000; object-fit: cover;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""
#     <div style="font-family: 'Times New Roman', serif; padding: 50px; background: white; color: black; border: 1px solid #eee;">
#         {photo_html}
#         <h1 style="margin: 0; text-transform: uppercase; font-size: 26px;">{data['name']}</h1>
#         <p style="font-size: 14px;">{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000; clear: both; margin-top: 15px;">
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Summary</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['summary']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Professional Experience</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['experience']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Key Projects</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['projects']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Education</h3>
#         <p style="white-space: pre-wrap; font-size: 14px;">{data['education']}</p>
#         <h3 style="border-bottom: 1px solid #000; text-transform: uppercase;">Skills</h3>
#         <p style="font-size: 14px;">{data['skills']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.set_page_config(page_title="AI Resume Builder Pro", layout="wide")
    
#     # CSS (No changes to existing, except adding button styles for the new button)
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
        
#         /* Specific Button styling to match the image across all steps */
#         .stButton>button {
#             background-color: #1a1e3a !important; /* Dark blue background from image */
#             color: #d89667 !important; /* Light orange text from image */
#             border: 1px solid rgba(216, 150, 103, 0.3) !important;
#             border-radius: 8px !important;
#             font-weight: 600 !important;
#             text-transform: uppercase !important;
#             letter-spacing: 0.5px !important;
#             transition: all 0.3s !important;
#         }

#         .stButton>button:hover {
#             border-color: #d89667 !important;
#             background-color: rgba(216, 150, 103, 0.1) !important;
#             color: #ff9f57 !important; /* brighter orange on hover */
#             transform: translateY(-2px) !important;
#             box-shadow: 0 4px 12px rgba(216, 150, 103, 0.15) !important;
#         }
        
#         .stButton>button:active {
#             background-color: #0f1225 !important;
#             transform: translateY(1px) !important;
#         }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "adv.jpg")]
        
#         for i, (name, img_file) in enumerate(layouts):
#             with cols[i]:
#                 # Conversion to base64 for display
#                 img_base64 = get_local_img_base64(img_file)
                
#                 st.markdown(f'''
#                     <div class="template-card">
#                         <img src="{img_base64}" style="width: 100%; border-radius: 10px; margin-bottom: 15px; border: 1px solid #334155;">
#                         <h4 style="color:white;">{name} Layout</h4>
#                     </div>
#                 ''', unsafe_allow_html=True)
                
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         # Using a regular streamlit div/container instead of a form because we need two buttons with different actions
#         st.markdown('<div style="margin-bottom: 40px;">', unsafe_allow_html=True)
        
#         c1, c2 = st.columns(2)
#         name = c1.text_input("Full Name", value=st.session_state.resume_data.get("name", ""), placeholder="Aman Deep Singh")
#         email = c2.text_input("Email ID", value=st.session_state.resume_data.get("email", ""), placeholder="aman@example.com")
#         phone = c1.text_input("Phone Number", value=st.session_state.resume_data.get("phone", ""), placeholder="+91 98765-43210")
#         addr = c2.text_input("Location", value=st.session_state.resume_data.get("address", ""), placeholder="Chandigarh, Punjab")
        
#         u_photo = None
#         if st.session_state.selected_template in ["Modern", "Advanced"]:
#             u_photo = st.file_uploader("Upload Profile Photo", type=['jpg','png','jpeg'])
        
#         summary = st.text_area("Professional Summary", value=st.session_state.resume_data.get("summary", ""))
#         edu = st.text_area("Education", value=st.session_state.resume_data.get("education", ""))
#         skl = st.text_input("Technical Skills", value=st.session_state.resume_data.get("skills", ""))
#         exp = st.text_area("Experience", value=st.session_state.resume_data.get("experience", ""))
#         prj = st.text_area("Key Projects", value=st.session_state.resume_data.get("projects", ""))
        
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         # Action buttons row
#         b_col_back, b_col_compile = st.columns([1,1])
#         with b_col_back:
#             if st.button("⬅️ BACK TO DESIGN", use_container_width=True):
#                 # Save what's entered and go back
#                 photo_data = process_image(u_photo) if u_photo is not None else st.session_state.resume_data.get("photo", "")
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": photo_data
#                 }
#                 st.session_state.builder_step = 1
#                 st.rerun()
                
#         with b_col_compile:
#             if st.button("COMPILE RESUME ✨", use_container_width=True):
#                 # Save and proceed to preview
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": process_image(u_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e; margin-bottom: 20px;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=800, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
        
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT DETAILS", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64
# import os
# from io import BytesIO
# import pdfkit

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     try:
#         path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#         config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
#         options = {
#             'page-size': 'A4',
#             'margin-top': '0in', 'margin-right': '0in', 'margin-bottom': '0in', 'margin-left': '0in',
#             'encoding': "UTF-8", 'enable-local-file-access': None, 'disable-smart-shrinking': None,
#         }
#         pdf_bytes = pdfkit.from_string(html_string, False, options=options, configuration=config)
#         return pdf_bytes
#     except Exception as e:
#         st.error(f"PDF Engine Error: {e}")
#         return None

# # --- 2. TEMPLATES (No Changes) ---
# def get_simple_template(data):
#     return f"""<div style="font-family: Arial; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; color: #1e1b4b;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">{data['email']} | {data['phone']} | {data['address']}</p>
#         <div style="margin-top: 20px;">
#             <h3>SUMMARY</h3><p>{data['summary']}</p>
#             <h3>EDUCATION</h3><p>{data['education']}</p>
#             <h3>SKILLS</h3><p>{data['skills']}</p>
#             <h3>EXPERIENCE</h3><p>{data['experience']}</p>
#         </div></div>"""

# def get_modern_template(data):
#     return f"""<div style="font-family: Arial; display: flex; background: white; min-height: 1000px; width: 100%;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center; float: left;">
#             <img src="{data['photo']}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
#             <h2>{data['name']}</h2><p style="font-size: 12px; text-align: left;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#         </div>
#         <div style="width: 65%; padding: 40px; color: #1e293b; float: right;">
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p>{data['experience']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p>{data['projects']}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EDUCATION</h3><p>{data['education']}</p>
#         </div><div style="clear: both;"></div></div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right;"><img src="{data["photo"]}" style="width: 110px; height: 130px; border: 1px solid #000;"></div>' if "placeholder" not in data['photo'] else ""
#     return f"""<div style="font-family: 'Times New Roman'; padding: 50px; background: white; color: black; border: 1px solid #eee;">
#         {photo_html}<h1>{data['name']}</h1><p>{data['address']} | {data['phone']} | {data['email']}</p>
#         <hr style="border-top: 2px solid #000;">
#         <h3>SUMMARY</h3><p>{data['summary']}</p>
#         <h3>EXPERIENCE</h3><p>{data['experience']}</p>
#         <h3>EDUCATION</h3><p>{data['education']}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.set_page_config(page_title="AI Resume Builder Pro", layout="wide")
    
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
        
#         /* The Pro Button Style */
#         .stButton>button {
#             background-color: #1a1e3a !important; color: #d89667 !important;
#             border: 1px solid rgba(216, 150, 103, 0.3) !important;
#             border-radius: 8px !important; font-weight: 600 !important;
#             text-transform: uppercase !important; transition: all 0.3s !important;
#         }
#         .stButton>button:hover {
#             border-color: #d89667 !important; background-color: rgba(216, 150, 103, 0.1) !important;
#             color: #ff9f57 !important; transform: translateY(-2px) !important;
#             box-shadow: 0 4px 12px rgba(216, 150, 103, 0.15) !important;
#         }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "adv.jpg")]
#         for i, (name, img_file) in enumerate(layouts):
#             with cols[i]:
#                 img_base64 = get_local_img_base64(img_file)
#                 st.markdown(f'<div class="template-card"><img src="{img_base64}" style="width: 100%; border-radius: 10px; margin-bottom: 15px;"><h4 style="color:white;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         c1, c2 = st.columns(2)
#         name = c1.text_input("Full Name", value=st.session_state.resume_data.get("name", ""))
#         email = c2.text_input("Email ID", value=st.session_state.resume_data.get("email", ""))
#         phone = c1.text_input("Phone Number", value=st.session_state.resume_data.get("phone", ""))
#         addr = c2.text_input("Location", value=st.session_state.resume_data.get("address", ""))
#         u_photo = st.file_uploader("Upload Photo", type=['jpg','png']) if st.session_state.selected_template != "Simple" else None
#         summary = st.text_area("Summary", value=st.session_state.resume_data.get("summary", ""))
#         edu = st.text_area("Education", value=st.session_state.resume_data.get("education", ""))
#         skl = st.text_input("Skills", value=st.session_state.resume_data.get("skills", ""))
#         exp = st.text_area("Experience", value=st.session_state.resume_data.get("experience", ""))
#         prj = st.text_area("Projects", value=st.session_state.resume_data.get("projects", ""))

#         b1, b2 = st.columns(2)
#         with b1:
#             if st.button("⬅️ BACK TO DESIGN", use_container_width=True):
#                 st.session_state.builder_step = 1; st.rerun()
#         with b2:
#             if st.button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {"name": name, "email": email, "phone": phone, "address": addr, "summary": summary, "education": edu, "skills": skl, "experience": exp, "projects": prj, "photo": process_image(u_photo)}
#                 st.session_state.builder_step = 3; st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         html = get_simple_template(d) if st.session_state.selected_template=="Simple" else get_modern_template(d) if st.session_state.selected_template=="Modern" else get_advanced_template(d)
        
#         # This is the Vdia Preview Box
#         st.markdown('<div style="background: white; border-radius: 20px; padding: 15px; border: 5px solid #22c55e; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=800, scrolling=True)
#         st.markdown('</div><br>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         c1, c2, c3 = st.columns(3)
#         with c1: st.download_button("📥 DOWNLOAD PDF", data=pdf_bytes, file_name="Resume.pdf", mime="application/pdf", use_container_width=True) if pdf_bytes else None
#         with c2: 
#             if st.button("✏️ RE-EDIT DETAILS", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with c3: 
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()


# import streamlit as st
# import base64
# import os
# from io import BytesIO
# from xhtml2pdf import pisa  

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return ""

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return ""

# def convert_html_to_pdf(html_string):
#     pdf_style = """
#     <style>
#         @page {
#             size: A4;
#             margin: 1cm;
#         }
#         body { font-family: 'Times New Roman', serif; margin: 0; padding: 0; }
#         img { display: block; }
#     </style>
#     """
#     full_html = pdf_style + html_string
#     pdf_output = BytesIO()
#     pisa_status = pisa.CreatePDF(BytesIO(full_html.encode("UTF-8")), dest=pdf_output)
#     if pisa_status.err:
#         return None
#     return pdf_output.getvalue()

# # --- 2. TEMPLATES ---
# def get_simple_template(data):
#     return f"""
#     <div style="padding: 20px; background: white; color: #333;">
#         <h1 style="text-align: center; text-transform: uppercase; color: #1e1b4b; margin-bottom: 5px;">{data['name']}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px; font-size: 12px;">
#             {data['email']} | {data['phone']} | {data['address']}
#         </p>
#         <div style="margin-top: 15px;">
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">PROFESSIONAL SUMMARY</h3>
#             <p style="white-space: pre-wrap; font-size: 12px;">{data['summary']}</p>
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">EDUCATION</h3>
#             <p style="white-space: pre-wrap; font-size: 12px;">{data['education']}</p>
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">SKILLS</h3>
#             <p style="font-size: 12px;">{data['skills']}</p>
#             <h3 style="color: #1e1b4b; border-bottom: 1px solid #ccc;">EXPERIENCE</h3>
#             <p style="white-space: pre-wrap; font-size: 12px;">{data['experience']}</p>
#         </div>
#     </div>"""

# def get_modern_template(data):
#     photo_part = f'<img src="{data["photo"]}" width="100" height="100" style="border-radius: 50px; border: 3px solid #22c55e; margin-bottom: 15px;">' if data["photo"] else ""
#     return f"""
#     <table style="width: 100%; height: 100%; border-collapse: collapse;">
#         <tr>
#             <td style="width: 30%; background-color: #062d24; color: white; padding: 25px; vertical-align: top; text-align: center;">
#                 {photo_part}
#                 <h2 style="margin-bottom: 10px; font-size: 18px;">{data['name']}</h2>
#                 <p style="font-size: 10px; text-align: left; line-height: 1.4;">{data['email']}<br>{data['phone']}<br>{data['address']}</p>
#             </td>
#             <td style="width: 70%; padding: 30px; color: #1e293b; vertical-align: top; background-color: white;">
#                 <h3 style="border-bottom: 2px solid #22c55e; color: #062d24; font-size: 14px; margin-top: 0;">PROFESSIONAL SUMMARY</h3>
#                 <p style="white-space: pre-wrap; font-size: 11px; margin-bottom: 15px;">{data['summary']}</p>
#                 <h3 style="border-bottom: 2px solid #22c55e; color: #062d24; font-size: 14px;">EXPERIENCE</h3>
#                 <p style="white-space: pre-wrap; font-size: 11px; margin-bottom: 15px;">{data['experience']}</p>
#                 <h3 style="border-bottom: 2px solid #22c55e; color: #062d24; font-size: 14px;">PROJECTS</h3>
#                 <p style="white-space: pre-wrap; font-size: 11px; margin-bottom: 15px;">{data['projects']}</p>
#                 <h3 style="border-bottom: 2px solid #22c55e; color: #062d24; font-size: 14px;">EDUCATION</h3>
#                 <p style="white-space: pre-wrap; font-size: 11px;">{data['education']}</p>
#             </td>
#         </tr>
#     </table>"""

# def get_advanced_template(data):
#     # Using a table to fix the header layout for the PDF engine
#     photo_html = f'<td style="text-align: right; vertical-align: top;"><img src="{data["photo"]}" width="90" height="110" style="border: 1px solid #000;"></td>' if data["photo"] else "<td></td>"
#     return f"""
#     <div style="background-color: white; padding: 10px;">
#         <table style="width: 100%; border-collapse: collapse; margin-bottom: 10px;">
#             <tr>
#                 <td style="vertical-align: top;">
#                     <h1 style="margin: 0; text-transform: uppercase; font-size: 22px;">{data['name']}</h1>
#                     <p style="font-size: 12px; margin-top: 5px;">{data['address']} | {data['phone']} | {data['email']}</p>
#                 </td>
#                 {photo_html}
#             </tr>
#         </table>
#         <div style="border-top: 2px solid #000; padding-top: 10px;">
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 14px; margin-bottom: 5px;">Professional Summary</h3>
#             <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 12px;">{data['summary']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 14px; margin-bottom: 5px;">Professional Experience</h3>
#             <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 12px;">{data['experience']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 14px; margin-bottom: 5px;">Key Projects</h3>
#             <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 12px;">{data['projects']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 14px; margin-bottom: 5px;">Education</h3>
#             <p style="white-space: pre-wrap; font-size: 12px; margin-bottom: 12px;">{data['education']}</p>
#             <h3 style="border-bottom: 1px solid #000; text-transform: uppercase; font-size: 14px; margin-bottom: 5px;">Skills</h3>
#             <p style="font-size: 12px;">{data['skills']}</p>
#         </div>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .template-img { width: 100%; height: 300px; object-fit: cover; border-radius: 12px; }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
#     </style>""", unsafe_allow_html=True)

#     st.markdown("<h1 style='text-align: center; color: #22c55e; font-size: 45px; font-weight: 800;'>AI RESUME BUILDER PRO</h1>", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "advanced.jpg")]
#         for i, (name, img) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><img src="{get_local_img_base64(img)}" class="template-img"><h4 style="color:white; margin-top:10px;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
#         with st.form("resume_form"):
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", placeholder="Aman Deep Singh")
#             email = c2.text_input("Email ID", placeholder="aman@example.com")
#             phone = c1.text_input("Phone Number", placeholder="+91 98765-43210")
#             addr = c2.text_input("Location", placeholder="Chandigarh, Punjab")
            
#             u_photo = None
#             if st.session_state.selected_template in ["Modern", "Advanced"]:
#                 u_photo = st.file_uploader("Upload Profile Photo", type=['jpg','png','jpeg'])
            
#             summary = st.text_area("Professional Summary")
#             edu = st.text_area("Education")
#             skl = st.text_input("Technical Skills")
#             exp = st.text_area("Experience")
#             prj = st.text_area("Key Projects")
            
#             if st.form_submit_button("COMPILE RESUME ✨", use_container_width=True):
#                 st.session_state.resume_data = {
#                     "name": name, "email": email, "phone": phone, "address": addr,
#                     "summary": summary, "education": edu, "skills": skl, 
#                     "experience": exp, "projects": prj,
#                     "photo": process_image(u_photo)
#                 }
#                 st.session_state.builder_step = 3
#                 st.rerun()

#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         st.markdown('<div style="background:white; border-radius:15px; padding:10px; border:4px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=750, scrolling=True)
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         col_dl, col_edit, col_back = st.columns(3)
#         with col_dl:
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD AS PDF", data=pdf_bytes, file_name=f"Resume_{d['name']}.pdf", mime="application/pdf", use_container_width=True)
#         with col_edit:
#             if st.button("✏️ RE-EDIT", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with col_back:
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()



# import streamlit as st
# import base64
# import os
# from io import BytesIO
# import pdfkit

# # --- 1. HELPER FUNCTIONS ---
# def get_local_img_base64(image_path):
#     if os.path.exists(image_path):
#         with open(image_path, "rb") as img_file:
#             return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
#     return "https://via.placeholder.com/300x400?text=No+Preview"

# def process_image(uploaded_file):
#     if uploaded_file is not None:
#         return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
#     return "https://via.placeholder.com/150"

# def convert_html_to_pdf(html_string):
#     try:
#         path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#         config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
#         options = {
#             'page-size': 'A4',
#             'margin-top': '0in', 'margin-right': '0in', 'margin-bottom': '0in', 'margin-left': '0in',
#             'encoding': "UTF-8", 'enable-local-file-access': None, 'disable-smart-shrinking': None,
#         }
#         pdf_bytes = pdfkit.from_string(html_string, False, options=options, configuration=config)
#         return pdf_bytes
#     except Exception as e:
#         st.error(f"PDF Engine Error: {e}")
#         return None

# # --- 2. TEMPLATES (Sahi Keys de Naal) ---
# def get_simple_template(data):
#     return f"""<div style="font-family: Arial; padding: 40px; background: white; color: #333;">
#         <h1 style="text-align: center; color: #1e1b4b;">{data.get('name', '')}</h1>
#         <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">{data.get('email', '')} | {data.get('phone', '')} | {data.get('address', '')}</p>
#         <div style="margin-top: 20px;">
#             <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data.get('summary', '')}</p>
#             <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">SKILLS</h3><p>{data.get('skills', '')}</p>
#             <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data.get('experience', '')}</p>
#             <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">PROJECTS</h3><p style="white-space: pre-wrap;">{data.get('projects', '')}</p>
#             <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">EDUCATION</h3><p style="white-space: pre-wrap;">{data.get('education', '')}</p>
#         </div></div>"""

# def get_modern_template(data):
#     return f"""<div style="font-family: Arial; display: flex; background: white; min-height: 1000px; width: 100%;">
#         <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center; float: left;">
#             <img src="{data.get('photo', '')}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
#             <h2>{data.get('name', '')}</h2><p style="font-size: 12px; text-align: left;">{data.get('email', '')}<br>{data.get('phone', '')}<br>{data.get('address', '')}</p>
#             <div style="text-align: left; margin-top:20px;"><h4>SKILLS</h4><p style="font-size:12px;">{data.get('skills', '')}</p></div>
#         </div>
#         <div style="width: 65%; padding: 40px; color: #1e293b; float: right;">
#             <h3 style="border-bottom: 2px solid #22c55e;">SUMMARY</h3><p style="white-space: pre-wrap;">{data.get('summary', '')}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data.get('experience', '')}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p style="white-space: pre-wrap;">{data.get('projects', '')}</p>
#             <h3 style="border-bottom: 2px solid #22c55e;">EDUCATION</h3><p style="white-space: pre-wrap;">{data.get('education', '')}</p>
#         </div><div style="clear: both;"></div></div>"""

# def get_advanced_template(data):
#     photo_html = f'<div style="float: right;"><img src="{data.get("photo", "")}" style="width: 110px; height: 130px; border: 1px solid #000; object-fit: cover;"></div>' if "placeholder" not in data.get('photo', '') else ""
#     return f"""<div style="font-family: 'Times New Roman'; padding: 50px; background: white; color: black; border: 1px solid #eee;">
#         {photo_html}<h1 style="margin:0;">{data.get('name', '')}</h1><p>{data.get('address', '')} | {data.get('phone', '')} | {data.get('email', '')}</p>
#         <hr style="border-top: 2px solid #000;">
#         <h3>SUMMARY</h3><p style="white-space: pre-wrap;">{data.get('summary', '')}</p>
#         <h3>SKILLS</h3><p>{data.get('skills', '')}</p>
#         <h3>EXPERIENCE</h3><p style="white-space: pre-wrap;">{data.get('experience', '')}</p>
#         <h3>PROJECTS</h3><p style="white-space: pre-wrap;">{data.get('projects', '')}</p>
#         <h3>EDUCATION</h3><p style="white-space: pre-wrap;">{data.get('education', '')}</p>
#     </div>"""

# # --- 3. MAIN UI ---
# def show_builder_ui():
#     st.set_page_config(page_title="AI Resume Builder Pro", layout="wide")
    
#     # CSS remains the same
#     st.markdown("""<style>
#         .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
#         label { color: #f8fafc !important; font-weight: 600; }
#         .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
#         .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
#         .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
#         .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
#         .stButton>button {
#             background-color: #1a1e3a !important; color: #d89667 !important;
#             border: 1px solid rgba(216, 150, 103, 0.3) !important;
#             border-radius: 8px !important; font-weight: 600 !important;
#             text-transform: uppercase !important; transition: all 0.3s !important;
#         }
#         .stButton>button:hover {
#             border-color: #d89667 !important; background-color: rgba(216, 150, 103, 0.1) !important;
#             color: #ff9f57 !important; transform: translateY(-2px) !important;
#         }
#     </style>""", unsafe_allow_html=True)

#     if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
#     if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

#     # STEP 1: LAYOUT SELECTION
#     if st.session_state.builder_step == 1:
#         st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
#         cols = st.columns(3)
#         layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "adv.jpg")]
#         for i, (name, img_file) in enumerate(layouts):
#             with cols[i]:
#                 st.markdown(f'<div class="template-card"><h4 style="color:white;">{name} Layout</h4></div>', unsafe_allow_html=True)
#                 if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
#                     st.session_state.selected_template = name
#                     st.session_state.builder_step = 2
#                     st.rerun()

#     # STEP 2: DATA ENTRY (Sahi mapping)
#     elif st.session_state.builder_step == 2:
#         st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
        
#         with st.container():
#             c1, c2 = st.columns(2)
#             name = c1.text_input("Full Name", value=st.session_state.resume_data.get("name", ""))
#             email = c2.text_input("Email ID", value=st.session_state.resume_data.get("email", ""))
#             phone = c1.text_input("Phone Number", value=st.session_state.resume_data.get("phone", ""))
#             addr = c2.text_input("Location", value=st.session_state.resume_data.get("address", ""))
            
#             u_photo = None
#             if st.session_state.selected_template != "Simple":
#                 u_photo = st.file_uploader("Upload Photo", type=['jpg','png','jpeg'])

#             summary = st.text_area("Professional Summary", value=st.session_state.resume_data.get("summary", ""))
#             skl = st.text_input("Technical Skills", value=st.session_state.resume_data.get("skills", ""))
#             exp = st.text_area("Experience", value=st.session_state.resume_data.get("experience", ""))
#             prj = st.text_area("Key Projects", value=st.session_state.resume_data.get("projects", ""))
#             edu = st.text_area("Education", value=st.session_state.resume_data.get("education", ""))

#             b1, b2 = st.columns(2)
#             with b1:
#                 if st.button("⬅️ BACK TO DESIGN", use_container_width=True):
#                     st.session_state.builder_step = 1; st.rerun()
#             with b2:
#                 if st.button("COMPILE RESUME ✨", use_container_width=True):
#                     # Save everything properly
#                     st.session_state.resume_data = {
#                         "name": name, "email": email, "phone": phone, "address": addr,
#                         "summary": summary, "skills": skl, "experience": exp, 
#                         "projects": prj, "education": edu,
#                         "photo": process_image(u_photo) if u_photo else st.session_state.resume_data.get("photo", "https://via.placeholder.com/150")
#                     }
#                     st.session_state.builder_step = 3; st.rerun()

#     # STEP 3: PREVIEW & EXPORT
#     elif st.session_state.builder_step == 3:
#         st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
#         d = st.session_state.resume_data
#         t = st.session_state.selected_template
        
#         # Template logic
#         html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
#         # Glassy Container for Preview
#         st.markdown('<div style="background: white; border-radius: 20px; padding: 15px; border: 5px solid #22c55e;">', unsafe_allow_html=True)
#         st.components.v1.html(html, height=850, scrolling=True)
#         st.markdown('</div><br>', unsafe_allow_html=True)
        
#         pdf_bytes = convert_html_to_pdf(html)
#         c1, c2, c3 = st.columns(3)
#         with c1: 
#             if pdf_bytes:
#                 st.download_button("📥 DOWNLOAD PDF", data=pdf_bytes, file_name=f"Resume_{d.get('name','User')}.pdf", mime="application/pdf", use_container_width=True)
#         with c2: 
#             if st.button("✏️ RE-EDIT DETAILS", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
#         with c3: 
#             if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

# if __name__ == "__main__":
#     show_builder_ui()

import streamlit as st
import base64
import os
from io import BytesIO
import pdfkit

# --- 1. HELPER FUNCTIONS ---
def get_local_img_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    return "https://via.placeholder.com/300x400?text=No+Preview"

def process_image(uploaded_file):
    if uploaded_file is not None:
        return f"data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}"
    return "https://via.placeholder.com/150"

def convert_html_to_pdf(html_string):
    try:
        path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        options = {
            'page-size': 'A4',
            'margin-top': '0in', 'margin-right': '0in', 'margin-bottom': '0in', 'margin-left': '0in',
            'encoding': "UTF-8", 'enable-local-file-access': None, 'disable-smart-shrinking': None,
        }
        pdf_bytes = pdfkit.from_string(html_string, False, options=options, configuration=config)
        return pdf_bytes
    except Exception as e:
        st.error(f"PDF Engine Error: {e}")
        return None

# --- 2. TEMPLATES ---
def get_simple_template(data):
    return f"""<div style="font-family: Arial; padding: 40px; background: white; color: #333;">
        <h1 style="text-align: center; color: #1e1b4b;">{data.get('name', '')}</h1>
        <p style="text-align: center; border-bottom: 2px solid #22c55e; padding-bottom: 10px;">{data.get('email', '')} | {data.get('phone', '')} | {data.get('address', '')}</p>
        <div style="margin-top: 20px;">
            <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">PROFESSIONAL SUMMARY</h3><p style="white-space: pre-wrap;">{data.get('summary', '')}</p>
            <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">SKILLS</h3><p>{data.get('skills', '')}</p>
            <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data.get('experience', '')}</p>
            <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">PROJECTS</h3><p style="white-space: pre-wrap;">{data.get('projects', '')}</p>
            <h3 style="color:#1e1b4b; border-bottom: 1px solid #eee;">EDUCATION</h3><p style="white-space: pre-wrap;">{data.get('education', '')}</p>
        </div></div>"""

def get_modern_template(data):
    return f"""<div style="font-family: Arial; display: flex; background: white; min-height: 1000px; width: 100%;">
        <div style="width: 30%; background: #062d24; color: white; padding: 30px; text-align: center; float: left;">
            <img src="{data.get('photo', '')}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid #22c55e; margin-bottom: 20px; object-fit: cover;">
            <h2>{data.get('name', '')}</h2><p style="font-size: 12px; text-align: left;">{data.get('email', '')}<br>{data.get('phone', '')}<br>{data.get('address', '')}</p>
            <div style="text-align: left; margin-top:20px;"><h4>SKILLS</h4><p style="font-size:12px;">{data.get('skills', '')}</p></div>
        </div>
        <div style="width: 65%; padding: 40px; color: #1e293b; float: right;">
            <h3 style="border-bottom: 2px solid #22c55e;">SUMMARY</h3><p style="white-space: pre-wrap;">{data.get('summary', '')}</p>
            <h3 style="border-bottom: 2px solid #22c55e;">EXPERIENCE</h3><p style="white-space: pre-wrap;">{data.get('experience', '')}</p>
            <h3 style="border-bottom: 2px solid #22c55e;">PROJECTS</h3><p style="white-space: pre-wrap;">{data.get('projects', '')}</p>
            <h3 style="border-bottom: 2px solid #22c55e;">EDUCATION</h3><p style="white-space: pre-wrap;">{data.get('education', '')}</p>
        </div><div style="clear: both;"></div></div>"""

def get_advanced_template(data):
    photo_html = f'<div style="float: right;"><img src="{data.get("photo", "")}" style="width: 110px; height: 130px; border: 1px solid #000; object-fit: cover;"></div>' if "placeholder" not in data.get('photo', '') else ""
    return f"""<div style="font-family: 'Times New Roman'; padding: 50px; background: white; color: black; border: 1px solid #eee;">
        {photo_html}<h1 style="margin:0;">{data.get('name', '')}</h1><p>{data.get('address', '')} | {data.get('phone', '')} | {data.get('email', '')}</p>
        <hr style="border-top: 2px solid #000;">
        <h3>SUMMARY</h3><p style="white-space: pre-wrap;">{data.get('summary', '')}</p>
        <h3>SKILLS</h3><p>{data.get('skills', '')}</p>
        <h3>EXPERIENCE</h3><p style="white-space: pre-wrap;">{data.get('experience', '')}</p>
        <h3>PROJECTS</h3><p style="white-space: pre-wrap;">{data.get('projects', '')}</p>
        <h3>EDUCATION</h3><p style="white-space: pre-wrap;">{data.get('education', '')}</p>
    </div>"""

# --- 3. MAIN UI ---
def show_builder_ui():
    st.set_page_config(page_title="AI Resume Builder Pro", layout="wide")
    
    st.markdown("""<style>
        .stApp { background: radial-gradient(circle at top left, #020617, #0f172a, #020617) !important; }
        label { color: #f8fafc !important; font-weight: 600; }
        .step-title { color: #22c55e; font-weight: 800; font-size: 32px; margin: 30px 0; text-align: center; }
        .template-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); text-align: center; transition: 0.3s; }
        .template-card:hover { border-color: #22c55e; transform: translateY(-5px); }
        .stTextInput input, .stTextArea textarea { background: white !important; color: black !important; border-radius: 8px !important; }
        .stButton>button {
            background-color: #1a1e3a !important; color: #d89667 !important;
            border: 1px solid rgba(216, 150, 103, 0.3) !important;
            border-radius: 8px !important; font-weight: 600 !important;
            text-transform: uppercase !important; transition: all 0.3s !important;
        }
        .stButton>button:hover {
            border-color: #d89667 !important; background-color: rgba(216, 150, 103, 0.1) !important;
            color: #ff9f57 !important; transform: translateY(-2px) !important;
        }
    </style>""", unsafe_allow_html=True)

    if 'builder_step' not in st.session_state: st.session_state.builder_step = 1
    if 'resume_data' not in st.session_state: st.session_state.resume_data = {}

    # STEP 1: LAYOUT SELECTION (Image Preview Added)
    if st.session_state.builder_step == 1:
        st.markdown('<div class="step-title">Step 1: Select Layout Architecture</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        # Make sure simple.jpg, modern.jpg, adv.jpg are in the same folder
        layouts = [("Simple", "simple.jpg"), ("Modern", "modern.jpg"), ("Advanced", "adv.jpg")]
        
        for i, (name, img_file) in enumerate(layouts):
            with cols[i]:
                # Local image loading
                img_base64 = get_local_img_base64(img_file)
                st.markdown(f"""
                    <div class="template-card">
                        <img src="{img_base64}" style="width: 100%; border-radius: 10px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.1);">
                        <h4 style="color:white;">{name} Layout</h4>
                    </div>""", unsafe_allow_html=True)
                
                if st.button(f"USE {name.upper()}", key=name, use_container_width=True):
                    st.session_state.selected_template = name
                    st.session_state.builder_step = 2
                    st.rerun()

    # STEP 2 & 3 remain exactly the same as your previous working version
    elif st.session_state.builder_step == 2:
        st.markdown(f'<div class="step-title">Step 2: Enter Details ({st.session_state.selected_template})</div>', unsafe_allow_html=True)
        with st.container():
            c1, c2 = st.columns(2)
            name = c1.text_input("Full Name", value=st.session_state.resume_data.get("name", ""))
            email = c2.text_input("Email ID", value=st.session_state.resume_data.get("email", ""))
            phone = c1.text_input("Phone Number", value=st.session_state.resume_data.get("phone", ""))
            addr = c2.text_input("Location", value=st.session_state.resume_data.get("address", ""))
            u_photo = st.file_uploader("Upload Photo", type=['jpg','png','jpeg']) if st.session_state.selected_template != "Simple" else None

            summary = st.text_area("Professional Summary", value=st.session_state.resume_data.get("summary", ""))
            skl = st.text_input("Technical Skills", value=st.session_state.resume_data.get("skills", ""))
            exp = st.text_area("Experience", value=st.session_state.resume_data.get("experience", ""))
            prj = st.text_area("Key Projects", value=st.session_state.resume_data.get("projects", ""))
            edu = st.text_area("Education", value=st.session_state.resume_data.get("education", ""))

            b1, b2 = st.columns(2)
            with b1:
                if st.button("⬅️ BACK TO DESIGN", use_container_width=True):
                    st.session_state.builder_step = 1; st.rerun()
            with b2:
                if st.button("COMPILE RESUME ✨", use_container_width=True):
                    st.session_state.resume_data = {
                        "name": name, "email": email, "phone": phone, "address": addr,
                        "summary": summary, "skills": skl, "experience": exp, 
                        "projects": prj, "education": edu,
                        "photo": process_image(u_photo) if u_photo else st.session_state.resume_data.get("photo", "https://via.placeholder.com/150")
                    }
                    st.session_state.builder_step = 3; st.rerun()

    elif st.session_state.builder_step == 3:
        st.markdown('<div class="step-title">Step 3: Preview & Save</div>', unsafe_allow_html=True)
        d = st.session_state.resume_data
        t = st.session_state.selected_template
        html = get_simple_template(d) if t=="Simple" else get_modern_template(d) if t=="Modern" else get_advanced_template(d)
        
        st.markdown('<div style="background: white; border-radius: 20px; padding: 15px; border: 5px solid #22c55e;">', unsafe_allow_html=True)
        st.components.v1.html(html, height=850, scrolling=True)
        st.markdown('</div><br>', unsafe_allow_html=True)
        
        pdf_bytes = convert_html_to_pdf(html)
        c1, c2, c3 = st.columns(3)
        with c1: 
            if pdf_bytes:
                st.download_button("📥 DOWNLOAD PDF", data=pdf_bytes, file_name=f"Resume_{d.get('name','User')}.pdf", mime="application/pdf", use_container_width=True)
        with c2: 
            if st.button("✏️ RE-EDIT DETAILS", use_container_width=True): st.session_state.builder_step = 2; st.rerun()
        with c3: 
            if st.button("🎨 NEW DESIGN", use_container_width=True): st.session_state.builder_step = 1; st.rerun()

if __name__ == "__main__":
    show_builder_ui()