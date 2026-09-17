import os
import streamlit as st
from core.pipeline import AirefiyPipeline

# Page Configuration
st.set_page_config(
    page_title="Airefiy | Document Credibility Analyzer",
    page_icon="🎓",
    layout="wide"
)

# Initialize Pipeline
@st.cache_resource
def load_pipeline():
    pipeline = AirefiyPipeline()
    if not os.path.exists("artifacts/credibility_model.pkl"):
        pipeline.bootstrap_default_model()
    else:
        try:
            pipeline.classifier.load_model()
        except Exception:
            pipeline.bootstrap_default_model()
    return pipeline

pipeline = load_pipeline()

# UI Layout - Sidebar
st.sidebar.title("🎓 Airefiy Control Panel")
st.sidebar.info(
    "**Course Project:** Fundamentals in AI & ML\n\n"
    "Upload research papers or project reports (.pdf or .docx) to evaluate "
    "their linguistic profiles, empirical markers, and classification risk index."
)

if st.sidebar.button("🔄 Reset / Retrain Model Pipeline"):
    pipeline.bootstrap_default_model()
    st.sidebar.success("Default baseline model retrained successfully!")

# UI Layout - Main Body
st.title("Airefiy: Document & Research Credibility Analyzer")
st.markdown("Upload your research document (**PDF** or **Word .docx**) below to check its academic rigor and credibility index.")

# File Uploader Widget
uploaded_file = st.file_uploader("Choose an academic document...", type=["pdf", "docx"])

if uploaded_file is not None:
    # Display basic file info
    st.success(f"Successfully uploaded: **{uploaded_file.name}**")
    
    # Extract text using our updated parser
    raw_text = pipeline.parser.extract_text_from_file(uploaded_file)
    
    if raw_text.startswith("Error") or raw_text.startswith("Unsupported"):
        st.error(raw_text)
    else:
        with st.expander("👁️ Preview Extracted Raw Text"):
            st.text_area("Extracted Content Preview", value=raw_text[:1500] + ("..." if len(raw_text) > 1500 else ""), height=150)

        if st.button("Run Credibility Analysis on Document", type="primary"):
            with st.spinner("Extracting features and running machine learning evaluation..."):
                report = pipeline.process_and_analyze(raw_text)

            if "error" in report:
                st.error(report["error"])
            else:
                # Display Top-Level Metrics
                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                
                cred_index = report["classification_results"]["credibility_index"]
                status_label = report["classification_results"]["status"]
                
                with col1:
                    st.metric(label="Credibility Index (0-100)", value=f"{cred_index} / 100")
                with col2:
                    st.metric(label="Classification Status", value=status_label)
                with col3:
                    st.metric(label="Total Words Analyzed", value=report["input_metrics"]["processed_word_count"])

                # Detailed Breakdown Tabs
                tab1, tab2, tab3 = st.tabs(["📊 Linguistic Metrics", "⚙️ Structural Signals", "🔍 Full JSON Report"])

                with tab1:
                    st.subheader("Empirical vs. Sensational Lexicon Analysis")
                    ling = report["linguistic_analysis"]
                    
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Empirical Term Matches", ling["empirical_matches"])
                    m2.metric("Sensational Term Matches", ling["sensational_matches"])
                    m3.metric("Linguistic Balance Index", ling["linguistic_ratio_index"])

                    st.progress(min(cred_index / 100.0, 1.0))

                with tab2:
                    st.subheader("Document Structural Inspection")
                    struct = report["input_metrics"]
                    st.write(f"- **Contains Quantitative Metrics (Percentages/Numbers):** `{struct['contains_quantitative_metrics']}`")
                    st.write(f"- **Contains Citations / References:** `{struct['contains_citations']}`")
                    st.write(f"- **Original Word Count:** `{struct['original_word_count']}`")

                with tab3:
                    st.subheader("Raw Engine Output Payload")
                    st.json(report)

# Footer
st.markdown("---")
st.caption("Airefiy AI/ML Course Project Engine • Built for academic evaluation requirements.")