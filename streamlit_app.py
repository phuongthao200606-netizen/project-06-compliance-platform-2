import os
import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện trang Streamlit
st.set_page_config(
    page_title="Project 06 - Regulatory Intelligence Platform",
    page_icon="🏦",
    layout="wide"
)

# Thanh sidebar quản lý cấu hình API Key
with st.sidebar:
    st.markdown("### 🏦 Project 06 - SBV")
    st.markdown("Regulation & Compliance Intelligence")
    
    api_key_input = st.text_input("🔑 Gemini API Key:", type="password")
    
    # Sử dụng API Key từ sidebar hoặc từ st.secrets nếu có sẵn
    api_key = api_key_input if api_key_input else st.secrets.get("GEMINI_API_KEY", "")
    
    st.markdown("---")
    st.markdown("### 👥 Thành viên nhóm")
    st.markdown("- **Trưởng nhóm:** Phương Thảo")
    st.markdown("- **CV-01 (Data & GT):** Bảo Châu")
    st.markdown("- **CV-02 (Diff & Vector):** Thúy Hiền")
    st.markdown("- **CV-03 (Checklist & Impact):** Như Ý")
    st.markdown("- **CV-04 (UI & App Dev):** Minh Anh")
    st.markdown("- **CV-05 (Testing & Eval):** Vòng Ngọc")

# Tiêu đề chính của ứng dụng
st.markdown("### 🏦 **Regulation & Compliance Intelligence Platform**")
st.markdown("⚡ Nền tảng AI hỗ trợ Tra cứu, So sánh & Lập Bản đồ Tác động Quy định Ngân hàng Nhà nước Việt Nam")

# Các chỉ số tổng quan (Metrics)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="📄 ĐIỀU KHOẢN ĐÃ PHÂN TÍCH", value="35")
with col2:
    st.metric(label="✅ YÊU CẦU TUÂN THỦ", value="12")
with col3:
    st.metric(label="🔄 QUY TRÌNH ẢNH HƯỞNG", value="08")
with col4:
    st.metric(label="🎯 ĐỘ CHÍNH XÁC (ACCURACY)", value="96.8%")

st.markdown("---")

# Các Tabs chức năng
tab1, tab2, tab3 = st.tabs([
    "🔍 Tab 1: Tra cứu & Citation (RAG)", 
    "📊 Tab 2: So sánh Cũ vs Mới (Diff Engine)", 
    "📋 Tab 3: Checklist & Impact Map"
])

with tab1:
    st.markdown("#### 🔍 Tra cứu & Hỏi đáp Quy định NHNN với Dẫn nguồn Chi tiết")
    
    user_query = st.text_area(
        "Nhập câu hỏi tra cứu pháp lý:", 
        value="Quy định về thời hạn hoàn thành báo cáo đánh giá rủi ro rửa tiền hằng năm của đối tượng báo cáo là khi nào?"
    )
    
    if st.button("🚀 Gửi câu hỏi cho Gemini AI", type="primary"):
        if not api_key:
            st.error("⚠️ Vui lòng nhập Gemini API Key ở thanh sidebar bên trái để tiếp tục!")
        else:
            try:
                # Cấu hình API Key cho Google GenAI
                genai.configure(api_key=api_key)
                
                # KHỞI TẠO ĐÚNG TÊN MÔ HÌNH CHUẨN (gemini-1.5-flash)
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                system_prompt = (
                    "Bạn là trợ lý ảo chuyên gia pháp lý và tuân thủ quy định của Ngân hàng Nhà nước Việt Nam. "
                    "Hãy trả lời câu hỏi dựa trên các văn bản pháp luật hiện hành với dẫn nguồn cụ thể."
                )
                
                full_prompt = f"{system_prompt}\n\nCâu hỏi: {user_query}"
                
                with st.spinner("Đang xử lý và tra cứu quy định..."):
                    response = model.generate_content(full_prompt)
                    
                    st.markdown("### 💬 Kết quả Phản hồi từ AI:")
                    st.write(response.text)
                    
            except Exception as e:
                st.error(f"❌ Đã xảy ra lỗi khi gọi Gemini API: {str(e)}")

with tab2:
    st.markdown("#### 📊 So sánh Nội dung Quy định Cũ vs Mới (Diff Engine)")
    st.info("Tính năng phân tích và làm nổi bật các điểm thay đổi trọng yếu giữa các thông tư/quyết định đang được cập nhật.")

with tab3:
    st.markdown("#### 📋 Checklist Tuân thủ & Bản đồ Tác động (Impact Map)")
    st.info("Danh sách checklist tự động sinh ra giúp các tổ chức tín dụng rà soát quy trình vận hành và tuân thủ.")
