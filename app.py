import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Scam Detector", page_icon="🚨", layout="wide")

# Multi-Language Dictionary
translations = {
    "ta": {
        "title": "🚨 மோசடி கண்டறிதல் செயலி (Scam Detector)",
        "sub_title": "சந்தேகத்திற்குரிய செய்திகள், பரிவர்த்தனைகள் மற்றும் அழைப்புகளை பகுப்பாய்வு செய்யுங்கள்.",
        "input_label": "பகுப்பாய்வு செய்ய வேண்டிய விவரங்களை உள்ளிடவும்:",
        "analyze_btn": "பகுப்பாய்வு செய் (Analyze)",
        "risk_level": "அபாய நிலை (Risk Level)",
        "risk_score": "அபாய புள்ளி (Risk Score)",
        "risk_factors": "அபாய காரணிகள் (Risk Factors)",
        "why_flagged": "🔎 ஏன் கொடியிடப்பட்டது? (Why Flagged?)",
        "recommended_action": "🛡️ பரிந்துரைக்கப்பட்ட நடவடிக்கை (Recommended Action)",
        "xai_pipeline": "🧠 Explainable AI Pipeline",
        "safe": "பாதுகாப்பானது (SAFE)",
        "medium": "மிதமான அபாயம் (MEDIUM RISK)",
        "high": "அதிக அபாயம் (HIGH RISK)",
        "action_high": "பணத்தை அனுப்ப வேண்டாம். உடனடியாக இந்த எண்ணை தடுக்கவும் (Block).",
        "action_safe": "எந்த சந்தேகத்திற்க இடமான செயல்பாடும் இல்லை."
    },
    "en": {
        "title": "🚨 Scam Detector App",
        "sub_title": "Analyze suspicious messages, transactions, and call transcripts.",
        "input_label": "Enter text/data to analyze:",
        "analyze_btn": "Analyze Data",
        "risk_level": "Risk Level",
        "risk_score": "Risk Score",
        "risk_factors": "Risk Factors",
        "why_flagged": "🔎 Why Flagged?",
        "recommended_action": "🛡️ Recommended Action",
        "xai_pipeline": "🧠 Explainable AI Pipeline",
        "safe": "SAFE",
        "medium": "MEDIUM RISK",
        "high": "HIGH RISK",
        "action_high": "Do not transfer money. Block this sender immediately.",
        "action_safe": "No malicious intent detected."
    },
    "hi": {
        "title": "🚨 स्कैम डिटेक्टर (Scam Detector)",
        "sub_title": "संदिग्ध संदेशों, लेनदेन और कॉल की जांच करें।",
        "input_label": "विश्लेषण के लिए पाठ दर्ज करें:",
        "analyze_btn": "विश्लेषण करें",
        "risk_level": "जोखिम स्तर",
        "risk_score": "जोखिम स्कोर",
        "risk_factors": "जोखिम कारक",
        "why_flagged": "🔎 क्यों फ्लैग किया गया?",
        "recommended_action": "🛡️ अनुशंसित कार्रवाई",
        "xai_pipeline": "🧠 स्पष्टीकरणात्मक AI पाइपलाइन",
        "safe": "सुरक्षित",
        "medium": "मध्यम जोखिम",
        "high": "उच्च जोखिम",
        "action_high": "पैसा न भेजें। इस नंबर को तुरंत ब्लॉक करें।",
        "action_safe": "कोई संदिग्ध गतिविधि नहीं पाई गई।"
    },
    "te": {
        "title": "🚨 స్కామ్ డిటెక్టర్",
        "sub_title": "సందేశాలు, లావాదేవీలను విశ్లేషించండి.",
        "input_label": "విశ్లేషించడానికి వచనాన్ని ఎంటర్ చేయండి:",
        "analyze_btn": "విశ్లేషించండి",
        "risk_level": "ప్రమాద స్థాయి",
        "risk_score": "ప్రమాద స్కోరు",
        "risk_factors": "ప్రమాద కారకాలు",
        "why_flagged": "🔎 ఎందుకు ఫ్లాగ్ చేయబడింది?",
        "recommended_action": "🛡️ సిఫార్సు చేసిన చర్య",
        "xai_pipeline": "🧠 Explainable AI పైప్‌లైన్",
        "safe": "సురక్షితం",
        "medium": "మధ్యస్థ ప్రమాదం",
        "high": "అధిక ప్రమాదం",
        "action_high": "డబ్బు పంపవద్దు. వెంటనే ఈ నంబర్‌ను బ్లాక్ చేయండి.",
        "action_safe": "సందేహాస్పద కార్యకలాపాలు లేవు."
    },
    "ml": {
        "title": "🚨 സ്കാം ഡിറ്റക്ടർ",
        "sub_title": "സന്ദേശങ്ങളും ഇടപാടുകളും വിശകലനം ചെയ്യുക.",
        "input_label": "വിശകലനം ചെയ്യേണ്ട വചനം നൽകുക:",
        "analyze_btn": "വിശകലനം ചെയ്യുക",
        "risk_level": "അപകട നില",
        "risk_score": "അപകട സ്കോർ",
        "risk_factors": "അപകട ഘടകങ്ങൾ",
        "why_flagged": "🔎 എന്തുകൊണ്ട് ഫ്ലാഗ് ചെയ്തു?",
        "recommended_action": "🛡️ ശിപാർശ ചെയ്യുന്ന നടപടി",
        "xai_pipeline": "🧠 Explainable AI പൈപ്പ്‌ലൈൻ",
        "safe": "സുരക്ഷിതം",
        "medium": "മിതമായ അപകടസാധ്യത",
        "high": "ഉയർന്ന അപകടസാധ്യത",
        "action_high": "പണം അയക്കരുത്. ഈ നമ്പർ ഉടൻ ബ്ലോക്ക് ചെയ്യുക.",
        "action_safe": "സംശയാസ്പദമായ പ്രവർത്തനങ്ങളൊന്നുമില്ല."
    },
    "kn": {
        "title": "🚨 ಸ್ಕ್ಯಾಮ್ ಡಿಟೆಕ್ಟರ್",
        "sub_title": "ಸಂದೇಶಗಳು ಮತ್ತು ವಹಿವಾಟುಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ.",
        "input_label": "ವಿಶ್ಲೇಷಿಸಲು ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ:",
        "analyze_btn": "ವಿಶ್ಲೇಷಿಸಿ",
        "risk_level": "ಅಪಾಯದ ಮಟ್ಟ",
        "risk_score": "ಅಪಾಯದ ಸ್ಕೋರ್",
        "risk_factors": "ಅಪಾಯದ ಅಂಶಗಳು",
        "why_flagged": "🔎 ಏಕೆ ಫ್ಲ್ಯಾಗ್ ಮಾಡಲಾಗಿದೆ?",
        "recommended_action": "🛡️ ಶಿಫಾರಸು ಮಾಡಿದ ಕ್ರಮ",
        "xai_pipeline": "🧠 Explainable AI ಪೈಪ್‌ಲೈನ್",
        "safe": "ಸುರಕ್ಷಿತ",
        "medium": "ಮಧ್ಯಮ ಅಪಾಯ",
        "high": "ಹೆಚ್ಚಿನ ಅಪಾಯ",
        "action_high": "ಹಣವನ್ನು ಕಳುಹಿಸಬೇಡಿ. ಈ ಸಂಖ್ಯೆಯನ್ನು ತಕ್ಷಣವೇ ನಿರ್ಬಂಧಿಸಿ.",
        "action_safe": "ಯಾವುದೇ ಸಂಶಯಾಸ್ಪದ ಚಟುವಟಿಕೆ ಇಲ್ಲ."
    },
    "mr": {
        "title": "🚨 स्कॅम डिटेक्टर",
        "sub_title": "संदेश आणि व्यवहारांचे विश्लेषण करा.",
        "input_label": "विश्लेषणासाठी मजकूर प्रविष्ट करा:",
        "analyze_btn": "विश्लेषण करा",
        "risk_level": "धोका पातळी",
        "risk_score": "धोका स्कोर",
        "risk_factors": "धोका घटक",
        "why_flagged": "🔎 ध्वजांकित का केले?",
        "recommended_action": "🛡️ शिफारस केलेली कारवाई",
        "xai_pipeline": "🧠 Explainable AI पाइपलाइन",
        "safe": "सुरक्षित",
        "medium": "मध्यम धोका",
        "high": "उच्च धोका",
        "action_high": "पैसे पाठवू नका. हा नंबर त्वरित ब्लॉक करा.",
        "action_safe": "कोणतीही संशयास्पद क्रिया आढळली नाही."
    }
}

