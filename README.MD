
# Auto collecting tgWebAppData
Script for Automatic Collection of query_id / user_id for TG Portable Without Using TG API

[TELEGRAM CHANNEL](https://t.me/cucumber_scripts)

# Warning

Before `git pull` save the `pic` folder with your screenshots to any other folder. 
So that your screenshots are not updated

## Updates 
**21.10.2024** 

Аdded the function of adding symbols/icons to the telegram name ([change_name.py](change_name.py)). To use this:

1. save your similar screenshots to the `pic/change_name` folder 
2. enter what you want to add to the name in the variable `add_to_name` in the file [core_change_name.py](src%2Fcore_change_name.py)


## Installation Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/cucumber-pickle/Auto-collecting-tgWebAppData.git
   cd Auto-collecting-tgWebAppData
   ```

2. **Create a Virtual Environment (Optional):**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

   
3. **Install dependencies:**


  ```bash
    pip install -r requirements.txt
  ```

## Configuration Settings

1. Enable WebView Inspecting on All Telegram Accounts:

[Setting](https://github.com/user-attachments/assets/df6954e1-ca3f-4ce3-875a-ce60946eb600) => 
[Advanced](https://github.com/user-attachments/assets/f078210b-259c-4624-8edc-2d4f5b0c64a1) => 
[Experimental settings](https://github.com/user-attachments/assets/8f332751-53b3-47f8-83b7-c2ecb6e66f9e) => 
[Enable webview inspecting](https://github.com/user-attachments/assets/61f3886b-41ce-40c3-aacc-e4dcaabb3452)

2.   [Set Directory for Telegram Accounts](https://github.com/user-attachments/assets/23dd772b-3b3f-4ddd-829f-27aa35f638aa): in global_config.py:
- Specify the folder where your Telegram accounts are located: - ```base_dir = r"C:\tg"```

- Each folder should contain tdata and Telegram.exe (ensure only one account per folder).

3. Ensure that the .exe files for Telegram [match the folder names](https://github.com/user-attachments/assets/6d7270ef-767d-4806-8a80-95c8d95a9a94) 
or [named "Telegram.exe"](https://github.com/user-attachments/assets/e0f9e5a0-5670-4c4b-9068-26efb93a1276)

4. The bot uses pyautogui, so you may need to take new screenshots of buttons if your screen resolution differs. 
Replace old screenshots in the pic folder.
[Reason](https://stackoverflow.com/questions/45302681/running-pyautogui-on-a-different-computer-with-different-resolution)

For easier screenshot cropping, consider using [lightshot](https://app.prntscr.com/en/)

 [Required Screenshots](#Required-Screenshots)

5. In the file ```bots.txt ``` – specify the names of the bots in the file ```acc.txt ``` - specify the names of the telegram folders

6. Ensure that Excel is closed, the keyboard layout is set to English, and CapsLock and Fn are disabled.

7. ```QueryOnly.py``` - finds the bot through the search engine and launches it,  
```Refferal.py``` - goes to my group and registers in the bot using a referral link.

Use one of the following commands to start:

```bash
    python QueryOnly.py
```

```bash
    python Refferal.py
```

## Correct Naming for Bots (for bots.txt)

#### For these bots, a special code is inserted into the console, so their names should be written exactly like this

```ruby
realgoats
tomarket
```

#### If Using Refferal.py, Include:

```ruby
banana
blum
kucoin
major
matchquest
pocketfi
realgoats
tomarket
depin
hamster
memefi
snapster
duckchain
yescoin
agent301bot
fintopio
okx
notpixel
clayton
moonbix
1win
cyberfinancebot
birds
pitchtalk
fomo
coub
```

## Required Screenshots

#### Mandatory Screenshots in the pic Folder:
1. [bot1](https://github.com/user-attachments/assets/a0b2f292-c6ac-45b6-8611-6898773f216d)
2. [bot2](https://github.com/user-attachments/assets/b72a7919-f551-4424-9d9c-f58b13182079)
3. [con1](https://github.com/user-attachments/assets/97465774-f33e-4b6e-9354-b22b21a7597f)
4. [con2](https://github.com/user-attachments/assets/212c4a02-2014-4bd9-bbcf-dad921e7b1b8)
5. [con3](https://github.com/user-attachments/assets/e2632afd-325a-48f0-93e4-645a596ef734)
6. [close1](https://github.com/user-attachments/assets/9a7ab3b9-11ec-4ec9-9f2c-f0b60c3cff6f)

#### If Using Refferal.py:
1. [seach1](https://github.com/user-attachments/assets/1ec351d0-0b5b-414f-a5b2-0bfc5f0fed48)
2. [Individual screenshots for each bot from the pic/bots folder.](https://github.com/user-attachments/assets/30c1c78f-dd89-46e4-b369-3917d2af71d6)


## Support and Donations
If you find this bot useful, consider subscribing to our channel or buying me a coffee:


``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - BSC (BEP 20)

``` UQBiNbT2cqf5gLwjvfstTYvsScNj-nJZlN2NSmZ97rTcvKz0 ``` - TON

``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - Optimism

``` THaLf1cdEoaA73Kk5yiKmcRwUTuouXjM17 ``` - TRX (TRC 20)

## License
This project is licensed under the `MIT License`.

## Contacts
For questions or suggestions, please reach out on Telegram at [CUCUMBER TG CHAT](https://t.me/cucumber_scripts_chat)