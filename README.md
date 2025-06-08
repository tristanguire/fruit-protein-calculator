# 🥭 Protein Tracker from Fruits

This Python script helps users calculate their recommended daily protein intake based on their body weight and activity level, then lets them log fruits eaten throughout the day to track how much protein they've consumed from those fruits using data from the [Fruityvice API](https://www.fruityvice.com/).

---

## ⚙️ Features

- Calculates recommended daily protein intake.
- Accepts activity level from sedentary to extremely active.
- Uses Fruityvice API to get nutritional info about fruits.
- Tracks total protein consumed from fruits.
- Compares actual intake against your recommended value.

---

## 🧪 Example

```
Enter your bodyweight in lbs: 160
Enter your activity level (1-5): 3
Your recommended protein value is 94.4 grams.

Enter the name of the fruit(s) eaten today (q to quit): banana
Enter the name of the fruit(s) eaten today (q to quit): apple
Enter the name of the fruit(s) eaten today (q to quit): q

Total protein from fruits: 1.23 grams.
You have consumed 1.30% of your recommended protein intake today through fruits.
```

---

## 🚀 How to Run

1. Install Python (>=3.6).
2. Install required library:
   ```
   pip install requests
   ```
3. Run the script:
   ```
   python protein_tracker.py
   ```

---

## 📌 Notes

- Activity level options:
  - `1`: Sedentary
  - `2`: Lightly active
  - `3`: Moderately active
  - `4`: Very active
  - `5`: Extremely active
- Protein content is only sourced from fruits via Fruityvice, which may be minimal compared to your actual needs.

---

## ❗ Disclaimer

This tool gives *rough estimates*. Always consult a health professional for serious dietary planning.
