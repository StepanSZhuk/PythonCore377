#CodeWars Stepan Zhuk
#Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
#String should be capitalized and properly spaced. Using re and string is not allowed.


def filter_words(st):
    st1 = st.capitalize()
    st2 = st1.split()
    st3 = ' '.join(st2)
    return st3
