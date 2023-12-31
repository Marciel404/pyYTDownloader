import time
from pytube import YouTube


class _EmptyName:

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "No Name"

    def __len__(self) -> int:
        return 0


EmptyName = _EmptyName()


class BuildConsole:

    def __init__(self):

        from translates import Translate
        from utils import printerLogo

        lang = "pt-BR"

        self.translate: dict[str] = Translate.lang(lang)

        printerLogo()

        print(self.translate["menu"])

        options = {
            0: lambda: self.config(),
            1: lambda: self.download_only_audio(input(self.translate["NameOrUrlA"])),
            2: lambda: self.download_video(input(self.translate["NameOrUrlV"])),
            3: lambda: self.download_only_video(input(self.translate["NameOrUrlVov"])),
            4: lambda: exit("Seção encerrada pelo client")
        }

        try:
            options[int(input(self.translate["selectOpt"]))]()
        except Exception as err:
            print(err)

        time.sleep(5)
        BuildConsole()

    @property
    def name(self) -> str:
        """
        This property return the name of music formated
        :return: str
        """
        return getattr(self, "_name", EmptyName)

    @name.setter
    def name(self, value: str) -> None:
        """
        This function is a setter to format the name of music
        :param value:
        :return:
        """
        import re
        self._name = re.sub(
            r"[&@¨|:!'\"\\/\n?]",
            "",
            f"{value}\n",
            0,
            re.MULTILINE | re.IGNORECASE
        )

    def config(self) -> None:
        ...

    def download_only_audio(self, name: str) -> None:

        """
        This function start download only audio of video from YouTube
        :param name:
        :return:
        """

        if "http" in name:

            print(self.translate["startD"])

            yt = YouTube(name)

            self.name = yt.title

            yt.streams \
                .get_audio_only() \
                .download(output_path="Musics",
                          filename=f"{self.name}.wav"
                          )

            print(self.translate["endD"])

        else:

            query = self.pesquisar(name)

            slcV = int(input(self.translate["slcV"])) - 1

            yt = YouTube(query[slcV]["link"])

            print(self.translate["startD"])

            self.name = query[slcV]["title"]

            yt.streams \
                .get_audio_only() \
                .download(output_path="Musics",
                          filename=f"{self.name}.wav",
                          )

            print(self.translate["endD"])

        time.sleep(5)
        BuildConsole()

    def download_video(self, name: str) -> None:
        """
        This function start download video from YouTube
        :param name:
        :return:
        """
        if "http" in name:

            yt = YouTube(name)

            print(self.translate["startD"])

            self.name = yt.title

            yt \
                .streams \
                .get_highest_resolution() \
                .first() \
                .download(output_path="Videos",
                          filename=f"{self.name}.mp4"
                          )

            print(self.translate["endD"])

        else:

            query = self.pesquisar(name)

            slcV = int(input(self.translate["slcV"])) - 1

            yt = YouTube(query[slcV]["link"])

            print(self.translate["startD"])

            self.name = query[slcV]["title"]

            yt \
                .streams \
                .get_highest_resolution() \
                .first() \
                .download(output_path="Videos",
                          filename=f"{self.name}.mp4"
                          )

            print(self.translate["endD"])

        time.sleep(5)
        BuildConsole()

    def download_only_video(self, name: str) -> None:

        """
        This function start download only video (no audio) from YouTube
        :param name:
        :return:
        """

        if "http" in name:

            yt = YouTube(name)

            print(self.translate["startD"])

            self.name = yt.title

            yt \
                .streams \
                .filter(only_video=True) \
                .first() \
                .download(output_path="Videos",
                          filename=f"{self.name}.mp4"
                          )

            print(self.translate["endD"])

        else:

            query = self.pesquisar(name)

            slcV = int(input(self.translate["slcV"])) - 1

            yt = YouTube(query[slcV]["link"])

            print(self.translate["startD"])

            self.name = query[slcV]["title"]

            yt \
                .streams \
                .filter(only_video=True) \
                .first() \
                .download(output_path="Videos",
                          filename=f"{self.name}.mp4"
                          )

            print(self.translate["endD"])

        time.sleep(5)
        BuildConsole()

    def pesquisar(self, name: str) -> list:
        """
        Search the YouTube videos and form them into a neat string and show them on the console
        :param name:
        :return: dict[str,dict[str,[str, str]]
        """

        from youtubesearchpython import Search

        query: list = Search(name, 5, "any", "any").result()["result"]

        Array: list = []

        for result in query:
            print(result)
            if "viewCount" in result and result["publishedTime"] is not None:
                Array.append(result)

        for i, r in enumerate(Array):
            self.formatString(i + 1, r)

        return Array

    def formatString(self, index: int, Array: dict[str, dict[str, str]]) -> None:

        """
        Formats surveys into prettier text
        :param index:
        :param Array:
        :return:
        """
        views = (Array["viewCount"]["short"]
                 if Array["viewCount"]["text"].count(",") >= 2
                 else Array["viewCount"]["text"])

        print("-" * 20)
        print(f"""{index} - {Array["title"]}
Link: {Array["link"]}
{self.translate["channel"]} {Array["channel"]["name"]} ({Array["channel"]["link"]})
{self.translate["tPB"]} {Array["publishedTime"]}
{self.translate["Views"]} {views}""")
        print("-" * 20)


if __name__ == "__main__":
    BuildConsole()
