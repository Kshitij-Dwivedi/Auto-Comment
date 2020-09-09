

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "C:\\Users\\hp\\Desktop\\client_secret_599729676410-89h63ku4ej32t4pc4565oo9hni1fgfcl.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.comments().insert(
        part="snippet",
        body={
          "snippet": {
            "parentId": "Ugypgz0idk6bPJ_Tih94AaABAg",
            "textOriginal": "This is the original comment."
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()