import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_plotly_events import plotly_events

st.title("**📁 Mô tả dữ liệu**")
region_df= pd.read_csv('streamlit_report/data_csv/Region.csv')
age_df= pd.read_csv('streamlit_report/data_csv/Age.csv')
career_df= pd.read_csv('streamlit_report/data_csv/Career.csv')
academic_df= pd.read_csv('streamlit_report/data_csv/Academic.csv')
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

dataframes = [region_df, age_df, career_df, academic_df, gender_df, location_df, birth_df, migration_df, immigration_df,
              un_2018_df, un_2019_df, un_2020_df, un_2021_df, un_2022_df,
              under_2018_df, under_2019_df, under_2020_df, under_2021_df, under_2022_df]

# Tạo một từ điển để lưu số lượng dòng dữ liệu của mỗi DataFrame

row_counts = {}
unemployment_row_counts = {}
underemployment_row_counts = {}
total_row_count = 0
total_unemployment_row_count = 0
total_underemployment_row_count = 0

# Lặp qua từng DataFrame và đếm số lượng dòng dữ liệu cũng như dòng dữ liệu có cột 'Tỷ lệ thất nghiệp' và 'Tỷ lệ thiếu việc làm'
for df_name, df in zip(["region_df", "age_df", "career_df",
                         "academic_df", "gender_df", "location_df", 
                         "birth_df", "migration_df", "immigration_df"], dataframes):
    row_counts[df_name] = df.shape[0]
    total_row_count += df.shape[0]
    if 'Tỷ lệ thất nghiệp' in df.columns:
        unemployment_row_counts[df_name] = df[df['Tỷ lệ thất nghiệp'].notnull()].shape[0]
        total_unemployment_row_count += unemployment_row_counts[df_name]
    else:
        unemployment_row_counts[df_name] = 0
    if 'Tỷ lệ thiếu việc làm' in df.columns:
        underemployment_row_counts[df_name] = df[df['Tỷ lệ thiếu việc làm'].notnull()].shape[0]
        total_underemployment_row_count += underemployment_row_counts[df_name]
    else:
        underemployment_row_counts[df_name] = 0


unemploy = [un_2018_df, un_2019_df, un_2020_df, un_2021_df, un_2022_df]
row_counts_un_province = {}
total_row_counts_un_province = 0

# Lặp qua từng DataFrame liên quan đến 'Tỷ lệ thất nghiệp' theo từng năm và tính tổng số lượng dòng dữ liệu
for df_name_un_province, df_un_province in zip(["un_2018_df", "un_2019_df", "un_2020_df", "un_2021_df", "un_2022_df"], unemploy):
    row_counts_un_province[df_name_un_province] = df_un_province.shape[0]
    total_row_counts_un_province += df_un_province.shape[0]

underemployed=[under_2018_df, under_2019_df, under_2020_df, under_2021_df, under_2022_df]
row_counts_under_province = {}
total_row_counts_under_province = 0
for df_name_under_province, df_under_province in zip(["under_2018_df","under_2019_df","under_2020_df","under_2021_df","under_2022_df"], underemployed):
    row_counts_under_province[df_name_under_province] = df_under_province.shape[0]
    total_row_counts_under_province += df_under_province.shape[0]


total= total_row_counts_under_province+total_row_counts_un_province+total_row_count
total_unemployment=total_row_counts_un_province+total_unemployment_row_count
total_underemployment=total_row_counts_under_province+total_underemployment_row_count

left_column, middle_column, right_column = st.columns(3)

with left_column:

    st.info(f'**🧮Tổng dữ liệu: {total}**')

with middle_column:
    st.info(f'**🧮Tổng dữ liệu thất nghiệp: {total_unemployment}**')

with right_column:
    st.info(f'**🧮Tổng dữ liệu thiếu việc làm: {total_underemployment}**')
st.markdown('---')



