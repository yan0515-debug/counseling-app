import streamlit as st
import pandas as pd
import altair as alt
import numpy as np # 新增 numpy 進行統計計算

# --- 系統設定 ---
st.set_page_config(page_title="諮商專業取向深度探索系統 (CTOS-Pro)", page_icon="🧭", layout="wide")

# --- Session State 初始化 ---
if 'axis_obj_sub' not in st.session_state:
    st.session_state.axis_obj_sub = 0.0 
if 'axis_ana_exp' not in st.session_state:
    st.session_state.axis_ana_exp = 0.0
if 'history' not in st.session_state:
    st.session_state.history = [] 
# 新增：記錄原始分數陣列，用於計算變異數 (Consistency Check)
if 'raw_scores_x' not in st.session_state:
    st.session_state.raw_scores_x = []
if 'raw_scores_y' not in st.session_state:
    st.session_state.raw_scores_y = []

# --- 輔助函數 ---
def update_axes(x_delta, y_delta, phase, choice_text, reasoning):
    st.session_state.axis_obj_sub += x_delta
    st.session_state.axis_ana_exp += y_delta
    
    # 記錄原始分數變化，用於矛盾檢測
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
        padding: 20px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .tool-icon { font-size: 40px; margin-bottom: 10px; }
    .tool-title { font-size: 22px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }
    .tool-desc { font-size: 16px; color: #555; line-height: 1.5; }
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
# 前言
# ==========================================
if step == "前言：方法論與架構":
    st.title("諮商專業取向深度探索系統 (CTOS-Pro)")
    st.markdown("### 系統建置邏輯與理論基礎")
    st.markdown("""
    本系統專為諮商心理學背景之專業人員設計，旨在透過多維度的自我評估，探索個人的**諮商理論取向**。
    
    #### 1. 理論架構 (Theoretical Framework)
    本測驗依據 **Poznanski & McLennan (1995) CTPS** 與 **TOPS-R** 量表，將取向解構為雙軸向：
    * **X 軸：知識論立場** (客觀實證 vs. 主觀建構)
    * **Y 軸：介入焦點** (理性分析 vs. 情感體驗)

    #### 2. 檢測機制 (Quality Control)
    為了確保結果的信度，本系統內建**矛盾檢測演算法**。若您的作答在不同階段出現高度牴觸（例如：在隱喻題選擇極度客觀，卻在情境題選擇極度主觀），系統將在最終報告中提出警示與整合性建議。

    #### 3. 聲明
    * **動態性**：結果僅代表「當下」的傾向。
    * **建議性質**：分析結果僅供自我覺察參考。
    
    ---
    #### ⚠️ 作答說明
    **請注意：每一題作答完畢後，皆須點擊該題下方的「確認按鈕」，系統才會進行計分。**
    """)

# ==========================================
# Phase 1: 隱喻投射 (圖片與工具優化)
# ==========================================
elif step == "Phase 1. 隱喻投射 (角色觀)":
    st.header("Phase 1: 治療關係中的角色隱喻")
    
    # --- Q1: 登山隱喻 (更換為更符合描述的圖片) ---
    st.markdown("#### Q1. 若將諮商歷程比喻為一次登山，請觀察下列圖像，您認為自己的功能最接近哪一種角色？")
    
    c1, c2 = st.columns(2)
    with c1:
        # A. 嚮導：一人在前指路，一人在後
        st.image("https://images.unsplash.com/photo-1501555088652-021faa106b9b?w=500", caption="A")
    with c2:
        # B. 伴侶：兩人在雪地/山徑並肩行走
        st.image("https://images.unsplash.com/photo-1605130284535-11dd9eedc58a?w=500", caption="B")
    
    c3, c4 = st.columns(2)
    with c3:
        # C. 觀察者：站在高處或遠處觀看 (用望遠鏡或背影)
        st.image("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=500", caption="C")
    with c4:
        # D. 教練：攀岩確保，明顯的指導與保護動作
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

    # --- Q2: 魔法工具 (卡片式設計 + 放大字體) ---
    st.markdown("#### Q2. 承上題，若您能擁有一項「核心工具」來協助個案，您的直覺首選為何？")
    st.markdown("請選擇您在治療中最習慣使用的「介入方向」。")

    # 使用 HTML 製作漂亮的卡片
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🔦</div>
            <div class="tool-title">手電筒</div>
            <div class="tool-desc">
                <b>功能：</b>照亮黑暗角落<br>
                <b>方向：</b>深入潛意識與未知<br>
                <b>隱喻：</b>看見被壓抑的真實
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("") # Spacer
        if st.checkbox("選擇「手電筒」"):
             update_axes(-1.0, 2.5, "P1-Q2", "手電筒", "工具：探索潛意識")
             st.success("已選擇手電筒")

    with t2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🧣</div>
            <div class="tool-title">毛毯</div>
            <div class="tool-desc">
                <b>功能：</b>提供溫暖與包容<br>
                <b>方向：</b>向內的情感撫慰<br>
                <b>隱喻：</b>建立安全的矯正性經驗
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.checkbox("選擇「毛毯」"):
            update_axes(-2.0, -1.5, "P1-Q2", "毛毯", "工具：提供涵容")
            st.success("已選擇毛毯")
            
    st.write("") # Spacer
    
    t3, t4 = st.columns(2)
    with t3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🪞</div>
            <div class="tool-title">鏡子</div>
            <div class="tool-desc">
                <b>功能：</b>如實反映原貌<br>
                <b>方向：</b>當下的現象學反映<br>
                <b>隱喻：</b>不加扭曲的真誠一致
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.checkbox("選擇「鏡子」"):
            update_axes(-1.0, -1.0, "P1-Q2", "鏡子", "工具：現象學反映")
            st.success("已選擇鏡子")

    with t4:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🧭</div>
            <div class="tool-title">指南針</div>
            <div class="tool-desc">
                <b>功能：</b>指出正確方位<br>
                <b>方向：</b>向外的目標導向<br>
                <b>隱喻：</b>回歸理性的現實判斷
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.checkbox("選擇「指南針」"):
            update_axes(2.0, 1.5, "P1-Q2", "指南針", "工具：目標導向")
            st.success("已選擇指南針")

    st.markdown("---")

    # --- Q3: 校準題 (回歸) ---
    st.markdown("#### Q3. 理論校準 (Calibration)")
    st.markdown("""
    <div style="font-size: 18px; padding: 15px; border: 1px solid #ddd; background-color:#fafafa; border-radius: 5px;">
    <b>題目說明：</b>此題用於校準您的基本知識論立場。請評估您對以下敘述的認同程度：<br><br>
    <b>「我認為治療師保持客觀中立的『技術專家』形象，比展現個人特質更重要。」</b>
    </div>
    """, unsafe_allow_html=True)
    
    q3_score = st.slider("1 (非常不同意 / 重視個人特質) <---> 5 (非常同意 / 重視專家形象)", 1, 5, 3)
    
    if st.button("確認 Q3 校準"):
        # 1分=主觀(-), 5分=客觀(+)
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
        if "2." in q2: update_axes(2.0, 1.0, "P2-Q2", "結構引導", "結構介入")
        if "3." in q2: update_axes(-2.0, -2.0, "P2-Q2", "臨在陪伴", "人本視角")
        if "4." in q2: update_axes(-1.0, 1.0, "P2-Q2", "過程溝通", "系統視角")

        if "1." in q3: update_axes(-1.0, 1.0, "P2-Q3", "合作對話", "後現代合作")
        if "2." in q3: update_axes(-2.0, -1.0, "P2-Q3", "同理接納", "人本同理")
        if "3." in q3: update_axes(-1.0, 3.0, "P2-Q3", "移情探索", "動力詮釋")
        if "4." in q3: update_axes(2.0, 2.0, "P2-Q3", "行動修正", "行為調整")
        st.success("數據已記錄。")

# ==========================================
# Phase 3: 陰影探索 (增加題目)
# ==========================================
elif step == "Phase 3. 陰影探索 (價值觀)":
    st.header("Phase 3: 陰影與反移情")
    st.markdown("本階段透過「反向指標」，測量您對於特定治療情境的潛在焦慮。")
    
    # --- Q1 ---
    st.subheader("Q1. 治療師特質的陰影")
    st.write("請選出您認為**最不可接受**（最像噩夢）的治療師形象：")
    
    shadow_options = {
        "A": "失控的治療師：界線模糊，被個案情緒淹沒，甚至跟著個案一起哭泣，失去專業位置。",
        "B": "冷血的治療師：像個冰冷的分析儀器，只有理論沒有溫度，讓個案感覺不到人性。",
        "C": "鬼打牆的治療師：談了很久卻毫無進展，沒有目標，每週只是漫無目的地聊天。",
        "D": "霸道的治療師：自以為是專家，將自己的價值觀強加在個案身上，不容許反駁。"
    }
    shadow_1 = st.selectbox("💀 第一名最無法忍受的是：", ["請選擇..."] + list(shadow_options.values()))
    shadow_2 = st.selectbox("💀 第二名無法忍受的是：", ["請選擇..."] + list(shadow_options.values()))
    
    # --- Q2 ---
    st.subheader("Q2. 治療歷程的僵局")
    process_fear = st.radio("在諮商過程中，哪一種「狀態」最讓您感到焦慮或自我懷疑？", [
        "1. 混亂無序：個案話題跳躍，情緒張力極大，我完全抓不到重點，覺得場面快要失控。",
        "2. 表層疏離：個案很有禮貌地配合，但感覺我們之間隔著一層厚厚的牆，無法接觸真實情感。",
        "3. 理智化：個案不斷地分析自己，說得頭頭是道，但完全沒有任何行為上的改變。",
        "4. 依賴退化：個案完全依賴我的建議，像個孩子一樣不願為自己負責，等待我去拯救他。"
    ])

    if st.button("確認 Phase 3 所有回答"):
        if shadow_1 != "請選擇..." and shadow_2 != "請選擇..." and shadow_1 != shadow_2:
             def analyze_shadow(text, weight):
                if "失控" in text: update_axes(1.5 * weight, 0, "P3-Q1", "怕失控", f"陰影：需求結構 (w={weight})")
                if "冷血" in text: update_axes(-1.5 * weight, -1.0 * weight, "P3-Q1", "怕冷血", f"陰影：需求情感 (w={weight})")
                if "鬼打牆" in text: update_axes(1.0 * weight, 1.5 * weight, "P3-Q1", "怕沒效", f"陰影：需求效能 (w={weight})")
                if "霸道" in text: update_axes(-1.5 * weight, 0, "P3-Q1", "怕霸道", f"陰影：需求尊重 (w={weight})")
             analyze_shadow(shadow_1, 1.5)
             analyze_shadow(shadow_2, 1.0)
        
        if "1." in process_fear: update_axes(1.5, 0.5, "P3-Q2", "怕混亂", "恐懼：渴望秩序")
        if "2." in process_fear: update_axes(-1.5, -1.5, "P3-Q2", "怕疏離", "恐懼：渴望接觸")
        if "3." in process_fear: update_axes(0, -2.0, "P3-Q2", "怕理智化", "恐懼：渴望體驗")
        if "4." in process_fear: update_axes(-1.0, 1.0, "P3-Q2", "怕依賴", "恐懼：渴望賦能")
        st.success("數據已記錄。")

# ==========================================
# Phase 4: 空間配置 (更生活化的情境)
# ==========================================
elif step == "Phase 4. 空間配置 (框架觀)":
    st.header("Phase 4: 空間心理與人際界線")
    st.markdown("""
    <div class="warning-box">
    <b>🔥 情境轉換：私人領域的深度對話</b><br>
    請暫時放下「諮商室標準配置」的考量。想像您邀請一位非常信任的摯友到家中，準備進行一場深入靈魂的徹夜長談。<br>
    為了讓<b>「您自己」</b>感到最自在、最能真誠交流，您身體直覺會選擇哪一種坐法？
    </div>
    """, unsafe_allow_html=True)

    def get_layout_svg(layout_type):
        base_svg = '<svg width="250" height="180" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff; border:1px solid #eee;">'
        if layout_type == "SideBySide":
            content = """<rect x="50" y="80" width="150" height="50" rx="10" fill="#f1c40f" opacity="0.3"/><circle cx="100" cy="105" r="20" fill="#3498db" /> <text x="90" y="110" fill="white" font-size="10">You</text><circle cx="150" cy="105" r="20" fill="#e74c3c" /> <text x="140" y="110" fill="white" font-size="10">Friend</text><text x="75" y="160" fill="#666" font-size="12">並肩而坐 (沙發)</text>"""
        elif layout_type == "L_Shape":
            content = """<rect x="120" y="90" width="40" height="40" fill="#ecf0f1" stroke="#bdc3c7"/><circle cx="90" cy="70" r="20" fill="#3498db" /> <text x="80" y="75" fill="white" font-size="10">You</text><circle cx="160" cy="140" r="20" fill="#e74c3c" /> <text x="150" y="145" fill="white" font-size="10">Friend</text><text x="150" y="40" fill="#666" font-size="12">舒適斜角 (L型)</text>"""
        elif layout_type == "Formal":
            content = """<rect x="105" y="40" width="40" height="100" fill="#ecf0f1" stroke="#bdc3c7"/><circle cx="60" cy="90" r="20" fill="#3498db" /> <text x="50" y="95" fill="white" font-size="10">You</text><circle cx="190" cy="90" r="20" fill="#e74c3c" /> <text x="180" y="95" fill="white" font-size="10">Friend</text><text x="90" y="25" fill="#666" font-size="12">面對面 (隔著桌子)</text>"""
        elif layout_type == "Separate":
            content = """<circle cx="50" cy="90" r="20" fill="#3498db" /> <text x="40" y="95" fill="white" font-size="10">You</text><circle cx="200" cy="90" r="20" fill="#e74c3c" /> <text x="190" y="95" fill="white" font-size="10">Friend</text><path d="M 80 90 L 170 90" stroke="#999" stroke-width="1" stroke-dasharray="4"/><text x="85" y="150" fill="#666" font-size="12">獨立座椅 (保持距離)</text>"""
        return base_svg + content + '</svg>'

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(get_layout_svg("SideBySide"), unsafe_allow_html=True)
        if st.button("1. 並肩而坐 (沙發)"):
            update_axes(-2.0, -1.5, "P4-Q1", "並肩", "空間：高親密體驗")
            st.success("已選擇")
        st.markdown(get_layout_svg("L_Shape"), unsafe_allow_html=True)
        if st.button("2. 舒適斜角 (L型)"):
            update_axes(-0.5, 0, "P4-Q1", "L型", "空間：人本折衷")
            st.success("已選擇")
    with c2:
        st.markdown(get_layout_svg("Formal"), unsafe_allow_html=True)
        if st.button("3. 面對面 (隔桌)"):
            update_axes(1.5, 1.0, "P4-Q1", "對坐", "空間：結構認知")
            st.success("已選擇")
        st.markdown(get_layout_svg("Separate"), unsafe_allow_html=True)
        if st.button("4. 獨立座椅 (距離)"):
            update_axes(1.0, 2.0, "P4-Q1", "獨立椅", "空間：界線觀察")
            st.success("已選擇")

    st.markdown("---")
    st.subheader("Q2. 輔助溝通偏好")
    st.write("在對話過程中，為了讓對方更清楚您的想法，您是否傾向**拿出一張紙或白板，畫圖/寫字/列點**來解釋？")
    
    use_visual = st.radio("直覺習慣：", ["是，我喜歡視覺化、畫圖或列點，這樣比較清楚。", "否，我傾向純口語描述，眼神與情感交流更重要。"])
    if st.button("確認 Q2"):
        if "是" in use_visual: update_axes(1.5, 1.5, "P4-Q2", "使用視覺", "溝通：結構視覺化")
        else: update_axes(-0.5, -0.5, "P4-Q2", "不使用", "溝通：口語流動")
        st.success("數據已記錄。")

# ==========================================
# Phase 5: 綜合分析報告 (新增矛盾檢測)
# ==========================================
elif step == "Phase 5. 綜合分析報告":
    st.title("📊 諮商專業取向分析報告")
    
    # 檢查是否有數據
    if len(st.session_state.raw_scores_x) == 0:
        st.error("⚠️ 尚未偵測到作答數據。請回到各階段完成題目並點擊「確認按鈕」。")
        st.stop()

    x = st.session_state.axis_obj_sub
    y = st.session_state.axis_ana_exp

    # --- 1. 矛盾與亂答檢測 (Consistency Check) ---
    st.markdown("---")
    st.subheader("1. 資料品質檢測 (Consistency Check)")
    
    # 計算變異數 (Variance)
    var_x = np.var(st.session_state.raw_scores_x) if len(st.session_state.raw_scores_x) > 1 else 0
    var_y = np.var(st.session_state.raw_scores_y) if len(st.session_state.raw_scores_y) > 1 else 0
    total_variance = var_x + var_y
    
    # 判斷邏輯
    is_inconsistent = total_variance > 3.5 # 設定一個閾值，變異過大代表忽左忽右
    is_random = (abs(x) < 2 and abs(y) < 2) and total_variance > 5.0 # 分數抵消至原點且變異極大 -> 亂答
    
    if is_random:
        st.error("⚠️ **作答有效性警示**：系統偵測到您的作答模式存在高度隨機性。")
        st.markdown("您的選項在不同階段互相高度牴觸，導致結果相互抵消。這可能源於：\n1. 隨機填答。\n2. 對題目理解尚有落差。\n**建議您重新靜心施測，以獲取準確評估。**")
    elif is_inconsistent:
        st.warning("⚠️ **整合性提示**：系統偵測到您的諮商風格具有「高度彈性」或「內在衝突」。")
        st.markdown("您在某些情境非常客觀，在其他情境又極度主觀。這顯示您可能正在發展一種**折衷/整合 (Eclectic/Integrative)** 的取向，或者您在不同學派間仍在擺盪。這是一個值得在督導中討論的議題。")
    else:
        st.success("✅ **作答一致性檢核通過**：您的作答風格穩定，顯示出清晰的理論傾向。")

    # --- 2. 理論地圖 ---
    st.header("2. 理論地圖定位")
    
    source = pd.DataFrame({'X': [x], 'Y': [y], 'Label': ['您的位置']})
    
    # 定義象限文字
    quadrants = pd.DataFrame({
        'x': [8, -8, -8, 8],
        'y': [8, 8, -8, -8],
        'text': ['I. 認知行為\n(客觀/理性)', 'II. 心理動力\n(主觀/理性)', 'III. 人本體驗\n(主觀/感性)', 'IV. 系統策略\n(客觀/行動)']
    })

    # 繪圖
    base = alt.Chart(source).encode(
        x=alt.X('X', scale=alt.Scale(domain=[-20, 20]), title='主觀建構 <---> 客觀實證'),
        y=alt.Y('Y', scale=alt.Scale(domain=[-20, 20]), title='情感體驗 <---> 理性分析')
    )
    
    # 十字線
    rules = alt.Chart(pd.DataFrame({'x': [0], 'y': [0]})).mark_rule(color='gray', strokeDash=[4,4]).encode(x='x', y='y')
    
    # 象限標籤
    text = alt.Chart(quadrants).mark_text(fontSize=16, color='#95a5a6').encode(x='x', y='y', text='text')
    
    # 您的落點
    points = base.mark_circle(size=500, color='#e74c3c').encode(tooltip=['Label', 'X', 'Y'])
    
    st.altair_chart((text + rules + points).properties(width=700, height=600).interactive(), use_container_width=True)

    # --- 3. 六大取向參照 ---
    st.header("3. 六大諮商取向參照")
    st.markdown("""
    依據您的座標，請參考以下最接近的學派方向：
    
    * **↗️ 第一象限 (認知行為 CBT/REBT)**：相信問題源於錯誤認知，需透過理性證據與行為練習來修正。
    * **↖️ 第二象限 (心理動力 Psychodynamic)**：相信問題源於潛意識衝突，需透過理性洞察與移情分析來修通。
    * **↙️ 第三象限 (人本/體驗/完形)**：相信關係與覺察即治療，重視此時此刻的情感接觸與真誠一致。
    * **↘️ 第四象限 (系統/策略/現實)**：重視互動模式與具體行動計畫，較少探索深層情感，強調問題解決。
    * **⬅️ 左側中軸 (後現代/敘事)**：介於分析與體驗之間，強調語言建構、故事重寫與去病理化。
    * **⬇️ 下方中軸 (表達性藝術)**：介於主客觀之間，強調非語言的創作歷程與身心體驗。
    """)

    # --- 4. 脈絡化分析 ---
    st.header("4. 個人化脈絡分析")
    st.write("以下是系統根據您各階段選擇所生成的整合分析：")
    
    if len(st.session_state.history) > 0:
        for item in st.session_state.history:
            st.markdown(f"**【{item['phase']}】** {item['choice']}")
            st.caption(f"💡 分析：{item['reasoning']}")
