import typer
from rich.console import Console
from app.core.loader import load_all
from app.core.fields import get_field

app = typer.Typer(help="Linux Command Library (text mode)")
console = Console()
DB = None

@app.callback()
def main():
    global DB
    if DB is None:
        DB = load_all()

@app.command()
def field(command: str, field: str, json_out: bool = typer.Option(False, "--json", help="Return JSON")):
    """
    Return exactly one field for a command.
    field can be:
      name | category | description | syntax | examples | options | options<flag>
    Examples:
      lcl field grep category
      lcl field tar description
      lcl field echo syntax
      lcl field grep options
      lcl field grep "options-i"
    """
    val = get_field(DB, command, field)
    if val is None: 
        raise typer.Exit(code=1)
    if json_out:
        import json
        console.print_json(data={"command": command, "field": field, "value": val})
    else:
        console.print(val)

# Convenience shorthands that print ONLY the value
@app.command()
def category(command: str):
    val = get_field(DB, command, "category")
    if val is None: raise typer.Exit(code=1)
    console.print(val)

@app.command()
def describe(command: str):
    val = get_field(DB, command, "description")
    if val is None: raise typer.Exit(code=1)
    console.print(val)
    
@app.command()
def syntax(command: str):
    val = get_field(DB, command, "syntax")
    if val is None: raise typer.Exit(code=1)
    console.print(val)
    
@app.command()
def examples(command: str):
    val = get_field(DB, command, "examples")
    if val is None: raise typer.Exit(code=1)
    console.print(val)
    
@app.command()
def options(command: str):
    val = get_field(DB, command, "options")
    if val is None: raise typer.Exit(code=1)
    console.print(val)
    
@app.command()
def option(command: str, flag: str):
    val = get_field(DB, command, f"options-{flag}")
    if val is None: raise typer.Exit(code=1)
    console.print(val)