st.title("**Overview**")
tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([
 "Vùng kinh tế", "Giới tính", "Nhóm tuổi","Học vấn","Nhóm ngành","Tỉnh/thành phố","Vị trí","Tỷ suất sinh", "Tỷ suất xuất cư","Tỷ suất nhập cư"
 ])
with tab1:
 st.write('🌐Vùng kinh tế: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo vùng và giới tính của mỗi vùng từ năm 2018 đến năm 2022')
 profile_df = region_df.profile_report()
 st_profile_report(profile_df)
with tab2:
 st.write('⚧ Giới tính: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo giới tính từ năm 2018 đến năm 2022')
 profile_df = gender_df.profile_report()
 st_profile_report(profile_df)
with tab3:
 st.write('🧙 Nhóm tuổi: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo nhóm tuổi từ năm 2018 đến năm 2022')
 profile_df = age_df.profile_report()
 st_profile_report(profile_df)
with tab4:
 st.write('📖 Học vấn: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo trình độ học vấn từ năm 2018 đến năm 2022')
 profile_df = academic_df.profile_report()
 st_profile_report(profile_df)
with tab5:
 st.write('👝 Nhóm ngành: chứa dữ liệu về thiếu việc làm phân theo nhóm ngành từ năm 2018 đến năm 2022')
 profile_df = career_df.profile_report()
 st_profile_report(profile_df)
with tab6:
   st.write('🗾 Tỉnh/ thành phố: chứa dữ liệu về tỷ lệ thất nghiệp và tỷ lệ thiếu việc làm của mỗi tỉnh thành từ năm 2018 đến năm 2022')

   tab_un, tab_under= st.tabs(["Tỷ lệ thất nghiệp","Tỷ lệ thiếu việc làm"])
   with tab_un:
    tab2018, tab2019, tab2020,tab2021,tab2022 = st.tabs(["2018","2019","2020","2021","2022"])
    with tab2018:
     profile_df = un_2018_df.profile_report()
     st_profile_report(profile_df)
    with tab2019:
     profile_df = un_2019_df.profile_report()
     st_profile_report(profile_df)
    with tab2020:
     profile_df = un_2020_df.profile_report()
     st_profile_report(profile_df)
    with tab2021:
     profile_df = un_2021_df.profile_report()
     st_profile_report(profile_df)
    with tab2022:
     profile_df = un_2022_df.profile_report()
     st_profile_report(profile_df)
   with tab_under:
    tab2018, tab2019, tab2020,tab2021,tab2022 = st.tabs(["2018","2019","2020","2021","2022"])
    with tab2018:
     profile_df = under_2018_df.profile_report()
     st_profile_report(profile_df)
    with tab2019:
     profile_df = under_2019_df.profile_report()
     st_profile_report(profile_df)
    with tab2020:
     profile_df = under_2020_df.profile_report()
     st_profile_report(profile_df)
    with tab2021:
     profile_df = under_2021_df.profile_report()
     st_profile_report(profile_df)
    with tab2022:
     profile_df = under_2022_df.profile_report()
     st_profile_report(profile_df)
with tab7:
 st.write('📌 Vị trí: chứa dữ liệu về kinh độ và vĩ độ của mỗi tỉnh/ thành phố')

 profile_df = location_df.profile_report()
 st_profile_report(profile_df) 
with tab8:
 st.write('👨‍👩‍👧‍👦 Tỷ suất sinh:  đơn vị đo mức sinh được tính bằng tương quan giữa số trẻ sinh ra với số dân tương ứng tại một địa phương trong năm 2018 đến năm 2022.')

 profile_df = birth_df.profile_report()
 st_profile_report(profile_df)
with tab9:
 st.write('🏃 Tỷ suất xuất cư: phản ánh số người xuất cư của một đơn vị lãnh thổ trong thời kỳ nghiên cứu tính bình quân trên 1000 dân của đơn vị lãnh thổ đó trong năm 2018 đến năm 2022.')
 profile_df = migration_df.profile_report()
 st_profile_report(profile_df)
