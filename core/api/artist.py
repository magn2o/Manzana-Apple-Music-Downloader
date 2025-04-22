from rich import box
from rich.table import Table
from rich.console import Console
from rich.columns import Columns

from utils import logger

console = Console()

def __user(contents: list):
    ids = []
    table = Table(box=box.ROUNDED)

    table.add_column("ID", justify="center")
    table.add_column("Name", justify="left")
    table.add_column("ContentID", justify="left")

    for i, content in enumerate(contents):
        ids.append(i)
        table.add_row(
            str(i),
            content.get("name"),
            content.get("contentId")
        )
    
    print()
    columns = Columns(["       ", table])
    console.print(columns)
    id = input("\n\t Enter ID: ")
    print()
    
    if id == "": logger.error("Please enter an ID to continue!", 1)
    elif id == "all": return [url.get("url") for url in contents]
    else:
        try: id = [int(i.strip()) for i in id.split(',')]
        except: logger.error("Input is invalid!", 1)
        id = list(set(id))

        returnContent = []

        for i in id:
            if i in ids: returnContent.append(contents[i]["url"])
            else: logger.warning(f'ID: {i} not in the list!')

        return returnContent

def get_urls(a, s, m, name):
    table = Table(
        box=box.ROUNDED
    )

    table.add_column("ID", justify="center")
    table.add_column("Kind", justify="center")
    table.add_column("Count", justify="center")

    groups = [(idx, kind, data) for idx, (kind, data) in enumerate([
        ('albums', a),
        ('singles', s),
        ('music-videos', m)
    ]) if len(data) > 0]

    for idx, (kind, data) in enumerate([(group[1], group[2]) for group in groups]):
        table.add_row(str(idx), kind, str(len(data)))

    print()
    columns = Columns(["       ", table])
    console.print(columns)
    id = input("\n\t Enter ID: ")
    print()

    if id == "": logger.error("Please enter an ID to continue!", 1)
    elif id == "all": id = [i for i in range(len(groups))]
    else:
        try: id = [int(id.strip()) for id in id.split(',')]
        except: logger.error("Input is invalid!", 1)
        id = list(set(id))

    contents = []

    for i in id:
        if i in range(len(groups)):
            kind, data = groups[i][1], groups[i][2]
            if kind == 'albums':
                logger.info(f"Getting {name}'s full-albums...")
                contents += __user(data)
            elif kind == 'singles':
                logger.info(f"Getting {name}'s singles...")
                contents += __user(data)
            elif kind == 'music-videos':
                logger.info(f"Getting {name}'s music-videos...")
                contents += __user(data)
        else:
            logger.warning(f'ID: {i} not in the list!')

    return contents
