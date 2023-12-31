class bcolors:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'


def pesquisar(name: str) -> list:
    """
    Search the YouTube videos and form them into a neat string and show them on the console
    :param name:
    :return: dict[str,dict[str,[str, str]]
    """

    from main import BuildConsole
    from youtubesearchpython import Search

    query: list = Search(name, 5, "any", "any").result()["result"]

    Array: list = []

    for result in query:
        if "viewCount" in result and result["publishedTime"] is not None:
            if "http" in name:
                if name == result["link"]:
                    Array.append(result)
            else:
                Array.append(result)

    for i, r in enumerate(Array):
        BuildConsole.formatString(i + 1, r)

    return Array


def printerLogo():
    import os
    import psutil

    parent_pid = os.getppid()

    if psutil.Process(parent_pid).name().lower() == "python.exe":
        print(f"""{bcolors.CBLACKBG}{bcolors.CWHITE}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{bcolors.CYELLOW}########::'##:::'##:::{bcolors.CRED}:'##:::'##:'########::{bcolors.CBLUE}'########:::'#######::'##:::::'##:'##::: ##:'##::::::::'#######:::::'###::::'########::'########:'########::
{bcolors.CYELLOW}##.... ##:. ##:'##::::{bcolors.CRED}:. ##:'##::... ##..:::{bcolors.CBLUE} ##.... ##:'##.... ##: ##:'##: ##: ###:: ##: ##:::::::'##.... ##:::'## ##::: ##.... ##: ##.....:: ##.... ##:
{bcolors.CYELLOW}##:::: ##::. ####:::::{bcolors.CRED}::. ####:::::: ##:::::{bcolors.CBLUE} ##:::: ##: ##:::: ##: ##: ##: ##: ####: ##: ##::::::: ##:::: ##::'##:. ##:: ##:::: ##: ##::::::: ##:::: ##:
{bcolors.CYELLOW}########::::. ##::::::{bcolors.CRED}:::. ##::::::: ##:::::{bcolors.CBLUE} ##:::: ##: ##:::: ##: ##: ##: ##: ## ## ##: ##::::::: ##:::: ##:'##:::. ##: ##:::: ##: ######::: ########::
{bcolors.CYELLOW}##.....:::::: ##::::::{bcolors.CRED}:::: ##::::::: ##:::::{bcolors.CBLUE} ##:::: ##: ##:::: ##: ##: ##: ##: ##. ####: ##::::::: ##:::: ##: #########: ##:::: ##: ##...:::: ##.. ##:::
{bcolors.CYELLOW}##::::::::::: ##::::::{bcolors.CRED}:::: ##::::::: ##:::::{bcolors.CBLUE} ##:::: ##: ##:::: ##: ##: ##: ##: ##:. ###: ##::::::: ##:::: ##: ##.... ##: ##:::: ##: ##::::::: ##::. ##::
{bcolors.CYELLOW}##::::::::::: ##::::::{bcolors.CRED}:::: ##::::::: ##:::::{bcolors.CBLUE} ########::. #######::. ###. ###:: ##::. ##: ########:. #######:: ##:::: ##: ########:: ########: ##:::. ##:
{bcolors.CYELLOW}..::::::::::::..::::::{bcolors.CRED}:::::..::::::::..:::::{bcolors.CBLUE}:........::::.......::::...::...:::..::::..::........:::.......:::..:::::..::........:::........::..:::::..:
{bcolors.CWHITE}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{bcolors.CEND}
""")
    else:
        os.system("cls")
        print("""::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::'########::'##:::'##:::::::'##:::'##:'########::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::: ##.... ##:. ##:'##::::::::. ##:'##::... ##..:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::: ##:::: ##::. ####::::::::::. ####:::::: ##:::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::: ########::::. ##::::::::::::. ##::::::: ##:::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::: ##.....:::::: ##::::::::::::: ##::::::: ##:::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::: ##::::::::::: ##::::::::::::: ##::::::: ##:::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::: ##::::::::::: ##::::::::::::: ##::::::: ##:::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::..::::::::::::..::::::::::::::..::::::::..::::::::::::::::::::::::::::::::::::
'########:::'#######::'##:::::'##:'##::: ##:'##::::::::'#######:::::'###::::'########::'########:'########::
 ##.... ##:'##.... ##: ##:'##: ##: ###:: ##: ##:::::::'##.... ##:::'## ##::: ##.... ##: ##.....:: ##.... ##:
 ##:::: ##: ##:::: ##: ##: ##: ##: ####: ##: ##::::::: ##:::: ##::'##:. ##:: ##:::: ##: ##::::::: ##:::: ##:
 ##:::: ##: ##:::: ##: ##: ##: ##: ## ## ##: ##::::::: ##:::: ##:'##:::. ##: ##:::: ##: ######::: ########::
 ##:::: ##: ##:::: ##: ##: ##: ##: ##. ####: ##::::::: ##:::: ##: #########: ##:::: ##: ##...:::: ##.. ##:::
 ##:::: ##: ##:::: ##: ##: ##: ##: ##:. ###: ##::::::: ##:::: ##: ##.... ##: ##:::: ##: ##::::::: ##::. ##::
 ########::. #######::. ###. ###:: ##::. ##: ########:. #######:: ##:::: ##: ########:: ########: ##:::. ##:
........::::.......::::...::...:::..::::..::........:::.......:::..:::::..::........:::........::..:::::..::
""")
