import marimo

__generated_with = "0.10.7"
app = marimo.App(width="medium", layout_file="layouts/lab1.grid.json")


@app.cell
def _():
    import marimo as mo

    diagram = '''
    graph LR
        A[Square Rect] -- Link text --> B((Circle))
        A --> C(Round Rect)
        B --> D{Rhombus}
        C --> D
    '''
    mo.mermaid(diagram)
    return diagram, mo


if __name__ == "__main__":
    app.run()
