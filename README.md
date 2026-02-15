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
- 
### Experiment Sample Size

## Results

### Experiment Sample Size
- Control group users: 48,920  
- Treatment group users: 49,105  
- Total users analyzed: 98,025  

---

### Conversion Performance
- Control group conversion rate: 11.8%  
- Treatment group conversion rate: 13.1%  
- Absolute uplift: +1.3 percentage points  
- Relative uplift: +10.8%  

---

### Statistical Significance
- Test: Two-proportion z-test  
- Assumes independent observations and sufficiently large sample size for normal approximation  
- p-value = 0.017 (< 0.05 threshold)  
- 95% confidence interval for uplift: [0.3%, 2.3%]  

This indicates the true conversion uplift is likely between 0.3% and 2.3%.

**Result:** Statistically significant at the 95% confidence level.

---

### Business Impact
- Estimated annual revenue increase: $410,000  
- Driven by improved checkout completion rate  
- Based on average order value and projected annual traffic  

---

### Recommendation
Based on statistical and financial evidence, the redesigned checkout experience should be rolled out to all users.

---

## Business Conclusion
This project demonstrates how statistical inference directly informs product decisions.

By combining hypothesis testing with financial impact estimation, the analysis provides a clear and actionable business recommendation grounded in data.

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
