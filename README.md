## 📂 Chick repository structure
The folder is organized into three main functional directories:

* **`📁 QuaQua/`** Contains the practical coding exercises completed during the first class.
* **`📁 Assignments/`** Houses the individual assignments for each class.
* **`📁 final_project/`** The core production directory containing the primary research pipeline.
    * `imitation_analysis.ipynb`: The main JupyterLab workbook containing the multi-block scientific workflow.
    * `behav_data.xlsx`: Consolidated absolute counts/occurrences of events per subject.
    * `frames_data.xlsx`: Consolidated raw sum of frames spent per subject.
    * `exported_labels.xlsx`: Raw frame-by-frame binary observations per subject.

---
  
# Avian Social Imitation Analysis (Gallus gallus)
This repository contains the codebase and project structure for analyzing behavioral tracking data from an avian social imitation experiment in domestic chicks (*Gallus gallus*).
The study focuses on evaluating whether naive newborn chicks spontaneously mirror "disgust" behaviors by observing conspecifics.

## 🔬 Project Overview: Experimental Design
The study explores social mirroring in newborn, naïve chicks by tracking their behavioral responses to stereotypical "disgust" patterns demonstrated by a conspecific on video.

### Experimental Groups
1.  **Actors (A):** Experience a bitter taste stimulus while watching a neutral control video.
2.  **Observers (O):** Watch a video of a conspecific demonstrating disgust responses, without tasting any bitter substance themselves.
3.  **Controls (C):** Experience neither a physical bitter taste nor a disgust video (neutral video baseline).

### Tracked Variables
The analysis compares two target **disgust motor patterns** against two baseline **general grooming behaviors**:
* **Disgust Patterns:** `Headshaking` (rapid lateral head motion) and `Beakwiping` (wiping beak on the ground).
* **Grooming Controls:** `Preening` (feather cleaning/adjustments) and `Scratching` (head/neck area scratching using a foot).

## ⚙️ Data Analysis Pipeline (`final_project/`)

The analysis is executed using a modular, step-by-step pipeline within `imitation_analysis.ipynb` built to meet rigorous publication standards:

1.  **Block 1: Raw Data Loading & Validation** Loads consolidated sheets into `pandas` DataFrames, verifies strict column structures, enforces correct data types for `Condition` (A, O, C) and `Sex` (M, F), and flags structural deficiencies.
2.  **Block 2: Descriptive Statistical Analysis** Groups data by group/sex and prints clear markdown tables displaying sample sizes ($n$), Means, Medians, SD, and SEM for all targeted actions.
3.  **Block 3: Inferential Statistical Evaluations** Computes One-Way ANOVAs across conditions, dynamically flags significant changes in red with classic mathematical asterisk notation ($*$, $* *$, $* * *$), triggers post-hoc Tukey HSD metrics, and evaluates Sex factors using a Two-Way ANOVA. Low variance exceptions are handled gracefully to ensure execution reliability.
4.  **Block 4: Data Visualization** Generates publication-ready 2x2 subplot grids comparing occurrences, durations (normalized by the exact video baseline of **5934 frames**), and sex break-downs.

### Visual Styling Guide
* **Condition Analysis:** Fixed blue gradient palette $\rightarrow$ Actor (Dark Blue), Observer (Medium Blue), Control (Light Blue).
* **Sex Demographics:** Standard High-contrast Blue (Males) vs. Pink (Females).
* **Annotations:** Statistical significance brackets are programmatically derived and drawn using `matplotlib.patches` directly from computed Tukey HSD p-adjusted values.

---

## 🛠️ Requirements & Environment

The analysis requires Python 3.8+ and the following scientific libraries:
* `pandas` & `openpyxl` (Data manipulation and Excel handling)
* `numpy` (Vectorized mathematics)
* `scipy` & `statsmodels` (Inferential biostatistics)
* `matplotlib` & `seaborn` (Advanced figure generation)

