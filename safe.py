import colors


def safe_print(
        text:str = None
):
    text = colors.ansi_wrap(
        text = text,
        color = 'grey'
    )
    print(text)