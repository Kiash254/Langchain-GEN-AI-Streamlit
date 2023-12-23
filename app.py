"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  " to_harm_category(d[\"category\"], harm_category_set): to_block_threshold(d[\"threshold\"])\n           ~^^^^^^^^^^^^\nTypeError: string indices must be integers, not 'str'\n\nPlease debug this code here is the code \nafter that Please Give Full python code\nimport streamlit as st\nfrom decouple import config\nimport google.generativeai as genai\n\nAPI_KEY = config('API_KEY')\n\nwith st.sidebar:\n    \"[View the source code](https://github.com/Kiash254/Langchain-GEN-AI-Streamlit/blob/main/stream.py)\"\n\nst.title(\"Agricultural Recommender System\")\nst.caption(\"🚀 Farmers Choice to get the fastest Solution\")\nif \"messages\" not in st.session_state:\n    st.session_state[\"messages\"] = [{\"role\": \"assistant\", \"content\": \"Hello Mkulima 👋 Naeza Kusaidia Ajy(How can i help you) ? \"}]\nfor msg in st.session_state.messages:\n    st.chat_message(msg[\"role\"]).write(msg[\"content\"])\n\nif prompt := st.chat_input():\n    model = genai.GenerativeModel('gemini-pro', API_KEY)\n    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n    st.chat_message(\"user\").write(prompt)\n    response = model.generate(prompt, max_tokens=150)  # Replace this line with the correct method to generate chat completions\n    msg = response.choices[0].message.content  # This line might also need to be updated based on the response structure\n    st.session_state.messages.append({\"role\": \"assistant\", \"content\": msg})\n    st.chat_message(\"assistant\").write(msg)\n\nThe error is in the line `to_harm_category(d[\"category\"], harm_category_set): to_block_threshold(d[\"threshold\"])`. The issue is that the `to_harm_category` and `to_block_threshold` functions appear to be called incorrectly. They should be called as separate function calls, not as a single line.\n\nThe corrected line should look like this:\n\n```python\nto_harm_category(d[\"category\"], harm_category_set)\nto_block_threshold(d[\"threshold\"])\n```\n\nThe corrected code with the issue fixed:\n\n```python\nimport streamlit as st\nfrom decouple import config\nimport google.generativeai as genai\n\nAPI_KEY = config('API_KEY')\n\nwith st.sidebar:\n    \"[View the source code](https://github.com/Kiash254/Langchain-GEN-AI-Streamlit/blob/main/stream.py)\"\n\nst.title(\"Agricultural Recommender System\")\nst.caption(\"🚀 Farmers Choice to get the fastest Solution\")\nif \"messages\" not in st.session_state:\n    st.session_state[\"messages\"] = [{\"role\": \"assistant\", \"content\": \"Hello Mkulima 👋 Naeza Kusaidia Ajy(How can i help you) ? \"}]\nfor msg in st.session_state.messages:\n    st.chat_message(msg[\"role\"]).write(msg[\"content\"])\n\nif prompt := st.chat_input():\n    model = genai.GenerativeModel('gemini-pro', API_KEY)\n    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n    st.chat_message(\"user\").write(prompt)\n    response = model.generate(prompt, max_tokens=150)  # Replace this line with the correct method to generate chat completions\n    msg = response.choices[0].message.content  # This line might also need to be updated based on the response structure\n    st.session_state.messages.append({\"role\": \"assistant\", \"content\": msg})\n    st.chat_message(\"assistant\").write(msg)\n```\nTypeError: string indices must be integers, not 'str'\nTraceback:\nFile \"/home/kali/dev/portfolio/env/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py\", line 534, in _run_script\n    exec(code, module.__dict__)\nFile \"/home/kali/dev/Langchain-model/streamlit/stream.py\", line 18, in <module>\n    model = genai.GenerativeModel('gemini-pro', API_KEY)\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nFile \"/home/kali/dev/portfolio/env/lib/python3.11/site-packages/google/generativeai/generative_models.py\", line 165, in __init__\n    self._safety_settings = safety_types.to_easy_safety_dict(\n                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nFile \"/home/kali/dev/portfolio/env/lib/python3.11/site-packages/google/generativeai/types/safety_types.py\", line 229, in to_easy_safety_dict\n    return {\n           ^\nFile \"/home/kali/dev/portfolio/env/lib/python3.11/site-packages/google/generativeai/types/safety_types.py\", line 230, in <dictcomp>\n    to_harm_category(d[\"category\"], harm_category_set): to_block_threshold(d[\"threshold\"])\n                     ~^^^^^^^^^^^^\nPlease give full updated code without an error\n ```python\nimport streamlit as st\nfrom decouple import config\nimport google.generativeai as genai\n\nAPI_KEY = config('API_KEY')\n\nwith st.sidebar:\n    \"[View the source code](https://github.com/Kiash254/Langchain-GEN-AI-Streamlit/blob/main/stream.py)\"\n\nst.title(\"Agricultural Recommender System\")\nst.caption(\"🚀 Farmers Choice to get the fastest Solution\")\n\nif \"messages\" not in st.session_state:\n    st.session_state[\"messages\"] = [{\"role\": \"assistant\", \"content\": \"Hello Mkulima 👋 Naeza Kusaidia Ajy(How can i help you) ? \"}]\n\nfor msg in st.session_state.messages:\n    st.chat_message(msg[\"role\"]).write(msg[\"content\"])\n\nif prompt := st.chat_input():\n    model = genai.GenerativeModel('gemini-pro', API_KEY)\n    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n    st.chat_message(\"user\").write(prompt)\n    response = model.generate(prompt, max_tokens=150)  # Replace this line with the correct method to generate chat completions\n    msg = response.choices[0].message.content  # This line might also need to be updated based on the response structure\n    st.session_state.messages.append({\"role\": \"assistant\", \"content\": msg})\n    st.chat_message(\"assistant\").write(msg)\n```\n\nThis code should now run without the error you were encountering.",
]

response = model.generate_content(prompt_parts)
print(response.text)