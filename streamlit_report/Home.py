import streamlit as st
import pandas as pd
st.set_page_config(page_title='Home',page_icon=":👥:",layout='wide')
st.title("Phân tích dữ liệu tỷ lệ thất nghiệp và thiếu việc làm tại Việt Nam từ năm 2018 đến năm 2022")
st.write("""Thị trường lao động Việt Nam đang có nhiều biến động, đặc biệt là sau đại dịch Covid-19. Tỷ lệ thất nghiệp và tỷ lệ thiếu 
         việc làm là những vấn đề ảnh hưởng trực tiếp đến đời sống của người lao động và sự phát triển kinh tế - xã hội của 
         đất nước. Phân tích tỷ lệ thất nghiệp và tỷ lệ thiếu việc làm trong giai đoạn từ năm 2018 đến năm 2022 sẽ giúp chúng ta hiểu 
         rõ hơn về thực trạng thị trường lao động, từ đó đề xuất các giải pháp phù hợp để giải quyết những vấn đề này.""")

st.image("streamlit_report/pic/pic_home.jpg", use_column_width=True)



