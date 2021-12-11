class fmt:
    """epic module to give ansi escape codes for colors and stuff"""
    #?controll codes
    #resets all set modes
    ESC = '\033['
    MRESET = '\033[0m'
    #?colors
    #bright colors, with spacific codes
    BGBLACK = ESC + '100m'
    FGBLACK = ESC + '90m'
    BGRED = ESC + '101m'
    FGRED = ESC + '91m'
    BGGREEN = ESC + '102m'
    FGGREEN = ESC + '92m'
    BGYELLOW= ESC + '103m'
    FGYELLOW = ESC + '93m'
    BGBLUE= ESC + '104m'
    FGBLUE = ESC + '94m'
    BGMAGENTA= ESC + '105m'
    FGMAGENTA = ESC + '95m'
    BGCYAN= ESC + '106m'
    FGCYAN = ESC + '96m'
    BGWHITE= ESC + '107m'
    FGWHITE = ESC + '97m'
    #color by ID
    #foreground
    @staticmethod
    def fgid(id: int) -> str:
        "foreground color by id"
        assert 0 <= id <= 255
        return f'\033[38;5;{id}m'
    #background
    @staticmethod
    def bgid(id: int) -> str:
        "background color by id"
        assert 0 <= id <= 255
        return f'\033[48;5;{id}m'
    #color by RGB
    #foreground
    @staticmethod
    def fgrgb(r, g, b) -> str:
        "foreground color by rgb"
        return f'\033[38;2;{r};{g};{b}m'
    #background
    @staticmethod
    def bgrgb(r, g, b) -> str:
        "background color by rgb"
        return f'\033[48;2;{r};{g};{b}m'
    #?text modes
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALICS = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    INVERSE = '\033[7m'
    INVISIBLE = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    #reset modes spacificaly  
    RBOLD = '\033[22m'
    RDIM = '\033[22m'
    RITALICS = '\033[23m'
    RUNDERLINE = '\033[24m'
    RBLINK = '\033[25m'
    RINVERSE = '\033[27m'
    RINVISIBLE = '\033[28m'
    RSTRIKETHROUGH = '\033[29m'