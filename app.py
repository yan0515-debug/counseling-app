import streamlit as st
import pandas as pd
import altair as alt

# --- 系統設定 ---
st.set_page_config(page_title="諮商專業取向深度探索系統 v4.0", page_icon="🧭", layout="wide")

# --- Session State 初始化 ---
if 'axis_obj_sub' not in st.session_state:
    st.session_state.axis_obj_sub = 0.0 
if 'axis_ana_exp' not in st.session_state:
    st.session_state.axis_ana_exp = 0.0
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 輔助函數 ---
def update_axes(x_delta, y_delta, reasoning):
    st.session_state.axis_obj_sub += x_delta
    st.session_state.axis_ana_exp += y_delta
    st.session_state.history.append(reasoning)

# --- CSS 樣式 ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; font-weight: bold; color: #2c3e50; }
    .scenario-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #4a90e2; margin-bottom: 20px;}
    .question-header { font-size: 18px; font-weight: bold; margin-top: 10px; color: #444; }
</style>
""", unsafe_allow_html=True)

# --- 側邊欄 ---
st.sidebar.title("🧭 專業導航")
step = st.sidebar.radio(
    "階段選擇：",
    ["前言：理論架構", "1. 隱喻投射 (角色觀)", "2. 臨床決策 (改變觀)", "3. 陰影探索 (價值觀)", "4. 空間配置 (框架觀)", "5. 綜合分析報告"]
)

# ==========================================
# 前言
# ==========================================
if step == "前言：理論架構":
    st.title("諮商專業取向深度探索系統 v4.0")
    st.markdown("### 歡迎來到您的專業探索旅程")
    st.info("本系統依據 CTPS 雙軸向理論，透過隱喻、情境模擬與空間心理學，協助您定位自己的治療風格。")

# ==========================================
# 階段 1: 隱喻投射 (修復圖片 + 新增題目)
# ==========================================
elif step == "1. 隱喻投射 (角色觀)":
    st.header("Phase 1: 治療關係中的角色")
    
    # --- Q1: 登山隱喻 ---
    st.markdown("#### Q1. 如果諮商是一次登山，看著下方的示意圖，您覺得自己最像哪一種角色？")
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1526772662000-3f88f10405ff?w=400", caption="A. 拿著地圖指引方向")
    with c2:
        st.image("https://images.unsplash.com/photo-1465311440653-ba9b1d9b0f5b?w=400", caption="B. 互相扶持並肩同行")
    
    c3, c4 = st.columns(2)
    with c3:
        # 修復：更換為一張更穩定的「眺望/觀察」圖片
        st.image("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=400", caption="C. 在高處觀察全貌")
    with c4:
        st.image("https://images.unsplash.com/photo-1522163182402-834f871fd851?w=400", caption="D. 確保安全的攀岩教練")

    choice1 = st.radio("請選擇您的角色：", [
        "A. 嚮導 (Guide)：我熟悉地圖，能預告危險並規劃安全路徑。(傾向指導)",
        "B. 伴侶 (Partner)：我配合他的速度，陪伴他經歷這段旅程。(傾向體驗)",
        "C. 觀察者 (Observer)：我保持視野，分析他走路的姿勢與慣性。(傾向分析)",
        "D. 教練 (Coach)：我確保安全，指導他手腳的施力點。(傾向理性)"
    ])
    
    if st.button("確認 Q1"):
        if "A" in choice1: update_axes(2.0, 1.0, "角色-嚮導: 客觀指導")
        if "B" in choice1: update_axes(-2.0, -2.0, "角色-伴侶: 主觀體驗")
        if "C" in choice1: update_axes(-1.0, 3.0, "角色-觀察者: 動力分析")
        if "D" in choice1: update_axes(2.0, 2.0, "角色-教練: 理性調整")
        st.success("Q1 已記錄。")

    st.markdown("---")

    # --- Q2: 新增題目 (治療法器) ---
    st.markdown("#### Q2. 如果您可以擁有一樣「魔法工具」來幫助個案，那會是什麼？")
    st.caption("這反映了您潛意識中認為「什麼才是對個案最有幫助的」。")

    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.info("🔦 手電筒")
        st.write("照亮黑暗角落，看見未知的盲點。")
    with t2:
        st.info("🧣 毛毯")
        st.write("提供溫暖與包容，讓他在安全中療癒。")
    with t3:
        st.info("🪞 鏡子")
        st.write("如實反映他的樣子，不加扭曲。")
    with t4:
        st.info("🧭 指南針")
        st.write("提供正確的方向，讓他不再迷路。")

    choice_tool = st.radio("請選擇您的魔法工具：", ["手電筒", "毛毯", "鏡子", "指南針"])

    if st.button("確認 Q2"):
        if choice_tool == "手電筒":
            update_axes(-1.0, 2.5, "工具-手電筒: 探索潛意識 (分析)")
        elif choice_tool == "毛毯":
            update_axes(-2.0, -1.5, "工具-毛毯: 提供涵容 (體驗/人本)")
        elif choice_tool == "鏡子":
            update_axes(-1.0, -1.0, "工具-鏡子: 真誠一致 (人本/完形)")
        elif choice_tool == "指南針":
            update_axes(2.0, 1.5, "工具-指南針: 解決導向 (CBT/SFBT)")
        st.success("Q2 已記錄。")

    st.markdown("---")

    # --- Q3: 校準題 ---
    st.markdown("### Q3. 請評估以下信念：")
    st.markdown("""
    <div style="font-size: 24px; font-weight: bold; padding: 15px; border: 2px dashed #aaa; border-radius: 10px; text-align: center; margin-bottom: 20px;">
    「我認為治療師保持客觀中立的『技術專家』形象，<br>比展現個人特質更重要。」
    </div>
    """, unsafe_allow_html=True)
    
    q3_score = st.slider("1 (非常不同意) <---> 5 (非常同意)", 1, 5, 3)
    
    if st.button("確認 Q3"):
        val = q3_score - 3
        update_axes(val * 1.5, 0, f"校準題-專家形象: {q3_score}分")
        st.success("校準完成。")

# ==========================================
# 階段 2: 臨床決策 (保持原樣)
# ==========================================
elif step == "2. 臨床決策 (改變觀)":
    st.header("Phase 2: 改變是如何發生的？")
    st.info("本階段包含三個情境，請憑直覺作答。")
    
    # (此處省略中間代碼，請直接保留您上一版 Phase 2 的完整內容，因為您說這部分很棒)
    # 為節省篇幅，這裡只需複製貼上上一版的 Phase 2 程式碼即可
    # --- 情境 1: 自我否定 ---
    st.markdown('<div class="scenario-box"><b>情境 1：自我否定</b><br>個案低著頭，雙手抓緊膝蓋，顫抖地說：「我覺得……我這輩子就是個失敗品，不管怎麼努力都會搞砸……」</div>', unsafe_allow_html=True)
    q1 = st.radio("你的直覺回應是？", ["1. 「你是依據什麼證據來定義自己是『失敗品』的？」(檢視證據)", "2. 「聽起來你現在真的好挫折，那種感覺像是被徹底打敗了……」(情感反映)", "3. 「這句話讓你聯想到過去誰對你的評價嗎？」(連結過去)", "4. 「有沒有哪個時刻，事情其實沒有搞砸得那麼嚴重？」(尋找例外)"], key="s2_q1")
    st.markdown("---")
    # --- 情境 2: 沈默僵局 ---
    st.markdown('<div class="scenario-box"><b>情境 2：沈默僵局</b><br>個案已經沈默了十分鐘。他看著窗外，似乎沒有要開口的意思。氣氛變得有些凝重。</div>', unsafe_allow_html=True)
    q2 = st.radio("你當下內心的假設是？", ["1. 他可能在抗拒什麼，我應該思考這份沈默背後的潛意識意義。(動力分析)", "2. 我需要做點什麼來打破僵局，也許回顧一下上次的作業或設定今天議程。(結構引導)", "3. 這份沈默是珍貴的，他正在整理自己，我只要安靜陪伴就好。(人本存在)", "4. 沈默也是一種溝通，他在透過沈默告訴我什麼？(系統/溝通)"], key="s2_q2")
    st.markdown("---")
    # --- 情境 3: 衝突與生氣 ---
    st.markdown('<div class="scenario-box"><b>情境 3：衝突</b><br>個案突然對你生氣：「你一直問我感受有什麼用？這對解決我的問題一點幫助都沒有！」</div>', unsafe_allow_html=True)
    q3 = st.radio("你最想採取的策略是？", ["1. 承認這份落差：「謝謝你告訴我，看來我們對於『什麼有幫助』的想法不太一樣，我們要不要來討論一下？」(後現代/合作)", "2. 接納情緒：「我看見你真的很著急，你很希望能快點好起來，是嗎？」(人本/同理)", "3. 探索移情：「你現在對我的生氣，是不是很像你平常對你父親感覺到的挫折？」(動力/移情)", "4. 修正方向：「好，那我們現在來看看，具體來說我們可以做哪些行為改變。」(CBT/焦點)"], key="s2_q3")
    
    if st.button("提交所有決策"):
        if "1." in q1: update_axes(1.5, 1.5, "S1-證據: 理性")
        if "2." in q1: update_axes(-1.5, -1.5, "S1-反映: 體驗")
        if "3." in q1: update_axes(-1.0, 2.0, "S1-連結: 分析")
        if "4." in q1: update_axes(1.0, 1.0, "S1-例外: 行動")
        if "1." in q2: update_axes(-1.0, 2.0, "S2-抗拒: 分析")
        if "2." in q2: update_axes(2.0, 1.0, "S2-結構: 客觀")
        if "3." in q2: update_axes(-2.0, -2.0, "S2-陪伴: 體驗")
        if "4." in q2: update_axes(-1.0, 1.0, "S2-溝通: 系統")
        if "1." in q3: update_axes(-1.0, 1.0, "S3-合作: 系統")
        if "2." in q3: update_axes(-2.0, -1.0, "S3-同理: 體驗")
        if "3." in q3: update_axes(-1.0, 3.0, "S3-移情: 分析")
        if "4." in q3: update_axes(2.0, 2.0, "S3-行為: 理性")
        st.success("決策分析完畢。")

# ==========================================
# 階段 3: 陰影探索 (保持原樣)
# ==========================================
elif step == "3. 陰影探索 (價值觀)":
    st.header("Phase 3: 恐懼與避免")
    st.markdown("請選出您心中的「第一名」與「第二名」無法忍受的特質：")
    shadow_options = {
        "A": "失控的治療師：界線模糊，被個案的情緒捲進去，跟著個案一起哭，不知所措。",
        "B": "冷血的治療師：像個冰冷的分析機器，只有理論沒有溫度，完全感覺不到人性。",
        "C": "鬼打牆的治療師：談了很久卻毫無進展，沒有目標，每週只是來聊聊天，浪費時間。",
        "D": "霸道的治療師：自以為是專家，把自己的價值觀強加在個案身上，不聽個案解釋。"
    }
    shadow_1 = st.selectbox("💀 第一名最無法忍受（最像噩夢）的是：", ["請選擇..."] + list(shadow_options.values()))
    shadow_2 = st.selectbox("💀 第二名無法忍受的是：", ["請選擇..."] + list(shadow_options.values()))
    
    if st.button("分析陰影"):
        if shadow_1 == "請選擇..." or shadow_2 == "請選擇...":
            st.error("請完成兩項選擇。")
        elif shadow_1 == shadow_2:
            st.error("第一名與第二名不能相同。")
        else:
            def analyze_shadow(text, weight):
                if "失控" in text: update_axes(1.5 * weight, 0, f"陰影-怕失控(w={weight})")
                if "冷血" in text: update_axes(-1.5 * weight, -1.0 * weight, f"陰影-怕冷血(w={weight})")
                if "鬼打牆" in text: update_axes(1.0 * weight, 1.5 * weight, f"陰影-怕沒效(w={weight})")
                if "霸道" in text: update_axes(-1.5 * weight, 0, f"陰影-怕霸道(w={weight})")
            analyze_shadow(shadow_1, 1.5)
            analyze_shadow(shadow_2, 1.0)
            st.success("陰影價值觀分析完成。")

# ==========================================
# 階段 4: 空間配置 (SVG 修正與偏差消除)
# ==========================================
elif step == "4. 空間配置 (框架觀)":
    st.header("Phase 4: 物理環境與治療框架")
    
    # 策略調整：消除「考試標準答案」的偏差
    st.markdown("""
    <div style="background-color:#fff3cd; padding:15px; border-radius:10px; border-left: 5px solid #ffc107;">
    <b>🔥 破除框架挑戰：</b><br>
    我們知道在台灣的諮商訓練中，「L型座位」通常是標準配置。
    但請您現在<b>忘掉考試、忘掉督導的評價</b>。<br>
    <br>
    想像這是您私人的客廳，您邀請一位好朋友來進行一場<b>深入靈魂的對話</b>。
    為了讓<b>「您自己」</b>感到最自在、最能真誠交流，您身體直覺會想選哪一種坐法？
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 定義 SVG 繪圖 (修正 Layout)
    def get_layout_svg(layout_type):
        base_svg = '<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg" style="background-color:#f9f9f9; border:1px solid #ddd;">'
        
        if layout_type == "Intimate":
            # 親密
            content = """
            <circle cx="100" cy="100" r="25" fill="#3498db" /> <text x="90" y="105" fill="white" font-size="12">Th</text>
            <circle cx="200" cy="100" r="25" fill="#e74c3c" /> <text x="190" y="105" fill="white" font-size="12">Cl</text>
            <path d="M 125 100 L 175 100" stroke="#999" stroke-width="2" stroke-dasharray="4"/>
            <text x="110" y="150" fill="#666" font-size="12">膝蓋幾可相觸</text>
            """
        elif layout_type == "Social":
            # 舒適斜角 (修正座標，避免切到)
            # 將 Y 軸整體上移，Cl 的 cy 從 200 改為 160
            content = """
            <rect x="130" y="100" width="40" height="40" fill="#ecf0f1" stroke="#bdc3c7"/>
            <circle cx="100" cy="80" r="25" fill="#3498db" /> <text x="90" y="85" fill="white" font-size="12">Th</text>
            <circle cx="180" cy="160" r="25" fill="#e74c3c" /> <text x="170" y="165" fill="white" font-size="12">Cl</text>
            <text x="180" y="40" fill="#666" font-size="12">舒適斜角 (L型)</text>
            """
        elif layout_type == "Formal":
            # 正式
            content = """
            <rect x="130" y="50" width="40" height="100" fill="#ecf0f1" stroke="#bdc3c7"/>
            <circle cx="80" cy="100" r="25" fill="#3498db" /> <text x="70" y="105" fill="white" font-size="12">Th</text>
            <circle cx="220" cy="100" r="25" fill="#e74c3c" /> <text x="210" y="105" fill="white" font-size="12">Cl</text>
            <text x="120" y="30" fill="#666" font-size="12">桌子隔開</text>
            """
        elif layout_type == "Analytic":
            # 躺椅
            content = """
            <rect x="100" y="80" width="120" height="40" rx="10" fill="#e74c3c" /> <text x="140" y="105" fill="white" font-size="12">躺椅</text>
            <circle cx="250" cy="100" r="20" fill="#3498db" /> <text x="240" y="105" fill="white" font-size="10">Th</text>
            <text x="100" y="50" fill="#666" font-size="12">分析設置</text>
            """
        return base_svg + content + '</svg>'

    # 顯示選項
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(get_layout_svg("Intimate"), unsafe_allow_html=True)
        if st.button("A. 親密靠近 (無阻隔)"):
            update_axes(-2.0, -1.5, "空間-親密: 體驗優先")
            st.success("已選擇：親密靠近")
            
        st.markdown(get_layout_svg("Social"), unsafe_allow_html=True)
        if st.button("B. 舒適斜角 (L型)"):
            # 這裡的分數調整：雖然是標準答案，但如果是在「私密情境」下選的，代表他真的喜歡這種「有點黏又不會太黏」的人本/折衷距離
            update_axes(-0.5, 0, "空間-舒適: 人本/折衷")
            st.success("已選擇：舒適斜角")

    with col2:
        st.markdown(get_layout_svg("Formal"), unsafe_allow_html=True)
        if st.button("C. 正式對坐 (有桌子)"):
            update_axes(1.5, 1.0, "空間-正式: 教學/CBT")
            st.success("已選擇：正式對坐")
            
        st.markdown(get_layout_svg("Analytic"), unsafe_allow_html=True)
        if st.button("D. 躺椅設置 (在後方)"):
            update_axes(-1.0, 3.0, "空間-躺椅: 深度分析")
            st.success("已選擇：躺椅設置")

    st.markdown("---")
    whiteboard = st.checkbox("Q2. 我希望牆上有一塊大白板 (用途：教學/列點/畫結構圖)")
    if whiteboard:
        if st.button("確認白板"):
            update_axes(1.5, 1.5, "空間-白板: 重視結構")
            st.success("已記錄白板需求")

# ==========================================
# 階段 5: 綜合分析報告
# ==========================================
elif step == "5. 綜合分析報告":
    st.title("📊 諮商專業取向分析報告")
    
    x = st.session_state.axis_obj_sub
    y = st.session_state.axis_ana_exp
    
    st.subheader("1. 理論地圖定位")
    st.write(f"座標落點：X (客觀性) = {x:.1f}, Y (理性分析) = {y:.1f}")
    
    source = pd.DataFrame({'X': [x], 'Y': [y], 'Label': ['您的位置']})
    
    chart = alt.Chart(source).mark_circle(size=300, color='#e74c3c').encode(
        x=alt.X('X', scale=alt.Scale(domain=[-15, 15]), title='主觀/建構 <-----> 客觀/實證'),
        y=alt.Y('Y', scale=alt.Scale(domain=[-15, 15]), title='體驗/情感 <-----> 理性/思考'),
        tooltip=['Label', 'X', 'Y']
    ).interactive().properties(width=600, height=500)
    
    st.altair_chart(chart, use_container_width=True)
    
    st.subheader("2. 風格解析")
    if x >= 0 and y >= 0:
        st.success("【第一象限：認知與行為取向 (CBT/SFBT)】\n相信問題有客觀成因，可透過理性思考與練習來解決。")
    elif x < 0 and y >= 0:
        st.info("【第二象限：心理動力取向 (Psychodynamic)】\n相信透過對過去與潛意識的理性洞察 (Insight)，能帶來深層改變。")
    elif x < 0 and y < 0:
        st.warning("【第三象限：人本與體驗取向 (Humanistic/Gestalt)】\n相信關係與當下的情感體驗本身就是治療。")
    else:
        st.error("【第四象限：策略與系統取向 (Strategic/Systemic)】\n重視具體的改變行動，但關注個別化的主觀意義與溝通模式。")

    with st.expander("查看詳細判斷歷程"):
        for item in st.session_state.history:
            st.write(f"- {item}")
