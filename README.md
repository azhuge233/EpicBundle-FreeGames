# EpicBundle-FreeGames
There's a [dotnet version](https://github.com/azhuge233/EpicBundle-FreeGames-dotnet), any future updates will be added there first.

## My Free Games Collection

- SteamDB
    - [https://github.com/azhuge233/SteamDB-FreeGames](https://github.com/azhuge233/SteamDB-FreeGames)(Python)
    - [https://github.com/azhuge233/SteamDB-FreeGames-dotnet](https://github.com/azhuge233/SteamDB-FreeGames-dotnet)
- EpicBundle
    - [https://github.com/azhuge233/EpicBundle-FreeGames](https://github.com/azhuge233/EpicBundle-FreeGames)(Python)
    - [https://github.com/azhuge233/EpicBundle-FreeGames-dotnet](https://github.com/azhuge233/EpicBundle-FreeGames-dotnet)
- Indiegala
    - [https://github.com/azhuge233/IndiegalaFreebieNotifier](https://github.com/azhuge233/IndiegalaFreebieNotifier)
- GOG
    - [https://github.com/azhuge233/GOGGiveawayNotifier](https://github.com/azhuge233/GOGGiveawayNotifier)

## Usage

Clone repo

``` shell
git clone https://github.com/azhuge233/EpicBundle-FreeGames.git
```

Install packages

```shell
pip3 install -r requirements.txt
```

Fill your bot TOKEN and your account ID to CONFIG field in the app.py file, then run

```shell
python3 app.py
```

To schedule the script, use cron.d in Linux(macOS) or Task Scheduler in Windows.

**Notice**: when the script used as a scheduled task, change the "PATH" variable to your absolute path.

Tested on Windows Server 2019 (python3.9) and macOS Big Sur (python3.9).
