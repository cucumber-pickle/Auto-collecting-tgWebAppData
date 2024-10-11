
# Auto collecting tgWebAppData
Скрипт для автоматического сбора query_id / user_id для TG portable без использования API TG

[TELEGRAM CHANNEL](https://t.me/cucumber_scripts)

## Инструкции по установке

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/cucumber-pickle/Auto-collecting-tgWebAppData.git
   cd Auto-collecting-tgWebAppData
   ```

2. **Создайте виртуальную среду (не обязательно):**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

   
3. **Установите зависимости::**


  ```bash
    pip install -r requirements.txt
  ```

## Настройки:

1. На всех аккаунтах телеграма необходимо включить - ``` Enable webview inspecting``` 

[Setting](https://github.com/user-attachments/assets/df6954e1-ca3f-4ce3-875a-ce60946eb600) => 
[Advanced](https://github.com/user-attachments/assets/f078210b-259c-4624-8edc-2d4f5b0c64a1) => 
[Experimental settings](https://github.com/user-attachments/assets/8f332751-53b3-47f8-83b7-c2ecb6e66f9e) => 
[Enable webview inspecting](https://github.com/user-attachments/assets/61f3886b-41ce-40c3-aacc-e4dcaabb3452)

2. В ```global_config.py``` укажите [папку, где находятся ваши ТГ аккаунты](https://github.com/user-attachments/assets/23dd772b-3b3f-4ddd-829f-27aa35f638aa):
Например - ```base_dir = r"C:\tg"```

В каждой папке должена лежать tdata и "Telegram.exe" (не больше 1 аккаунта в 1 папке)

3. Названия файлов .exe telegram должны [совпадать с названиями папок](https://github.com/user-attachments/assets/6d7270ef-767d-4806-8a80-95c8d95a9a94) 
или [называться "Telegram.exe"](https://github.com/user-attachments/assets/e0f9e5a0-5670-4c4b-9068-26efb93a1276)

4. Бот работает с помощью pyautogui и скорее всего, вам придётся собирать новые скрины кнопок.
Замените старые скриншоты на свои в папке pic. 
[Причина в разном масштабе экранов](https://stackoverflow.com/questions/45302681/running-pyautogui-on-a-different-computer-with-different-resolution)

Чтобы было удобнее делать обрезать скриншоты установите программу [lightshot](https://app.prntscr.com/en/)

[Скриншоты которые надо сделать](#cкриншоты)

5. В файле ```bots.txt``` – указать названия ботов, в файле ```acc.txt``` - указать названия папок телеграм

6. Когда запускаете скрипт – должен быть закрыт файл эксель, включена английская раскладка клавиатуры, отключены CapsLock и Fn

7. ```QueryOnly.py``` - находит бота через поисковую и запускает его, 
```Refferal.py``` - переходит в мою группу и регистрируется в боте по реферальной ссылке.

Запустите 1 из этих файлов:

```bash
    python QueryOnly.py
```

```bash
    python Refferal.py
```

## Правильное написание названий ботов (для bots.txt)

#### Для данных ботов вставляется специальный код в консоль, поэтому их названия надо писать именно так

```ruby
realgoats
tomarket
```

#### Если используете Refferal.py:

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
```

## Cкриншоты

Надо сделать на своем комьютере, чтобы бот работал коректно

#### Скрины в папке pic (обязательные):
1. [bot1](https://github.com/user-attachments/assets/a0b2f292-c6ac-45b6-8611-6898773f216d)
2. [bot2](https://github.com/user-attachments/assets/b72a7919-f551-4424-9d9c-f58b13182079)
3. [con1](https://github.com/user-attachments/assets/97465774-f33e-4b6e-9354-b22b21a7597f)
4. [con2](https://github.com/user-attachments/assets/212c4a02-2014-4bd9-bbcf-dad921e7b1b8)
5. [con3](https://github.com/user-attachments/assets/e2632afd-325a-48f0-93e4-645a596ef734)
6. [close1](https://github.com/user-attachments/assets/9a7ab3b9-11ec-4ec9-9f2c-f0b60c3cff6f)

#### Если используете Refferal.py:
1. [seach1](https://github.com/user-attachments/assets/1ec351d0-0b5b-414f-a5b2-0bfc5f0fed48)
2. [Отдельный скриншот для каждого бота из папки pic/bots](https://github.com/user-attachments/assets/30c1c78f-dd89-46e4-b369-3917d2af71d6)


## Этот бот был Вам полезен? Пожалуйста, подписывайтесь на канал или можете купить мне кофе: 
``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - BSC (BEP 20)

``` UQBiNbT2cqf5gLwjvfstTYvsScNj-nJZlN2NSmZ97rTcvKz0 ``` - TON

``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - Optimism

``` THaLf1cdEoaA73Kk5yiKmcRwUTuouXjM17 ``` - TRX (TRC 20)

## License
This project is licensed under the `MIT License`.

## Контакты
Если есть вопросы или предложения, пишите в Telegram  [CUCUMBER TG CHAT](https://t.me/cucumber_scripts_chat)