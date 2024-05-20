import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objs as go
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import hydralit_components as hc
st.set_page_config(page_title='Dashboard',page_icon=":📊:",layout='wide')
# Data Source
region_df= pd.read_csv('streamlit_report/data_csv/Region.csv')
age_df= pd.read_csv('streamlit_report/data_csv/Age.csv')
career_df= pd.read_csv('streamlit_report/data_csv/Career.csv')
education_df= pd.read_csv('streamlit_report/data_csv/Education.csv')
gender_df= pd.read_csv('streamlit_report/data_csv/Gender.csv')
location_df=pd.read_csv('streamlit_report/data_csv/data_location.csv')
birth_df=pd.read_csv('streamlit_report/data_csv/data_birth.csv')
migration_df=pd.read_csv('streamlit_report/data_csv/data_migration.csv')
immigration_df=pd.read_csv('streamlit_report/data_csv/data_immigration.csv')

un_2018_df= pd.read_csv('streamlit_report/data_csv/unemployment_province/un_province_2018.csv')
un_2019_df= pd.read_csv('streamlit_report/data_csv/unemployment_province/un_province_ 2019.csv')
un_2020_df= pd.read_csv('streamlit_report/data_csv/unemployment_province/un_province_2020.csv')
un_2021_df= pd.read_csv('streamlit_report/data_csv/unemployment_province/un_province_2021.csv')
un_2022_df= pd.read_csv('streamlit_report/data_csv/unemployment_province/un_province_2022.csv')

under_2022_df=pd.read_csv('streamlit_report/data_csv/underemployment_province/under_province_ 2022.csv')
under_2021_df=pd.read_csv('streamlit_report/data_csv/underemployment_province/under_province_2021.csv')
under_2020_df=pd.read_csv('streamlit_report/data_csv/underemployment_province/under_province_2020.csv')
under_2018_df=pd.read_csv('streamlit_report/data_csv/underemployment_province/under_province_2018.csv')
under_2019_df=pd.read_csv('streamlit_report/data_csv/underemployment_province/under_province_2019.csv') 

# Tạo sidebar
with st.sidebar: 
    st.title("📈Dashboard")
    # Tạo các mục lựa chọn
    choice = st.radio("", ["Xu hướng","Tình trạng thất nghiệp", "Tình trạng thiếu việc làm","Bản đồ"])
    

if choice =="Xu hướng":
    st.sidebar.image("streamlit_report/pic/200-unscreen.gif", use_column_width=True)
    st.title("**📊Dashboard biến động tình trạng thất nghiệp và thiếu việc làm tại Việt Nam(2018-2022)**")
    st.info("""Dashboard xu hướng biến động tình trạng thất nghiệp và thiếu việc làm cung cấp cái nhìn tổng quan về thị trường lao động
                trong giai đoạn 2018-2022""")
    
    col1,col2=st.columns([2,1])
    with col1:
        years = [2018, 2019, 2020, 2021, 2022]
        unemployment={}
        underemployed={}
        for year in years:
            filt=region_df[region_df['Năm'] == year]
            unemployment[year]=filt['Tỷ lệ thất nghiệp'].mean()
            underemployed[year]=filt['Tỷ lệ thiếu việc làm'].mean()
        # Tạo biểu đồ xu hướng tỷ lệ thất nghiệp và thiếu việc làm
        trace_unemployment = go.Scatter(x=years, y=list(unemployment.values()), mode='lines', name='Tỷ lệ thất nghiệp')
        trace_underemployed = go.Scatter(x=years, y=list(underemployed.values()), mode='lines', name='Tỷ lệ thiếu việc làm')
        # Layout
        layout = go.Layout(
            title='Biến động tình trạng thất nghiệp và thiếu việc làm (2018-2022)',
            xaxis=dict(title='Năm', range=[2018, 2022]),
            yaxis=dict(title='Tỷ lệ (%)'),
            width=770, height=500)
        fig = go.Figure(data=[trace_unemployment, trace_underemployed], layout=layout)
        st.plotly_chart(fig)    
        with st.expander('📝 See note:'):
            st.write("""Biểu đồ cho thấy rằng tỷ lệ thất nghiệp và thiếu việc làm tại Việt Nam đã tăng mạnh trong những năm này. Điều này
                      có thể được giải thích bởi ảnh hưởng của đại dịch COVID-19, khi nền kinh tế gặp khó khăn và nhiều ngành công nghiệp 
                     phải đối mặt với sự suy giảm sản xuất và thu nhập.
* Năm 2020-2021 là một năm bị ảnh hưởng nặng nề bởi đại dịch COVID-19, khiến nền kinh tế bị gián đoạn nghiêm trọng và buộc nhiều doanh nghiệp
                      phải thu hẹp quy mô hoặc tạm thời đóng cửa. Nhiều người lao động không bị mất việc hoàn toàn mà phải chấp nhận giảm giờ 
                     làm hoặc chuyển sang làm việc bán thời gian, khiến tình trạng thiếu việc làm gia tăng.
* Mặc dù tỷ lệ thất nghiệp và thiếu việc làm vẫn cao hơn năm 2018 và 2019, nhưng sẽ có một số mức giảm vào năm 2022. Điều này có thể cho thấy
                      các biện pháp phục hồi sau đại dịch và kích thích kinh tế đang bắt đầu phát huy tác dụng, dẫn đến ít áp lực lên thị 
                     trường lao động. Sự sụt giảm nhẹ vào năm 2022 cho thấy sự phục hồi dần dần, nhưng con số vẫn ở mức cao do ảnh hưởng kéo 
                     dài của đại dịch và các vấn đề tài chính đang diễn ra.""")
  

