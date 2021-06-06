from pathlib import Path
import json
from argparse_prompt import PromptParser
from typing import IO

from pathlib import Path
import json
from argparse import ArgumentParser
from typing import IO

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
    def __init__(self, data):
        self.data = data
        self.id = self.data["id"].replace("-", "_")
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
        self.cells = list(map(NotebookCell, self.data["cells"]))
    
    def render(self, out_file_path: Path, asset_folder: Path):
        out_file_path = Path(out_file_path)
        asset_folder = Path(asset_folder)
        out_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_file_path, "w+") as f:
            f.write("---\n")
            for key, value in self.metadata.items():
              f.write(f"{key}: {value}\n")
            f.write("---\n")
            f.write(HEADER)
            for cell in self.cells:
                cell.render(f, asset_folder)

if __name__ == "__main__":
    parser = PromptParser(description="A utility for converting Jupyter Notebooks into UBI Center posts.")
    parser.add_argument("notebook", help="The notebook file to convert.")
    parser.add_argument("--layout", default="post", help="The layout style")
    parser.add_argument("--current", default="post")
    parser.add_argument("--cover", default="", help="The cover image path")
    parser.add_argument("--navigation", default=True)
    parser.add_argument("--title", default="Title goes here", help="The title")
    parser.add_argument("--date", default="2012-09-01", help="The publishing date")
    parser.add_argument("--tags", default="[]", help="The tags")
    parser.add_argument("--class_", default="post-template")
    parser.add_argument("--subclass", default="'post'")
    parser.add_argument("--author", default="max", help="The author name")
    parser.add_argument("--excerpt", default="Excerpt goes here", help="The excerpt to show on the website")
    parser.add_argument("--output-file", default="_posts/2021-05-04-post.md")
    parser.add_argument("--asset-folder", default="assets/markdown_assets/post")
    args = parser.parse_args()

    metadata = dict(
        layout=args.layout,
        current=args.current,
        cover=args.cover,
        navigation=args.navigation,
        title=args.title,
        date=args.date,
        tags=args.tags,
        subclass=args.subclass,
        author=args.author,
        excerpt=args.excerpt
    )
    metadata["class"] = args.class_

    notebook = NotebookPost(args.notebook, metadata)
    notebook.render(args.output_file, args.asset_folder)