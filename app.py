import streamlit as st
import pandas as pd
import altair as alt

# --- 系統設定 ---
st.set_page_config(page_title="諮商專業取向深度探索系統 v3.0", page_icon="🧭", layout="wide")

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

# --- CSS 樣式優化 ---
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
    st.title("諮商專業取向深度探索系統 v3.0")
    st.markdown("### 歡迎來到您的專業探索旅程")
    st.info("本系統依據 CTPS 雙軸向理論，透過隱喻、情境模擬與空間心理學，協助您定位自己的治療風格。")

# ==========================================
# 階段 1: 隱喻投射 (圖片風格統一)
# ==========================================
elif step == "1. 隱喻投射 (角色觀)":
    st.header("Phase 1: 治療關係中的角色")
    st.markdown("#### Q1. 如果諮商是一次登山，看著下方的示意圖，您覺得自己最像哪一種角色？")
    
    # 使用 Unsplash 圖片，風格統一為戶外/登山
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1526772662000-3f88f10405ff?w=400", caption="A. 拿著地圖指引方向")
    with c2:
        st.image("https://images.unsplash.com/photo-1465311440653-ba9b1d9b0f5b?w=400", caption="B. 互相扶持並肩同行")
    
    c3, c4 = st.columns(2)
    with c3:
        st.image("https://images.unsplash.com/photo-1518050212373-d1f50b2404b0?w=400", caption="C. 拿著望遠鏡觀察遠方")
    with c4:
        st.image("https://images.unsplash.com/photo-1522163182402-834f871fd851?w=400", caption="D. 確保安全的攀岩教練")

    choice1 = st.radio("請選擇您的角色：", [
        "A. 嚮導 (Guide)：我走在前面，熟悉地圖，能預告危險並規劃安全路徑。",
        "B. 伴侶 (Partner)：我走在旁邊，配合他的速度，陪伴他經歷這段旅程。",
        "C. 觀察者 (Observer)：我走在後方，保持視野，分析他走路的姿勢與慣性。",
        "D. 教練 (Coach)：我在旁確保安全，指導他手腳的施力點，發揮潛能。"
    ])
    
    if st.button("確認 Q1"):
        if "A" in choice1: update_axes(2.0, 1.0, "角色-嚮導: 傾向客觀指導")
        if "B" in choice1: update_axes(-2.0, -2.0, "角色-伴侶: 傾向主觀體驗")
        if "C" in choice1: update_axes(-1.0, 3.0, "角色-觀察者: 傾向動力分析")
        if "D" in choice1: update_axes(2.0, 2.0, "角色-教練: 傾向理性調整")
        st.success("角色傾向已記錄。")

    st.markdown("---")
    
    # 放大加粗的題目 (Markdown語法)
    st.markdown("### Q2. 請評估以下信念：")
    st.markdown("""
    <div style="font-size: 24px; font-weight: bold; padding: 15px; border: 2px dashed #aaa; border-radius: 10px; text-align: center; margin-bottom: 20px;">
    「我認為治療師保持客觀中立的『技術專家』形象，<br>比展現個人特質更重要。」
    </div>
    """, unsafe_allow_html=True)
    
    q2_score = st.slider("1 (非常不同意) <---> 5 (非常同意)", 1, 5, 3)
    
    if st.button("確認 Q2"):
        val = q2_score - 3
        update_axes(val * 1.5, 0, f"校準題-專家形象: {q2_score}分")
        st.success("校準完成。")

