import colors


def ugly_print(
        text:str = None
):
    text = colors.ansi_wrap(
        text = text,
        color = 'yellow'
    )
    print(text)

def look_print(
        text:str = None
):
    text = colors.ansi_wrap(
        text = text,
        color = 'yellow',
        mode = 'blinking'
    )
    print(text)