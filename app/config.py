import os

newsApiKey = os.environ['newsApiKey']
appLanguage = "en"
pageSize = 30
firebaseAuth = {
  "type": "service_account",
  "project_id": "wrap-it-9f8b4",
  "private_key_id": os.environ['FireBase_private_key_id'],
  "private_key": os.environ['FireBase_private_key'].replace('\\n', '\n'),
  "client_email": "firebase-adminsdk-6xnyn@wrap-it-9f8b4.iam.gserviceaccount.com",
  "client_id": "118218319032305289257",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6xnyn%40wrap-it-9f8b4.iam.gserviceaccount.com"
}
