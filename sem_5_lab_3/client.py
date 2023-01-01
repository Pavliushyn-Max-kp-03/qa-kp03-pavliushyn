from typing import Optional
import requests
import typer
cli = typer.Typer()
api_url = 'http://127.0.0.1:5000'

@cli.command()
def main(name: str):
    print(f"Hello {name}")

@cli.command()
def get(type: str, file_id: int):
    r = requests.get(url=f'{api_url}/{type}/{file_id}')
    return print(r.text)
@cli.command()
def delete(type: str, file_id: int):
    r = requests.delete(url=f'{api_url}/{type}/{file_id}')
    return print(r.text)
@cli.command()
def create(type: str, arr_name: str, content: Optional[str] = typer.Argument(None)):
    r = requests.post(url=f'{api_url}/{type}/{arr_name}',
                      headers={'content-type': 'application/json'},
                      data=content)
    return print(r.text)
@cli.command()
def getall(command: str):
    r = requests.get(url=f'{api_url}/{command}')
    return print(r.text)

@cli.command()
def change(type: str, file_id: int, content: Optional[str] = typer.Argument(None)):
    r = requests.put(url=f'{api_url}/{type}/{file_id}',
                      headers={'content-type': 'application/json'},
                      data=content)
    return print(r.text)

if __name__ == "__main__":
    cli()
