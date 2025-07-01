# Exam02 - Lessons[13-24]

### ✅ 1. **Calculator (Kalkulyator)**

**🧠 Vazifa**: Foydalanuvchi ikkita son va amal kiritadi (`+`, `-`, `*`, `/`). Siz tegishli natijani hisoblab chiqaring.

**➡️ Kirish**:

* Son 1: 8
* Amal: `*`
* Son 2: 5

**⬅️ Chiqish**:

* Natija: 40

**🔧 Funksiyalar**:

```python
def add(a, b): ...
def subtract(a, b): ...
def multiply(a, b): ...
def divide(a, b): ...
```

---

### ✅ 2. **Simple ATM Simulation**

**🧠 Vazifa**: Foydalanuvchi quyidagi amallardan birini bajaradi:

* **Pul qo‘yish** (deposit)
* **Pul yechish** (withdraw)
* **Balansni ko‘rish** (check balance)

**➡️ Kirish**:

* Boshlang‘ich balans: 100000
* Amal: deposit
* Miqdor: 50000

**⬅️ Chiqish**:

* Yangi balans: 150000

**🔧 Funksiyalar**:

```python
def deposit(balance, amount): ...
def withdraw(balance, amount): ...
def check_balance(balance): ...
```

---

### ✅ 3. **Tax Calculator**

**🧠 Vazifa**: Maoshga qarab soliqni hisoblang va sof maoshni chiqaring.

**Shart**:

* Maosh 5,000,000 dan katta bo‘lsa → soliq 20%
* Aks holda → soliq 13%

**➡️ Kirish**:

* Maosh: 6\_000\_000

**⬅️ Chiqish**:

* Soliq: 1\_200\_000
* Sof maosh: 4\_800\_000

**🔧 Funksiyalar**:

```python
def calculate_tax(salary): ...
def calculate_net_salary(salary): ...
```

---

### ✅ 4. **FISH tartibini o‘zgartirish**

**🧠 Vazifa**: Foydalanuvchi FISH (Familiya Ism Sharif) kiritadi. Siz uni `Ism Sharif, Familiya` shaklida chiqarishingiz kerak.

**➡️ Kirish**: `"Aliyev Vali G'aniyevich"`
**⬅️ Chiqish**: `"Vali G'aniyevich, Aliyev"`

---

### ✅ 5. **So‘zlar sonini hisoblash**

**🧠 Vazifa**: Matn ichidagi har bir so‘z necha marta qatnashganini aniqlang. Natijani `dict` tarzida qaytaring.

**➡️ Kirish**: `"salom salom dunyo"`
**⬅️ Chiqish**: `{'salom': 2, 'dunyo': 1}`

---

### ✅ 6. **Baholar tizimi**

**🧠 Vazifa**: Talabalar ro‘yxati `dict` tarzida berilgan. O‘rtacha bahoni hisoblang.
o'rtacha balldan yuqori baho olgan talabalarni chiqarish kerak.

**➡️ Kirish**:

```python
students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
```

**⬅️ Chiqish**:

* O‘rtacha baho: 4.25
* 4.25 dan yuqorilar: `Ali, Hasan`

---

### ✅ 7. **Mahsulotlar savatchasi**

**🧠 Vazifa**: Har bir mahsulot uchun narx va miqdor berilgan. Umumiy narxni hisoblang.

**➡️ Kirish**:

```python
cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
```

* Tushuntirish: `3000*2 + 8000*1 + 5000*5 = 37000`

**⬅️ Chiqish**:

* `Umumiy summa: 37000`

---

### ✅ 8. **Yig‘indi (`Input/numbers.txt`)**

**🧠 Vazifa**: `Input/numbers.txt` faylida berilgan sonlar yig‘indisini hisoblang va `Output/output08.txt` fayliga yozing.

**⬅️ Output (misol)**:

```
Yig'indi: 44
```

---

### ✅ 9. **Eng katta son (`Input/numbers.txt`)**

**🧠 Vazifa**: Fayldagi eng katta sonni toping va `Output/output09.txt` fayliga yozing.

**⬅️ Output (misol)**:

```
Eng katta son: 22
```

---

### ✅ 10. **Tartiblash (`Input/numbers.txt`)**

**🧠 Vazifa**: Fayldagi sonlarni tartiblang va `Output/output10.txt` fayliga yozing.

**⬅️ Output (misol)**:

```
-8
-5
0
3
7
10
15
22
```

