import streamlit as st
import ldap

pass=st.secrets["ldap"]["pass"]

def search_user(username):
    try:
        l = ldap.initialize("ldap://pitchfork.itc.virginia.edu")
        l.protocol_version = 3
        l.simple_bind_s()

        search_filter = f"(&(objectClass=person)(cn={username}))"
        result = l.search_s("dc=example,dc=com", ldap.SCOPE_SUBTREE, search_filter)

        if not result:
            return "User not found"

        return result
    except ldap.LDAPError as e:
        return f"LDAP error: {e}"

st.title("LDAP User Lookup")

username = st.text_input("Enter username:")

if username:
    result = search_user(username)
    st.write("Result:", result)
