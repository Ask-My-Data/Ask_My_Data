from typer.testing import CliRunner

from askmydata import __version__
from askmydata.cli.main import app

runner = CliRunner()


def test_version_prints_installed_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.output.strip() == f"askmydata {__version__}"
