import typer

from askmydata import __version__

app = typer.Typer(
    help="AskMyData : interrogez vos données en langage naturel.", no_args_is_help=True
)


@app.callback()
def main() -> None:
    pass


@app.command()
def version() -> None:
    """Affiche la version installée d'AskMyData."""
    typer.echo(f"askmydata {__version__}")