if choice =="Tình trạng thất nghiệp":
    st.sidebar.image("streamlit_report/pic/gif_chart.gif", use_column_width=True)
    st.title("**📊Dashboard các yếu tố ảnh hưởng đến tình trạng thất nghiệp tại Việt Nam(2018-2022)**")
    st.info("""Cung cấp cái nhìn tổng quan, trực quan về xu hướng tình trạng thất nghiệp trong giai đoạn 2018-2022.\n
Giúp người dùng dễ dàng theo dõi, so sánh các chỉ số về thất nghiệp theo thời gian, khu vực, ngành nghề, nhóm đối tượng,...""")
    
    left_column, right_column = st.columns(2)
    with left_column:
        un_gen = gender_df['Tỷ lệ thất nghiệp'].sum()
        un_age = age_df['Tỷ lệ thất nghiệp'].sum()
        un_education = education_df['Tỷ lệ thất nghiệp'].sum()
        labels = ['Giới tính', 'Tuổi', 'Học vấn']
        sizes = [un_gen, un_age, un_education]

        # Tạo biểu đồ tròn
        fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, textinfo='percent')])
        fig.update_layout(title='Các yếu tố ảnh hưởng đến tình trạng thất nghiệp',
                          width=500, height=500)
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
             st.write("""Học vấn: Chiếm tỷ lệ cao nhất (48%) trong các yếu tố ảnh hưởng đến tình trạng thất nghiệp. Điều này cho thấy 
                      trình độ học vấn đóng vai trò quan trọng trong việc tìm kiếm việc làm và tránh thất nghiệp. Tuổi: Chiếm tỷ lệ
                       35,2% .Giới tính: Chiếm tỷ lệ 16,8%.\n\n Biểu đồ cho thấy tầm quan trọng của việc nâng cao trình độ học vấn. Biểu đồ cũng cho thấy cần có các chính sách hỗ trợ việc làm phù 
                      hợp với từng nhóm đối tượng khác nhau như giới tính, độ tuổi, ... để giảm thiểu tỷ lệ thất nghiệp.""")


    with right_column:
        # giới tính ảnh hưởng đến tình trạng thất nghiệp
        fig = px.line(gender_df, x='Năm', y='Tỷ lệ thất nghiệp', color='Giới tính', labels={'Năm': 'Năm', 'Tỷ lệ thất nghiệp': 'Tỷ lệ'})
        
        fig.update_layout(title='Tình trạng thất nghiệp phân theo giới tính (2018-2022)',
                        xaxis=dict(title='Năm'),
                        yaxis=dict(title='Tỷ lệ (%)'),
                        width=600, height=500)
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
            st.write("""Đối với biểu đồ **“Tình trạng thất nghiệp phân theo giới tính”**, ta nhìn thấy được một số phụ nữ vẫn gặp phải sự phân 
                     biệt đối xử trong nơi làm việc, bao gồm mức lương thấp hơn, cơ hội nghề nghiệp hạn chế và áp lực tăng cao. Sự phân biệt
                      đối xử này có thể làm tăng tỷ lệ thất nghiệp ở phụ nữ. Nhiều phụ nữ phải đối mặt với áp lực giữa việc chăm sóc gia đình
                      và làm việc ngoài xã hội. Điều này có thể làm giảm khả năng của họ trong việc tìm kiếm và duy trì một công việc, dẫn
                      đến tỷ lệ thất nghiệp cao hơn. Tuy nhiên việc tỷ lệ thất nghiệp ở nữ giới giảm vào năm 2022 tuy không đáng kể nhưng có
                      phần thấp hơn nam giới có thể phản ánh sự hồi phục của một số ngành nghề và sự cân nhắc của chính sách trong việc hỗ 
                     trợ người lao động, bao gồm cả phụ nữ, sau đại dịch COVID-19.""")


    left_column, right_column = st.columns(2)
    with right_column:
        #Trình độ học vấn ảnh hưởng đến tình trạng thất nghiệp
        fig = px.line(education_df, x='Năm', y='Tỷ lệ thất nghiệp', color='Học vấn', labels={'Năm': 'Năm', 'Tỷ lệ thất nghiệp': 'Tỷ lệ'})
        
        fig.update_layout(title='Tình trạng thất nghiệp phân theo trình độ học vấn (2018-2022)',
                        xaxis=dict(title='Năm'),
                        yaxis=dict(title='Tỷ lệ (%)'))
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
            st.write("""* Người có trình độ cao đẳng hoặc đại học thường cạnh tranh trong các ngành nghề yêu cầu trình độ cao hơn. 
                     Điều này có thể dẫn đến một số người không thể tìm được việc làm phù hợp với trình độ học vấn của họ, dẫn đến 
                     tỷ lệ thất nghiệp cao hơn trong nhóm này. Người có trình độ học vấn cao thường được trang bị với kỹ năng và 
                     kiến thức chuyên môn cần thiết để làm việc trong các lĩnh vực chuyên môn. Tuy nhiên, nếu thị trường lao động 
                     yêu cầu các kỹ năng đặc biệt hoặc không phản ánh đầy đủ nhu cầu thực tế của doanh nghiệp, một số người có trình 
                     độ cao đẳng hoặc đại học có thể gặp khó khăn trong việc tìm kiếm việc làm phù hợp.\n
* Một số ngành nghề, như lao động phổ thông trong nông nghiệp, xây dựng, dịch vụ, 
                     và ngành công nghiệp nhẹ, thường có nhu cầu lao động lớn và đơn giản hóa quy trình tuyển dụng. 
                     Các ngành nghề mà không yêu cầu trình độ học vấn cao thường có môi trường làm việc linh hoạt và ít yêu cầu về
                      kỹ năng chuyên môn. Điều này có thể làm giảm áp lực tìm kiếm việc làm và tạo ra nhiều cơ hội việc làm hơn.""")

    with left_column:
        fig = px.line(age_df, x='Năm', y='Tỷ lệ thất nghiệp', color='Nhóm tuổi', labels={'Năm': 'Năm', 'Tỷ lệ thất nghiệp': 'Tỷ lệ'})
        
        fig.update_layout(title='Tình trạng thất nghiệp phân theo nhóm tuổi (2018-2022)',
                        xaxis=dict(title='Năm'),
                        yaxis=dict(title='Tỷ lệ (%)'))
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
             st.write("""* Nhóm tuổi từ 15 đến 24 tuổi: Đây thường là nhóm tuổi của các bạn trẻ mới tốt nghiệp trung học phổ thông hoặc 
                      đại học và đang tìm kiếm việc làm lần đầu trong cuộc sống. Tính trạng thất nghiệp cao ở nhóm này có thể phản 
                      ánh sự khó khăn trong việc nhập cuộc vào thị trường lao động, thiếu kinh nghiệm làm việc, cũng như sự cạnh tranh 
                      gay gắt trong việc tìm kiếm việc làm phù hợp với trình độ và mong muốn của họ.\n\n* Nhóm tuổi từ 25 đến 49 tuổi: 
                      Đây là nhóm tuổi mà người lao động thường đạt đến đỉnh cao về sự nghiệp và kinh 
                      nghiệm làm việc. Tuy nhiên, mặc dù có kinh nghiệm làm việc, nhóm này vẫn có thể gặp khó khăn trong việc duy trì 
                      việc làm do sự cạnh tranh từ các thế hệ trẻ tuổi, và các yếu tố kinh tế toàn cầu khác.\n\n* Nhóm tuổi 50+: Đây thường 
                      là nhóm tuổi của người lao động đã có nhiều kinh nghiệm làm việc nhưng có thể gặp 
                      khó khăn trong việc tìm kiếm việc làm mới do sự phân biệt đối xử dựa trên tuổi tác, kỹ năng công nghệ thấp hoặc 
                      sự khó khăn trong việc thích nghi với sự biến đổi của thị trường lao động.""")


    # Tạo biểu đồ thanh theo dõi tỷ lệ thất nghiệp của nữ
    trace_unemployment_female = go.Bar(x=gender_df[gender_df['Giới tính'] == 'Nữ']['Năm'],
                                    y=gender_df[gender_df['Giới tính'] == 'Nữ']['Tỷ lệ thất nghiệp'],
                                    name='Tỷ lệ thất nghiệp (Nữ)',
                                    text=gender_df[gender_df['Giới tính'] == 'Nữ']['Tỷ lệ thất nghiệp'])
    # Tạo biểu đồ thanh theo dõi tỷ lệ sinh
    trace_birth_rate = go.Bar(x=birth_df.groupby('Năm')['Tỷ suất sinh'].mean().index,
                            y=birth_df.groupby('Năm')['Tỷ suất sinh'].mean().values, name='Tỷ suất sinh',
                            text=birth_df.groupby('Năm')['Tỷ suất sinh'].mean().values.round(3))
    # Layout
    layout = go.Layout(title='Biểu đồ tỷ suất sinh và tỷ lệ thất nghiệp (Nữ) theo năm',
                    xaxis=dict(title='Năm'),
                    yaxis=dict(title='Tỷ lệ (%)'),
                    width=800, height=500)
    # Kết hợp
    fig = go.Figure(data=[trace_birth_rate, trace_unemployment_female], layout=layout)
    # Hiển thị biểu đồ trên Streamlit
    st.plotly_chart(fig)
    with st.expander("📝See note:"):
        st.write("""Tỷ suất sinh= ( Tổng số sinh trong thời kỳ nghiên cứu/ Dân số trung bình)*1000
* Biểu đồ chỉ ra mối tương quan nghịch, nghĩa là khi tỷ lệ thất nghiệp của phụ nữ tăng thì tỷ lệ sinh sẽ giảm.
                  Điều này có thể là do một số yếu tố, chẳng hạn như sự bất an về kinh tế, có thể khiến các cặp vợ chồng trì hoãn 
                 hoặc từ bỏ việc sinh con. Các vấn đề:
    * **Bất an kinh tế:** Khi phụ nữ thất nghiệp, họ có thể cảm thấy kém an toàn hơn về mặt tài chính và có nhiều 
                 khả năng trì hoãn hoặc từ bỏ việc sinh con.
    * **Cân bằng giữa công việc và cuộc sống:** Cân bằng giữa công việc và cuộc sống gia đình có thể là một thách thức 
                 và phụ nữ thất nghiệp có thể có nhiều thời gian hơn để chăm sóc con cái. Tuy nhiên, họ cũng có thể phải đối mặt với 
                 những thách thức trong việc tìm kiếm người chăm sóc trẻ khi tái gia nhập lực lượng lao động.
    * **Khát vọng về học vấn và nghề nghiệp:** Phụ nữ có trình độ học vấn và nguyện vọng nghề nghiệp cao hơn 
                 có thể có nhiều khả năng trì hoãn việc sinh con cho đến khi họ đã ổn định được sự nghiệp của mình.""")


    traces = []
    # Năm để trực quan hóa
    years = [2018, 2019, 2020, 2021, 2022]
    # Lặp qua mỗi năm
    for year in years:
        # Lọc dữ liệu cho năm hiện tại
        filtered_data = region_df[region_df['Năm'] == year]
        # Nhóm dữ liệu theo 'Vùng' và tính trung bình tỷ lệ thất nghiệp
        grouped_data = filtered_data.groupby(['Vùng'])['Tỷ lệ thất nghiệp'].mean().reset_index()
        # Tạo một trace bar cho năm hiện tại
        trace = go.Bar(
            x=grouped_data['Vùng'],
            y=grouped_data['Tỷ lệ thất nghiệp'],
            name=str(year))
        # Thêm trace vào danh sách các traces
        traces.append(trace)
    # Tạo biểu đồ
    fig = go.Figure(data=traces)
    # Layout
    fig.update_layout(
        title='Tình trạng thất nghiệp theo phân theo vùng',
        xaxis=dict(title='Vùng'),
        yaxis=dict(title='Tỷ lệ(%)'),width=1100, height=500)
    # Hiển thị biểu đồ trên Streamlit 
    st.plotly_chart(fig)
    with st.expander("📝 See note:"):
        st.write("""- **Vùng trung du và miền núi phía bắc:**           
    - Nông nghiệp vẫn là ngành kinh tế chủ lực: Tuy nhiên, năng suất lao động thấp, không đủ linh hoạt để tạo ra nhiều việc làm.
                  Do đó, khi các ngành công nghiệp này gặp khó khăn, tỷ lệ thất nghiệp sẽ dễ dàng tăng cao.\n\n- **Bắc Trung Bộ và Duyên hải Miền Trung:**\n\n
    - Vùng này phụ thuộc vào một số ngành công nghiệp nhất định, chẳng hạn như du lịch, nông nghiệp và khai thác khoáng sản. 
                 Tuy nhiên, những ngành này có thể không tạo đủ việc làm cho dân số ngày càng tăng. Các thiên tai này gây ra thiệt 
                 hại kinh tế nghiêm trọng, làm giảm khả năng tạo ra việc làm.
- **Đồng bằng sông Cửu Long:**
    - Đồng bằng sông Cửu Long nổi tiếng với nền nông nghiệp trù phú, đóng góp đáng kể vào sản xuất lương thực quốc gia. Với điều kiện
                 khí hậu thuận lợi, đất đai màu mỡ, khu vực này là nơi canh tác nhiều loại cây trồng. Tuy nhiên, nông nghiệp phụ thuộc 
                 nhiều vào điều kiện thời tiết và mùa màng. Vào những thời điểm ngoài mùa vụ, nhu cầu lao động giảm mạnh, dẫn đến tình trạng mất việc làm.
- **Vùng Đông Nam Bộ:**
    - Đối với các thành phố phát triển như Thành phố Hồ Chí Minh, nơi tập trung đông dân và là trung tâm kinh tế lớn, thì việc đô thị 
hóa thường dẫn đến sự cạnh tranh tìm việc làm rất cao giữa người lao động. Bởi khi đó, nhu cầu tìm việc tăng mạnh trong khi số lượng 
                 việc làm lại có sự hạn chế và phân bổ không đều, tạo nên sự chênh lệch lớn giữa các ngành nghề, các khu vực. 
                 Điều này có thể dẫn đến tình trạng thừa lao động ở một số lĩnh vực và thiếu hụt lao động ở một số lĩnh vực khác.
- **Tây Nguyên:**
    - Tây Nguyên chủ yếu dựa vào nông nghiệp, trong khi công nghiệp và dịch vụ vẫn chưa phát triển mạnh. Nông nghiệp tập trung sử 
                 dụng nhiều lao động nhưng năng suất thấp, dẫn đến thu nhập không cao cho người dân. Tình trạng này cũng góp phần 
                 làm tăng tỷ lệ thất nghiệp trong khu vực.
- **Đồng bằng sông Hồng:**
    - Vùng đồng bằng sông Hồng có tỷ lệ thất nghiệp tương đối thấp, dao động quanh mốc trung bình so với các khu vực khác của Việt Nam. 
   - Trong những tháng giãn cách vì đại dịch Covid-19, các ngành công nghiệp chính ít bị ảnh hưởng: Các ngành công nghiệp chế biến, 
                 sản xuất thường liên quan đến nhu cầu cơ bản của người tiêu dùng, do đó ít bị ảnh hưởng bởi các biến động ngắn hạn như dịch bệnh.""")


    # Tạo biểu đồ thanh theo dõi tỷ lệ nhập cư của theo năm 
    trace_dt_immigration = go.Bar(x=immigration_df.groupby('Năm')['Tỷ suất nhập cư'].mean().index,
                            y=immigration_df.groupby('Năm')['Tỷ suất nhập cư'].mean().values, name='Tỷ suất nhập cư')
    # Tạo biểu đồ thanh theo dõi tỷ lệ xuất cư của theo năm 
    trace_dt_migration = go.Bar(x=migration_df.groupby('Năm')['Tỷ suất xuất cư'].mean().index,
                            y=migration_df.groupby('Năm')['Tỷ suất xuất cư'].mean().values, name='Tỷ suất xuất cư')
    # Tạo biểu đồ thanh theo dõi tỷ lệ thất nghiệp theo năm
    trace_combined_region = go.Bar(x=region_df.groupby('Năm')['Tỷ lệ thất nghiệp'].mean().index,
                            y=region_df.groupby('Năm')['Tỷ lệ thất nghiệp'].mean().values, name='Tỷ lệ thất nghiệp')
    # Layout
    layout = go.Layout(title='Tình trạng xuất nhập cư gây ảnh hưởng đến tình trạng thất nghiệp của các năm từ 2018 đến 2022',
                    xaxis=dict(title='Năm'),
                    yaxis=dict(title='Tỷ lệ (%)'),
                    width=1000, height=600)
    # Combine
    fig = go.Figure(data=[trace_combined_region,trace_dt_immigration,trace_dt_migration], layout=layout)
    # Hiển thị biểu đồ trên Streamlit
    st.plotly_chart(fig)
    with st.expander("📝See note:"):
        st.write("""Biểu đồ cho thấy tình trạng xuất nhập cư có ảnh hưởng đáng kể đến tỷ lệ thất nghiệp vì một số lý do sau:\n
1. **Tỷ lệ thất nghiệp giảm có thể dẫn đến tình trạng di cư giảm:** Khi người dân dễ dàng tìm được việc làm ở địa phương, 
                 họ ít có xu hướng di chuyển đến những nơi khác để tìm kiếm cơ hội việc làm tốt hơn. Điều này làm giảm áp lực 
                 di cư và giữ cho nguồn lao động ổn định ở địa phương.
2. **Tỷ lệ xuất cư giảm cũng có thể ảnh hưởng đến tỷ lệ thất nghiệp:** Khi người dân ít di cư ra khỏi một địa phương, 
                 nguồn cung lao động ở đó sẽ tăng lên, dẫn đến tình trạng dư thừa lao động và có thể đẩy tỷ lệ thất nghiệp tăng lên. 
                 Điều này thường xảy ra khi một khu vực đối diện với tình trạng thất nghiệp cao và người dân không có nhiều cơ hội để tìm kiếm việc làm ở nơi khác.\n
**Tỷ lệ xuất cư cao có thể được giải thích bởi các yếu tố sau:**
- **Thu nhập thấp:** Thu nhập bình quân đầu người ở Việt Nam vẫn thấp so với nhiều nước trong khu vực, khiến người dân tìm kiếm 
                 cơ hội việc làm và thu nhập cao hơn ở các nước có mức sống cao hơn.
- **Thiếu việc làm:** Tỷ lệ thất nghiệp ở Việt Nam, đặc biệt là ở khu vực nông thôn, vẫn cao. Điều này khiến nhiều người tìm kiếm
                  việc làm ở các thành phố lớn hoặc các quốc gia khác.
- **Điều kiện làm việc:** Một số ngành nghề ở Việt Nam có điều kiện làm việc khó khăn, vất vả và nguy hiểm, khiến người lao động
                  tìm kiếm việc làm ở những nơi có điều kiện làm việc tốt hơn và an toàn hơn.""")


