import streamlit as st
st.title("Kết luận 📑💡")

col1,col2,col3=st.columns([2,0.1,0.9])
with col1:
    st.write("""Hiểu rõ hơn về thị trường lao động: Dữ liệu về tỷ lệ thất nghiệp theo từng ngành nghề, khu vực, nhóm tuổi, giới tính,... cho ta biết 
         nhu cầu lao động ở đâu là cao nhất và thấp nhất. Từ đó, các nhà hoạch định chính sách có thể đưa ra định hướng phát triển 
         nguồn nhân lực phù hợp, khuyến khích đầu tư vào các ngành nghề có nhu cầu cao, đồng thời có giải pháp hỗ trợ đào tạo, chuyển 
         đổi nghề nghiệp cho những người lao động thất nghiệp. 
             
Dữ liệu về tỷ lệ thất nghiệp theo trình độ học vấn, kỹ năng cho ta biết trình độ và kỹ năng nào đang thiếu hụt và dư thừa trên thị 
         trường lao động. Nhờ vậy, các cơ sở giáo dục và đào tạo có thể điều chỉnh chương trình giảng dạy để đáp ứng nhu cầu của thị 
         trường, giúp người lao động có được kỹ năng phù hợp để dễ dàng tìm kiếm việc làm.s""")

with col3:
    st.image("streamlit_report/pic/gif_conclusion.gif", use_column_width=True)
    
st.title("**🔑Giải pháp**")    
st.write(""" * Phát triển kinh tế - xã hội: Thúc đẩy tăng trưởng kinh tế ở tất cả các ngành, lĩnh vực, đặc biệt là các ngành có khả năng tạo ra nhiều việc làm.
  * Đa dạng hóa cơ cấu kinh tế: Phát triển các ngành kinh tế mới, tiềm năng như: kinh tế số, kinh tế sáng tạo, kinh tế xanh,...
  * Tăng cường đầu tư: Tạo môi trường đầu tư thuận lợi, thu hút vốn đầu tư trong và ngoài nước vào các lĩnh vực có tiềm năng phát triển và tạo ra nhiều việc làm.
  * Hỗ trợ doanh nghiệp: Hỗ trợ doanh nghiệp về vốn, công nghệ, thủ tục hành chính,... để tạo điều kiện cho doanh nghiệp phát triển, mở rộng sản xuất, kinh doanh và tạo ra nhiều việc làm.
  * Đổi mới giáo dục - đào tạo: Thay đổi phương pháp giảng dạy, cập nhật nội dung giáo dục theo nhu cầu thị trường lao động, chú trọng đào tạo kỹ năng cho người học.
  * Liên kết đào tạo với doanh nghiệp: Phối hợp giữa nhà trường và doanh nghiệp trong công tác đào tạo, để đáp ứng nhu cầu thực tế của thị trường lao động.
  Phát triển giáo dục nghề nghiệp: Nâng cao chất lượng giáo dục nghề nghiệp, đa dạng hóa các ngành nghề đào tạo, đáp ứng nhu cầu thị trường lao động.
  * Tạo lập thị trường lao động hiệu quả: Hoàn thiện hệ thống thông tin thị trường lao động, hỗ trợ người lao động tìm kiếm việc làm, tạo điều kiện cho người lao động chuyển đổi nghề nghiệp.
  * Hỗ trợ người thất nghiệp: Cung cấp các chương trình hỗ trợ về tài chính, đào tạo nghề,... cho người thất nghiệp để họ có thể nhanh chóng tìm được việc làm mới.
  * Bảo trợ xã hội: Mở rộng phạm vi bảo trợ xã hội, đảm bảo người dân có mức sống tối thiểu khi thất nghiệp.""")
