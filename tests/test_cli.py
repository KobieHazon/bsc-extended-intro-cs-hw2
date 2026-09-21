from extended_intro_hw2_cli import cli


def test_power_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw2", "power", "2", "10"])

    cli()

    assert capsys.readouterr().out == "1024\n"


def test_rotation_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw2", "is-rotation", "abc", "cab"])

    cli()

    assert capsys.readouterr().out == "True\n"
