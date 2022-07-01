import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["zhijie_li", "yijun_lin", "damg7245_team4", "parth_shah", "srikanth_krishnamurthy"]
usernames = ["zhijie", "yijun", "team4", "parth", "srikanth"]
passwords = ["zhijiepw-", "yijunpw-", "team4pw-", "parthpw-", "srikanthpw-"]

hashed_passwards = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "streamlitUserPW.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwards, file)