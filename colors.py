color_hex = {
    "black": "#000000",
    "red": "#FF0000",
    "green": "#00FF00",
    "yellow": "#FFFF00",
    "blue": "#0000FF",
    "magenta": "#FF00FF",
    "cyan": "#00FFFF",
    "white": "#FFFFFF",
    "grey": "#CCCCCC",
    # "light blue": "light blue"
}

hex_ansi = {
    "#000000": "30m",  # Black
    "#FF0000": "31m",  # Red
    "#00FF00": "32m",  # Green
    "#FFFF00": "33m",  # Yellow
    "#0000FF": "34m",  # Blue
    "#FF00FF": "35m",  # Magenta
    "#00FFFF": "36m",  # Cyan
    "#FFFFFF": "37m",  # White
    # "#CCCCCC": "37;5m",  #Grey blinking!
    # "#CCCCCC": "37;3m",  #Grey italicized!
    # "#CCCCCC": "37;4m",  #Grey underlined!
    "#CCCCCC": "37;6m",  #Grey!
    # "light blue":"104m"
}

def ansi_open(
        ansi_color:str,
        mode:str = None
):
    return f"\033[{ansi_color}"

def ansi_close(
        
):
    return "\033[0m"

def ansi_from_color(
        color:str
):
    return hex_ansi.get(color_hex.get(color,"#000000"),"30m")

def ansi_wrap(
        text:str,
        color:str,
        mode:str = None,
):
    ansi_color = ansi_from_color(color)
    if mode:
        if mode == 'blinking':
            ansi_color = ansi_color.replace("m",";5m")
    return f"{ansi_open(ansi_color)}{text[1:]}{ansi_close()}"