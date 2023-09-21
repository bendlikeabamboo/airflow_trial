import click

ERROR = "Error: No name provided"


def get_last_name(name: str):
    """Simple program that extracts the last name from a full name"""
    return name.split(",")[0] if name is not None else ERROR


def get_first_name(name: str):
    """Simple program that extracts the first name from a full name"""
    return (
        "".join([x for x in name.split(" ")[1] if "." not in x])
        if name is not None
        else ERROR
    )


def get_middle_initial(name: str):
    """Simple program that extracts the middle initial from a full name"""
    return (
        "".join([x for x in name.split(" ")[1] if "." in x])
        if name is not None
        else ERROR
    )


@click.command()
@click.option("--fn", default=False, is_flag=True, help="Get full name")
@click.option("--ln", default=False, is_flag=True, help="Get last name")
@click.option("--mi", default=False, is_flag=True, help="Get middle initial")
@click.option("--name", default=None, help="Full name")
def run(name, fn, ln, mi):
    "Run the names program"
    print("Program for extracting First Name, Last Name, and Middle Initial\n\n")
    if name is None:
        name = input("Enter your full name in [Last Name, First Name M.I.] format: ")

    res = {}
    if fn:
        res["fn"] = get_first_name(name).strip()
    if ln:
        res["ln"] = get_last_name(name).strip()
    if mi:
        res["mi"] = get_middle_initial(name)

    click.echo(str(res))
    return res
