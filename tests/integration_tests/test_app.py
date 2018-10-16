import sys
from src.app import main

def test_most_loyal(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["", "most_loyal", ""])
        assert sys.argv[1] == "most_loyal"

        response = main()
        assert response is not None

def test_total_spend(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["", "total_spend", "travis_kshlerin@wunsch.net"])
        assert sys.argv[1] == "total_spend"

        response = main()
        assert response is not None

def test_most_sold(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["", "most_sold", ""])
        assert sys.argv[1] == "most_sold"

        response = main()
        assert response is not None
