import streamlist as st # type: ignore
import pandas as pd # type: ignore
import os
from io import BytesIO

st.set_page_config(page_title == "Data Sweeper",layout-'wide') # type: ignore

#CUSTOM CSS
st.markdown(
    """
   <style>
   .stApp{
         background-color :black;
        color:white;
   } 
   </style>
    """,
    unsafe_allow_html=True
)

#TITLE AND DESCRIPTION 
st.title("Datasweeper Sterling Integrator By Sania Shakeel")
st.write("Transform your files between CSV and Excel formulas with built-in data clearing and visualization Creating the project for Quater 3!")

#FILE UPLOADER
uploaded_files = st.file_uploader("Upload your files (accepts CSV or Excel):", type:["cvs","xlsx"],accept_multiple_files=(True))

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == "xlsx":   
            df = pd.read_excel(file)
        else:
                st.error(f"Unsupported file type:{file_ext}") 
                continue

#FILE DETAILS
st.write("Preview the head of the Dataframe")
st.dataframe(df.head())

#DATA CLEANING OPTION 
st.subheader("dta Cleaning Options")
if st.checkbox(f"Clean data for {file.name}"):
    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"Remove duplicates from the file : {file.name}"):
            df.drop_duplicates(inplace=True)
            st.write("Duplicates removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(includes =['number']).columns 
                df[numeric_cols] = df [numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing values have been filled!")

        st.subheader ("Select Columns to keep")
        columns = st.multiselect(f"Choose columns for { file.name}",df.columns,default=df.columns)
        df = df[columns]


    #DATA VISUALIZATION
    st.subheader("Dta Visualization")
    if st.checkbox(f"show visualization for {file.name}"):
                st. bar_chart(df.select_dtypes(include='number').iloc[:,:2])
                
    #CONVERSATION OPTION
                
    st.subheader("Conversation options")
    conversation_type = st.radio (f"Convert {file.name} to:",["CVS" , "Excel"],key=file.name)
    if st.button(f"Convert{file.name}"):
         buffer = BytesIO()
         if conversation_type =="CSV":
              df.to.csv(buffer, index=False)
              file_name = file.name.replace(file_ext, ".csv")
              mine_type = "text/csv"

         elif conversation_type == "Excel":
              df.to.to_excel(buffer, index=False)
              file_name = file.name.replace(file_ext, ".xlsx")
              mine_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
              buffer.seek(0)


st.download_button(
     label=f"Download {file.name} as {conversation_type}",
     data=buffer,
     file_name=file_name,
     mine=mine_type
)
st.success(" All files processed successfully!")