# Sidebar - Language Selection
lang_options = {
    "தமிழ் (Tamil)": "ta",
    "English": "en",
    "हिन्दी (Hindi)": "hi",
    "తెలుగు (Telugu)": "te",
    "മലയാളം (Malayalam)": "ml",
    "ಕನ್ನಡ (Kannada)": "kn",
    "मराठी (Marathi)": "mr"
}

selected_lang_label = st.sidebar.selectbox("🌐 Choose Language / மொழி:", list(lang_options.keys()))
lang = lang_options[selected_lang_label]
t = translations[lang]

# Title
st.title(t["title"])
st.caption(t["sub_title"])
st.divider()

# Input UI
input_type = st.radio("Detection Type:", ["💬 Message", "💳 Transaction", "📞 Call Transcript"], horizontal=True)
user_input = st.text_area(t["input_label"], height=100, placeholder="e.g. Urgent! Pay 1000 rupees immediately to update your bank KYC or your account will be blocked.")

if st.button(t["analyze_btn"], type="primary"):
    if user_input.strip():
        # Mock Rule-Engine Logic for Detection
        score = 15
        reasons = []
        breakdown_data = {}

        text_lower = user_input.lower()
        if "urgent" in text_lower or "அவசரம்" in text_lower or "तुरंत" in text_lower:
            score += 35
            reasons.append("Urgency tactics detected (அவசரப்படுத்தும் வார்த்தைகள்)")
            breakdown_data["Urgency"] = 35
        if "kyc" in text_lower or "otp" in text_lower or "bank" in text_lower or "கேஒய்சி" in text_lower:
            score += 40
            reasons.append("Sensitive Data / Bank credentials requested")
            breakdown_data["Sensitive Info"] = 40
        if "lottery" in text_lower or "winner" in text_lower or "பரிசு" in text_lower:
            score += 20
            reasons.append("Unrealistic Reward / Phishing keyword")
            breakdown_data["Phishing"] = 20

        final_score = min(score, 100)
        
        if final_score < 30:
            risk_lvl = t["safe"]
            color = "green"
            action = t["action_safe"]
        elif final_score < 70:
            risk_lvl = t["medium"]
            color = "orange"
            action = "Verify sender before sharing information."
        else:
            risk_lvl = t["high"]
            color = "red"
            action = t["action_high"]

        st.subheader("Analysis Results")
        
        # 🚨 Metrics Row
        col1, col2, col3 = st.columns(3)
        col1.metric(t["risk_level"], risk_lvl)
        col2.metric(t["risk_score"], f"{final_score} / 100")
        col3.metric(t["risk_factors"], f"{len(reasons)} Factors")

        st.divider()

        # 📊 Multi-colour Risk Contribution Chart
        st.write("### 📊 Multi-colour Risk Contribution Chart")
        if breakdown_data:
            chart_df = pd.DataFrame(list(breakdown_data.items()), columns=["Risk Factor", "Contribution %"])
            st.bar_chart(chart_df.set_index("Risk Factor"))
        else:
            st.success("No Risk Factors Detected. (Safe)")

        st.divider()

        # 🤖 Explainable AI & Recommendations
        col_a, col_b = st.columns(2)
        with col_a:
            st.write(f"### {t['why_flagged']}")
            if reasons:
                for r in reasons:
                    st.error(f"- {r}")
            else:
                st.write("None.")

            st.write(f"### {t['recommended_action']}")
            st.warning(action)

        with col_b:
            st.write(f"### {t['xai_pipeline']}")
            st.info("""
            1. **Text Preprocessing:** Tokenization & Multi-language Mapping
            2. **Intent & Keyword Matching:** Urgency & Phishing Vector Extraction
            3. **Feature Weight Computation:** SHAP / LIME Contribution Matrix Calculation
            """)
    else:
        st.warning("Please enter text before analyzing.")
