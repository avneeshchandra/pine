import colors


def bad_print(
        text:str = None
):
    text = colors.ansi_wrap(
        text = text,
        color = 'red'
    )
    print(text)