if choice =="Tình trạng thiếu việc làm":
    st.sidebar.image("streamlit_report/pic/gif_gene.gif", use_column_width=True)
    st.title("**📊Dashboard các yếu tố ảnh hưởng đến tình trạng thiếu việc làm tại Việt Nam(2018-2022)**")
    st.info("""Cung cấp cái nhìn tổng quan, trực quan về xu hướng tình trạng thiếu việc làm trong giai đoạn 2018-2022.\n\n Giúp người 
            dùng dễ dàng theo dõi, so sánh các chỉ số về thất nghiệp theo thời gian, khu vực, ngành nghề, nhóm đối tượng,...""")
    under_gen = gender_df['Tỷ lệ thiếu việc làm'].sum()
    under_age = age_df['Tỷ lệ thiếu việc làm'].sum()
    under_education = education_df['Tỷ lệ thiếu việc làm'].sum()
    career = career_df['Tỷ lệ thiếu việc làm'].sum()

    labels = ['Học vấn', 'Tuổi', "Ngành nghề", 'Giới tính']
    sizes = [under_education, under_age, career,under_gen,]
    # Tạo biểu đồ tròn
    trace_pie = go.Pie(labels=labels, values=sizes)
    # Layout 
    layout = go.Layout(title='Các yếu tố ảnh hưởng đến tình trạng thiếu việc làm',
                       yaxis=dict(title='Tỷ lệ(%)'),
                        xaxis=dict(title='Năm'),
                        width=1000, height=500)
    # Combine
    fig = go.Figure(data=[trace_pie], layout=layout)
    # Hiển thị biểu đồ trên Streamlit
    st.plotly_chart(fig)
    with st.expander("📝See note:"):
        st.write("""Biểu đồ hình tròn thể hiện tỷ lệ phần trăm các yếu tố ảnh hưởng đến tỷ lệ thiếu vệc làm tại Việt Nam. Trình độ học vấn có
                  ảnh hưởng lớn hơn so với ngành nghề, độ tuổi và giới tính: đối với trình độ học vấn chiếm tỷ lệ cao nhất **(31,2%)**, cho thấy
                  sự quan trọng của trình độ học vấn trong việc tìm kiếm và duy trì công việc. Trong khi đó, ngành nghề và giới tính có tỷ lệ 
                 ảnh hưởng lớn hơn so với giới tính **(25,9% so với 16,3%)**. Điều này có thể thấy rằng sự lựa chọn ngành nghề và giới tính cũng 
                 có vai trò quan trọng trong việc xác định khả năng tìm kiếm việc làm và ổn định nghề nghiệp của một người. Mặc dù tỷ lệ ảnh 
                 hưởng của tuổi không phải là thấp nhất **(26,5%)**, nhưng nó vẫn thấp hơn so với học vấn và ngành nghề. Điều này có thể cho thấy 
                 rằng trong một số trường hợp, người lao động có thể vượt qua sự ảnh hưởng của tuổi tác thông qua việc có trình độ học vấn 
                 cao và lựa chọn ngành nghề phù hợp. Tỷ lệ ảnh hưởng của các yếu tố như học vấn, ngành nghề, giới tính và tuổi tác thể hiện 
                 sự phức tạp và đa dạng của các nguyên nhân gây ra tình trạng thất nghiệp và thiếu việc làm.""")


    left_column, right_column = st.columns(2)
    with left_column:
        fig = px.line(age_df, x='Năm', y='Tỷ lệ thiếu việc làm', color='Nhóm tuổi', labels={'Năm': 'Năm', 'Tỷ lệ thiếu việc làm': 'Tỷ lệ'})
        # Đặt tên tiêu để và nhãn
        fig.update_layout(title='Tình trạng thiếu việc làm phân theo nhóm tuổi (2018-2022)',
                          yaxis=dict(title='Tỷ lệ(%)'),
                          xaxis=dict(title='Năm'),
                          width=500, height=500)
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
            st.write("""Tuổi tác được coi là một yếu tố quan trọng ảnh hưởng đến tỷ lệ thiếu việc làm vì nó ảnh hưởng đến nhiều khía cạnh 
                     khác nhau của khả năng tiếp cận việc làm và khả năng thích ứng với biến động của thị trường lao động. 
* **Nhóm tuổi trẻ (từ 15 đến 24 tuổi):**\n\n  Đây thường là nhóm tuổi của các bạn trẻ mới tốt nghiệp trung học phổ thông hoặc đại học và đang
                      tìm kiếm việc làm lần đầu trong cuộc sống. Tính trạng thất nghiệp cao ở nhóm này có thể phản ánh sự khó khăn trong việc
                      nhập cuộc vào thị trường lao động, thiếu kinh nghiệm làm việc, cũng như sự cạnh tranh gay gắt trong việc tìm kiếm việc 
                     làm phù hợp với trình độ và mong muốn của họ.
* **Nhóm tuổi trung niên (từ 25 đến 49 tuổi):**\n\n     Nhóm này thường có kinh nghiệm làm việc và kỹ năng chuyên môn phong phú hơn so với 
                     nhóm tuổi trẻ, giúp họ có khả năng tìm kiếm và duy trì việc làm tốt hơn. Tuy nhiên, họ có thể gặp khó khăn trong việc 
                     thích ứng với các biến động của thị trường lao động, đặc biệt là trong thời kỳ bùng nổ công nghệ, khi mà các kỹ năng mới 
                     và sự linh hoạt trở nên quan trọng. Ngoài ra, gánh nặng gia đình như con cái hoặc cha mẹ già yếu cũng có thể ảnh hưởng 
                     đến khả năng tham gia thị trường lao động của họ, làm giảm sự linh hoạt và khả năng đáp ứng các yêu cầu công việc.
* **Nhóm tuổi cao (trên 50 tuổi):**\n\n     Nhóm lao động lớn tuổi thường gặp khó khăn trong việc tìm kiếm việc làm mới do các yếu tố như sự
                      phân biệt đối xử dựa trên tuổi tác và khả năng thích ứng với công nghệ mới. Tuy nhiên, một số người trong nhóm này đã 
                     tích lũy được nhiều kinh nghiệm và xây dựng được mạng lưới liên kết trong nghề nghiệp, giúp họ duy trì việc làm ổn định
                      hơn. Ngoài ra, chính sách nghỉ hưu sớm ở một số quốc gia cũng có thể ảnh hưởng đến tỷ lệ thiếu việc làm của nhóm tuổi 
                     này, khi nhiều người lựa chọn hoặc bị khuyến khích nghỉ hưu trước tuổi lao động chính thức.""")


    with right_column:
        fig = px.line(education_df, x='Năm', y='Tỷ lệ thiếu việc làm', color='Học vấn', labels={'Năm': 'Năm', 'Tỷ lệ thiếu việc làm': 'Tỷ lệ'})
        # Đặt tên tiêu để và nhãn
        fig.update_layout(title='Tình trạng thiếu việc làm phân theo trình độ học vấn(2018-2022)',
                          yaxis=dict(title='Tỷ lệ(%)'),
                          xaxis=dict(title='Năm'),
                          width=600, height=500)
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
            st.write("""* Nhóm có trình độ học vấn sơ cấp và không có trình độ chuyên môn kỹ thuật có tỷ lệ thiếu việc làm cao xuất phát từ việc thiếu hụt kỹ năng 
                     và kiến thức chuyên môn, khiến họ khó tìm kiếm được việc làm ổn định và phù hợp. Các ngành nghề truyền thống mà nhóm này 
                     thường tham gia thường có nhu cầu lao động thấp và mức lương không cao, dẫn đến việc họ gặp khó khăn trong việc tìm kiếm 
                     công việc có thu nhập tốt. Khả năng cạnh tranh của nhóm này trong thị trường lao động cũng hạn chế, do đó họ dễ bị rơi 
                     vào tình trạng thiếu việc làm khi nền kinh tế gặp biến động. 
* Nhóm có trình độ học vấn cao đẳng hoặc đại học nhờ có kỹ năng và kiến thức chuyên môn tốt hơn, tỷ lệ thiếu việc làm của nhóm này thấp hơn 
                     so với nhóm có trình độ sơ cấp. Họ có nhiều cơ hội nghề nghiệp hơn và sở hữu mạng lưới quan hệ rộng rãi, giúp  tiếp cận 
                     với nhiều vị trí công việc đa dạng và ổn định. Khả năng thích ứng với các biến động của thị trường lao động cũng cao hơn,
                      cho phép dễ dàng chuyển đổi hoặc thăng tiến trong sự nghiệp khi có thay đổi trong nền kinh tế.""")  
      


    left_column, right_column = st.columns(2)
    with left_column:
    # Biểu đồ đường "thiếu việc làm theo nhóm ngành"        
        fig = px.line(gender_df, x='Năm', y='Tỷ lệ thiếu việc làm', color='Giới tính', labels={'Năm': 'Năm', 'Tỷ lệ thiếu việc làm': 'Tỷ lệ'})
        # Đặt tên tiêu để và nhãn
        fig.update_layout(title='Tình trạng thiếu việc làm phân theo giới tính(2018-2022)',
                          yaxis=dict(title='Tỷ lệ(%)'),
                          xaxis=dict(title='Năm'),
                          width=500, height=500)
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
            st.write("""Trong một số ngành nghề, như xây dựng, sản xuất, và ngành công nghiệp, thường có sự ưu tiên tuyển dụng nam 
                     giới hơn là nữ giới. Ngược lại, trong các lĩnh vực như giáo dục và chăm sóc sức khỏe, nữ giới thường có xu hướng 
                     chiếm ưu thế hơn. Sự phân chia ngành nghề này có thể dẫn đến sự chênh lệch về tỷ lệ thất nghiệp giữa nam và nữ.""")


    # Biểu đồ đường "thiếu việc làm theo nhóm tuổi"
    with right_column:
        fig = px.line(career_df, x='Năm', y='Tỷ lệ thiếu việc làm', color='Ngành', labels={'Năm': 'Năm', 'Tỷ lệ thiếu việc làm': 'Tỷ lệ'})
        # Đặt tên tiêu để và nhãn
        fig.update_layout(title='Tình trạng thiếu việc làm phân theo nhóm nghành(2018-2022)',
                          yaxis=dict(title='Tỷ lệ(%)'),
                          xaxis=dict(title='Năm'),
                          width=600, height=500)
        # Hiển thị biểu đồ trên Streamlit
        st.plotly_chart(fig)
        with st.expander("📝See note:"):
            st.write("""Yếu tố ngành nghề có thể ảnh hưởng đến tỷ lệ thiếu việc làm do sự biến động trong cơ hội việc làm và thu nhập 
                     của từng ngành, cũng như sự phản ánh của các biến động kinh tế và xã hội lên thị trường lao động.
* **Ngành nông lâm nghiệp thủy sản** là những ngành nghề có cơ hội việc làm không ổn định và thu nhập thấp, phụ thuộc nhiều vào yếu tố 
                     thiên nhiên và các yếu tố khác nằm ngoài tầm kiểm soát của người lao động.
* **Ngành công nghiệp xây dựng** thường phản ánh sự phát triển kinh tế và xây dựng cơ sở hạ tầng của một quốc gia. Các dự án xây dựng có 
                     thể tạo ra nhiều việc làm mới trong giai đoạn xây dựng, nhưng sau đó có thể gây ra sự giảm sút khi các dự án hoàn 
                     thành. Sự biến động trong việc đầu tư công và tư nhân, cũng như biến động trong thị trường bất động sản, có thể ảnh hưởng đến tỷ lệ thiếu việc làm của ngành này.
* Một số ngành **dịch vụ** có tỷ lệ thiếu việc làm thấp hơn do nhu cầu ổn định trong các dịch vụ cơ bản như y tế, giáo dục và các dịch vụ 
                     chăm sóc cá nhân. Tuy nhiên, sự biến động trong nền kinh tế có thể ảnh hưởng đến ngành dịch vụ, ví dụ như sự suy 
                     giảm của doanh số bán hàng trong ngành du lịch và giải trí do ảnh hưởng của đại dịch COVID-19.""")


    # Khởi tạo danh sách trống
    traces = []
        # Năm để trực quan hóa
    years = [2018, 2019, 2020, 2021, 2022]
        # Lặp qua mỗi năm
    for year in years:
        # Lọc dữ liệu cho năm hiện tại
        filtered_data = region_df[region_df['Năm'] == year]
        # Nhóm dữ liệu theo 'Vùng' và tính trung bình tỷ lệ thiếu việc làm
        grouped_data = filtered_data.groupby(['Vùng'])['Tỷ lệ thiếu việc làm'].mean().reset_index()
        # Tạo một trace bar cho năm hiện tại
        trace = go.Bar(
            x=grouped_data['Vùng'],
            y=grouped_data['Tỷ lệ thiếu việc làm'],
            name=str(year))
        # Thêm trace vào danh sách các traces
        traces.append(trace)
        # Tạo biểu đồ
    fig = go.Figure(data=traces)
        # Layout
    fig.update_layout(
        title='Tình trạng thiếu việc làm theo phân theo vùng',
        xaxis=dict(title='Vùng'),
        yaxis=dict(title='Tỷ lệ(%)'),
        barmode='group',width=1000, height=600)
    # Hiển thị biểu đồ trên Streamlit
    st.plotly_chart(fig)
    with st.expander("📝See note:"):
        st.write("""* **Đồng bằng sông Hồng:** có tỷ lệ thiếu việc làm thấp nhất do nền kinh tế phát triển đa dạng, nhu cầu lao động cao trong 
                 các lĩnh vực công nghiệp và dịch vụ, và hệ thống giáo dục phát triển.  Nhu cầu lao động cao trong các lĩnh vực này đã tạo ra 
                 nhiều cơ hội việc làm cho người lao động. Hệ thống giáo dục phát triển cũng góp phần cung cấp nguồn nhân lực chất lượng cao đáp 
                 ứng nhu cầu thị trường lao động.
* **Đồng bằng sông Cửu Long:** có tỷ lệ thiếu việc làm cao nhất do kinh tế chủ yếu dựa vào nông nghiệp, năng suất lao động thấp, ảnh hưởng của biến đổi khí hậu, hạn hán,  xâm nhập mặn,...
* **Đông Nam Bộ:** có tỷ lệ thiếu việc làm tương đối thấp do nền kinh tế phát triển mạnh mẽ. Nền  kinh tế khu vực này có tốc độ phát triển nhanh chóng, đặc 
                 biệt là trong các ngành công nghiệp và dịch vụ. Nhờ thu hút  được nhiều nguồn vốn đầu tư trong và ngoài nước, khu vực này đã tạo 
                 ra nhiều cơ hội việc làm cho người lao động.
* **Tây Nguyên:** có tỷ lệ thiếu việc làm tương đối thấp nhưng trong năm 2021 có 
                 tỷ lệ cao thứ 2 so với các vùng còn lại.  Nền kinh tế chủ yếu dựa vào nông nghiệp và lâm nghiệp, với năng suất lao động thấp do 
                 điều kiện tự nhiên khó khăn. Mùa vụ không đồng đều cũng dẫn đến tình trạng thiếu việc làm vào một số thời điểm trong năm. Bên cạnh 
                 đó, khu vực này cũng chịu ảnhhưởng nặng nề bởi biến đổi khí hậu, hạn hán,...
* **Bắc Trung Bộ và duyên hải miền Trung:** có tỷ lệ thiếu việc làm ở mức trung bình do nền kinh tế phát triển đa dạng nhưng năng suất lao động 
                 nhìn chung vẫn thấp hơn so với các khu vực khác. Thiên tai, bão lũ cũng là những yếu tố ảnh hưởng đến thị trường lao động ở khu vực này.
* **Trung du và miền núi phía Bắc:** có tỷ lệ thiếu việc làm ở mức trung bình do nền kinh tế chủ yếu dựa vào nông nghiệp và lâm nghiệp, năng suất lao động 
                 thấp và mức độ phát triển kinh tế - xã hội thấp.""")


    # Tạo biểu đồ thanh theo dõi tỷ lệ nhập cư của theo năm 
    trace_immigration = go.Bar(x=immigration_df.groupby('Năm')['Tỷ suất nhập cư'].mean().index,
                            y=immigration_df.groupby('Năm')['Tỷ suất nhập cư'].mean().values, name='Tỷ suất nhập cư')
    # Tạo biểu đồ thanh theo dõi tỷ lệ xuất cư của theo năm 
    trace_migration = go.Bar(x=migration_df.groupby('Năm')['Tỷ suất xuất cư'].mean().index,
                            y=migration_df.groupby('Năm')['Tỷ suất xuất cư'].mean().values, name='Tỷ suất xuất cư')    
    # Tạo biểu đồ thanh theo dõi tỷ lệ thiếu việc làm theo năm
    trace_combined_region = go.Bar(x=region_df.groupby('Năm')['Tỷ lệ thiếu việc làm'].mean().index,
                            y=region_df.groupby('Năm')['Tỷ lệ thiếu việc làm'].mean().values, name='Tỷ lệ thiếu việc làm')
    
    # Layout
    layout = go.Layout(title='Tình trạng xuất nhập cư gây ảnh hưởng đến tình trạng thiếu việc làm của các năm từ 2018 đến 2022',
                    xaxis=dict(title='Năm'),
                    yaxis=dict(title='Tỷ lệ (%)'),
                    width=1000, height=600)
    
    # Combine 
    fig = go.Figure(data=[ trace_combined_region,trace_immigration,trace_migration], layout=layout)

    # Hiển thị biểu đồ trên Streamlit
    st.plotly_chart(fig)

    with st.expander("📝See note:"):
        st.write("""- **Tỷ suất nhập cư cao:** Tỷ suất nhập cư tăng có thể tạo ra một lượng lớn lao động mới nhập cư vào thị trường lao động.
                  Điều này có thể tạo ra một áp lực tăng về cạnh tranh trong việc tìm kiếm việc làm, đặc biệt là trong các ngành nghề nơi mà 
                 lao động nhập cư thường tìm kiếm việc làm.
- **Tỷ suất xuất cư cao:** Tỷ suất xuất cư tăng, điều này có thể gây ra một số vấn đề cho tình trạng thiếu việc làm ở Việt Nam. Cụ thể,
                  người lao động Việt Nam rời bỏ nước để tìm kiếm cơ hội việc làm tốt hơn ở nước ngoài. Điều này có thể làm giảm áp lực 
                 đối với thị trường lao động nội địa, nhưng cũng có thể tạo ra một hiện tượng thiếu hụt lao động trong một số ngành 
                 nghề, đặc biệt là các ngành nghề đòi hỏi kỹ năng cao.""")

