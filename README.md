# 🤖 Hausa Giveaway Telegram Bot

Wannan Telegram bot yana gudanar da giveaway ta atomatik tare da tsari mai kyau da tsafta. Bot ɗin zai:

- Tura sanarwa zuwa Telegram Channel
- Tura tunatarwa (countdown) zuwa Group
- Karɓi account details daga users
- Raba su bisa jinsi (Mata 20, Maza 30)
- Hana duplicate entries
- Fara aika sakon receipt daga 10:00PM zuwa 11:00PM
- Tura saƙon ƙarshe da godiya

## 🕒 Lokutan Aiki

| Lokaci    | Aiki                                                                 |
|-----------|----------------------------------------------------------------------|
| 8:00 PM   | Tura sako zuwa **Channel** game da giveaway                          |
| 8:30 PM   | Tura tunatarwa zuwa **Group** cewa saura 30 mins                    |
| 8:50 PM   | Tura tunatarwa cewa saura 10 mins                                   |
| 9:00 PM   | Tura sako: *It's time to drop account details!*                      |
| 10–11 PM  | Aika receipt na *an tura kudi* ga winners 50 (Mata 20, Maza 30)      |
| 11:00 PM  | Tura sako na ƙarshe da godiya                                        |

## 📥 Misalin Format ɗin da Users zasu bi

```text
Bank num: 9131***779  
Bank name: Opay  
Name holder: Bashir Rabiu
```

Bot zai gane mace/namiji daga sunan **Name holder**.

## 🚫 Idan mutum ya turawa sau biyu

Bot zai ce:

```
⚠️ Ka riga ka sa account details naka.
📦 Idan kana cikin winners, zaka samu gift naka daga 10:00 zuwa 11:00PM.
🙏 Mun gode.
🤵 Nine naku – Bashir Rabiu.
```

## ⚙️ Gudanar da Bot

1. **Shigar da dependencies:**
```bash
pip install aiogram
```

2. **Saka Bot Token ɗinka a `config.py`:**
```python
BOT_TOKEN = "TOKEN_DINKA_ANAN"
```

3. **Gudanar da Bot:**
```bash
python main.py
```

> ⚠️ Kada ka saka `config.py` ko token ɗinka a GitHub.
