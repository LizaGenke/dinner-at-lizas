# dinner-at-lizas
An amazing tool that will simplify our meal planning process

## Requirements to run:
Our application runs with a firebase database. See <https://firebase.google.com/> for setup instructions.

It expects a pyrebase config file under `env/databse_config.json`, sample contents are:

```json
config = {
    "apiKey": "${apiKey}",
    "authDomain": "${projectId}.firebaseapp.com",
    "databaseURL": "https://${databaseName}.firebaseio.com",
    "storageBucket": "${projectId}.appspot.com",
    "serviceAccount": "${path_to_your_service_account_credentials}.json"
}
```

See : <https://github.com/thisbejim/Pyrebase>