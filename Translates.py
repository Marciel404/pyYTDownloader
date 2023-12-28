class Translate:
    lg = {
        "pt-BR": {
            "menu": """
0 - Opções
1 - Download aúdio
2 - Download Vídeo
3 - Download somente vídeo (Sem áudio)
            """,
            "selectOpt": "Selecione uma opção: ",
            "NameOrUrlA": "Nome ou Url do video que deseja baixar o áudio: ",
            "NameOrUrlV": "Nome ou Url do video que deseja baixar: ",
            "NameOrUrlVoV": "Nome ou Url do video que deseja baixar sem audio: ",
            "tPB": "Tempo Publicado:",
            "time": "Duração:",
            "Views": "Visualizações:",
            "channel": "Canal:",
            "slcV": "Selecione o número do video: ",
            "startD": "Iniciando Download",
            "endD": "Download concluido"
        },

    }

    @classmethod
    def lang(cls, lang: str, arg: str) -> str:
        return cls.lg[lang][arg]