# ==========================================
# 階段 2: 臨床決策 (擴充為 3 題)
# ==========================================
elif step == "2. 臨床決策 (改變觀)":
    st.header("Phase 2: 改變是如何發生的？")
    st.info("本階段擴充為三個情境，以提升評估信度。請憑直覺作答。")
    
    # --- 情境 1: 自我否定 ---
    st.markdown('<div class="scenario-box"><b>情境 1：自我否定</b><br>個案低著頭，雙手抓緊膝蓋，顫抖地說：「我覺得……我這輩子就是個失敗品，不管怎麼努力都會搞砸……」</div>', unsafe_allow_html=True)
    
    q1 = st.radio("你的直覺回應是？", [
        "1. 「你是依據什麼證據來定義自己是『失敗品』的？」(檢視證據)",
        "2. 「聽起來你現在真的好挫折，那種感覺像是被徹底打敗了……」(情感反映)",
        "3. 「這句話讓你聯想到過去誰對你的評價嗎？」(連結過去)",
        "4. 「有沒有哪個時刻，事情其實沒有搞砸得那麼嚴重？」(尋找例外)"
    ], key="s2_q1")
    
    st.markdown("---")
    
    # --- 情境 2: 沈默僵局 ---
    st.markdown('<div class="scenario-box"><b>情境 2：沈默僵局</b><br>個案已經沈默了十分鐘。他看著窗外，似乎沒有要開口的意思。氣氛變得有些凝重。</div>', unsafe_allow_html=True)
    
    q2 = st.radio("你當下內心的假設是？", [
        "1. 他可能在抗拒什麼，我應該思考這份沈默背後的潛意識意義。(動力分析)",
        "2. 我需要做點什麼來打破僵局，也許回顧一下上次的作業或設定今天議程。(結構引導)",
        "3. 這份沈默是珍貴的，他正在整理自己，我只要安靜陪伴就好。(人本存在)",
        "4. 沈默也是一種溝通，他在透過沈默告訴我什麼？(系統/溝通)"
    ], key="s2_q2")

    st.markdown("---")

    # --- 情境 3: 衝突與生氣 ---
    st.markdown('<div class="scenario-box"><b>情境 3：衝突</b><br>個案突然對你生氣：「你一直問我感受有什麼用？這對解決我的問題一點幫助都沒有！」</div>', unsafe_allow_html=True)
    
    q3 = st.radio("你最想採取的策略是？", [
        "1. 承認這份落差：「謝謝你告訴我，看來我們對於『什麼有幫助』的想法不太一樣，我們要不要來討論一下？」(後現代/合作)",
        "2. 接納情緒：「我看見你真的很著急，你很希望能快點好起來，是嗎？」(人本/同理)",
        "3. 探索移情：「你現在對我的生氣，是不是很像你平常對你父親感覺到的挫折？」(動力/移情)",
        "4. 修正方向：「好，那我們現在來看看，具體來說我們可以做哪些行為改變。」(CBT/焦點)"
    ], key="s2_q3")
    
    if st.button("提交所有決策"):
        # Q1 計分
        if "1." in q1: update_axes(1.5, 1.5, "S1-證據: 理性")
        if "2." in q1: update_axes(-1.5, -1.5, "S1-反映: 體驗")
        if "3." in q1: update_axes(-1.0, 2.0, "S1-連結: 分析")
        if "4." in q1: update_axes(1.0, 1.0, "S1-例外: 行動")
        
        # Q2 計分
        if "1." in q2: update_axes(-1.0, 2.0, "S2-抗拒: 分析")
        if "2." in q2: update_axes(2.0, 1.0, "S2-結構: 客觀")
        if "3." in q2: update_axes(-2.0, -2.0, "S2-陪伴: 體驗")
        if "4." in q2: update_axes(-1.0, 1.0, "S2-溝通: 系統")

        # Q3 計分
        if "1." in q3: update_axes(-1.0, 1.0, "S3-合作: 系統")
        if "2." in q3: update_axes(-2.0, -1.0, "S3-同理: 體驗")
        if "3." in q3: update_axes(-1.0, 3.0, "S3-移情: 分析")
        if "4." in q3: update_axes(2.0, 2.0, "S3-行為: 理性")
        
        st.success("三個臨床決策皆已分析完畢。")

# ==========================================
# 階段 3: 陰影探索 (排序法)
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
                if "失控" in text: update_axes(1.5 * weight, 0, f"陰影-怕失控(w={weight}): 需求結構")
                if "冷血" in text: update_axes(-1.5 * weight, -1.0 * weight, f"陰影-怕冷血(w={weight}): 需求情感")
                if "鬼打牆" in text: update_axes(1.0 * weight, 1.5 * weight, f"陰影-怕沒效(w={weight}): 需求改變")
                if "霸道" in text: update_axes(-1.5 * weight, 0, f"陰影-怕霸道(w={weight}): 需求尊重")

            analyze_shadow(shadow_1, 1.5)
            analyze_shadow(shadow_2, 1.0)
            st.success("陰影價值觀分析完成。")

