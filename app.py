# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 
from home_page import run_home_page
from eda_app import run_eda
from ml_app import run_ml

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">AI Sales Predictor</h1>
		<h4 style="color:white;text-align:center;">Courtesy of SecureCapita</h4>
		</div>
		"""

def main():
	stc.html(html_temp)
	menu = ["Home","EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		# run_home_page()
		run_ml()
		pass
	elif choice == "EDA":
		run_eda()
	elif choice == "ML":
		run_ml()
	else:
		st.subheader("About")
		st.info("Built with Streamlit")
		st.text("Let's Predict the Future Together!")
		st.text("Courtesy of SecureCapita")



if __name__ == '__main__':
	main()