with tab10:
 st.write('🏃‍♀️ Tỷ suất nhập cư: phản ánh số người từ đơn vị lãnh thổ khác (nơi xuất cư) nhập cư đến một đơn vị lãnh thổ trong kỳ nghiên cứu tính bình quân trên 1000 dân của đơn vị lãnh thổ đó (nơi nhập cư) trong năm 2018 đến năm 2022.')
 profile_df = immigration_df.profile_report()
 st_profile_report(profile_df)







# st.write('🌐Vùng kinh tế: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo vùng và giới tính của mỗi vùng từ năm 2018 đến năm 2022')
# st.write('🧙 Nhóm tuổi: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo nhóm tuổi từ năm 2018 đến năm 2022')
# st.write('📖 Học vấn: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo trình độ học vấn từ năm 2018 đến năm 2022')
# st.write('⚧ Giới tính: chứa dữ liệu về tỷ lệ thất nghiệp và thiếu việc làm phân theo giới tính từ năm 2018 đến năm 2022')
# st.write('👝 Nhóm ngành: chứa dữ liệu về thiếu việc làm phân theo nhóm ngành từ năm 2018 đến năm 2022')
# st.write('🗾 Tỉnh/ thành phố: chứa dữ liệu về tỷ lệ thất nghiệp và tỷ lệ thiếu việc làm của mỗi tỉnh thành từ năm 2018 đến năm 2022')
# st.write('📌 Vị trí: chứa dữ liệu về kinh độ và vĩ độ của mỗi tỉnh/ thành phố')
# st.write('👨‍👩‍👧‍👦 Tỷ suất sinh:  đơn vị đo mức sinh được tính bằng tương quan giữa số trẻ sinh ra với số dân tương ứng tại một địa phương.')
# st.write('🏃 Tỷ suất xuất cư: phản ánh số người xuất cư của một đơn vị lãnh thổ trong thời kỳ nghiên cứu tính bình quân trên 1000 dân của đơn vị lãnh thổ đó.')
# st.write('🏃‍♀️ Tỷ suất nhập cư: phản ánh số người từ đơn vị lãnh thổ khác (nơi xuất cư) nhập cư đến một đơn vị lãnh thổ trong kỳ nghiên cứu tính bình quân trên 1000 dân của đơn vị lãnh thổ đó (nơi nhập cư).')



# tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([
#  "Vùng kinh tế", "Giới tính", "Nhóm tuổi","Học vấn","Nhóm ngành","Tỉnh/thành phố","Vị trí","Tỷ suất sinh", "Tỷ suất xuất cư","Tỷ suất nhập cư"
#  ])
# with tab1:
#  st.write(region_df)
# with tab2:
#  st.write(gender_df)
# with tab3:
#  st.write(age_df)
# with tab4:
#  st.write(academic_df)
# with tab5:
#  st.write(career_df)
# with tab6:
#    tab_un, tab_under= st.tabs(["Tỷ lệ thất nghiệp","Tỷ lệ thiếu việc làm"])
#    with tab_un:
#     tab2018, tab2019, tab2020,tab2021,tab2022 = st.tabs(["2018","2019","2020","2021","2022"])
#     with tab2018:
#      st.write(un_2018_df)
#     with tab2019:
#      st.write(un_2019_df)
#     with tab2020:
#      st.write(un_2020_df)
#     with tab2021:
#      st.write(un_2021_df)
#     with tab2022:
#      st.write(un_2022_df)
#    with tab_under:
#     tab2018, tab2019, tab2020,tab2021,tab2022 = st.tabs(["2018","2019","2020","2021","2022"])
#     with tab2018:
#      st.write(under_2018_df)
#     with tab2019:
#      st.write(under_2019_df)
#     with tab2020:
#      st.write(under_2020_df)
#     with tab2021:
#      st.write(under_2021_df)
#     with tab2022:
#      st.write(under_2022_df)
# with tab7:
#  st.write(location_df)
# with tab8:
#  st.write(birth_df)
# with tab9:
#  st.write(migration_df)
# with tab10:
#  st.write(immigration_df)


