#import required libraries

import streamlit as st
import pandas as pd
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

#Define the main function 

def main():
    # Streamlit app title
    logo = Image.open("frddet.jpg")  # Replace with your logo path
    
    st.image(logo, width=800)
    st.title("Fraud Detection in Treasury Management System")
    st.subheader("Outliers Prediction by Various Models:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
      button1 = st.button('DBSCAN Clustering')

      if button1:
        df1=pd.read_csv("dbscan_outliers_output.csv")
        st.write("Total Outliers Count :",len(df1))
        st.write(df1)

    with col2:
      button2 = st.button('K-Means Clustering')

      if button2:
        df2=pd.read_csv("k_means_anomalies_output.csv")
        st.write("Total Outliers Count :",len(df2))
        st.write(df2)

    with col3:
      button3 = st.button('Isolation Forest')

      if button3:
        df3=pd.read_csv("Isolation_Forest_anomalies_output.csv")
        st.write("Total Outliers Count :",len(df3))
        st.write(df3)

    with col4:
      button4 = st.button('Hierarchical Clustering')

      if button4:
        df4=pd.read_csv("hierarchical_output.csv")
        anomalies = df4[df4['Anomaly'] == 1]
        
        st.write("Total Outliers Count :",len(anomalies))
        st.write(df4)
    



if __name__ == "__main__":
    #Call the main function
    main()
