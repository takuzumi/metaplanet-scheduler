import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# 認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# スプレッドシートに書き込む
sheet = client.open("テスト").worksheet("シート1")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sheet.append_row([now, "自動入力"])
