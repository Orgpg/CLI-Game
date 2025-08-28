
```markdown
# 🚀 PyPI အစကတည်းက Package တင်နည်း Guide

ဒီ Document မှာ Python Project ကို PyPI (pip) မှာ အစကတည်းက Publish လုပ်နိုင်ဖို့လိုအပ်တဲ့ အဆင့်တွေကို တစ်ခုချင်း ဖော်ပြထားပါတယ်။

---

## 1. PyPI Account ဖန်တီး
1. [PyPI.org](https://pypi.org/account/register/) သွားပြီး Account ဖန်တီးပါ။
2. Email ကို Confirm လုပ်ပါ။

---

## 2. API Token ဖန်တီး
1. PyPI → **Account settings → API tokens**
2. **Create API token** ကိုနှိပ်ပါ  
   - Token name: e.g. `CLI-Games-HND68`
   - Scope: Entire account (သို့) Project-specific
3. Generate လုပ်ပြီး ထွက်လာတဲ့ **Token** ကို Copy ထားပါ  
   ⚠️ Token ကို တစ်ကြိမ်ထဲပဲ ပြသပေးမလို့ ထိန်းသိမ်းထားဖို့လိုပါသည်။

---

## 3. Project Structure စီမံ
Project folder ကို အောက်ပါအတိုင်း သေချာထားပါ👇

CLI-Game-HND68/
├── cli_games/
│   ├── __init__.py
│   ├── guess_the_number.py
│   ├── math_quiz_duel.py
│   └── typing_speed_race.py
├── README.md
├── LICENSE
├── requirements.txt
└── setup.py


---

## 4. setup.py ဖိုင်ရေး
```python
from setuptools import setup, find_packages

setup(
    name="cli-games-hnd68",  # pip install name (unique ဖြစ်ရမယ်)
    version="0.1.0",
    description="Fun CLI games: Number Guessing Duel, Math Quiz Duel, Typing Speed Race",
    author="Wai Phyo Aung",
    author_email="info@waiphyoaung.dev",
    url="https://github.com/Orgpg/CLI-Game-HND68",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'guessing=cli_games.guess_the_number:play_game',
            'mathquiz=cli_games.math_quiz_duel:play_game',
            'typerace=cli_games.typing_speed_race:play_game',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
````

---

## 5. Build Package

```bash
pip install --upgrade build twine
python -m build
```

အောင်မြင်ရင် `dist/` folder ထဲမှာ

* `.whl`
* `.tar.gz`

၂ ဖိုင်ထွက်လာမယ်။

---

## 6. Upload to PyPI

```bash
python -m twine upload dist/*
```

Prompt တက်လာတဲ့အချိန် Username / Password ထည့်ပါ

* **Username** → `__token__`
* **Password** → မင်း Generate လုပ်ထားတဲ့ API Token

---

## 7. Install & Test

Upload အောင်မြင်ပြီးရင် တခြားသူတွေ (မင်းပါ) install လို့ရမယ်👇

```bash
pip install cli-games-hnd68
```

ပြီးရင် CLI command တွေ run လို့ရမယ်👇

```bash
guessing
mathquiz
typerace
```

---

## 📌 မှတ်သားရန်

* **Project name (setup.py → name=)** သည် PyPI ထဲမှာ unique ဖြစ်ရမယ် (ထပ်မရ)
* တင်တိုင်း **version number တိုးပေးရမယ်** (`0.1.0 → 0.1.1 → 0.1.2 ...`)
* Token ကို အသုံးပြုတဲ့အခါ Username = `__token__`, Password = API Token

---
