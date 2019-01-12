def reverse(st):
    inputWords=st.split(" ")
    inputWords=inputWords[-1::-1]
    st=' '.join(inputWords)
    return st
