# 🍎 Personal Health Calculator

A simple, Python-based Command Line Interface (CLI) tool designed to help users track essential health metrics. This application calculates Body Mass Index (BMI), Basal Metabolic Rate (BMR), Daily Water Intake, and Ideal Body Weight (IBW) based on user inputs.

## 🚀 Features

* **BMI Calculator:** Determines if you are in a healthy weight range based on height and weight.
* **BMR Calculation:** Uses the **Harris-Benedict Equation** to estimate the number of calories your body burns at rest.
* **Daily Water Intake:** Calculates the recommended daily water consumption based on body weight.
* **Ideal Body Weight (IBW):** Estimates ideal weight using the **Devine Formula**.
* **Continuous Loop:** The program runs continuously, allowing multiple calculations without restarting.

## ⚙️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/health-calc-python.git](https://github.com/KULLANICI_ADIN/health-calc-python.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd health-calc-python
    ```
3.  **Run the script:**
    ```bash
    python health_calc.py
    ```

## 🧠 Formulas Used

This tool uses widely accepted scientific formulas for its calculations:

| Metric | Formula Used |
| :--- | :--- |
| **BMI** | `Weight (kg) / Height (m)²` |
| **BMR** | **Harris-Benedict Equation** (Revised by Roza and Shizgal, 1984) |
| **Water** | `Weight (kg) * 0.035 Liters` |
| **IBW** | **Devine Formula** (1974) |

## ⚠️ Important Notes

* **IBW Accuracy:** The Ideal Body Weight calculation (Devine Formula) is most accurate for adults taller than **152 cm (5 feet)**. Results for shorter individuals may not be clinically accurate.
* **Disclaimer:** This tool is for informational purposes only and does not constitute medical advice. Please consult a healthcare professional for personalized medical guidance.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for new features (like body fat percentage or macronutrient calculator), feel free to fork the repo and submit a pull request.

## 📄 License

This project is licensed under the MIT License.