from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.ex_ola_mundo import html


def test_restorne_ola_mundo():
    client = TestClient(html)

    response = client.get('/olamundo')

    assert response.status_code == HTTPStatus.OK
