def solution(phone_book):
    st = set()
    for ph in phone_book:
        for l in range(1, len(ph)):
            st.add(ph[:l])

    for ph in phone_book:
        if ph in st:
            return False
    return True