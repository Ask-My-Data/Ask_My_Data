import typer

from askmydata import __version__

app = typer.Typer(help="AskMyData: query your data in natural language.", no_args_is_help=True)


@app.callback()
def main() -> None:
    pass


@app.command()
def version() -> None:
    """Show the installed AskMyData version."""
    typer.echo(f"askmydata {__version__}")
