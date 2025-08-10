import streamlit as st

st.title("📒 Danh bạ bạn thân")


friends = {
    "Huy": {
        "Tuổi": 20,
        "Sở thích": "Đá bóng, chơi game",
        "Quê quán": "Hà Nội"
    },
    "Lan": {
        "Tuổi": 19,
        "Sở thích": "Đọc sách, nghe nhạc",
        "Quê quán": "TP. Hồ Chí Minh"
    },
    "Minh": {
        "Tuổi": 21,
        "Sở thích": "Chụp ảnh, du lịch",
        "Quê quán": "Đà Nẵng"
    }
}

=
st.sidebar.header("Chọn một người bạn")
selected_friend = st.sidebar.selectbox("Danh sách bạn:", list(friends.keys()))


st.subheader(f" Thông tin của {selected_friend}:")
info = friends[selected_friend]
st.write(f"**Tuổi:** {info['Tuổi']}")
st.write(f"**Sở thích:** {info['Sở thích']}")
st.write(f"**Quê quán:** {info['Quê quán']}")


with st.expander(" Thêm bạn mới"):
    name = st.text_input("Tên:")
    age = st.number_input("Tuổi:", min_value=1, max_value=100, step=1)
    hobby = st.text_input("Sở thích:")
    hometown = st.text_input("Quê quán:")
    if st.button("Lưu"):
        if name:
            friends[name] = {"Tuổi": age, "Sở thích": hobby, "Quê quán": hometown}
            st.success(f"Đã thêm {name} vào danh sách!")
        else:
            st.error("Vui lòng nhập tên!")
