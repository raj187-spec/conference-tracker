import streamlit as st
import pandas as pd
import os

# Full attendee list extracted from the conference document
ATTENDEE_DATA = [
    {"First Name": "Lucy", "Last Name": "Rigby KC MP", "Job Title": "Economic Secretary to the Treasury", "Organisation": "HM Treasury"},
    {"First Name": "Tom", "Last Name": "Bentley", "Job Title": "CRO", "Organisation": "10x Banking"},
    {"First Name": "Nikhil", "Last Name": "Sengupta", "Job Title": "Business Development Director", "Organisation": "10x Banking"},
    {"First Name": "Simon", "Last Name": "Black", "Job Title": "Managing Partner", "Organisation": "1805 Ltd"},
    {"First Name": "Stacey Ann", "Last Name": "Mitchinson", "Job Title": "Director of Operations", "Organisation": "1st Class Credit Union"},
    {"First Name": "Gayle", "Last Name": "Lloyd", "Job Title": "CEO", "Organisation": "1st Class Credit Union"},
    {"First Name": "Robert", "Last Name": "Hall", "Job Title": "Director", "Organisation": "1st Class Credit Union"},
    {"First Name": "Bruce", "Last Name": "Devenport", "Job Title": "Chair", "Organisation": "1st Class Credit Union"},
    {"First Name": "Jim", "Last Name": "McNicholls", "Job Title": "Board Member", "Organisation": "1st Class Credit Union"},
    {"First Name": "Geoff", "Last Name": "Poulter", "Job Title": "Cyber SME", "Organisation": "A Jolly Consulting"},
    {"First Name": "Matthew", "Last Name": "Neall", "Job Title": "Director", "Organisation": "A Jolly Consulting"},
    {"First Name": "Krysta", "Last Name": "Collin", "Job Title": "Manager", "Organisation": "A Jolly Consulting"},
    {"First Name": "Matt", "Last Name": "Bland", "Job Title": "Chief Executive", "Organisation": "ABCUL"},
    {"First Name": "Tom", "Last Name": "Mack", "Job Title": "Business Development Rep", "Organisation": "ACI Worldwide"},
    {"First Name": "Richard", "Last Name": "Albery", "Job Title": "Head of UK & Ireland", "Organisation": "ACI Worldwide"},
    {"First Name": "Simon", "Last Name": "Lofthouse", "Job Title": "Partner", "Organisation": "Addleshaw Goddard LLP"},
    {"First Name": "Ben", "Last Name": "Koehne", "Job Title": "Partner", "Organisation": "Addleshaw Goddard LLP"},
    {"First Name": "Rosanna", "Last Name": "Bryant", "Job Title": "Partner", "Organisation": "Addleshaw Goddard LLP"},
    {"First Name": "David", "Last Name": "Pygott", "Job Title": "Partner", "Organisation": "Addleshaw Goddard LLP"},
    {"First Name": "Priscilla", "Last Name": "Hetherton", "Job Title": "Legal Director", "Organisation": "Addleshaw Goddard LLP"},
    {"First Name": "Mark", "Last Name": "Hallam", "Job Title": "Partner", "Organisation": "Addleshaw Goddard LLP"},
    {"First Name": "Alex", "Last Name": "Valy", "Job Title": "Designer", "Organisation": "Alex Valy Design"},
    {"First Name": "Archie", "Last Name": "Dickinson", "Job Title": "Senior Manager", "Organisation": "Allia C&C"},
    {"First Name": "Crispin", "Last Name": "Pugh", "Job Title": "Sales Trader", "Organisation": "Allia C&C"},
    {"First Name": "Luke", "Last Name": "DiRollo", "Job Title": "CEP", "Organisation": "ALMIS International"},
    {"First Name": "Jake", "Last Name": "Rose", "Job Title": "Chief Commercial Officer", "Organisation": "ALMIS International"},
    {"First Name": "Neil", "Last Name": "Irvine-Hess", "Job Title": "Head of Implementation", "Organisation": "ALMIS International"},
    {"First Name": "Emma", "Last Name": "Farrugia", "Job Title": "Product Owner", "Organisation": "ALMIS International"},
    {"First Name": "Sophie", "Last Name": "Scott", "Job Title": "Product Owner", "Organisation": "ALMIS International"},
    {"First Name": "Deborah", "Last Name": "Dray", "Job Title": "Account Manager", "Organisation": "ALMIS International"},
    {"First Name": "James", "Last Name": "Scott", "Job Title": "CP Exec", "Organisation": "AND Digital"},
    {"First Name": "Amy", "Last Name": "Cockram", "Job Title": "Club Exec", "Organisation": "AND Digital"},
    {"First Name": "Eran", "Last Name": "Baram", "Job Title": "M&A Manager", "Organisation": "Andromeda"},
    {"First Name": "Gearoid", "Last Name": "Power", "Job Title": "CEO", "Organisation": "Antuar"},
    {"First Name": "Rahul", "Last Name": "Sisodia", "Job Title": "Director", "Organisation": "Apex Software Solutions Ltd"},
    {"First Name": "James", "Last Name": "Pagan", "Job Title": "Director of Product", "Organisation": "April Mortgages"},
    {"First Name": "Jim", "Last Name": "Murphy", "Job Title": "Founder & Chair", "Organisation": "Arden Strategies"},
    {"First Name": "Ellie", "Last Name": "Miller", "Job Title": "MD External Affairs", "Organisation": "Arden Strategies"},
    {"First Name": "Andrew", "Last Name": "Whyte", "Job Title": "Chief Executive", "Organisation": "Association of Financial Mutuals"},
    {"First Name": "Stephanie", "Last Name": "Charman", "Job Title": "Chief Executive", "Organisation": "Mortgage Intermediaries"},
    {"First Name": "Christian", "Last Name": "Konig", "Job Title": "Managing Director", "Organisation": "Private Bausparkassen"},
    {"First Name": "Max", "Last Name": "Lesemann", "Job Title": "Head of Regulation", "Organisation": "Private Bausparkassen"},
    {"First Name": "Jonathan", "Last Name": "Stallard", "Job Title": "Regional Director", "Organisation": "Backbase"},
    {"First Name": "Frederico", "Last Name": "Venturieri", "Job Title": "Head of Partnerships", "Organisation": "Backbase"},
    {"First Name": "Richard", "Last Name": "Waghorn", "Job Title": "Business Dev Manager", "Organisation": "Backbase"},
    {"First Name": "Jacqui", "Last Name": "Ashe", "Job Title": "Head of Division", "Organisation": "Bank of England"},
    {"First Name": "Charlotte", "Last Name": "Gerken", "Job Title": "Executive Director", "Organisation": "Bank of England"},
    {"First Name": "Chris", "Last Name": "Donald", "Job Title": "Prudential Regulation", "Organisation": "Bank of England"},
    {"First Name": "Andrew", "Last Name": "Wilkie", "Job Title": "Director", "Organisation": "Baringa Partners"},
    {"First Name": "David", "Last Name": "Harris", "Job Title": "Partner", "Organisation": "Baringa Partners"},
    {"First Name": "Paul", "Last Name": "Mihajlovic", "Job Title": "Partner", "Organisation": "Baringa Partners"},
    {"First Name": "Sarah", "Last Name": "Applegarth", "Job Title": "Director", "Organisation": "Baringa Partners"},
    {"First Name": "Richard", "Last Name": "Ingle", "Job Title": "Chief Executive", "Organisation": "Bath Building Society"},
    {"First Name": "Emma", "Last Name": "Davis", "Job Title": "Chief Customer Officer", "Organisation": "Bath Building Society"},
    {"First Name": "Andrew", "Last Name": "Payton", "Job Title": "Non-Executive Director", "Organisation": "Bath Building Society"},
    {"First Name": "Steve", "Last Name": "Burnard", "Job Title": "Chief Digital Officer", "Organisation": "Bath Building Society"},
    {"First Name": "Craig", "Last Name": "Brown", "Job Title": "Chief Mortgage Officer", "Organisation": "Bath Building Society"},
    {"First Name": "Paul", "Last Name": "Gilbert", "Job Title": "Partner", "Organisation": "BDO"},
    {"First Name": "Jen", "Last Name": "Hale", "Job Title": "Partner", "Organisation": "BDO"},
    {"First Name": "Tim", "Last Name": "Lawrence", "Job Title": "Partner", "Organisation": "BDO"},
    {"First Name": "Sarah", "Last Name": "Collins", "Job Title": "Director", "Organisation": "BDO"},
    {"First Name": "James", "Last Name": "Billingham", "Job Title": "Partner", "Organisation": "BDO"},
    {"First Name": "Graham", "Last Name": "FitzGerald", "Job Title": "Business Dev Director", "Organisation": "Be Inspirational Group"},
    {"First Name": "Janet", "Last Name": "Bedford", "Job Title": "Chief Executive", "Organisation": "Beverley Building Society"},
    {"First Name": "Kevin", "Last Name": "Mowles", "Job Title": "COO", "Organisation": "Beverley Building Society"},
    {"First Name": "Sally", "Last Name": "Hall", "Job Title": "CFO", "Organisation": "Beverley Building Society"},
    {"First Name": "Karen", "Last Name": "Wint", "Job Title": "NED", "Organisation": "Beverley Building Society"},
    {"First Name": "Bob", "Last Name": "Andrews", "Job Title": "NED", "Organisation": "Beverley Building Society"},
    {"First Name": "Guru", "Last Name": "Vaidyanathan", "Job Title": "Principal", "Organisation": "Boston Consulting Group"},
    {"First Name": "Sukand", "Last Name": "Ramachandran", "Job Title": "Managing Director", "Organisation": "Boston Consulting Group"},
    {"First Name": "Brendan", "Last Name": "Gilmore", "Job Title": "Managing Director", "Organisation": "BPG Strategy"},
    {"First Name": "Emily", "Last Name": "Gore", "Job Title": "VP Strategy", "Organisation": "Broadridge"},
    {"First Name": "Brendan", "Last Name": "Carter", "Job Title": "Marketing Specialist", "Organisation": "Broadridge"},
    {"First Name": "Joseph", "Last Name": "Oakenfold", "Job Title": "Sales Director", "Organisation": "Broadridge"},
    {"First Name": "Dominic", "Last Name": "Rix", "Job Title": "Senior Director", "Organisation": "Broadridge"},
    {"First Name": "Barney", "Last Name": "Hosey", "Job Title": "General Manager", "Organisation": "Broadridge"},
    {"First Name": "Karen", "Last Name": "Scrimgeour", "Job Title": "Senior Consultant", "Organisation": "Broadridge"},
    {"First Name": "Dan", "Last Name": "Wass", "Job Title": "CEO", "Organisation": "Buckinghamshire Building Society"},
    {"First Name": "Sarah", "Last Name": "Harrison CB MBE", "Job Title": "Chief Executive", "Organisation": "Building Societies Association"},
    {"First Name": "Paul", "Last Name": "Broadhead", "Job Title": "Head of Mortgage Policy", "Organisation": "Building Societies Association"},
    {"First Name": "Sandhya", "Last Name": "Kawar", "Job Title": "Chief Risk Officer", "Organisation": "Cambridge Building Society"},
    {"First Name": "Peter", "Last Name": "Burrows", "Job Title": "Chief Executive", "Organisation": "Cambridge Building Society"},
    {"First Name": "Samantha", "Last Name": "Homer", "Job Title": "CEO", "Organisation": "Capital Credit Union"},
    {"First Name": "Kim", "Last Name": "Roby", "Job Title": "Customer Services Director", "Organisation": "Chorley Building Society"},
    {"First Name": "Sophie", "Last Name": "Bell", "Job Title": "Finance Lead", "Organisation": "Co-operative Bank"},
    {"First Name": "Steve", "Last Name": "Hughes", "Job Title": "Group CEO", "Organisation": "Coventry Building Society"},
    {"First Name": "David", "Last Name": "Thorburn", "Job Title": "Chairman", "Organisation": "Coventry Building Society"},
    {"First Name": "Stuart", "Last Name": "Miller", "Job Title": "CEO", "Organisation": "Cumberland Building Society"},
    {"First Name": "Alex", "Last Name": "Windle", "Job Title": "CEO", "Organisation": "Darlington Building Society"},
    {"First Name": "Raj", "Last Name": "Kohli", "Job Title": "Managing Director", "Organisation": "DCR Partners"},
    {"First Name": "Jason", "Last Name": "John", "Job Title": "Partner", "Organisation": "Deloitte"},
    {"First Name": "Charlotte", "Last Name": "Nordberg", "Job Title": "Partner", "Organisation": "Deloitte"},
    {"First Name": "Russell", "Last Name": "Davis", "Job Title": "Partner", "Organisation": "Deloitte"},
    {"First Name": "Gareth", "Last Name": "Griffiths", "Job Title": "CEO", "Organisation": "Ecology Building Society"},
    {"First Name": "Christopher", "Last Name": "Woolard CBE", "Job Title": "Partner", "Organisation": "EY"},
    {"First Name": "Sarah", "Last Name": "Pritchard", "Job Title": "Deputy Chief Executive", "Organisation": "Financial Conduct Authority"},
    {"First Name": "Dominic", "Last Name": "Cashman", "Job Title": "Director of Authorisations", "Organisation": "Financial Conduct Authority"},
    {"First Name": "Gareth", "Last Name": "Richardson", "Job Title": "CEO", "Organisation": "Finova"},
    {"First Name": "Rich", "Last Name": "Wainwright", "Job Title": "CEO and Founder", "Organisation": "FinProxy Limited"},
    {"First Name": "Simon", "Last Name": "Broadley", "Job Title": "Chief Executive Officer", "Organisation": "Frontier Services"},
    {"First Name": "David", "Last Name": "Ross", "Job Title": "CEO", "Organisation": "Hometrack"},
    {"First Name": "Max", "Last Name": "Shepherd", "Job Title": "Group Economist", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Jason", "Last Name": "Vickerman", "Job Title": "Director of Tech", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Garth", "Last Name": "Newboult", "Job Title": "Head of AI", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Rich", "Last Name": "Bowles", "Job Title": "Chief Risk Officer", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Vicky", "Last Name": "Oygard", "Job Title": "General Counsel", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Fraser", "Last Name": "Ingram", "Job Title": "COO", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Louise", "Last Name": "Slater", "Job Title": "Director of Risk", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Simone", "Last Name": "Fox", "Job Title": "Director of Support", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Tina", "Last Name": "Hughes", "Job Title": "Director of Savings", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Chris", "Last Name": "Irwin", "Job Title": "Director of Performance", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Simon", "Last Name": "Martin", "Job Title": "Director of Credit Risk", "Organisation": "Yorkshire Building Society"},
    {"First Name": "David", "Last Name": "Wood", "Job Title": "Director of ERM", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Jessica", "Last Name": "Sparksman", "Job Title": "Director of Risk", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Daniel", "Last Name": "Macey", "Job Title": "Public Affairs Lead", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Sharon", "Last Name": "Mistry", "Job Title": "Internal Audit Manager", "Organisation": "Yorkshire Building Society"},
    {"First Name": "Trudi", "Last Name": "Flanagan", "Job Title": "Chief Executive Officer", "Organisation": "Zanoo"},
    {"First Name": "Jessica", "Last Name": "Flanagan", "Job Title": "Chief Operating Officer", "Organisation": "Zanoo"}
]

STORAGE_FILE = "networking_progress.csv"

def load_data():
    if os.path.exists(STORAGE_FILE):
        return pd.read_csv(STORAGE_FILE)
    df = pd.DataFrame(ATTENDEE_DATA)
    for col in ['Speak To', 'Spoken To', 'Follow Up']:
        df[col] = False
    df['Notes'] = ""
    return df

def save_data(df):
    df.to_csv(STORAGE_FILE, index=False)

def main():
    st.set_page_config(page_title="BSA 2026 Networking", layout="centered")
    
    if 'df' not in st.session_state:
        st.session_state.df = load_data()

    st.title("💼 BSA 2026 Networking")
    
    # Persistent Search
    search = st.text_input("Search Name, Role, or Organisation", placeholder="e.g. CRO, Yorkshire, Treasury")
    
    mask = (
        st.session_state.df['First Name'].str.contains(search, case=False) |
        st.session_state.df['Last Name'].str.contains(search, case=False) |
        st.session_state.df['Job Title'].str.contains(search, case=False) |
        st.session_state.df['Organisation'].str.contains(search, case=False)
    )
    filtered = st.session_state.df[mask]

    # Mobile optimized display
    for idx, row in filtered.iterrows():
        # Using a clean format for the expander title
        label = f"{row['First Name']} {row['Last Name']} ({row['Organisation']})"
        with st.expander(label):
            st.write(f"**Role:** {row['Job Title']}")
            
            c1, c2, c3 = st.columns(3)
            # We update session state immediately on change
            st.session_state.df.at[idx, 'Speak To'] = c1.checkbox("Target", value=row['Speak To'], key=f"s_{idx}")
            st.session_state.df.at[idx, 'Spoken To'] = c2.checkbox("Met", value=row['Spoken To'], key=f"m_{idx}")
            st.session_state.df.at[idx, 'Follow Up'] = c3.checkbox("Follow", value=row['Follow Up'], key=f"f_{idx}")
            
            note_val = str(row['Notes']) if pd.notna(row['Notes']) else ""
            st.session_state.df.at[idx, 'Notes'] = st.text_area("Notes", value=note_val, key=f"n_{idx}")
            
            # Save automatically whenever an entry is modified
            save_data(st.session_state.df)

    # Summary and Export in Sidebar
    st.sidebar.header("Progress Tracker")
    targets = st.session_state.df['Speak To'].sum()
    met = st.session_state.df['Spoken To'].sum()
    st.sidebar.metric("Key Targets", targets)
    st.sidebar.metric("Met", met)
    
    st.sidebar.divider()
    csv = st.session_state.df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button("📥 Export CSV to Phone", data=csv, file_name="BSA_Networking_Final.csv")

if __name__ == "__main__":
    main()
