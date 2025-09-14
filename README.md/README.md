# Coders of Delhi - Social Network Analysis in Pure Python

## Project Overview
**Coders of Delhi** is a mini social-network analysis project inspired by platforms like Facebook/LinkedIn.  
It simulates a coder community ("CodeBook") where users can connect with friends and like pages.  

This project is built **only with Python's standard library** (no Pandas, NumPy, or external libraries).  
It demonstrates:
- Data loading & cleaning
- Social network analysis
- Friend recommendations (**People You May Know**)
- Page recommendations (**Pages You Might Like**)

Implemented in a **Jupyter Notebook** for clear explanation and reproducibility.

---

## Dataset
The dataset (`massive_data.json`) contains:
- **Users**: ID, name, friends (connections), liked pages
- **Pages**: ID, name of community/page

Example User:
```json
{"id": 1, "name": "Amit", "friends": [2, 3, 4, 5, 6], "liked_pages": [101, 102]}
```

Example Page:
```json
{"id": 101, "name": "Python Developers"}
```

---

## Features Implemented
1. **Data Loading & Display**
2. **Data Cleaning**
   - Remove users with missing names
   - Deduplicate friends & pages
   - Remove inactive users
3. **Analysis**
   - Find most connected user
   - Find most popular page
4. **Recommendations**
   - People You May Know (mutual friends)
   - Pages You Might Like (collaborative filtering)

---

## How to Run
1. Open the repository in **Jupyter Lab** or **Jupyter Notebook**.
2. Open `Coders_of_Delhi.ipynb`.
3. Run all cells to reproduce the results.

---

## Sample Output
**Dataset Summary**
```
Total Users : 30
Total Pages : 27
```

**Insights**
```
Most Connected User: Neha (5 friends)
Most Popular Page : Data Science Enthusiasts (liked by 4 users)
```

**Recommendations for Amit**
```
People You May Know:
- Sara (ID 4), Mutual Friends: 2
- Ravi (ID 9), Mutual Friends: 1

Pages You Might Like:
- AI & ML Community (ID 103), Score: 2
- Blockchain Innovators (ID 105), Score: 1
```

---

## Tech Stack
- Python (Standard Library only)
- Jupyter Notebook

