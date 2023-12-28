import re
from youtubesearchpython import Search
from pytube import YouTube
from Translates import Translate


class _EmptyName:

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "No Name"

    def __len__(self) -> int:
        return 0


EmptyName = _EmptyName()


def formatString(index: int, Array: dict[str, dict[str, str]]):

    """
    Formats surveys into prettier text
    :param index:
    :param Array:
    :return:
    """

    views = Array["viewCount"]["short"] if Array["viewCount"]["text"].count(",") >= 2 else Array["viewCount"][
        "text"]

    print("-" * 20)
    print(f"""{index} - {Array["title"]}
Link: {Array["link"]}
{Translate.lang("pt-BR", "channel")} {Array["channel"]["name"]} ({Array["channel"]["link"]})
{Translate.lang("pt-BR", "tPB")} {Array["publishedTime"]}
{Translate.lang("pt-BR", "Views")} {views}""")
    print("-" * 20)


class Build:

    def __init__(self):

        print(Translate.lang("pt-BR", "menu"))

        Option = int(input(Translate.lang("pt-BR", "selectOpt")))

        match Option:

            case 0:
                ...

            case 1:

                name = input(Translate.lang("pt-BR", "NameOrUrlA"))
                self.only_audio(name)

            case 2:
                ...

            case 3:
                ...

            case 4:
                ...

            case _:
                ...

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
        self._name = re.sub(
            r"[&@¨|:!'\"\\/\n]",
            "",
            f"{value}\n",
            0,
            re.MULTILINE | re.IGNORECASE
        )

    def only_audio(self, name: str) -> None:

        """
        This function start only audio of video from YouTube
        :param name:
        :return:
        """

        if "http" in name:

            print(Translate.lang("pt-BR", "startD"))

            yt = YouTube(name)

            self.name = yt.title

            yt.streams \
                .get_audio_only() \
                .download(
                    output_path="Musics",
                    filename=f"{self.name}.wav",
                )

            print(Translate.lang("pt-BR", "endD"))

        else:

            query = Search(name, 5, "any", "any").result()["result"]

            for i, r in enumerate(query):
                formatString(i + 1, r)

            slcV = int(input(Translate.lang("pt-BR", "slcV")))-1

            yt = YouTube(query[slcV]["link"])

            print(Translate.lang("pt-BR", "startD"))

            self.name = query[slcV]["title"]

            yt.streams \
                .get_audio_only() \
                .download(
                    output_path="Musics",
                    filename=f"{self.name}.wav",
                )

            print(Translate.lang("pt-BR", "endD"))


if __name__ == '__main__':
    Build()
