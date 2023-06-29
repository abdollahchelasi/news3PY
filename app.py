import requests
import streamlit as st

st.set_page_config(page_title="خبر3",page_icon="https://cdn-icons-png.flaticon.com/512/330/330703.png")


st.text('خبر 3')


tt = st.text_input("اخبار کدام تیم رو دنبال می کنید ؟ ")

st.button(f"بزن📝 {tt}")



st.text("آخرین خبرهای ورزشی")

st.divider()

    





with open('c.css') as f:
    
    
    st.markdown(f'<style> {f.read()} </style>',unsafe_allow_html=True)
    
st.markdown("""<style>
              
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>""",unsafe_allow_html=True)


r = requests.get(f'https://search-api.varzesh3.com/v1.0/query?q={tt}')

x = r.json()



for i in x['news']:
    
    
    
    st.write(i['title'])
    st.success(i['persianPublishedOn'])
    st.image(i['picture'])
    st.write(i['shortDescription'])
    st.write('-----------------')





st.markdown("[ طراحی شده توسط عبدالله چلاسی](https://abdollahchelasi.ir)")
