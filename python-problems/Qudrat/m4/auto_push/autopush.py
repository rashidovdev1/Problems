import os
import datetime

# === GitHub repo manzilingni bu yerda yoz ===
repo_path = r"D:\git\Problems"  # <-- o'zingning repong yo'lini yoz

# === Repository ichiga kiramiz ===
os.chdir(repo_path)

# === Sana bilan commit nomi ===
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"Auto commit on {today}"

# === Git komandalar ===
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")  # agar branch 'main' bo'lmasa, 'master' yoki boshqasiga o'zgartir
