# **{{ cookiecutter.project_name }}**
<p align="center"><img src="reports/figures/banner.png"></p>
<p><b>Author: {{ cookiecutter.author_name }}</b></p>

---

# **Table of contents**
  0. Getting started
  1. Business problem
  2. Strategy
  3. Insights
  4. Solution
  5. Conclusions
  6. References

---

# **0. 📦 Getting started**
## 0.1. 📋 Requirements
* Python >= 3.10
* Poetry >= 1.2
* Docker
* Docker-compose
* GNU Makefile

## 0.2. ⚙️ How to run
**On unix-based systems**

First, download the source code by typing:
```bash
$ git clone https://github.com/cenciati/{{ cookiecutter.repo_name }}.git
```

Now, `Makefile` will do all the dirty work for you. It's going to set up a containerized environment with all the dependencies installed and the project ready to use. 
```bash
$ make setup
```

Once you're done, you can clean up everything just by typing:
```bash
$ make clean
```

---

# **1. 💼 Business problem**
## 1.1. Introduction
Placeholder

**Problem statement:** Placeholder

**Stakeholders:** Placeholder

## 1.2. Assumptions
- Placeholder

## 1.3. Target metric
Placeholder

<p name="" align="center"><img src="reports/figures/metric.png"></p>

---

# **2. 📃 Strategy**
## 2.1. CRISP-DM
CRISP-DM stands for cross-industry process for data mining. The CRISP-DM methodology provides a structured approach to planning a data mining project. It is a robust and well-proven methodology.

This model is an idealised sequence of events. In practice many of the tasks can be performed in a different order and it will often be necessary to backtrack to previous tasks and repeat certain actions. The model does not try to capture all possible routes through the data mining process.
<p align="center"><img src="reports/figures/crisp-methodology.jpg"></p>

## 2.2. Steps
### 2.2.1. Project architecture
<p align="center"><img src="reports/figures/project-architecture.png"></p>

### 2.2.2. Pipeline
0. Data acquisition
1. Data cleaning and description
2. Feature engineering
3. Exploratory data analysis
4. Data balancing
5. Data preprocessing
6. Feature selection
7. Machine learning modeling
8. Hyperparameters fine-tuning
9. Calibration
10. Deployment

---

# **3. 🤯 Insights**
## 3.1. Hypotheses
Placeholder

## 3.2. Further exploration
Placeholder

---

# **4. 📌 Solution**
## 4.1. Algorithm applied
Placeholder

## 4.2. Performance and impact
Placeholder

---

# **5. 💭 Conclusions**
## 5.1. Results
Placeholder

## 5.2. What's next
Placeholder

---

# **6. 📎 References**
- Placeholder