---


### ✅ 11. **Ismlar soni (`Input/students.json`)**

**🧠 Vazifa**: `students.json` faylidagi o‘quvchilar sonini hisoblang va natijani `Output/output11.json` fayliga yozing.

**⬅️ Output (misol)**:

```json
{
  "count": 20
}
```

---

### ✅ 12. **Ismlarni alfavit bo‘yicha tartiblash (`Input/students.json`)**

**🧠 Vazifa**: `students.json` faylidagi barcha `name` maydonlarini alfavit bo‘yicha tartiblang va `Output/output12.json` fayliga yozing.

**⬅️ Output (misol)**:

```json
{
  "sorted_names": [
    "Abdukarim", "Abdulaziz", "Ali", "Alisher", "Anvar", "Aziza", "Aziz",
    "Diyor", "Jasurbek", "Kamola", "Lola", "Madina", "Muhammad", "Olim",
    "Ravshan", "Rustam", "Sardor", "Sherzod", "Umida", "Ziyoda"
  ]
}
```

---

### ✅ 13. **Uzun ismlar (`Input/students.json`)**

**🧠 Vazifa**: `name` uzunligi 5 harfdan oshadigan o‘quvchilarni aniqlang va `Output/output13.json` fayliga yozing.

**⬅️ Output (misol)**:

```json
{
  "long_names": [
    "Jasurbek", "Muhammad", "Abdulaziz", "Sherzod", "Alisher",
    "Kamola", "Rustam", "Ravshan", "Abdukarim", "Ziyoda"
  ]
}
```

---

### ✅ 14. **“A” bilan boshlanuvchilarni ajratish (`Input/students.json`)**

**🧠 Vazifa**: `name` qiymati "A" harfi bilan boshlanuvchi o‘quvchilarni toping va `Output/output14.json` fayliga yozing.

**⬅️ Output (misol)**:

```json
{
  "a_names": [
    "Ali", "Abdulaziz", "Anvar", "Alisher", "Abdukarim", "Aziza", "Aziz"
  ]
}
```

---

### ✅ 15. **Eng yuqori bahoni topish (`Input/grades.csv`)**

**🧠 Vazifa**: `grades.csv` faylidan eng yuqori baho olgan o‘quvchini aniqlang va `Output/output15.txt` fayliga yozing.

**⬅️ Output (misol)**:

```
Bahosi eng yuqori o‘quvchi: Ali - 5
```

---

### ✅ 16. **Bahosi 5 bo‘lganlar soni (`Input/grades.csv`)**

**🧠 Vazifa**: `grades.csv` faylidan bahosi 5 bo‘lganlar sonini hisoblang va `Output/output16.txt` fayliga yozing.

**⬅️ Output (misol)**:

```
5 baho olganlar soni: 6
```

---

### ✅ 17. **Musbat sonlarni ajratish (`filter` + list\[dict])**

**🧠 Vazifa**: Quyidagi ro‘yxatdan **qiymati musbat** bo‘lgan sonlarni ajrating (`value` qiymati bo‘yicha). Har bir element `dict` ko‘rinishida.

**➡️ Kirish**:

```python
numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]
```

**⬅️ Chiqish**:

```python
[{'value': 10}, {'value': 7}]
```

---

### ✅ 18. **Sonlarni kvadratga oshirish (`map` + list\[dict])**

**🧠 Vazifa**: Har bir elementning `value` qiymatini kvadratga oshiring. Natija ham `dict` ko‘rinishida bo‘lsin.

**➡️ Kirish**:

```python
numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]
```

**⬅️ Chiqish**:

```python
[{'value': 4}, {'value': 9}, {'value': 16}]
```

---

### ✅ 19. **Eng uzun ismni topish (`max` + list\[str])**

**🧠 Vazifa**: Ismlar ro‘yxatidan **eng uzun** ismni toping. Oddiy `list[str]` ishlating.

**➡️ Kirish**:

```python
names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']
```

**⬅️ Chiqish**:

```python
Muhammad
```

---

### ✅ 20. **Eng qisqa ismli o‘quvchini topish (`min` + list\[dict])**

**🧠 Vazifa**: Quyidagi o‘quvchilar ro‘yxatidan **ismi eng qisqa** bo‘lgan o‘quvchini toping.

**➡️ Kirish**:

```python
students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]
```

**⬅️ Chiqish**:

```python
Ali
```
