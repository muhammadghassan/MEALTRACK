Here's the complete `README.md` file with **all steps included** in a proper block format:  

```markdown
# 🥗 MEALTRACK  

## 📌 COMP3330 Interactive Mobile Application Design and Programming Project  

**MEALTRACK** is a mobile application that helps users track their dietary habits efficiently. It allows users to log meals with timestamps, photos, and food categories. The app also provides **data visualization and analytics** to help users understand their eating patterns and make healthier choices.  

---

## 🚀 Features  

✅ **Record Meals** – Log what you eat with timestamps and images.  
✅ **Cloud Sync** – Save and access meal records from anywhere.  
✅ **Diet Insights** – Visualize eating patterns using graphs and charts.  
✅ **Reminders** – Get notifications to eat at scheduled times.  
✅ **Food Suggestions** – Personalized meal recommendations based on your dietary habits.  

---

## 📥 Installation & Setup  

### 🔧 Prerequisites  

Before running the project, ensure that you have:  
- Python installed on your system.  
- Android Studio (for modifying and running the app).  
- The mobile app installed on your Android device.  

---

### 🛠 Steps to Run the Project  

#### 1️⃣ **Generate the Database**  
Run the following command to set up the database:  

```bash
python db.py
```

#### 2️⃣ **Start the Server**  
Execute the server script:  

```bash
python server.py
```

- After running the command, the terminal will display **two IP addresses**.  
- Copy the **second IP address** (`192.xxx.xxx.xxx:xxxx`).  
- Open the mobile app source code (`MainActivity`) and replace the `serverIP` variable with this IP.  

#### 3️⃣ **Login to the Mobile App**  
Use the following test accounts:  

| Username | Password  | Records Available |
|----------|----------|------------------|
| A        | password | 26/11/2023 – 02/12/2023 |
| C        | aabBbcc  | 19/11/2023 – 25/11/2023 |

---

## 📖 Usage Guide  

### 🔹 Quick Date Selection in Calendar View  
- Tap the **date text label** to open a date picker.  

### 🔹 Image Upload & Download  
- **Known Issue:** The app may fail to download images larger than **1 MB**.  

---

## 🔮 Future Enhancements  

- 📌 **Smart Watch Integration** – Sync food intake data with health devices.  
- 📌 **Medication Reminders** – Notify users when to take prescribed medications.  
- 📌 **AI-based Meal Suggestions** – Recommend meals based on user habits.  
- 📌 **WHO Nutrient Comparison** – Analyze intake based on age and activity levels.  

---

## 🛠 Troubleshooting  

### ❌ Issue: Server Not Running  
- Ensure Python is installed and `server.py` is executed without errors.  

### ❌ Issue: Cannot Download Images >1 MB  
- Try reducing the image size before uploading.  

---

## 🏗️ Project Structure  

```
📂 MealTrack/
│── 📂 app/                 # Mobile app source code
│── 📂 backend/             # Backend server scripts
│── ├── db.py               # Database initialization script
│── ├── server.py           # Main server script
│── 📂 docs/                # Documentation and reports
│── 📂 images/              # Screenshots and promotional materials
│── README.md               # Project overview and setup instructions
│── requirements.txt        # Dependencies list
```

---

## 👨‍💻 Contributors  

- **Chan Ka Ho**  
- **Jawwad Muhammad Ghassan**  
- **Tai Yu Yeung**  
- **Wong Wai Ching**  

---

## 📜 License  

This project is licensed under the **MIT License**. See `LICENSE` for details.  

---

Feel free to contribute or raise issues for improvements! 🚀
```  

Now, this **includes all steps properly formatted** for GitHub. You can copy and paste it directly into your repository! ✅
