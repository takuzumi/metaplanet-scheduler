import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ✅ 環境変数からJSON文字列を取得し辞書に変換
creds_json = os.environ["GOOGLE_CREDENTIALS_JSON"]
creds_dict = json.loads(creds_json)

# ✅ サービスアカウント認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# ✅ スプレッドシートに書き込み
sheet = client.open("テスト").worksheet("シート1")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sheet.append_row([now, "自動入力"])
