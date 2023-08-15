import logging
import streamlit as st
from models.spotify_model import Spotify_Model
from views.search_result import artist_search_result

def main():
    logging.basicConfig(level=logging.INFO)
    spotify = Spotify_Model()
    menu = ['Home', 'About']
    choice = st.sidebar.selectbox("Menu", menu)

    st.title('Spotify Dashboard')

    if choice == 'Home':
        st.subheader('Home')
        with st.form(key='searchform'):
            nav1, nav2 = st.columns([2,1])

            with nav1:
                search_term = st.text_input('Search Artist')

            with nav2:
                submit_search = st.form_submit_button(label='Search')
            
        # st.success('You seached for {}.'.format(search_term))

        col1, col2 = st.columns([2,1])

        with col1:
            if submit_search:
                search_results = spotify.query_artists(search_term)
                num_of_results = len(search_results)
                st.subheader('Showing {} artists for `{}`:'.format(num_of_results, search_term))
                if num_of_results > 0:
                    for item in search_results:
                        id, name, genres, popularity, num_followers, images = item['id'], item['name'], item['genres'], item['popularity'], item['followers'], item['images']
                        st.markdown(artist_search_result(item), unsafe_allow_html=True)
            

    elif choice == 'About':
        st.subheader('About')
    

if __name__ == '__main__':
    main()