import streamlit as st
import pandas as pd
import numpy as np

st.header("**Star Lord'un Uzay Verileri - Star Lord's Space Data's**")
st.markdown("Ben **Süleyman Kaplan**. **Star Lord** olarak kendimi veri biliminde geliştirmekteyim. "
            "**Uzay ve Uydu Mühendisliği** 1. sınıf öğrencisi olarak eğitim hayatıma devam etmekteyim. **ABD Ankara"
            "Büyükelçiliği** ve TED Koleji'nin düzenlediği ACCESS Projesini derece ile tamamladım. "
            "Kısa bir süre Teknofest Roket Takımında Ar-Ge Sorumlusu olarak görev yaptım. "
            "**Defence Turk**'te Editör olarak **Takım Uydular, Fırlatma Sistemleri** ve **Uzay Teleskopları** konularında dergi yazısı yazdım. "
            "**T3 Girişim Merkezi Girişimci Yetiştirme Programı**'ndan Girişimci Adayı unvanı ile mezun oldum. "
            "**CarryVibe Logistics Technologies** adlı girişimimde iş geliştirme, tasarım, planlama ve bağlantı oluşturma konularında kurucu ortak ve takım lideri görevlerini yürütmekteyim. "
            "Şu anda **veri bilimi, makine öğrenmesi** ve **MBA** alanlarında kendimi geliştirmekteyim.")




st.subheader("SpaceX Görevleri (2006-Şimdi)")
spacex_data = pd.read_csv("spacex_missions.csv")
st.dataframe(spacex_data)


st.subheader("100 Adet Havalimanının Uzaydan Görüntüleri")
airport_data = pd.read_csv("airport_desc.csv", encoding = 'latin1')
st.dataframe(airport_data)

