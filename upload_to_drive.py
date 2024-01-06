import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# サービスアカウントの認証情報を読み込む
SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Google Drive API クライアントを構築
service = build('drive', 'v3', credentials=credentials)

# 環境変数からフォルダIDを取得
folder_id = os.environ['DRIVE_FOLDER_ID']

# アップロードするファイル
file_metadata = {
    'name': 'test.txt',  # ここにアップロードするファイル名を指定
    'parents': [folder_id]
}
media = MediaFileUpload('test.txt', mimetype='text/plain')

# ファイルをアップロード
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print('Uploaded File ID:', file.get('id'))
