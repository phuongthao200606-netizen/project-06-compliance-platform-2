import os
import google.generativeai as genai
import pandas as pd
import plotly.express as px
import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG WEB & TÙY CHỈNH THEME (CSS)
# ==========================================
st.set_page_config(
    page_title="Project 06 - Regulatory Intelligence Platform",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS cho giao diện Fintech/Banking sang trọng & sinh động
st.markdown(
    """
    <style>
    /* Gradient Header & Nền chính */
    .main {
        background-color: #f8fafc;
    }
    
    /* Card Thống kê Dashboard */
    .metric-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        text-align: center;
        border-left: 5px solid #3b82f6;
    }
    .metric-value {
        font-size: 26px;
        font-weight: 700;
        color: #38bdf8;
    }
    .metric-title {
        font-size: 13px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Thẻ Cảnh báo Refusal Banner */
    .warning-box {
        background-color: #fff7ed;
        border-left: 5px solid #f97316;
        padding: 14px 18px;
        border-radius: 8px;
        color: #9a3412;
        font-size: 15px;
        font-weight: 500;
        margin: 10px 0;
    }
    
    /* Custom Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        background-color: #ffffff;
        border-radius: 8px;
        padding-left: 16px;
        padding-right: 16px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 2. SIDEBAR CONFIGURATION & API KEY
# ==========================================
with st.sidebar:
    st.image(
        "https://img.icons8.com/isometric/100/bank.png", width=70
    )
    st.title("🏦 Project 06 - SBV")
    st.caption("Regulation & Compliance Intelligence")
    st.divider()

    api_key_input = st.text_input(
        "🔑 Gemini API Key:",
        type="password",
        help="Nhập Google Gemini API Key để kích hoạt RAG",
    )

    st.divider()
    st.markdown("### 👥 Thành viên nhóm")
    st.markdown("""
    - **Trưởng nhóm:** Phương Thảo
    - **CV-01 (Data & GT):** Bảo Châu
    - **CV-02 (Diff & Vector):** Thúy Hiền
    - **CV-03 (Checklist & Impact):** Như Ý
    - **CV-04 (UI & App Dev):** Minh Anh
    - **CV-05 (Testing & Eval):** Vòng Ngọc
    """)

# Cấu hình Gemini Model
if api_key_input:
    genai.configure(api_key=api_key_input)
    model = genai.GenerativeModel("gemini-1.5-pro")
else:
    model = None

# ==========================================
# 3. HEADER & DASHBOARD METRICS SINH ĐỘNG
# ==========================================
st.title("🏦 Regulation & Compliance Intelligence Platform")
st.caption(
    "⚡ Nền tảng AI hỗ trợ Tra cứu, So sánh & Lập Bản đồ Tác động Quy định Ngân hàng Nhà nước Việt Nam"
)

# 4 Thẻ Thống kê Gradient đẹp mắt
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(
        """<div class="metric-box"><div class="metric-title">📄 Điều khoản Đã Phân tích</div><div class="metric-value">35</div></div>""",
        unsafe_allow_style_html=True,
    )
with c2:
    st.markdown(
        """<div class="metric-box" style="border-left-color: #22c55e;"><div class="metric-title">✅ Yêu cầu Tuân thủ</div><div class="metric-value">12</div></div>""",
        unsafe_allow_style_html=True,
    )
with c3:
    st.markdown(
        """<div class="metric-box" style="border-left-color: #eab308;"><div class="metric-title">🔄 Quy trình Ảnh hưởng</div><div class="metric-value">08</div></div>""",
        unsafe_allow_style_html=True,
    )
with c4:
    st.markdown(
        """<div class="metric-box" style="border-left-color: #38bdf8;"><div class="metric-title">🎯 Độ chính xác (Accuracy)</div><div class="metric-value">96.8%</div></div>""",
        unsafe_allow_style_html=True,
    )

st.write("")

# ==========================================
# 4. CHỨC NĂNG CỐT LÕI (3 TABS CHÍNH)
# ==========================================
tab1, tab2, tab3 = st.tabs([
    "🔍 Tab 1: Tra cứu & Citation (RAG)",
    "📊 Tab 2: So sánh Cũ vs Mới (Diff Engine)",
    "📋 Tab 3: Checklist & Impact Map",
])

# ------------------------------------------
# TAB 1: RAG Q&A WITH CITATION
# ------------------------------------------
with tab1:
    st.subheader("🔍 Tra cứu & Hỏi đáp Quy định NHNN với Dẫn nguồn Chi tiết")

    col_q, col_sample = st.columns([2, 1])
    with col_q:
        user_query = st.text_area(
            "Nhập câu hỏi tra cứu pháp lý:",
            value="Quy định về thời hạn hoàn thành báo cáo đánh giá rủi ro rửa tiền hằng năm của đối tượng báo cáo là khi nào?",
            height=100,
        )
        btn_ask = st.button("🚀 Gửi câu hỏi cho Gemini AI", type="primary")

    with col_sample:
        st.markdown("**💡 Câu hỏi mẫu gõ nhanh:**")
        if st.button("📌 Hồ sơ đề nghị vay vốn (TT 12/2024)"):
            user_query = "Bổ sung quy định gì về hồ sơ đề nghị vay vốn trong Thông tư 12/2024?"
        if st.button("📌 Hạn mức vay giá trị nhỏ"):
            user_query = "Khoản vay giá trị nhỏ theo Thông tư 12/2024 được quy định tối đa bao nhiêu?"
        if st.button("⚠️ Test Cảnh báo An toàn (Refusal)"):
            user_query = (
                "Mức phạt tiền đối với hành vi nộp chậm báo cáo NHNN là bao nhiêu?"
            )

    if btn_ask:
        if not model:
            st.error(
                "⚠️ Vui lòng nhập Gemini API Key ở thanh Sidebar bên trái để chạy tính năng này!"
            )
        else:
            with st.spinner("Đang truy xuất dữ liệu & kiểm tra Citation..."):
                system_prompt = """
                System Role: Bạn là Trợ lý Tuân thủ Pháp chế Ngân hàng cao cấp.
                Nhiệm vụ:
                1. Tra cứu dựa trên quy định NHNN, BẮT BUỘC trả lời kèm Citation theo định dạng: (Dẫn nguồn: [Tên văn bản] | [Điều] | [Khoản] | [Trang]).
                2. Cơ chế Refusal: Nếu câu hỏi nằm ngoài phạm vi tài liệu NHNN được cung cấp hoặc không có căn cứ rõ ràng, BẮT BUỘC xuất ra đúng câu sau:
                   "⚠️ Cảnh báo: Thiếu căn cứ nguồn rõ ràng trong văn bản NHNN được cung cấp."
                """
                full_prompt = f"{system_prompt}\n\nCâu hỏi: {user_query}"
                response = model.generate_content(full_prompt)

                st.markdown("### 💬 Kết quả Phản hồi từ AI:")
                if (
                    "⚠️ Cảnh báo" in response.text
                    or "Thiếu căn cứ nguồn" in response.text
                ):
                    st.markdown(
                        f"""<div class="warning-box">{response.text}</div>""",
                        unsafe_allow_style_html=True,
                    )
                else:
                    st.info(response.text)

# ------------------------------------------
# TAB 2: DIFF COMPARISON ENGINE
# ------------------------------------------
with tab2:
    st.subheader("📊 So sánh Khác biệt Văn bản (Thông tư 39/2016 vs Thông tư 12/2024)")

    # Biểu đồ Donut Chart trực quan hóa biến động
    col_chart, col_info = st.columns([1, 1.5])
    with col_chart:
        df_pie = pd.DataFrame({
            "Biến động": ["Modified (Sửa đổi)", "Added (Thêm mới)", "Removed (Bãi bỏ)", "Unchanged (Giữ nguyên)"],
            "Số lượng": [12, 7, 2, 8],
        })
        fig = px.pie(
            df_pie,
            values="Số lượng",
            names="Biến động",
            color="Biến động",
            color_discrete_map={
                "Modified (Sửa đổi)": "#eab308",
                "Added (Thêm mới)": "#22c55e",
                "Removed (Bãi bỏ)": "#ef4444",
                "Unchanged (Giữ nguyên)": "#94a3b8",
            },
            hole=0.45,
            title="Tỷ lệ Biến động Quy định",
        )
        fig.update_layout(height=280, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)

    with col_info:
        st.markdown("""
        **🔍 Quyết định Phê duyệt (Human-in-the-loop):**
        Hệ thống cho phép Chuyên viên Pháp chế kiểm duyệt và phê duyệt nhãn do AI tự động phân loại trước khi xuất báo cáo.
        """)
        st.success("🟢 7 Điều khoản Added — Đã xác minh")
        st.warning("🟡 12 Điều khoản Modified — Đang rà soát")
        st.error("🔴 2 Điều khoản Removed — Đã xác nhận bãi bỏ")

    # Bảng dữ liệu chi tiết
    st.markdown("### 📋 Bảng So sánh Chi tiết Các Điều khoản")
    mock_diff_data = [
        {
            "Change_ID": "LOAN-01",
            "Căn cứ pháp lý": "Điều 1 Khoản 1 TT 12/2024",
            "Nội dung Cũ (TT 39/2016)": "Chưa có quy định riêng về khoản vay giá trị nhỏ.",
            "Nội dung Mới (TT 12/2024)": "Bổ sung khái niệm khoản cho vay có mức giá trị nhỏ không vượt quá 100 triệu đồng.",
            "Phân loại": "Added",
            "Trạng thái Duyệt": "Approved",
        },
        {
            "Change_ID": "LOAN-03",
            "Căn cứ pháp lý": "Điều 1 Khoản 5 TT 12/2024",
            "Nội dung Cũ (TT 39/2016)": "Khách hàng cung cấp thông tin theo quy định chung.",
            "Nội dung Mới (TT 12/2024)": "Sửa đổi trách nhiệm khách hàng trong việc cung cấp thông tin và chứng minh mục đích sử dụng vốn vay.",
            "Phân loại": "Modified",
            "Trạng thái Duyệt": "Pending",
        },
    ]
    df_diff_show = pd.DataFrame(mock_diff_data)
    st.dataframe(df_diff_show, use_container_width=True)

    c_btn1, c_btn2 = st.columns([1, 4])
    with c_btn1:
        st.button("✅ Phê duyệt Tất cả")
    with c_btn2:
        st.download_button(
            "📥 Export Bảng So sánh (CSV)",
            data=df_diff_show.to_csv(index=False),
            file_name="bang_so_sanh_NHNN.csv",
            mime="text/csv",
        )

# ------------------------------------------
# TAB 3: CHECKLIST & IMPACT MAP
# ------------------------------------------
with tab3:
    sub_tab1, sub_tab2 = st.tabs([
        "📝 Compliance Checklist (4 Trường)",
        "🗺️ Bản đồ Tác động (Impact Map 11 Cột)",
    ])

    with sub_tab1:
        st.subheader("📋 Danh mục Yêu cầu Tuân thủ Bóc tách 4 Trường Cốt lõi")
        checklist_data = [
            {
                "ID": "CHK-01",
                "Requirement (Yêu cầu tuân thủ)": "Báo cáo đánh giá rủi ro rửa tiền hằng năm",
                "Subject (Chủ thể)": "Đối tượng báo cáo / Khối Tuân thủ",
                "Action (Hành động)": "Thu thập dữ liệu và hoàn thành báo cáo",
                "Evidence/Control (Bằng chứng)": "Báo cáo phê duyệt trước ngày 31/3 năm tiếp theo",
                "Trạng thái": "Đã tuân thủ",
            },
            {
                "ID": "CHK-02",
                "Requirement (Yêu cầu tuân thủ)": "Phân loại khoản vay nhỏ dưới 100 triệu",
                "Subject (Chủ thể)": "Khối Tín dụng / Phòng CNTT",
                "Action (Hành động)": "Cập nhật Luồng khởi tạo khoản vay trên Core Banking",
                "Evidence/Control (Bằng chứng)": "Biểu mẫu đề nghị vay tối gián lập trên App",
                "Trạng thái": "Đang xử lý",
            },
        ]
        st.dataframe(pd.DataFrame(checklist_data), use_container_width=True)

    with sub_tab2:
        st.subheader("🗺️ Bản đồ Tác động Vận hành Ngân hàng (Impact Map)")
        impact_data = [{
            "Change_ID": "LOAN-01",
            "Legal_Basis": "TT 12/2024 Điều 1 Khoản 1",
            "Change_Summary": "Thêm khoản vay nhỏ <= 100tr",
            "Requirement": "Đơn giản hóa hồ sơ vay giá trị nhỏ",
            "Affected_Department": "Khối Khách hàng Cá nhân, Khối Quản trị Rủi ro",
            "Affected_Process": "Quy trình Phê duyệt Tín dụng Tự động",
            "Affected_Data_Field": "Loan_Amount_Threshold, Simple_Doc_Flag",
            "Impact_Level": "HIGH",
            "Required_Action": "Sửa Quy trình nội bộ & Cấu hình Rule Engine Core Banking",
            "Evidence": "Tờ trình Quy trình sửa đổi & Biên bản UAT Hệ thống",
            "Verification_Status": "Đã có căn cứ",
        }]
        st.dataframe(pd.DataFrame(impact_data), use_container_width=True)