if choice =="Bản đồ":
    st.sidebar.image("streamlit_report/pic/gif_gunner.gif", use_column_width=True)
    st.title("🗺 Bản đồ thể hiện tình trạng thất nghiệp và thiếu việc làm theo địa phương")
    st.info("""Biểu đồ heatmap thể thể hiện tình trạng thất nghiệp/ thiếu việc làm ở các khu vực khác nhau của Việt Nam trên bản đồ.\n\n Các 
            màu sắc khác nhau có thể biểu thị mức độ của tỷ lệ thất nghiệp và thiếu liệc làm, giúp phát hiện ra các khu vực có mức độ thất 
            nghiệp cao hơn so với các khu vực khác.""")
    
    #Tạo tab
    unemployment = 'Tình trạng thất nghiệp'
    underemployment = 'Tình trạng thiếu việc làm'
    tabs = [unemployment, underemployment]
    option_data = [{'icon': "🔅", 'label': unemployment},
                   {'icon': "🔆", 'label': underemployment}]
    # Layout
    over_theme = {'txc_inactive': 'black', 'menu_background': '#CEDCF7', 'txc_active': 'white', 'option_active': '#789EF1'}
    font_fmt = {'font-class': 'h3', 'font-size': '50%'}
    # 
    chosen_tab = hc.option_bar(
        option_definition=option_data,
        title='',
        key='PrimaryOptionx',
        override_theme=over_theme,
        horizontal_orientation=True)
    
    if chosen_tab == unemployment:
        un_2018_df.rename(columns={'Chung': 'Chung_2018', 'Thành thị':'TT_2018','Nông thôn':'NT_2018'}, inplace=True)
        un_2019_df.rename(columns={'Chung': 'Chung_2019', 'Thành thị':'TT_2019','Nông thôn':'NT_2019'}, inplace=True)
        un_2020_df.rename(columns={'Chung': 'Chung_2020', 'Thành thị':'TT_2020','Nông thôn':'NT_2020'}, inplace=True)
        un_2021_df.rename(columns={'Chung': 'Chung_2021', 'Thành thị':'TT_2021','Nông thôn':'NT_2021'}, inplace=True)
        un_2022_df.rename(columns={'Chung': 'Chung_2022', 'Thành thị':'TT_2022','Nông thôn':'NT_2022'}, inplace=True)
        un_2018_df = un_2018_df[['Tỉnh', 'Chung_2018', 'TT_2018', 'NT_2018']]
        un_2019_df = un_2019_df[['Tỉnh', 'Chung_2019', 'TT_2019', 'NT_2019']]
        un_2020_df = un_2020_df[['Tỉnh', 'Chung_2020', 'TT_2020', 'NT_2020']]
        un_2021_df = un_2021_df[['Tỉnh', 'Chung_2021', 'TT_2021', 'NT_2021']]
        un_2022_df = un_2022_df[['Tỉnh', 'Chung_2022', 'TT_2022', 'NT_2022']]
        # Kết hợp các DataFrame theo cột 'Tỉnh'
        combined_un_province_df = pd.merge(un_2018_df, un_2019_df, on='Tỉnh')
        combined_un_province_df = pd.merge(combined_un_province_df, un_2020_df, on='Tỉnh')
        combined_un_province_df = pd.merge(combined_un_province_df, un_2021_df, on='Tỉnh')
        combined_un_province_df = pd.merge(combined_un_province_df, un_2022_df, on='Tỉnh')
        combined_un_df = pd.merge(location_df, combined_un_province_df, on='Tỉnh')

        # Tình trung bình để xác định vị trí trung tâm hiển thị bản đồ
        mean_latitude = location_df['Vĩ độ'].mean()
        mean_longitude = location_df['Kinh độ'].mean()
        mymap = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=6)

        # Tạo Selectbox từ năm 2018 đến 2022
        selected_year = st.selectbox('**Bản đồ tỷ lệ thất nghiệp năm:**', ['2018-2022',2018, 2019, 2020, 2021, 2022])
        if selected_year=='2018-2022':
            left_column, right_column = st.columns([2.6,0.4])
            with right_column:
                choice = st.radio("", ["Chung", "Thành thị", "Nông thôn"], key='radio_choice')
                    
            with left_column:
                if choice=="Chung":
                    # Tính trung bình của mỗi tỉnh
                    combined_un_province_df['avg_province'] = combined_un_province_df[['Chung_2018','Chung_2019', 'Chung_2020', 'Chung_2021', 'Chung_2022']].mean(axis=1)
                    # Chuyển đổi kiểu dữ liệu của cột 'avg' thành float64
                    combined_un_province_df['avg_province'] = combined_un_province_df['avg_province']
                    # Kết hợp với DataFrame location_df
                    combined_un_df = pd.merge(location_df, combined_un_province_df, on='Tỉnh')
                    # Tạo dữ liệu heatmap từ combined_un_df
                    heatmap_data = combined_un_df[['Vĩ độ', 'Kinh độ', 'avg_province']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)
                    # Hiển thị bản đồ trong Streamlit
                    folium_static(mymap, width=900, height=700)

                    with st.expander("📝See note:"):
                        st.write("""**Trong 5 năm từ 2018 đến 2022, thành phố Đà Nẵng là tỉnh, thành phố có tỷ lệ thất nghiệp cao nhất.**
* **Đà Nẵng** là một trong những điểm du lịch hàng đầu của Việt Nam. Đại dịch COVID-19 đã gây ra sự suy giảm mạnh mẽ trong lưu lượng 
                                khách du lịch tới Đà Nẵng. Sự sụt giảm này đã tác động mạnh đến các ngành liên quan đến du lịch dẫn đến việc 
                                giảm số lượng việc làm trong những ngành này.
* **Tỉnh Lạng Sơn** là một tỉnh miền núi nằm ở phía Bắc Việt Nam, với điều kiện kinh tế còn nhiều khó khăn. Ngành công nghiệp và dịch vụ tại đây
                                  phát triển chậm do thiếu đầu tư và đào tạo nghề. Do đó, chất lượng lao động vẫn chưa cao, lực lượng lao động 
                                 có xu hướng tăng trưởng chậm với trình độ thấp, dẫn đến tỷ lệ thất nghiệp cao.
* **Thành phố Hồ Chí Minh** là trung tâm kinh tế, thương mại và tài chính lớn nhất cả nước,  với tốc độ tăng trưởng kinh tế luôn ở mức cao. Các 
                                 ngành công nghiệp, dịch vụ và xây dựng tại đây luôn có nhu cầu lao động lớn với số lượng lớn. Bên cạnh đó,  
                                 **Thành phố Hồ Chí Minh** là thành phố đông dân nhất Việt Nam, với dân số hơn 9 triệu người.  Mỗi năm, có hàng 
                                 trăm nghìn người từ các tỉnh thành khác đến thành phố này lập nghiệp, vì thế nguồn cung lao động tại đây ngày 
                                 càng tăng nhanh. Tuy nguồn lao động tại thành phố luôn dồi dào, nhưng trình độ tay nghề và kỹ năng chuyên môn 
                                 của nhiều lao động vẫn còn hạn chế, không đáp ứng được yêu cầu của thị trường lao động. Điều này dẫn đến tình 
                                 trạng thất nghiệp ngày càng cao tại thành phố này.
* Vùng tập trung các tỉnh thành phố có màu đậm hơn tập trung ở vùng **Đồng Bằng Sông Cửu Long**. **Đồng Bằng Sông Cửu Long** là một trong 
                                 những vùng lớn nhất về nông nghiệp và ngư nghiệp tại Việt Nam. Tuy nhiên, các ngành này thường phụ thuộc nhiều 
                                 vào yếu tố thiên nhiên và có thể gặp phải các vấn đề như thiếu nước, sạt lở đất và sự biến động của thị trường. 
                                 Điều này dẫn đến sự không ổn định của nguồn thu nhập và đời sống của người dân trong vùng. Bên cạnh đó, Đồng Bằng 
                                 Sông Cửu Long có dân số đông đúc, đặc biệt là ở các tỉnh và thành phố lớn như **Cần Thơ** và các tỉnh **Đồng Tháp,
                                  An Giang**. Sự tập trung dân số có thể tạo ra áp lực lớn đối với cơ sở hạ tầng và thị trường lao động.""")

                if choice=="Thành thị":
                    combined_un_province_df['avg_tt'] = combined_un_province_df[['TT_2018','TT_2019', 'TT_2020', 'TT_2021', 'TT_2022']].mean(axis=1)
                    # Chuyển đổi kiểu dữ liệu của cột 'avg' thành float64
                    combined_un_province_df['avg_tt'] = combined_un_province_df['avg_tt'].astype('float64')
                    combined_un_df = pd.merge(location_df, combined_un_province_df, on='Tỉnh')
                    # Tạo dữ liệu heatmap từ combined_un_df
                    heatmap_data = combined_un_df[['Vĩ độ', 'Kinh độ', 'avg_tt']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)
                    st.write("**Phân theo thành thị:**")
                    folium_static(mymap, width=900, height=800)
                    with st.expander("📝See note:"):
                        st.write("""**Ở khu vực thành thị**, thường có nhiều cơ hội việc làm hơn so với nông thôn do sự tập trung của các 
                                 doanh nghiệp, công ty, cơ sở sản xuất và dịch vụ. Tuy nhiên, với số lượng lớn người lao động di chuyển 
                                 đến thành thị để tìm kiếm cơ hội việc làm, cạnh tranh cho các vị trí công việc thường cao hơn, dẫn đến 
                                 tình trạng thất nghiệp tăng.""")

                if choice=="Nông thôn":
                    combined_un_province_df['avg_nt'] = combined_un_province_df[['NT_2018','NT_2019', 'NT_2020', 'NT_2021', 'NT_2022']].mean(axis=1)
                    # Chuyển đổi kiểu dữ liệu của cột 'avg' thành float64
                    combined_un_province_df['avg_nt'] = combined_un_province_df['avg_nt'].astype('float64')
                    combined_un_df = pd.merge(location_df, combined_un_province_df, on='Tỉnh')
                    # Tạo dữ liệu heatmap từ combined_un_df
                    heatmap_data = combined_un_df[['Vĩ độ', 'Kinh độ', 'avg_nt']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)

                    st.write("**Phân theo nông thôn:**")
                    folium_static(mymap, width=900, height=800)
                    with st.expander("📝See note:"):
                        st.write("""**Ở khu vực nông thôn**, cơ hội việc làm thường ít hơn so với thành thị do sự thiếu hụt các doanh 
                                 nghiệp và cơ sở kinh doanh lớn. Đây là do nông thôn thường tập trung vào các ngành nghề chủ yếu như nông 
                                 nghiệp và chăn nuôi, ít có các cơ sở sản xuất lớn hoặc dịch vụ đa dạng. Hơn nữa, thiếu hụt hạ tầng và dịch 
                                 vụ cơ bản như giáo dục, y tế và giao thông ở nông thôn khiến cho việc tạo ra và duy trì các công việc trở 
                                 nên khó khăn. Những rào cản này giảm đi khả năng tiếp cận của người dân nông thôn với các cơ hội việc làm""")
                        
        else:
            left_column, right_column = st.columns([2.6,0.4])
            with right_column:
                choice = st.radio("", ["Chung", "Thành thị", "Nông thôn"], key='radio_choice')

            with left_column:
                if choice=="Chung":
                    # Lọc dữ liệu heatmap theo năm được chọn
                    heatmap_data = combined_un_df[['Vĩ độ', 'Kinh độ', f'Chung_{selected_year}']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)
                    # Hiển thị bản đồ trong Streamlit
                    folium_static(mymap, width=900, height=800)
                    
                if choice=="Thành thị":
                    # Lọc dữ liệu heatmap theo năm được chọn
                    heatmap_data = combined_un_df[['Vĩ độ', 'Kinh độ', f'TT_{selected_year}']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)
                    # Hiển thị bản đồ trong Streamlit
                    st.write("**Phân theo thành thị:**")
                    folium_static(mymap, width=900, height=800)
                
                if choice=="Nông thôn":
                    # Lọc dữ liệu heatmap theo năm được chọn
                    heatmap_data = combined_un_df[['Vĩ độ', 'Kinh độ', f'NT_{selected_year}']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)
                    # Hiển thị bản đồ trong Streamlit
                    st.write("**Phân theo nông thôn:**")
                    folium_static(mymap, width=900, height=700)


    if chosen_tab == underemployment:
        # Đổi tên cột 'Chung' để tránh xung đột
        under_2018_df.rename(columns={'Chung': 'Chung_2018', 'Thành thị':'TT_2018','Nông thôn':'NT_2018'}, inplace=True)
        under_2019_df.rename(columns={'Chung': 'Chung_2019', 'Thành thị':'TT_2019','Nông thôn':'NT_2019'}, inplace=True)
        under_2020_df.rename(columns={'Chung': 'Chung_2020', 'Thành thị':'TT_2020','Nông thôn':'NT_2020'}, inplace=True)
        under_2021_df.rename(columns={'Chung': 'Chung_2021', 'Thành thị':'TT_2021','Nông thôn':'NT_2021'}, inplace=True)
        under_2022_df.rename(columns={'Chung': 'Chung_2022', 'Thành thị':'TT_2022','Nông thôn':'NT_2022'}, inplace=True)
        under_2018_df = under_2018_df[['Tỉnh', 'Chung_2018', 'TT_2018', 'NT_2018']]
        under_2019_df = under_2019_df[['Tỉnh', 'Chung_2019', 'TT_2019', 'NT_2019']]
        under_2020_df = under_2020_df[['Tỉnh', 'Chung_2020', 'TT_2020', 'NT_2020']]
        under_2021_df = under_2021_df[['Tỉnh', 'Chung_2021', 'TT_2021', 'NT_2021']]
        under_2022_df = under_2022_df[['Tỉnh', 'Chung_2022', 'TT_2022', 'NT_2022']]
        # Kết hợp các DataFrame theo cột 'Tỉnh'
        combined_under_province_df = pd.merge(under_2018_df, under_2019_df, on='Tỉnh')
        combined_under_province_df = pd.merge(combined_under_province_df, under_2020_df, on='Tỉnh')
        combined_under_province_df = pd.merge(combined_under_province_df, under_2021_df, on='Tỉnh')
        combined_under_province_df = pd.merge(combined_under_province_df, under_2022_df, on='Tỉnh')
        combined_under_df = pd.merge(location_df, combined_under_province_df, on='Tỉnh')
        mean_latitude = combined_under_df['Vĩ độ'].mean()
        mean_longitude = combined_under_df['Kinh độ'].mean()
        mymap = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=6)
        # ------------------------------------------------
            # Tạo Selectbox từ năm 2018 đến 2022
        selected_year = st.selectbox('**Bản đồ tỷ lệ thiếu việc làm năm:**', ['2018-2022',2018, 2019, 2020, 2021, 2022])
        if selected_year=='2018-2022':
            left_column , right_column = st.columns([2.6,0.4])

            with right_column:
                choice = st.radio("", ["Chung", "Thành thị", "Nông thôn"], key='radio_choice')
            with left_column:
                if choice=="Chung":
                    # Tính trung bình của mỗi tỉnh
                    combined_under_province_df['avg_province'] = combined_under_province_df[['Chung_2018','Chung_2019', 'Chung_2020', 'Chung_2021', 'Chung_2022']].mean(axis=1)
                    # Chuyển đổi kiểu dữ liệu của cột 'avg' thành float64
                    combined_under_province_df['avg_province'] = combined_under_province_df['avg_province'].astype('float64')
                    # Kết hợp với DataFrame location_df
                    combined_under_df = pd.merge(location_df, combined_under_province_df, on='Tỉnh')

                    # Tạo dữ liệu heatmap từ combined_under_df
                    heatmap_data = combined_under_df[['Vĩ độ', 'Kinh độ', 'avg_province']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)

                    # Hiển thị bản đồ trong Streamlit
                    folium_static(mymap, width=900, height=800)
                    with st.expander("📝See note:"):
                        st.write("""* **Đắk Lắk** là một trong những tỉnh có nền kinh tế nông nghiệp phát triển, nhưng ngành này thường gặp phải 
                                 những thách thức như sự thiếu hụt vốn đầu tư, công nghệ lạc hậu và khí hậu không ổn định. Ngoài ra, sự chuyển 
                                 dịch từ nông nghiệp sang công nghiệp thường chậm trễ, dẫn đến sự phụ thuộc lớn vào lao động nông thôn và một 
                                 tỷ lệ thất nghiệp cao.
* **Đồng Bằng sônng Cửu Long** là một trong những vùng đất có mật độ 
                                 dân số cao nhất ở Việt Nam. Sự gia tăng dân số, đặc biệt là ở các thành phố và thị trấn lớn, có thể tạo ra áp lực 
                                 lớn cho thị trường lao động và gây ra tình trạng thiếu việc làm. Đồng Bằng sông Cửu Long chủ yếu làm việc trong 
                                 ngành nông nghiệp, nhưng sự phát triển của ngành công nghiệp và dịch vụ ở khu vực này không đồng đều,gây ra sự 
                                 không ổn định trong nền kinh tế và việc làm.
    Trong đó có 2 tỉnh/thành phố có tỷ lệ thất nghiệp cao nhất nước, đó là:
    * **Vĩnh Long** là một tỉnh nằm trong khu vực Đồng bằng sông Cửu Long, nền kinh tế chủ yếu là nông nghiệp và các ngành công nghiệp như chế biến 
                                 thực phẩm, dệt may và xây dựng. Nếu có sự suy giảm trong các ngành này hoặc nhu cầu lao động không đủ để đáp ứng, 
                                 tỷ lệ thiếu việc làm có thể tăng lên.
    * **Rạch Giá** chủ yếu phụ thuộc vào một số ngành nghề cụ thể như nông nghiệp hoặc ngư nghiệp, thì khi có biến động trong các ngành này (như 
                                 thời tiết xấu, giảm sản lượng, hoặc vấn đề môi trường), có thể dẫn đến tăng tỷ lệ thiếu việc làm.""")

                if choice=="Thành thị":
                    combined_under_province_df['avg_tt'] = combined_under_province_df[['TT_2018','TT_2019', 'TT_2020', 'TT_2021', 'TT_2022']].mean(axis=1)
                    # Chuyển đổi kiểu dữ liệu của cột 'avg' thành float64
                    combined_under_province_df['avg_tt'] = combined_under_province_df['avg_tt'].astype('float64')
                    combined_under_df = pd.merge(location_df, combined_under_province_df, on='Tỉnh')
                    # Tạo dữ liệu heatmap từ combined_under_df
                    heatmap_data = combined_under_df[['Vĩ độ', 'Kinh độ', 'avg_tt']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)

                    st.write(f"Phân theo thành thị:")
                    folium_static(mymap, width=900, height=800)
                    with st.expander("📝See note:"):
                        st.write("""**Ở thành thị**, thị trường lao động của các thành phố thường rất cạnh tranh, đặc biệt là trong các 
                                 ngành nghề phổ biến như dịch vụ, bán lẻ và công nghệ thông tin. Người lao động có thể gặp khó khăn trong 
                                 việc tìm kiếm việc làm phù hợp với kỹ năng và kinh nghiệm của họ. Ngoài ra, sự di cư từ các khu vực nông 
                                 thôn hoặc các khu vực khác có thể tạo ra sự cạnh tranh trong thị trường lao động đô thị, đặc biệt là trong 
                                 các ngành nghề phổ biến.""")

                if choice=="Nông thôn":
                    combined_under_province_df['avg_nt'] = combined_under_province_df[['NT_2018','NT_2019', 'NT_2020', 'NT_2021', 'NT_2022']].mean(axis=1)
                    # Chuyển đổi kiểu dữ liệu của cột 'avg' thành float64
                    combined_under_province_df['avg_nt'] = combined_under_province_df['avg_nt'].astype('float64')

                    combined_under_df = pd.merge(location_df, combined_under_province_df, on='Tỉnh')

                    # Tạo dữ liệu heatmap từ combined_under_df
                    heatmap_data = combined_under_df[['Vĩ độ', 'Kinh độ', 'avg_nt']].values.tolist()

                    # Thêm heatmap vào bản đồs
                    HeatMap(heatmap_data).add_to(mymap)

                    folium_static(mymap, width=900, height=800)

                    st.write(f"Phân theo nông thôn:")
                    with st.expander("📝See note:"):
                        st.write("""**Nông thôn**, Một số vùng gặp phải thách thức lớn về trình độ giáo dục và kỹ năng lao động. Do người dân 
                                 thiếu trình độ giáo dục và kỹ năng phù hợp với nhu cầu thị trường lao động, họ gặp khó khăn trong việc tìm
                                  kiếm việc làm. Hơn nữa, nông thôn thường phụ thuộc chủ yếu vào ngành nông nghiệp để có nguồn thu nhập. Nếu 
                                  ngành nông nghiệp gặp sự suy giảm do tác động của biến đổi khí hậu, tỷ lệ thiếu việc làm có thể tăng lên.""")
                    
        else:
            left_column, right_column = st.columns([2,1])
            with right_column:
                choice = st.radio("", ["Chung", "Thành thị", "Nông thôn"], key='radio_choice')

            with left_column:
                if choice=="Chung":
                    # Lọc dữ liệu heatmap theo năm được chọn
                    heatmap_data = combined_under_df[['Vĩ độ', 'Kinh độ', f'Chung_{selected_year}']].values.tolist()
                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)

                    # Hiển thị bản đồ trong Streamlit
                    folium_static(mymap, width=900, height=800)

                if choice=="Thành thị":
                    # Lọc dữ liệu heatmap theo năm được chọn
                    heatmap_data = combined_under_df[['Vĩ độ', 'Kinh độ', f'TT_{selected_year}']].values.tolist()

                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)

                    # Hiển thị bản đồ trong Streamlit
                    st.write("**Phân theo thành thị:**")

                    folium_static(mymap, width=900, height=800)

                if choice=="Nông thôn":
                    # Lọc dữ liệu heatmap theo năm được chọn
                    heatmap_data = combined_under_df[['Vĩ độ', 'Kinh độ', f'NT_{selected_year}']].values.tolist()

                    # Thêm heatmap vào bản đồ
                    HeatMap(heatmap_data).add_to(mymap)

                    # Hiển thị bản đồ trong Streamlit
                    st.write("**Phân theo nông thôn:**")
                    folium_static(mymap, width=900, height=800)