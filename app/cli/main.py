import typer
from rich.console import Console
from rich.table import Table
from app.core.loader import load_all, list_categories

app = typer.Typer(help="Linux Command Library (text mode)")
console = Console()
DB = None

@app.callback()
def main():
    global DB
    if DB is None:
        DB = load_all()

@app.command()
def categories():
    """List available categories."""
    cats +list_categories(DB)
    console.print("\n".join(cats))
    
@app.command()
def list(category: str = typer.Option(None, "--category", "-c", help="Filter by category")):
    """List commands, (optionally filter by category)."""
    t = Table(title=f"Commands" + (f" - {category}" if category else ""))
    t.add_column("Name"); t.add_column("Category"); t.add_column("Description")
    for name, meta in sorted(DB.items()):
        cat = meta.get("category","")
        if category and cat != category:
            continue
        t.add_row(name, cat, meta.get("description",""))
    console.print(t)
    