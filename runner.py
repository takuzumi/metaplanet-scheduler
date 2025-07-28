from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# スコープと認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# スプレッドシート
spreadsheet = client.open("テスト")
sheet = spreadsheet.worksheet("シート1")

# データを書き込む
today = datetime.now().strftime("%Y-%m-%d")
value = "自動取得値"  # ← 後でSeleniumなどで取得した値に置き換える
sheet.append_row([today, value])
