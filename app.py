import streamlit as st
import google.generativeai as genai
import asyncio
import edge_tts
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="ND Movie Recap Studio", layout="wide")
st.title("🎬 ND Movie Recap Studio (Myanmar)")

# --- SIDEBAR (Settings) ---
with st.sidebar:
    st.header("⚙️ Configuration")
    user_api_key = st.text_input("Gemini API Key", type="password")
    
    st.subheader("🎤 Voice Options")
    # မြန်မာသံထွက်ကောင်းသည့် Neural Voices များ
    voice_list = {
        "Thiha (Male 1)": "my-MM-ThihaNeural",
        "ZawZaw (Male 2 - Deep)": "en-US-GuyNeural",
        "Nann (Female 1)": "my-MM-ZawZawNeural",
        "Jenny (Female 2 - Natural)": "en-US-JennyNeural"
    }
    selected_voice = st.selectbox("Choose Voice", list(voice_list.keys()))
    
    st.subheader("📏 Format")
    length = st.radio("Script Length", ["TikTok (1 min)", "Facebook (3 min)"])
    tone = st.radio("Tone", ["သည်းထိတ်ရင်ဖို", "ဟာသ", "ဝမ်းနည်းစရာ"])

# --- MAIN INTERFACE ---
st.info("YouTube Link ထည့်ပါ သို့မဟုတ် မူရင်း Video ကို Upload တင်ပါ")
yt_url = st.text_input("YouTube URL")
upload_video = st.file_uploader("Upload Original Video (MP4)", type=["mp4", "mov"])

if st.button("Generate Recap & Audio 🔥"):
    if not user_api_key:
        st.error("Gemini API Key အရင်ထည့်ပေးပါ!")
    else:
        st.success(f"{voice_list[selected_voice]} အသံဖြင့် {tone} ပုံစံ Script စတင်ထုတ်လုပ်နေပါပြီ...")
        # Audio & Script logic starts here
        st.write("---")
        st.subheader("📝 Generated Script Preview")
        st.text_area("စာသားများ (Copy ယူရန်)", "AI က စာသားများကို ဤနေရာတွင် ထုတ်ပေးပါမည်...", height=200)
        
        st.subheader("🔊 Audio Preview")
        st.info("အသံဖိုင်ကို ဤနေရာတွင် နားထောင်နိုင်ပါမည်။")

st.markdown("---")
st.caption("Developed by ND Team | 2026")
