try:
    import requests, json, re, time, os, urllib.parse, random, uuid, datetime, sys, base64, http.client, certifi, ssl
    from urllib.error import HTTPError, URLError
    import shutup; shutup.please()
    from concurrent.futures import ThreadPoolExecutor
    from platform import platform
    from urllib.request import Request, urlopen
    from rich import print as printf
    from rich.console import Console
    from rich.progress import Progress
    from rich.panel import Panel
except (ModuleNotFoundError) as error:
    import urllib.parse, sys, os
    os.system(f'xdg-open https://wa.me/6283847921480?text=X-HACK%20%3A%20{urllib.parse.quote(str(error))}')
    print(f"Error: {error}")
    sys.exit(1)

Console(width=65, style="bold slate_blue1").print(
    Panel(
        r"""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold blue]             `7MMF'  `7MMF'               `7MM
               MM      MM                   MM             
 `7M'   `MF'   MM      MM   ,6"Yb.  ,p6"bo  MM  ,MP',pP"Ybd
   `VA ,V'     MMmmmmmmMM  8)   MM 6M'  OO  MM ;Y   8I   `"
     XMX mmmmm MM      MM   ,pm9MM 8M       MM;Mm   `YMMMa.
   ,V' VA.     MM      MM  8M   MM YM.    , MM `Mb. L.   I8
 .AM.   .MA. .JMML.  .JMML.`Moo9^Yo.YMbmd'.JMML. YA.M9mmmP'
[bold white]  || Developer:[bold red] Rozhak[bold white] || Version:[bold green] 1.0.0[bold white] || Type:[bold yellow] Public[bold white] ||[/]""",
    )
)
Console(width=65, style="bold slate_blue1").print(
    Panel(
        "[bold white]Saat ini, X-Hacks masih dalam tahap pengembangan aktif untuk memastikan kualitas terbaik.\n\n"
        f"Rencana peluncuran: [bold cyan]1 January 2025[/bold cyan]\n\n"
        "Terima kasih atas kesabaran dan dukungan Anda. Ikuti terus informasi terbaru terkait rilis ini "
        "untuk menjadi yang pertama mencoba fitur-fitur inovatif kami.",
        title=">> [Warning] <<"
    )
)