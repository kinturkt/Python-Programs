import speedtest as st

speed_test = st.Speedtest()

download_speed = st.download()
print("Your Download speed is", download_speed) 

upload_speed = st.upload()
print("Your Upload speed is", upload_speed)
