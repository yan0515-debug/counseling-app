import streamlit as st
import pandas as pd
import altair as alt

# --- 系統設定 ---
st.set_page_config(page_title="諮商專業取向深度探索系統 (CTOS-Pro)", page_icon="🧭", layout="wide")

# --- Session State 初始化 ---
if 'axis_obj_sub' not in st.session_state:
    st.session_state.axis_obj_sub = 0.0 
if 'axis_ana_exp' not in st.session_state:
    st.session_state.axis_ana_exp = 0.0
if 'history' not in st.session_state:
    st.session_state.history = [] 
if 'raw_scores_x' not in st.session_state:
    st.session_state.raw_scores_x = []
if 'raw_scores_y' not in st.session_state:
    st.session_state.raw_scores_y = []

# --- 輔助函數 ---
def update_axes(x_delta, y_delta, phase, choice_text, reasoning):
    st.session_state.axis_obj_sub += x_delta
    st.session_state.axis_ana_exp += y_delta
    
    # 記錄原始分數變化
    st.session_state.raw_scores_x.append(x_delta)
    st.session_state.raw_scores_y.append(y_delta)
    
    st.session_state.history.append({
        "phase": phase,
        "choice": choice_text,
        "reasoning": reasoning
    })

# --- CSS 樣式 ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; font-weight: 600; color: #2c3e50; }
    .tool-card {
        background-color: #ffffff;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 25px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .tool-icon { font-size: 45px; margin-bottom: 15px; }
    .tool-title { font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }
    .tool-desc { font-size: 18px; color: #555; line-height: 1.6; text-align: left;}
    .scenario-box { 
        background-color: #f8f9fa; 
        padding: 25px; 
        border-radius: 8px; 
        border-left: 6px solid #34495e; 
        margin-bottom: 25px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.6;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        color: #856404;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 側邊欄 ---
st.sidebar.title("🧭 系統導航")
st.sidebar.warning("⚠️ 重要提示：\n每一題作答後，請務必點擊下方的「確認送出」按鈕，系統才會記錄您的數據。")

step = st.sidebar.radio(
    "進度：",
    ["前言：方法論與架構", "Phase 1. 隱喻投射 (角色觀)", "Phase 2. 臨床決策 (改變觀)", "Phase 3. 陰影探索 (價值觀)", "Phase 4. 空間配置 (框架觀)", "Phase 5. 綜合分析報告"]
)

# ==========================================
# 前言：恢復詳細版
# ==========================================
if step == "前言：方法論與架構":
    st.title("諮商專業取向深度探索系統 (CTOS-Pro)")
    st.markdown("### 系統建置邏輯與理論基礎")
    
    st.markdown("""
    本系統專為諮商心理學相關背景之學生與實務工作者設計，旨在透過多維度的自我評估，探索個人的**諮商理論取向 (Counseling Theoretical Orientation)**。
    
    #### 1. 理論架構 (Theoretical Framework)
    本測驗主要依據 **Poznanski & McLennan (1995)** 所提出的 **Counselor Theoretical Position Scale (CTPS)** 以及 **Worthington & Dillon (2011)** 的 **TOPS-R** 量表進行架構設計。系統將諮商取向解構為兩個核心的連續變項 (Continuum)：
    
    * **X 軸：知識論立場 (Epistemological Stance)**
        * **客觀實證 (Objective/Empirical)**：傾向相信真理的外在性、可觀察性，重視結構、測量與科學證據。
        * **主觀建構 (Subjective/Constructivist)**：傾向相信真理的內在性、個別性，重視現象學、個人意義與獨特經驗。
    
    * **Y 軸：介入焦點 (Intervention Focus)**
        * **理性分析 (Rational/Analytical)**：傾向透過認知重構、邏輯分析、洞察 (Insight) 潛意識結構來促成改變。
        * **情感體驗 (Experiential/Affective)**：傾向透過情感宣洩、此時此刻的覺察、矯正性情緒經驗來促成改變。

    #### 2. 評估方法論 (Methodology)
    本系統採用 **三角檢證法 (Triangulation)** 設計題型，以提升效度：
    * **隱喻投射 (Phase 1)**：測量潛意識中的治療師角色認同。
    * **情境模擬 (Phase 2)**：測量臨床現場的直覺反應與介入偏好。
    * **反向指標 (Phase 3)**：透過「陰影 (Shadow)」與恐懼，推論個人的核心價值（例如：恐懼失控可能反映對結構的需求）。
    * **環境心理 (Phase 4)**：透過空間配置偏好，測量對治療框架與界線的看法。

    #### 3. 聲明與限制 (Limitations)
    * **動態性**：諮商取向是一個動態發展的過程，本結果僅代表您「當下」的傾向，並非永久的標籤。
    * **建議性質**：分析結果僅供自我覺察與督導討論之參考，不應作為評斷專業能力之依據。
    
    ---
    #### ⚠️ 作答說明
    本系統包含不同形式的題目（選擇、排序、情境）。**請注意：每一題作答完畢後，皆須點擊該題下方的「確認按鈕」，系統才會進行計分。**
    """)

# ==========================================
# Phase 1: 隱喻投射 (圖片更新)
# ==========================================
elif step == "Phase 1. 隱喻投射 (角色觀)":
    st.header("Phase 1: 治療關係中的角色隱喻")
    
    # --- Q1: 登山隱喻 ---
    st.markdown("#### Q1. 若將諮商歷程比喻為一次登山，請觀察下列圖像，您認為自己的功能最接近哪一種角色？")
    
    c1, c2 = st.columns(2)
    with c1:
        # A. 嚮導：兩個人，其中一人指著遠方 (Direction)
        st.image("https://images.unsplash.com/photo-1544367563-12123d845e89?w=500", caption="A")
    with c2:
        # B. 伴侶：兩個人並肩行走，互動親密 (Side by side)
        st.image("https://images.unsplash.com/photo-1627662055655-2076fa4c6796?w=500", caption="B")
    
    c3, c4 = st.columns(2)
    with c3:
        # C. 觀察者：一人在旁觀察紀錄，或透過鏡頭觀察 (Observation)
        st.image("https://images.unsplash.com/photo-1523456386829-05574581ea3d?w=500", caption="C")
    with c4:
        # D. 教練：攀岩確保，明顯的指導與保護動作 (Support/Instruction)
        st.image("https://images.unsplash.com/photo-1522163182402-834f871fd851?w=500", caption="D")

    choice1 = st.radio("請選擇最貼近的角色原型：", [
        "A. 嚮導 (Guide)：熟悉地圖與地形，能預告潛在危險並規劃安全路徑。",
        "B. 伴侶 (Partner)：配合對方的速度並肩同行，共同經歷旅程的風雨。",
        "C. 觀察者 (Observer)：位於制高點或後方，保持視野，分析其步伐與慣性。",
        "D. 教練 (Coach)：在旁確保安全，指導手腳的施力點，協助發揮潛能。"
    ])
    
    if st.button("確認 Q1"):
        if "A" in choice1: update_axes(2.0, 1.0, "P1-Q1", choice1, "嚮導：客觀指導")
        if "B" in choice1: update_axes(-2.0, -2.0, "P1-Q1", choice1, "伴侶：主觀體驗")
        if "C" in choice1: update_axes(-1.0, 3.0, "P1-Q1", choice1, "觀察者：動力分析")
        if "D" in choice1: update_axes(2.0, 2.0, "P1-Q1", choice1, "教練：理性行動")
        st.success("數據已記錄。")

    st.markdown("---")

    # --- Q2: 魔法工具 (卡片式說明 + 單選) ---
    st.markdown("#### Q2. 承上題，若您能擁有一項「核心工具」來協助個案，您的直覺首選為何？")
    st.markdown("請選擇您在治療中最習慣使用的「介入方向」。")

    # 顯示卡片說明 (僅作展示)
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🔦</div>
            <div class="tool-title">手電筒</div>
            <div class="tool-desc">
                <b>功能：</b>照亮黑暗角落<br>
                <b>方向：</b>深入潛意識與未知
            </div>
        </div>
        """, unsafe_allow_html=True)
    with t2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🧣</div>
            <div class="tool-title">毛毯</div>
            <div class="tool-desc">
                <b>功能：</b>提供溫暖與包容<br>
                <b>方向：</b>向內的情感撫慰
            </div>
        </div>
        """, unsafe_allow_html=True)
            
    st.write("") # Spacer
    
    t3, t4 = st.columns(2)
    with t3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🪞</div>
            <div class="tool-title">鏡子</div>
            <div class="tool-desc">
                <b>功能：</b>如實反映原貌<br>
                <b>方向：</b>當下的現象學反映
            </div>
        </div>
        """, unsafe_allow_html=True)
    with t4:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🧭</div>
            <div class="tool-title">指南針</div>
            <div class="tool-desc">
                <b>功能：</b>指出正確方位<br>
                <b>方向：</b>向外的目標導向
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    
    # 單選題
    tool_choice = st.radio("請選擇一項工具：", ["🔦 手電筒", "🧣 毛毯", "🪞 鏡子", "🧭 指南針"])

    if st.button("確認 Q2"):
        if "手電筒" in tool_choice: update_axes(-1.0, 2.5, "P1-Q2", "手電筒", "工具：探索潛意識")
        elif "毛毯" in tool_choice: update_axes(-2.0, -1.5, "P1-Q2", "毛毯", "工具：提供涵容")
        elif "鏡子" in tool_choice: update_axes(-1.0, -1.0, "P1-Q2", "鏡子", "工具：現象學反映")
        elif "指南針" in tool_choice: update_axes(2.0, 1.5, "P1-Q2", "指南針", "工具：目標導向")
        st.success("已記錄數據。")

    st.markdown("---")

    # --- Q3: 校準題 ---
    st.markdown("#### Q3. 理論校準 (Calibration)")
    st.markdown("""
    <div style="font-size: 18px; padding: 15px; border: 1px solid #ddd; background-color:#fafafa; border-radius: 5px;">
    <b>題目說明：</b>此題用於校準您的基本知識論立場。請評估您對以下敘述的認同程度：<br><br>
    <b>「我認為治療師保持客觀中立的『技術專家』形象，比展現個人特質更重要。」</b>
    </div>
    """, unsafe_allow_html=True)
    
    q3_score = st.slider("1 (非常不同意 / 重視個人特質) <---> 5 (非常同意 / 重視專家形象)", 1, 5, 3)
    
    if st.button("確認 Q3 校準"):
        val = q3_score - 3
        update_axes(val * 1.5, 0, "P1-Q3", f"校準分數 {q3_score}", "校準：專家形象認同度")
        st.success("校準數據已記錄。")

# ==========================================
# Phase 2: 臨床決策 (純淨版)
# ==========================================
elif step == "Phase 2. 臨床決策 (改變觀)":
    st.header("Phase 2: 改變機制的觀點")
    
    # --- 情境 1 ---
    st.markdown('<div class="scenario-box"><b>情境 1：自我否定</b><br>個案低著頭，語氣顫抖地說：「我覺得……我這輩子就是個失敗品，不管怎麼努力最後都會搞砸……」</div>', unsafe_allow_html=True)
    q1 = st.radio("介入焦點：", ["1. 檢視證據：「你是依據什麼具體事件或證據，來定義自己是『失敗品』的？」", "2. 情感反映：「聽起來你現在真的感到很挫折，那種感覺像是被徹底打敗了……」", "3. 連結過去：「這句話讓你聯想到過去誰對你的評價嗎？或是誰曾經這樣對你說？」", "4. 尋找例外：「在過去這段時間裡，有沒有哪個時刻，事情其實沒有搞砸得那麼嚴重？」"], key="s2_q1")
    
    # --- 情境 2 ---
    st.markdown('<div class="scenario-box"><b>情境 2：沈默僵局</b><br>個案已經沈默了將近十分鐘。他看著窗外，似乎沒有要開口的意思。治療室的空氣變得有些凝重。</div>', unsafe_allow_html=True)
    q2 = st.radio("處置方向：", ["1. 抗拒分析：他可能在抗拒某些痛苦的素材，我應思考這份沈默背後的潛意識意義。", "2. 結構引導：我需要做點什麼來打破僵局，例如回顧一下上次的作業或設定今天議程。", "3. 臨在陪伴：這份沈默是珍貴的，他正在整理自己，我只需安靜陪伴，提供安全的空間。", "4. 過程溝通：沈默本身就是一種溝通，我應該詢問：「透過沈默，你似乎想告訴我些什麼？」"], key="s2_q2")

    # --- 情境 3 ---
    st.markdown('<div class="scenario-box"><b>情境 3：治療關係破裂</b><br>個案突然對你生氣：「你一直問我感受有什麼用？這對解決我的現實問題一點幫助都沒有！」</div>', unsafe_allow_html=True)
    q3 = st.radio("首要回應：", ["1. 合作對話：「謝謝你告訴我，看來我們對於『什麼有幫助』的想法不太一樣，我們要不要來討論一下？」", "2. 同理接納：「我看見你真的很著急，你很希望能快點好起來，而我的提問讓你感到挫折，是嗎？」", "3. 移情探索：「你現在對我的生氣，是不是很像你平常對父親感覺到的那種無力感？」", "4. 行動修正：「好，那我們現在來調整方向，看看具體來說我們可以做哪些行為改變。」"], key="s2_q3")
    
    if st.button("確認 Phase 2 所有回答"):
        if "1." in q1: update_axes(1.5, 1.5, "P2-Q1", "檢視證據", "理性證據")
        if "2." in q1: update_axes(-1.5, -1.5, "P2-Q1", "情感反映", "情感體驗")
        if "3." in q1: update_axes(-1.0, 2.0, "P2-Q1", "連結過去", "動力分析")
        if "4." in q1: update_axes(1.0, 1.0, "P2-Q1", "尋找例外", "行動建構")
        
        if "1." in q2: update_axes(-1.0, 2.0, "P2-Q2", "抗拒分析", "分析視角")
        if "2." in q2: update_
