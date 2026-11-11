import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

st.set_page_config(
    page_title="TalentFlow AI | HR Agency",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Demo dashboard: interactive workflow simulation using fictional data.
# It does not call an LLM or contact real candidates unless separately integrated.

AGENTS = [
    ("Talent Acquisition Specialist", "Sources and organizes potential talent", "🔎", "Sourcing"),
    ("CV Screening Analyst", "Reviews fictional CV summaries against role criteria", "📄", "Screening"),
    ("Skills Assessment Agent", "Maps skills to job requirements", "🧠", "Assessment"),
    ("Interview Coordinator", "Prepares interview stages and question sets", "🗓️", "Coordination"),
    ("Candidate Experience Agent", "Drafts candidate updates and follow-ups", "💬", "Communication"),
    ("Recruitment Operations Agent", "Tracks pipeline stages and process tasks", "⚙️", "Operations"),
    ("HR Policy Assistant", "Flags policy checkpoints for human review", "🛡️", "Compliance"),
    ("Project Manager", "Coordinates the workflow and records activity", "📊", "Management"),
]

if "activity" not in st.session_state:
    st.session_state.activity = [
        {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Agent Name": "Project Manager",
            "Task Performed": "Initialized TalentFlow demonstration dashboard",
            "Output Status": "Ready (demo)",
        }
    ]
if "run_count" not in st.session_state:
    st.session_state.run_count = 0

st.markdown("""
<style>
.block-container {padding-top: 1.7rem; padding-bottom: 2.5rem; max-width: 1400px;}
.hero {
  padding: 1.4rem 1.6rem; border-radius: 18px;
  background: linear-gradient(120deg, #10213c 0%, #173e5c 55%, #176b72 100%);
  color: white; margin-bottom: 1.2rem;
}
.hero h1 {font-size: 2.25rem; margin: 0 0 .35rem 0;}
.hero p {font-size: 1.02rem; margin: 0; color: #e0f2f5;}
.agent {
  border: 1px solid rgba(120,140,160,.35); border-radius: 14px;
  padding: 1rem; min-height: 150px; background: rgba(120,140,160,.06);
}
.agent-icon {font-size: 1.65rem;}
.agent-name {font-weight: 700; font-size: 1rem; margin: .35rem 0;}
.muted {color: #64748b; font-size: .88rem;}
.small-note {font-size: .82rem; color: #64748b;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🧭 TalentFlow AI")
    st.caption("Autonomous HR Agency • RNU project")
    page = st.radio("Navigation", ["Overview", "AI Employee Team", "Run Workflow", "Activity Log", "About"])
    st.divider()
    st.markdown("**Project owner**")
    st.write("Apurva Arpit")
    st.write("Riga Nordic University (RNU)")
    st.divider()
    st.caption("Presentation build • Demo data only")

st.markdown("""
<div class="hero">
  <h1>TalentFlow AI</h1>
  <p>Autonomous HR Agency · An interactive view of an eight-agent recruitment workflow</p>
</div>
""", unsafe_allow_html=True)

if page == "Overview":
    st.subheader("Agency command center")
    st.write("Explore the team, run a sample recruitment workflow, and inspect the activity ledger.")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("AI employee roles", "8")
    c2.metric("Workflow runs", st.session_state.run_count)
    c3.metric("Activity records", len(st.session_state.activity))
    c4.metric("External actions", "Disabled")
    st.markdown("### Workflow at a glance")
    stages = [
        ("01", "Talent sourcing", "Collect role requirements and sourcing plan"),
        ("02", "CV screening", "Review fictional candidate summaries"),
        ("03", "Skills assessment", "Compare evidence with role criteria"),
        ("04", "Interview planning", "Prepare structured interview topics"),
        ("05", "Candidate communication", "Draft respectful status updates"),
        ("06", "Operations & compliance", "Track pipeline and human-review checks"),
        ("07", "Project management", "Summarize outcomes and log the run"),
    ]
    cols = st.columns(2)
    for i, (num, title, desc) in enumerate(stages):
        with cols[i % 2]:
            st.markdown(f"**{num} · {title}**")
            st.caption(desc)
    st.info("This public demonstration uses simulated outputs and fictional candidate information. It does not make real hiring decisions or send emails.")
    if st.button("Run a sample workflow", type="primary", use_container_width=False):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.run_count += 1
        for name, description, icon, category in AGENTS:
            st.session_state.activity.append({
                "Timestamp": now,
                "Agent Name": name,
                "Task Performed": f"Demo run: {description.lower()}",
                "Output Status": "Completed (simulated)",
            })
        st.success("Sample workflow completed. Open Activity Log to review the generated records.")
        st.rerun()

elif page == "AI Employee Team":
    st.subheader("AI Employee Team")
    st.write("Eight role-based agents, coordinated by the Project Manager.")
    cols = st.columns(2)
    for i, (name, description, icon, category) in enumerate(AGENTS):
        with cols[i % 2]:
            st.markdown(
                f"""<div class="agent">
                <div class="agent-icon">{icon}</div>
                <div class="agent-name">{name}</div>
                <div>{description}</div>
                <p class="muted">Department: {category}</p>
                </div>""",
                unsafe_allow_html=True,
            )
            st.write("")

elif page == "Run Workflow":
    st.subheader("Run a recruitment workflow")
    st.caption("Use fictional details for the class demonstration.")
    with st.form("workflow_form"):
        role = st.text_input("Role to recruit for", value="Junior Data Analyst")
        seniority = st.selectbox("Seniority", ["Intern / Graduate", "Junior", "Mid-level", "Senior"])
        skills = st.text_input("Key skills", value="SQL, Python, communication")
        candidate_count = st.slider("Fictional candidate profiles to simulate", 1, 10, 3)
        submitted = st.form_submit_button("Start simulated workflow", type="primary")
    if submitted:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.run_count += 1
        st.markdown("### Workflow execution")
        st.write(f"**Role:** {role}  ·  **Level:** {seniority}  ·  **Skills:** {skills}")
        progress = st.progress(0, text="Preparing demonstration workflow...")
        statuses = []
        for idx, (name, description, icon, category) in enumerate(AGENTS):
            status = f"{name}: {description} — simulated output created"
            statuses.append(status)
            st.session_state.activity.append({
                "Timestamp": now,
                "Agent Name": name,
                "Task Performed": f"{role}: {description.lower()}",
                "Output Status": "Completed (simulated)",
            })
            progress.progress((idx + 1) / len(AGENTS), text=f"Processing {name}...")
        progress.empty()
        st.success("Workflow simulation completed.")
        st.markdown("#### Sample pipeline summary")
        summary = pd.DataFrame([
            {"Stage": "Profiles reviewed", "Result": candidate_count},
            {"Stage": "Skills criteria", "Result": len([x for x in skills.split(",") if x.strip()])},
            {"Stage": "Human review required", "Result": "Yes"},
            {"Stage": "External messages sent", "Result": "No"},
        ])
        st.dataframe(summary, use_container_width=True, hide_index=True)
        st.markdown("#### Agent outputs")
        for item in statuses:
            st.write("✓ " + item)
        st.warning("All results are illustrative. No real CVs were assessed, and no candidate should be selected solely by automated scoring.")

elif page == "Activity Log":
    st.subheader("Project Manager · Activity Log")
    st.write("Each run records a timestamp, agent, task, and output status.")
    df = pd.DataFrame(st.session_state.activity)
    if not df.empty:
        q = st.text_input("Filter by agent or task")
        if q:
            mask = df.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
            df = df[mask]
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button(
            "Download activity log as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="talentflow_activity_log.csv",
            mime="text/csv",
        )
    else:
        st.info("No activity records yet. Run a sample workflow first.")
    if st.button("Clear session activity"):
        st.session_state.activity = []
        st.session_state.run_count = 0
        st.rerun()

elif page == "About":
    st.subheader("About this project")
    st.markdown("""
**TalentFlow AI — Autonomous HR Agency**

- **Prepared by:** Apurva Arpit
- **University:** Riga Nordic University (RNU)
- **Agency type:** HR and recruitment operations
- **Team:** Eight role-based AI employee concepts, including a Project Manager
- **Purpose:** Demonstrate how recruitment tasks can be divided, tracked, and reviewed as a coordinated workflow.

### What this demonstration does
- Provides an interactive dashboard with navigation.
- Simulates a recruitment workflow using fictional inputs.
- Displays agent activity records and lets you download them as CSV.
- Keeps external email and Google Sheets writes disabled.

### Current limitation
This dashboard is a classroom demonstration. The workflow results are simulated; the dashboard does not itself call an LLM or execute the repository's underlying automation script. Real integrations require separate configuration, testing, and secure credentials.
""")

st.divider()
st.caption("TalentFlow AI • Classroom demonstration • Human review remains essential for all hiring decisions.")
