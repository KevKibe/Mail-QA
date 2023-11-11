from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/calendar']


def authenticate():
    """Authenticate the user and obtain valid credentials."""
    credentials = None

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            credentials = run_authentication_flow() 
    return credentials.to_json()

def run_authentication_flow():
    """Run the OAuth 2.0 authentication flow to get new credentials."""
    flow = InstalledAppFlow.from_client_secrets_file(
        'credss.json',
        scopes=SCOPES,
        # redirect_uri='https://e719-41-80-117-13.ngrok-free.app:8081/oauth2/callback',
        redirect_uri='http://localhost:8050/',
    )

    flow.run_local_server( port = 8050, prompt='consent', authorization_prompt_message='')

    return flow.credentials
