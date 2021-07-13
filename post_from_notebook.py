from pathlib import Path
import json
from argparse import ArgumentParser
from typing import IO
import yaml

HEADER = """
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://requirejs.org/docs/release/2.3.5/minified/require.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
"""

SCRIPT_TEMPLATE = """
<div>
  <script>
    $(document).ready(function(){
      $("#graph_{id}").load("{{site.baseurl}}{asset_filename}");
    });
  </script>
</div>
<div id = "graph_{id}"></div>
"""

CODE_BLOCK = """
<button onclick="show_code_{id}()">Click to show code</button>
<div id="code_block_{id}" style="display: none;">
  <pre>
    <code>
{code}
    </code>
  </pre>
</div>

<script>
function show_code_{id}() {
  var x = document.getElementById("code_block_{id}");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>
"""

class NotebookCell:
    def __init__(self, id, data):
        self.data = data
        self.id = str(id)
        self.cell_type = self.data["cell_type"]
    
    def render(self, out_file: IO, asset_folder: Path):
        out_file.write("\n")
        if self.cell_type == "markdown":
            # write markdown to file
            for line in self.data["source"]:
                out_file.write(line)
        elif self.cell_type == "code":
            # write code block with show-code button
            formatted_code_block = CODE_BLOCK.replace("{id}", self.id).replace("{code}", "".join(self.data["source"]))
            for line in formatted_code_block:
                out_file.write(line)
            # write outputs
            for i, output_holder in enumerate(self.data["outputs"]):
              output = output_holder["data"]["text/html"]
              html = "".join(output)
              graph_id = f"graph_{self.id}_{i + 1}"
              asset_filename = asset_folder / f"{graph_id}.html"
              asset_filename.parent.mkdir(parents=True, exist_ok=True)
              out_file.write(SCRIPT_TEMPLATE.replace("{asset_filename}", str(asset_filename)).replace("{id}", graph_id))
              with open(asset_filename, "w+") as f:
                  f.write(html)

class NotebookPost:
    def __init__(self, path: Path, metadata: dict):
        self.metadata = metadata
        with open(path) as f:
            self.data = json.load(f)
        self.cells = list(map(lambda x: NotebookCell(x[0], x[1]), enumerate(self.data["cells"])))
    
    def render(self, out_file_path: Path, asset_folder: Path):
        out_file_path = Path(out_file_path)
        asset_folder = Path(asset_folder)
        out_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_file_path, "w+") as f:
            f.write("---\n")
            for line in self.metadata:
              f.write(line)
            f.write("\n---\n")
            f.write(HEADER)
            for cell in self.cells:
                cell.render(f, asset_folder)

if __name__ == "__main__":
    parser = ArgumentParser(description="A utility for converting Jupyter Notebooks into UBI Center posts.")
    parser.add_argument("notebook", help="The notebook file to convert.")
    parser.add_argument("metadata", help="A YAML file containing the post metadata")
    parser.add_argument("--output-md", help="The markdown file to write", default="post.md")
    parser.add_argument("--output-folder", help="The folder to write html resources to", default="resources/")
    args = parser.parse_args()

    with open(args.metadata) as f:
      metadata = f.readlines()

    notebook = NotebookPost(args.notebook, metadata)
    notebook.render(args.output_md, args.output_folder)