# ==========================================
# 階段 4: 空間配置 (SVG 圖示化)
# ==========================================
elif step == "4. 空間配置 (框架觀)":
    st.header("Phase 4: 物理環境與治療框架")
    st.markdown("請點選下方不同的按鈕，選擇您最喜歡的**諮商室空間配置**：")

    # 定義 SVG 繪圖函數
    def get_layout_svg(layout_type):
        # 簡單的 SVG 字串來畫家具 (圓形代表椅子/沙發，方形代表桌子)
        base_svg = '<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg" style="background-color:#f9f9f9; border:1px solid #ddd;">'
        
        if layout_type == "Intimate":
            # 膝蓋碰膝蓋：兩椅面對面，距離很近
            content = """
            <circle cx="100" cy="100" r="25" fill="#3498db" /> <text x="90" y="105" fill="white" font-size="12">Th</text>
            <circle cx="200" cy="100" r="25" fill="#e74c3c" /> <text x="190" y="105" fill="white" font-size="12">Cl</text>
            <path d="M 125 100 L 175 100" stroke="#999" stroke-width="2" stroke-dasharray="4"/>
            <text x="135" y="90" fill="#666" font-size="10">極近距離</text>
            """
        elif layout_type == "Social":
            # 舒適社交：45度角，中間有小桌子
            content = """
            <rect x="130" y="130" width="40" height="40" fill="#ecf0f1" stroke="#bdc3c7"/>
            <circle cx="100" cy="100" r="25" fill="#3498db" /> <text x="90" y="105" fill="white" font-size="12">Th</text>
            <circle cx="200" cy="200" r="25" fill="#e74c3c" /> <text x="190" y="205" fill="white" font-size="12">Cl</text>
            <text x="180" y="50" fill="#666" font-size="10">舒適斜角 (L型)</text>
            """
        elif layout_type == "Formal":
            # 正式疏離：面對面，中間有桌子隔開
            content = """
            <rect x="130" y="50" width="40" height="100" fill="#ecf0f1" stroke="#bdc3c7"/>
            <circle cx="80" cy="100" r="25" fill="#3498db" /> <text x="70" y="105" fill="white" font-size="12">Th</text>
            <circle cx="220" cy="100" r="25" fill="#e74c3c" /> <text x="210" y="105" fill="white" font-size="12">Cl</text>
            <text x="120" y="30" fill="#666" font-size="10">桌子隔開</text>
            """
        elif layout_type == "Analytic":
            # 躺椅：諮商師在後方
            content = """
            <rect x="100" y="80" width="120" height="40" rx="10" fill="#e74c3c" /> <text x="140" y="105" fill="white" font-size="12">躺椅</text>
            <circle cx="250" cy="100" r="20" fill="#3498db" /> <text x="240" y="105" fill="white" font-size="10">Th</text>
            <text x="100" y="50" fill="#666" font-size="10">經典分析設置</text>
            """
        
        return base_svg + content + '</svg>'

    # 顯示選項與圖片
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(get_layout_svg("Intimate"), unsafe_allow_html=True)
        if st.button("A. 親密靠近 (無阻隔，膝蓋幾可相觸)"):
            update_axes(-2.0, -1.5, "空間-親密: 體驗優先")
            st.success("已選擇：親密靠近")
            
        st.markdown(get_layout_svg("Social"), unsafe_allow_html=True)
        if st.button("B. 舒適斜角 (L型座位，含茶几)"):
            update_axes(-0.5, 0, "空間-舒適: 人本/折衷")
            st.success("已選擇：舒適斜角")

    with col2:
        st.markdown(get_layout_svg("Formal"), unsafe_allow_html=True)
        if st.button("C. 正式對坐 (中間有書桌或長桌)"):
            update_axes(1.5, 1.0, "空間-正式: 教學/CBT")
            st.success("已選擇：正式對坐")
            
        st.markdown(get_layout_svg("Analytic"), unsafe_allow_html=True)
        if st.button("D. 躺椅設置 (諮商師在後方)"):
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
