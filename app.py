import streamlit as st
import pandas as pd
import altair as alt

# --- 系統設定 ---
st.set_page_config(page_title="諮商專業取向深度探索系統 (CTOS-Pro)", page_icon="🧭", layout="wide")

# --- Session State 初始化 ---
if 'axis_obj_sub' not in st.session_state:
    st.session_state.axis_obj_sub = 0.0  # X軸: 客觀(正) vs 主觀(負)
if 'axis_ana_exp' not in st.session_state:
    st.session_state.axis_ana_exp = 0.0  # Y軸: 理性(正) vs 體驗(負)
if 'history' not in st.session_state:
    st.session_state.history = [] # 記錄作答歷程用以生成報告

# --- 輔助函數 ---
def update_axes(x_delta, y_delta, phase, choice_text, reasoning):
    st.session_state.axis_obj_sub += x_delta
    st.session_state.axis_ana_exp += y_delta
    # 記錄詳細歷程供最後分析使用
    st.session_state.history.append({
        "phase": phase,
        "choice": choice_text,
        "reasoning": reasoning
    })

# --- CSS 樣式 (學術風格) ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; font-weight: 600; color: #2c3e50; }
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
    .question-header { font-size: 18px; font-weight: bold; margin-top: 15px; color: #444; }
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
# 前言：方法論與架構
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
# Phase 1: 隱喻投射
# ==========================================
elif step == "Phase 1. 隱喻投射 (角色觀)":
    st.header("Phase 1: 治療關係中的角色隱喻")
    st.markdown("本階段透過圖像隱喻，探索您對於「治療師－個案」關係的原型想像。")
    
    # --- Q1: 登山隱喻 ---
    st.markdown("#### Q1. 若將諮商歷程比喻為一次登山，請觀察下列圖像，您認為自己的功能最接近哪一種角色？")
    
    # 圖片統一為橫式，風格一致
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1526772662000-3f88f10405ff?w=400", caption="A")
    with c2:
        st.image("https://images.unsplash.com/photo-1465311440653-ba9b1d9b0f5b?w=400", caption="B")
    
    c3, c4 = st.columns(2)
    with c3:
        # 更換為橫式圖片：使用望遠鏡觀察
        st.image("https://images.unsplash.com/photo-1516214104703-d870798883c5?w=400", caption="C")
    with c4:
        st.image("https://images.unsplash.com/photo-1522163182402-834f871fd851?w=400", caption="D")

    # 去除括號內的說明，避免誘導
    choice1 = st.radio("請選擇最貼近的角色原型：", [
        "A. 嚮導 (Guide)：熟悉地圖與地形，能預告潛在危險並規劃安全路徑。",
        "B. 伴侶 (Partner)：配合對方的速度並肩同行，共同經歷旅程的風雨。",
        "C. 觀察者 (Observer)：位於制高點或後方，保持視野，分析其步伐與慣性。",
        "D. 教練 (Coach)：在旁確保安全，指導手腳的施力點，協助發揮潛能。"
    ])
    
    if st.button("確認 Q1"):
        if "A" in choice1: update_axes(2.0, 1.0, "P1-Q1", choice1, "選擇嚮導：傾向客觀指導與結構")
        if "B" in choice1: update_axes(-2.0, -2.0, "P1-Q1", choice1, "選擇伴侶：傾向主觀體驗與連結")
        if "C" in choice1: update_axes(-1.0, 3.0, "P1-Q1", choice1, "選擇觀察者：傾向內在動力分析")
        if "D" in choice1: update_axes(2.0, 2.0, "P1-Q1", choice1, "選擇教練：傾向理性調整與行動")
        st.success("已記錄數據。")

    st.markdown("---")

    # --- Q2: 魔法工具 ---
    st.markdown("#### Q2. 承上題，若您能擁有一項「核心工具」來協助個案，您的直覺首選為何？")
    
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.info("🔦 手電筒")
        st.caption("照亮黑暗，看見盲點")
    with t2:
        st.info("🧣 毛毯")
        st.caption("提供溫暖，涵容情緒")
    with t3:
        st.info("🪞 鏡子")
        st.caption("如實反映，不加扭曲")
    with t4:
        st.info("🧭 指南針")
        st.caption("指引方向，導正路徑")

    choice_tool = st.radio("請選擇您的核心工具：", ["手電筒", "毛毯", "鏡子", "指南針"])

    if st.button("確認 Q2"):
        if choice_tool == "手電筒":
            update_axes(-1.0, 2.5, "P1-Q2", choice_tool, "選擇手電筒：傾向探索潛意識與洞察")
        elif choice_tool == "毛毯":
            update_axes(-2.0, -1.5, "P1-Q2", choice_tool, "選擇毛毯：傾向提供矯正性情緒經驗")
        elif choice_tool == "鏡子":
            update_axes(-1.0, -1.0, "P1-Q2", choice_tool, "選擇鏡子：傾向真誠一致與現象學反映")
        elif choice_tool == "指南針":
            update_axes(2.0, 1.5, "P1-Q2", choice_tool, "選擇指南針：傾向解決導向與目標設定")
        st.success("已記錄數據。")

# ==========================================
# Phase 2: 臨床決策
# ==========================================
elif step == "Phase 2. 臨床決策 (改變觀)":
    st.header("Phase 2: 改變機制的觀點")
    st.markdown("本階段模擬臨床情境，測量您對於「改變如何發生」的內隱假設。")
    
    # --- 情境 1: 自我否定 ---
    st.markdown('<div class="scenario-box"><b>情境 1：自我否定</b><br>個案低著頭，語氣顫抖地說：「我覺得……我這輩子就是個失敗品，不管怎麼努力最後都會搞砸……」</div>', unsafe_allow_html=True)
    
    q1 = st.radio("針對此段陳述，您當下的介入焦點為何？", [
        "1. 檢視證據：「你是依據什麼具體事件或證據，來定義自己是『失敗品』的？」",
        "2. 情感反映：「聽起來你現在真的感到很挫折，那種感覺像是被徹底打敗了……」",
        "3. 連結過去：「這句話讓你聯想到過去誰對你的評價嗎？或是誰曾經這樣對你說？」",
        "4. 尋找例外：「在過去這段時間裡，有沒有哪個時刻，事情其實沒有搞砸得那麼嚴重？」"
    ], key="s2_q1")
    
    st.markdown("---")
    
    # --- 情境 2: 沈默僵局 ---
    st.markdown('<div class="scenario-box"><b>情境 2：沈默僵局</b><br>個案已經沈默了將近十分鐘。他看著窗外，似乎沒有要開口的意思。治療室的空氣變得有些凝重。</div>', unsafe_allow_html=True)
    
    q2 = st.radio("面對此僵局，您內心的假設與處置方向為何？", [
        "1. 抗拒分析：他可能在抗拒某些痛苦的素材，我應思考這份沈默背後的潛意識意義。",
        "2. 結構引導：我需要做點什麼來打破僵局，例如回顧一下上次的作業或設定今天議程。",
        "3. 臨在陪伴：這份沈默是珍貴的，他正在整理自己，我只需安靜陪伴，提供安全的空間。",
        "4. 過程溝通：沈默本身就是一種溝通，我應該詢問：「透過沈默，你似乎想告訴我些什麼？」"
    ], key="s2_q2")

    st.markdown("---")

    # --- 情境 3: 衝突與生氣 ---
    st.markdown('<div class="scenario-box"><b>情境 3：治療關係破裂</b><br>個案突然對你生氣：「你一直問我感受有什麼用？這對解決我的現實問題一點幫助都沒有！」</div>', unsafe_allow_html=True)
    
    q3 = st.radio("面對個案的質疑，您的首要回應策略是？", [
        "1. 合作對話：「謝謝你告訴我，看來我們對於『什麼有幫助』的想法不太一樣，我們要不要來討論一下？」",
        "2. 同理接納：「我看見你真的很著急，你很希望能快點好起來，而我的提問讓你感到挫折，是嗎？」",
        "3. 移情探索：「你現在對我的生氣，是不是很像你平常對父親感覺到的那種無力感？」",
        "4. 行動修正：「好，那我們現在來調整方向，看看具體來說我們可以做哪些行為改變。」"
    ], key="s2_q3")
    
    if st.button("確認 Phase 2 所有回答"):
        # 移除所有學派標籤，僅保留後台計分邏輯
        # Q1 計分
        if "1." in q1: update_axes(1.5, 1.5, "P2-Q1", "檢視證據", "介入焦點：理性與證據")
        if "2." in q1: update_axes(-1.5, -1.5, "P2-Q1", "情感反映", "介入焦點：情感體驗")
        if "3." in q1: update_axes(-1.0, 2.0, "P2-Q1", "連結過去", "介入焦點：分析與動力")
        if "4." in q1: update_axes(1.0, 1.0, "P2-Q1", "尋找例外", "介入焦點：行動與建構")
        
        # Q2 計分
        if "1." in q2: update_axes(-1.0, 2.0, "P2-Q2", "抗拒分析", "僵局處理：分析視角")
        if "2." in q2: update_axes(2.0, 1.0, "P2-Q2", "結構引導", "僵局處理：結構介入")
        if "3." in q2: update_axes(-2.0, -2.0, "P2-Q2", "臨在陪伴", "僵局處理：人本視角")
        if "4." in q2: update_axes(-1.0, 1.0, "P2-Q2", "過程溝通", "僵局處理：系統/溝通視角")

        # Q3 計分
        if "1." in q3: update_axes(-1.0, 1.0, "P2-Q3", "合作對話", "衝突處理：後現代合作")
        if "2." in q3: update_axes(-2.0, -1.0, "P2-Q3", "同理接納", "衝突處理：人本同理")
        if "3." in q3: update_axes(-1.0, 3.0, "P2-Q3", "移情探索", "衝突處理：動力詮釋")
        if "4." in q3: update_axes(2.0, 2.0, "P2-Q3", "行動修正", "衝突處理：行為調整")
        
        st.success("Phase 2 數據已記錄。")

# ==========================================
# Phase 3: 陰影探索 (擴充)
# ==========================================
elif step == "Phase 3. 陰影探索 (價值觀)":
    st.header("Phase 3: 陰影與反移情")
    st.markdown("依據榮格心理學，我們所強烈排斥的特質（陰影），往往反映了我們潛意識中對於特定治療價值的堅持。")
    
    # --- Q1: 治療師特質 ---
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
    
    st.markdown("---")

    # --- Q2: 治療歷程的僵局 (新增) ---
    st.subheader("Q2. 治療歷程的恐懼")
    st.write("在諮商過程中，哪一種「狀態」最讓您感到焦慮或自我懷疑？")
    
    process_fear = st.radio("請選擇讓您最焦慮的狀態：", [
        "1. 混亂無序：個案話題跳躍，情緒張力極大，我完全抓不到重點，覺得場面快要失控。",
        "2. 表層疏離：個案很有禮貌地配合，但感覺我們之間隔著一層厚厚的牆，無法接觸真實情感。",
        "3. 理智化：個案不斷地分析自己，說得頭頭是道，但完全沒有任何行為上的改變。",
        "4. 依賴退化：個案完全依賴我的建議，像個孩子一樣不願為自己負責，等待我去拯救他。"
    ])

    if st.button("確認 Phase 3 所有回答"):
        # Q1 分析
        if shadow_1 != "請選擇..." and shadow_2 != "請選擇..." and shadow_1 != shadow_2:
             def analyze_shadow(text, weight):
                if "失控" in text: update_axes(1.5 * weight, 0, "P3-Q1", "怕失控", f"陰影反映：對結構與界線的需求 (w={weight})")
                if "冷血" in text: update_axes(-1.5 * weight, -1.0 * weight, "P3-Q1", "怕冷血", f"陰影反映：對情感與人性的需求 (w={weight})")
                if "鬼打牆" in text: update_axes(1.0 * weight, 1.5 * weight, "P3-Q1", "怕沒效", f"陰影反映：對效能與改變的需求 (w={weight})")
                if "霸道" in text: update_axes(-1.5 * weight, 0, "P3-Q1", "怕霸道", f"陰影反映：對尊重與主體性的需求 (w={weight})")
             analyze_shadow(shadow_1, 1.5)
             analyze_shadow(shadow_2, 1.0)
        else:
             st.error("Q1 選擇有誤，請檢查。")

        # Q2 分析 (新增)
        # 怕混亂 -> 渴望結構 (CBT/Structual)
        if "1." in process_fear: update_axes(1.5, 0.5, "P3-Q2", "怕混亂", "恐懼反映：渴望結構與秩序")
        # 怕疏離 -> 渴望接觸 (Humanistic/Exp)
        if "2." in process_fear: update_axes(-1.5, -1.5, "P3-Q2", "怕疏離", "恐懼反映：渴望真誠接觸")
        # 怕理智化 -> 渴望體驗 (Experiential/Gestalt) OR 行動 (Behavioral) -> 這裡取渴望體驗
        if "3." in process_fear: update_axes(0, -2.0, "P3-Q2", "怕理智化", "恐懼反映：渴望情感流動")
        # 怕依賴 -> 渴望個案獨立/賦能 (PostModern/CBT)
        if "4." in process_fear: update_axes(-1.0, 1.0, "P3-Q2", "怕依賴", "恐懼反映：渴望個案賦能")

        st.success("Phase 3 數據已記錄。")

# ==========================================
# Phase 4: 空間配置 (情境轉化)
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

    # 定義 SVG (更新版)
    def get_layout_svg(layout_type):
        base_svg = '<svg width="250" height="180" xmlns="http://www.w3.org/2000/svg" style="background-color:#ffffff; border:1px solid #eee;">'
        
        if layout_type == "SideBySide":
            # 並肩坐在沙發上
            content = """
            <rect x="50" y="80" width="150" height="50" rx="10" fill="#f1c40f" opacity="0.3"/>
            <circle cx="100" cy="105" r="20" fill="#3498db" /> <text x="90" y="110" fill="white" font-size="10">You</text>
            <circle cx="150" cy="105" r="20" fill="#e74c3c" /> <text x="140" y="110" fill="white" font-size="10">Friend</text>
            <text x="75" y="160" fill="#666" font-size="12">並肩而坐 (沙發)</text>
            """
        elif layout_type == "L_Shape":
            # 舒適斜角
            content = """
            <rect x="120" y="90" width="40" height="40" fill="#ecf0f1" stroke="#bdc3c7"/>
            <circle cx="90" cy="70" r="20" fill="#3498db" /> <text x="80" y="75" fill="white" font-size="10">You</text>
            <circle cx="160" cy="140" r="20" fill="#e74c3c" /> <text x="150" y="145" fill="white" font-size="10">Friend</text>
            <text x="150" y="40" fill="#666" font-size="12">舒適斜角 (L型)</text>
            """
        elif layout_type == "Formal":
            # 正式對坐
            content = """
            <rect x="105" y="40" width="40" height="100" fill="#ecf0f1" stroke="#bdc3c7"/>
            <circle cx="60" cy="90" r="20" fill="#3498db" /> <text x="50" y="95" fill="white" font-size="10">You</text>
            <circle cx="190" cy="90" r="20" fill="#e74c3c" /> <text x="180" y="95" fill="white" font-size="10">Friend</text>
            <text x="90" y="25" fill="#666" font-size="12">面對面 (隔著桌子)</text>
            """
        elif layout_type == "Separate":
            # 獨立單人椅 (取代躺椅)
            content = """
            <circle cx="50" cy="90" r="20" fill="#3498db" /> <text x="40" y="95" fill="white" font-size="10">You</text>
            <circle cx="200" cy="90" r="20" fill="#e74c3c" /> <text x="190" y="95" fill="white" font-size="10">Friend</text>
            <path d="M 80 90 L 170 90" stroke="#999" stroke-width="1" stroke-dasharray="4"/>
            <text x="85" y="150" fill="#666" font-size="12">獨立座椅 (保持距離)</text>
            """
        return base_svg + content + '</svg>'

    # 顯示選項
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(get_layout_svg("SideBySide"), unsafe_allow_html=True)
        if st.button("1. 並肩而坐 (沙發)：無阻隔，身體方向一致，感覺親密且支持。"):
            update_axes(-2.0, -1.5, "P4-Q1", "並肩", "空間偏好：高親密與體驗")
            st.success("已選擇：並肩而坐")
            
        st.markdown(get_layout_svg("L_Shape"), unsafe_allow_html=True)
        if st.button("2. 舒適斜角 (L型)：有各自空間但容易眼神接觸，放鬆且自然。"):
            update_axes(-0.5, 0, "P4-Q1", "L型", "空間偏好：人本/折衷平衡")
            st.success("已選擇：舒適斜角")

    with col2:
        st.markdown(get_layout_svg("Formal"), unsafe_allow_html=True)
        if st.button("3. 面對面 (隔桌)：可以看清對方表情，但有物體作為界線，感覺清晰。"):
            update_axes(1.5, 1.0, "P4-Q1", "對坐", "空間偏好：高結構與認知")
            st.success("已選擇：面對面")
            
        st.markdown(get_layout_svg("Separate"), unsafe_allow_html=True)
        if st.button("4. 獨立座椅 (距離)：兩張單人椅，中間留有空間，保持彼此的獨立性。"):
            update_axes(1.0, 2.0, "P4-Q1", "獨立椅", "空間偏好：高界線與觀察")
            st.success("已選擇：獨立座椅")

    st.markdown("---")
    
    # Q2 優化：具體化情境
    st.subheader("Q2. 輔助溝通偏好")
    st.write("在對話過程中，為了讓對方更清楚您的想法，您是否傾向**拿出一張紙或白板，畫圖/寫字**來解釋？")
    
    use_visual = st.radio("您的直覺習慣：", [
        "是，我喜歡將概念視覺化，畫出關聯圖或條列重點，這樣比較清楚。",
        "否，我傾向用語言描述或譬喻，直接的眼神與情感交流更重要。"
    ])
    
    if st.button("確認 Q2"):
        if "是" in use_visual:
            update_axes(1.5, 1.5, "P4-Q2", "使用視覺輔助", "溝通偏好：結構化與視覺化")
        else:
            update_axes(-0.5, -0.5, "P4-Q2", "不使用輔助", "溝通偏好：口語流動")
        st.success("已記錄數據。")

# ==========================================
# Phase 5: 綜合分析報告
# ==========================================
elif step == "Phase 5. 綜合分析報告":
    st.title("📊 諮商專業取向分析報告")
    st.markdown("---")
    
    x = st.session_state.axis_obj_sub
    y = st.session_state.axis_ana_exp
    
    # 1. 理論地圖 (Static Chart)
    st.header("1. 理論地圖定位 (Theoretical Mapping)")
    st.write("下圖呈現您在知識論立場 (X軸) 與 介入焦點 (Y軸) 上的落點。")
    
    source = pd.DataFrame({
        'X': [x], 
        'Y': [y], 
        'Label': ['您的位置']
    })
    
    # 背景象限文字
    quadrant_text = pd.DataFrame({
        'x': [5, -5, -5, 5],
        'y': [5, 5, -5, -5],
        'text': ['第一象限\n客觀/理性\n(CBT/行為)', '第二象限\n主觀/理性\n(動力/分析)', '第三象限\n主觀/體驗\n(人本/存在)', '第四象限\n客觀/體驗\n(系統/策略)']
    })

    # 主圖表 (靜態)
    base = alt.Chart(source).encode(
        x=alt.X('X', scale=alt.Scale(domain=[-15, 15]), title='主觀建構 (Subjective) <-----------------> 客觀實證 (Objective)'),
        y=alt.Y('Y', scale=alt.Scale(domain=[-15, 15]), title='情感體驗 (Experiential) <-----------------> 理性分析 (Analytical)')
    )

    # 繪製十字線
    rules = alt.Chart(pd.DataFrame({'x': [0], 'y': [0]})).mark_rule(color='gray', strokeDash=[3,3]).encode(
        x='x', y='y'
    )
    
    # 繪製象限文字
    text_labels = alt.Chart(quadrant_text).mark_text(
        align='center', baseline='middle', dx=0, dy=0, fontSize=14, color='#bdc3c7'
    ).encode(x='x', y='y', text='text')

    # 繪製使用者落點
    points = base.mark_circle(size=400, color='#c0392b', opacity=1).encode(tooltip=['Label', 'X', 'Y'])

    final_chart = (text_labels + rules + points).properties(
        width=700, height=600, title="諮商取向座標圖"
    ).interactive(bind_y=False, bind_x=False) # 禁止滾動

    st.altair_chart(final_chart, use_container_width=True)

    # 2. 六大取向參照
    st.header("2. 六大諮商取向參照")
    st.markdown("""
    諮商學派繁多，但依據您的座標位置，可以主要參考以下六大方向的相對位置，找到學習的起點：
    
    * **認知行為取向 (CBT/REBT)**：落在 **第一象限 (右上)**。強調思考模式的修正與具體行為的改變。
    * **心理動力取向 (Psychodynamic)**：落在 **第二象限 (左上)**。強調對潛意識、過去經驗與移情的理性洞察。
    * **人本/存在/完形 (Humanistic/Existential)**：落在 **第三象限 (左下)**。強調此時此刻的真誠關係、情感體驗與人的主體性。
    * **系統/策略取向 (Systemic/Strategic)**：落在 **第四象限 (右下)**。強調人際互動模式的觀察與具體的行動介入，較少關注內在情感。
    * **後現代取向 (Post-Modern/Narrative)**：通常落在 **X軸左側 (主觀)**，介於分析與體驗之間。強調語言、社會建構與故事重寫。
    * **表達性藝術治療 (Expressive Arts)**：通常落在 **Y軸下方 (體驗)**，可跨越主客觀。強調非語言的媒材運用與歷程體驗。
    """)

    # 3. 個人化脈絡分析
    st.header("3. 個人化脈絡分析 (Contextual Analysis)")
    st.markdown("以下分析基於您在各階段的具體選擇，協助您理解結果背後的脈絡：")
    
    if len(st.session_state.history) > 0:
        for item in st.session_state.history:
            st.markdown(f"**【{item['phase']}】** 您選擇了「{item['choice']}」")
            st.caption(f"👉 系統解讀：{item['reasoning']}")
    else:
        st.warning("⚠️ 系統尚未偵測到您的作答紀錄。請確認您在每一階段都有點擊「確認按鈕」。")

    st.markdown("---")
    st.info("💡 **給您的建議**：此結果僅是一個起點。請試著閱讀距離您落點最近的兩個學派之相關文獻，感受哪一種語言讓您讀起來最「像自己」。")
