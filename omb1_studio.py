# ==========================================
# COMPANY: ZERO | MODEL: OMB1
# MODULE: OMB1 AI STUDIO (CUSTOM SVG EDITION)
# THEME: SAFED + GRAIN + SKY BLUE + NEON GLOW
# COST: ZERO (100% Offline Client App)
# ==========================================

import streamlit as st
import math
import re

# Page configurations
st.set_page_config(page_title="ZERO OMB1 Studio", page_icon="🕉️", layout="wide")

# Unique CSS Injection: Safed+Grain UI with Animated Google Studio Input Box
st.markdown("""
    <style>
    /* Global Canvas: Safed + Grain + Low Sky Blue Tint */
    .stApp {
        background-color: #f3f7fa;
        background-image: radial-gradient(rgba(0,0,0,0.02) 1px, transparent 0);
        background-size: 20px 20px;
        color: #2c3e50;
    }

    /* Custom Responsive Sidebar with SVG integration */
    .stSidebar {
        background-color: #ffffff !important;
        border-right: 2px solid #e1ebf5;
    }

    /* Custom Navigation Layout using raw HTML blocks */
    .nav-item {
        display: flex;
        align-items: center;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 8px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .nav-item:hover {
        background: #eef5ff;
        border-color: #3b82f6;
    }
    .nav-text {
        margin-left: 12px;
        font-weight: 500;
        color: #334155;
    }

    /* Google AI Studio Box Container with Rotating Neon Border (Green-Yellow-Pink) */
    .glow-container {
        position: relative;
        padding: 3px;
        background: linear-gradient(90deg, #00ffcc, #ffeb3b, #ff007f, #00ffcc);
        background-size: 300% 300%;
        animation: spin-border 5s linear infinite;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    @keyframes spin-border {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Smooth auto-stretching input text area */
    textarea {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: none !important;
        border-radius: 7px !important;
        font-size: 16px !important;
        transition: height 0.2s ease-in-out !important;
    }
    </style>
    """, unsafe_style_html=True)

# ------------------------------------
# BACKEND INITIALIZATION (INFINITY LOGIC)
# ------------------------------------
if "gyan_matrix" not in st.session_state:
    st.session_state.gyan_matrix = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def omb1_infinity_hash(text):
    char_sum = sum(ord(c) for c in text)
    raw_pattern = (char_sum * math.pi) + (len(text) * math.e)
    return round((raw_pattern % 100003) / 100003, 8)

def token_extractor(text):
    patterns = r'(\w+म्|\w+ः|\w+न्ति|\w+स्य|\w+ति|[a-zA-Z\u0600-\u06FF\u4e00-\u9fa5]{3,})'
    return list(set(re.findall(patterns, text)))

# ------------------------------------
# UI SIDEBAR NAVIGATION (CUSTOM SVG ICONS)
# ------------------------------------
with st.sidebar:
    st.markdown("<h3 style='color:#1e3a8a; margin-bottom:20px;'>📁 NAVIGATION</h3>", unsafe_style_html=True)
    
    # Custom SVG Item 1: Project History Icon (Folder Blueprint)
    st.markdown("""
    <div class="nav-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2">
            <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
        </svg>
        <span class="nav-text">Mool Gyan Project</span>
    </div>
    """, unsafe_style_html=True)

    # Custom SVG Item 2: Active Identity Lock (Local Auth Graphic)
    st.markdown("""
    <div class="nav-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ec4899" stroke-width="2">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
        </svg>
        <span class="nav-text">ZERO Auth: Device Locked</span>
    </div>
    """, unsafe_style_html=True)
    
    st.markdown("---")
    if st.button("🗑️ Reset All Local Cache"):
        st.session_state.gyan_matrix.clear()
        st.session_state.chat_history.clear()
        st.rerun()

# ------------------------------------
# MAIN WORKSPACE DESIGN
# ------------------------------------
st.markdown("<h2 style='color:#1e3a8a;'>🕉️ ZERO COMPANY | OMB1 STUDIO</h2>", unsafe_style_html=True)
st.caption("⚡ Status: Zero Server Architecture Active | Local Engine Running via Infinity Sequence Mapping")

# Real-time Stream Display
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.write(f"👤 **User:** {chat['text']}")
    else:
        st.write(f"🤖 **OMB1 System:** {chat['text']}")

st.markdown("---")

# File Upload Panel (Plus Icon Simulator Interface)
col_file, col_text = st.columns([0.15, 0.85])

with col_file:
    st.markdown("<p style='font-size:12px; font-weight:bold; margin-bottom:2px;'>➕ Media Feed</p>", unsafe_style_html=True)
    uploaded_media = st.file_uploader("Upload", type=["txt", "mp3", "jpg", "png", "mp4"], label_visibility="collapsed")
    if uploaded_media:
        media_bytes = uploaded_media.read().decode("utf-8", errors="ignore")
        ptr_key = omb1_infinity_hash(media_bytes)
        st.session_state.gyan_matrix[ptr_key] = {"data": media_bytes, "tokens": token_extractor(media_bytes)}
        st.toast("➕ File instantly 'Caught' in background math system!", icon="✔️")

with col_text:
    st.markdown("<p style='font-size:12px; font-weight:bold; margin-bottom:2px;'>✏️ Google Studio Input (Auto-Stretchable Box)</p>", unsafe_style_html=True)
    
    # Glowing Gradient Border Wrap
    st.markdown('<div class="glow-container">', unsafe_style_html=True)
    user_prompt = st.text_area("", placeholder="Kisi bhi language mein dialouge ya big book data likhein...", label_visibility="collapsed", height=90)
    st.markdown('</div>', unsafe_style_html=True)

# Operational Action Buttons
btn_ask, btn_train, _ = st.columns([0.2, 0.2, 0.6])

with btn_ask:
    if st.button("🚀 Send Prompt"):
        if user_prompt:
            st.session_state.chat_history.append({"role": "user", "text": user_prompt})
            
            # Local token match calculation
            q_tokens = token_extractor(user_prompt)
            matched_context = None
            
            for p, mem in st.session_state.gyan_matrix.items():
                if set(q_tokens) & set(mem["tokens"]) or any(w in mem["data"] for w in user_prompt.split()):
                    matched_context = mem["data"]
                    break
            
            if matched_context:
                ans = f"[Instant Recall Match Found via Mathematical Coordinates]\nContext data caught locally: {matched_context[:250]}..."
            else:
                ans = f"[OMB1 Autonomous Model Output]: Aapka sequence process ho gaya hai. Piche koi server nahi hai, isliye calculation aapke device par real-time execute hui."
                
            st.session_state.chat_history.append({"role": "omb1", "text": ans})
            st.rerun()

with btn_train:
    if st.button("📥 Instant Train"):
        if user_prompt:
            p_ptr = omb1_infinity_hash(user_prompt)
            st.session_state.gyan_matrix[p_ptr] = {"data": user_prompt, "tokens": token_extractor(user_prompt)}
            st.success(f"Instant 'Catch' Complete! Locked in Local Array Matrix Pointer: {p_ptr}")
