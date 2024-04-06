<h1 align="center">Genshin-utils</h1>

# Prerequisites 📋

- Install Browser (Now only supported Chrome)
- Login to Hoyolab with the Google account that will run the script

## Features
Features            | Chrome | Firefox | Edge | Safari | Opera |
|-------------------|--------|---------|---------|--------|--------|
Login               | ❌     | ❌      | ❌      | ❌     |  ❌    |
Obtain login bonus  | ✅     | ❌      | ❌      | ❌     |  ❌    |

## Usage

```bash
export GENSHIN_UTILS_USER_DATA_DIR=<C:\Users\{USERNAME}\AppData\Local\Google\Chrome\User Data>
export GENSHIN_UTILS_PROFILE_DIRECTORY=><Default>
```

```bash
pip install -r requirements.txt
python hoyolab\obtain_login_bonus.py --headless
```
