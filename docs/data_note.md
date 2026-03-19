# 📄 Data Note

## Overview
This project uses a **synthetically generated dataset** designed to simulate real-world fintech transaction systems.

The goal is to replicate realistic transaction behavior, failure patterns, and risk signals typically observed in digital payments platforms.

---

## 📊 Dataset Characteristics

- ~50,000 transactions  
- Multiple entities: users, merchants, issuing banks  
- Payment methods: Card, UPI, Wallet  
- Timestamp-based activity across a full day  

---

## ⚙️ Simulated Behaviors

The dataset intentionally includes patterns such as:

- **Failure spikes during peak hours** (post 7 PM)  
- **High concentration of UNKNOWN failures** (system-level issues)  
- **Bank-specific failure variations**  
- **Merchant-level failure concentration (Pareto effect)**  
- **High-risk user behavior patterns** (repeated high-value or failed transactions)  

---

## 🚨 Important Note

- This is **not real user data**  
- No personally identifiable information (PII) is used  
- Data is generated purely for analytical and demonstration purposes  

---

## 🎯 Why Synthetic Data?

Using synthetic data allows:

- Safe demonstration of fintech use cases  
- Controlled simulation of edge cases and anomalies  
- Reproducibility for anyone cloning the repository  

---

## 🔄 Limitations

- Does not capture full real-world noise and unpredictability  
- Fraud patterns are rule-based, not learned from real behavior  
- Assumes simplified system dynamics  

---

## 🚀 Future Enhancements

- Integration with real or anonymized datasets  
- More complex behavioral simulations  
- Real-time streaming data generation  
