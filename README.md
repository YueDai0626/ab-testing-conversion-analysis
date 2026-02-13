# A/B Testing Conversion Analysis

## Project Overview

This project simulates and analyzes an A/B test for an e-commerce checkout page redesign.  
The goal is to estimate conversion lift, evaluate statistical significance, and provide a clear business recommendation based on experimental results.

---

## Experiment Setup

- **Control (A):** Original checkout page  
- **Treatment (B):** Redesigned checkout page  

### Primary Metric
- Conversion (0/1)

### Secondary Metrics
- Revenue per user (RPU)  
- Average order value (AOV)

---

## Business Questions

1. Did the redesign improve conversion rate?  
2. Is the observed uplift statistically significant?  
3. What is the estimated impact on revenue?  
4. Should the company roll out the new version?

---

## Dataset

`dataset.csv` includes simulated user-level experiment data:

- user_id  
- date  
- group (A/B)  
- device  
- region  
- traffic_source  
- converted (0/1)  
- order_value  
- revenue  

---

## Statistical Methods

- Conversion rate comparison  
- Two-proportion z-test  
- Confidence interval estimation  
- Revenue uplift calculation  
- Segment-level analysis  

---

## How to Run

Install dependencies:

pip install pandas numpy scipy matplotlib

Run analysis:

python analysis.py

---

## Files

- dataset.csv – experiment dataset  
- analysis.py – statistical A/B testing analysis  
- README.md – project documentation  

---

## Key Skills Demonstrated

- A/B testing experiment design  
- Statistical inference (two-proportion z-test)  
- Confidence interval estimation  
- Revenue impact modeling  
- Segmentation analysis  
- Data-driven decision making  

---

## Author

Yue Dai  
MSBA Applicant | Business Analytics
