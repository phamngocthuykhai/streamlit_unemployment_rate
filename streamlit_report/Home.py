import streamlit as st
import pandas as pd
st.set_page_config(page_title='Home',page_icon=":👥:",layout='wide',base="light" )
st.title("Phân tích dữ liệu về tình trạng thất nghiệp và thiếu việc làm trong độ tuổi lao động tại Việt Nam từ năm 2018 đến năm 2022")
st.write("""Trong giai đoạn từ năm 2018 đến năm 2022, tình trạng thất nghiệp và thiếu việc làm tại Việt Nam đã trải qua nhiều biến động đáng 
         kể, đặc biệt dưới sự ảnh hưởng của đại dịch Covid-19. Từ một nền kinh tế tăng trưởng mạnh mẽ với tỷ lệ thất nghiệp thấp vào năm 2018 
         và 2019, Việt Nam đã phải đối mặt với những thách thức nghiêm trọng khi đại dịch bùng phát vào năm 2020 và 2021. Sự gián đoạn trong 
         hoạt động kinh doanh và sản xuất đã đẩy tỷ lệ thất nghiệp lên cao và gây ra tình trạng thiếu việc làm lan rộng. Tuy nhiên, nhờ vào
          các biện pháp hỗ trợ kinh tế và chính sách phục hồi hiệu quả của chính phủ, thị trường lao động đã dần phục hồi từ năm 2022, với tỷ 
         lệ thất nghiệp bắt đầu giảm xuống. Việc phân tích chi tiết tình trạng thất nghiệp và thiếu việc làm trong khoảng thời gian này không
          chỉ giúp hiểu rõ hơn về thực trạng thị trường lao động mà còn đề xuất các giải pháp phù hợp để thúc đẩy phát triển kinh tế và cải 
         thiện đời sống của người lao động.""")
st.image("streamlit_report/pic/pic_home.jpg", use_column_width=True)
