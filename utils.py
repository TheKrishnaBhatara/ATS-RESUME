# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # 🔐 Load API key
# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_ai_feedback(resume_text, jd_text):
#     try:
#         prompt = f"""
# You are an AI ATS Resume Analyzer.

# Compare the Resume and Job Description.

# Resume:
# {resume_text}

# Job Description:
# {jd_text}

# Give response in this format:

# 1. Overall Feedback
# 2. Missing Skills (bullet points)
# 3. Suggestions to Improve Resume
# 4. ATS Optimization Tips

# Keep it short, professional, and clear.
# """

#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7
#         )

#         return response.choices[0].message.content

#     except Exception as e:
#         return f"AI Feedback Error: {str(e)}"



# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # load env
# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
#     raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file")

# client = OpenAI(api_key=api_key)

# def generate_ai_feedback(resume_text, jd_text):
#     try:
#         prompt = f"""
# You are an AI ATS Resume Analyzer.

# Resume:
# {resume_text}

# Job Description:
# {jd_text}

# Give:
# 1. Overall Feedback
# 2. Missing Skills
# 3. Suggestions
# 4. ATS Tips
# """

#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[
#                 {"role": "user", "content": prompt}
#             ]
#         )

#         return response.choices[0].message.content

#     except Exception as e:
#         return f"AI Error: {str(e)}"
# print("API KEY:", os.getenv("OPENAI_API_KEY"))






import requests
import os

RAPID_API_KEY = "d40fb19ea9msh6376f1b7e8e460bp17d34ajsn12c8806179fa"

def generate_ai_feedback(resume_text, jd_text):

    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"""
You are an ATS Resume Analyzer.

Analyze Resume vs Job Description.

Resume:
{resume_text}

Job Description:
{jd_text}

Give:
1. Overall Feedback
2. Missing Skills
3. Suggestions
4. ATS Tips
"""
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        # 🔍 DEBUG (optional)
        print("RapidAPI Response:", data)

        # ✅ SAFE RETURN
        if "result" in data:
            return data["result"]
        elif "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            return "⚠️ AI response not available"

    except Exception as e:
        return f"RapidAPI Error: {str(e)}"

