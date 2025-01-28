import streamlit as st

def main():
    st.title("NetBIOS and SNMP Enumeration Quiz")

    questions = [
        {
            "question": "What is the primary function of NetBIOS?",
            "options": [
                "To encrypt network traffic",
                "To provide communication between applications on different systems within a local network",
                "To manage network devices remotely",
                "To route network packets"
            ],
            "answer": "To provide communication between applications on different systems within a local network",
            "explanation": "NetBIOS (Network Basic Input/Output System) is a protocol that allows applications on separate computers to communicate over a local area network (LAN). It does not encrypt traffic, manage devices, or route packets."
        },
        {
            "question": "Which TCP ports are commonly associated with NetBIOS services?",
            "options": [
                "21, 23, 25",
                "80, 443, 3389",
                "137, 138, 139",
                "53, 67, 68"
            ],
            "answer": "137, 138, 139",
            "explanation": "Port 137: NetBIOS Name Service\nPort 138: NetBIOS Datagram Service\nPort 139: NetBIOS Session Service\nThese ports are used for NetBIOS communication over TCP/IP."
        },
        {
            "question": "What type of information can be gathered using NetBIOS enumeration?",
            "options": [
                "Email addresses and social media profiles",
                "Machine names, group information, file shares, and printer shares",
                "GPS coordinates of network devices",
                "Stock prices and financial data"
            ],
            "answer": "Machine names, group information, file shares, and printer shares",
            "explanation": "NetBIOS enumeration can reveal details about the target network, such as machine names, shared resources (files and printers), and group or domain information. It does not provide GPS coordinates, financial data, or social media profiles."
        },
        {
            "question": "Which command-line utility can be used to display information about NetBIOS over TCP/IP?",
            "options": [
                "ipconfig",
                "nbtstat",
                "ping",
                "tracert"
            ],
            "answer": "nbtstat",
            "explanation": "The nbtstat command is specifically used to display NetBIOS over TCP/IP statistics, including NetBIOS name tables and cache."
        },
        {
            "question": "What is the purpose of SMB (Server Message Block) in Windows?",
            "options": [
                "To encrypt network traffic",
                "To manage SNMP devices",
                "To enable resource sharing, including files, directories, and printers",
                "To perform DNS lookups"
            ],
            "answer": "To enable resource sharing, including files, directories, and printers",
             "explanation": "SMB is a network file-sharing protocol that allows users to access shared resources like files, directories, and printers on a network."
        },
        {
            "question": 'What is a "community string" in the context of SNMP?',
            "options": [
                "A type of encryption algorithm",
                "A username and password combination",
                "A password-like string used for authentication and access control",
                "A set of network management tools"
            ],
            "answer": "A password-like string used for authentication and access control",
            "explanation": "A community string in SNMP acts as a shared secret (like a password) to authenticate access to SNMP-enabled devices. It is not an encryption algorithm or a toolset."
        },
        {
            "question": "Which of the following is a security concern with earlier versions of SNMP (e.g., version 1 and version 2)?",
            "options": [
                "They use complex encryption techniques, making it harder for attackers.",
                "They support encrypted community strings, making it harder to intercept.",
                "They lack encryption and hashing, making them vulnerable to eavesdropping and unauthorized access.",
                 "They are designed to only share data on a local network."
            ],
            "answer": "They lack encryption and hashing, making them vulnerable to eavesdropping and unauthorized access.",
            "explanation": "SNMPv1 and SNMPv2 transmit data (including community strings) in plaintext, making them susceptible to interception and misuse."
        },
         {
            "question": "Which component of SNMP runs on the networking device or node in the network?",
            "options": [
                "SNMP manager",
                "SNMP agent",
                "Management Information Base (MIB)",
                "Community string"
            ],
             "answer": "SNMP agent",
            "explanation": "The SNMP agent is the software component that runs on the network device (e.g., router, switch) and collects data for the SNMP manager."
        },
         {
            "question": "What does MIB stand for in the context of SNMP?",
            "options": [
                "Management Information Base",
                 "Message Information Buffer",
                "Main Interface Board",
                "Machine Identification Block"
            ],
            "answer": "Management Information Base",
             "explanation": "The MIB is a database that stores information about the network device, which can be queried using SNMP."
         },
         {
            "question": "Which version of SNMP is considered more secure, offering encryption and hashing?",
            "options": [
                 "Version 1",
                "Version 2",
                "Version 3",
                "All versions are equally secure"
            ],
            "answer": "Version 3",
            "explanation": "SNMPv3 introduces encryption, hashing, and user-based authentication, making it the most secure version of SNMP."
        }
    ]


    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}:")
        st.write(q["question"])
        selected_option = st.radio(f"Select an option:", q["options"], key=f"q{i}", index=None) # index=None to prevent default selection

        if st.button("Check Answer", key=f"btn{i}"):
            if selected_option == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            elif selected_option is not None:  # Prevents error when first button is clicked
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
            
            if selected_option is not None: # only display explanation if answer is given
              with st.expander("Explanation"):
                  st.write(q["explanation"])
            st.write("---") # adds a line after each question

    st.header("Quiz Results")
    st.write(f"Your final score is: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()