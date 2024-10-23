from collections import defaultdict
def solution(clothes):
    st = defaultdict(int)
    for a, b in clothes:
        st[b] += 1

    ret = 1
    for cnt in st.values():
        ret *= (cnt + 1)
    return ret - 1