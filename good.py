import colors


def good_print(
        text:str = None
):
    text = colors.ansi_wrap(
        text = text,
        color = 'green'
    )
    print(text)