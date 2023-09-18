import os
import tempfile
import typing


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_SRC = os.path.join(PROJECT_DIR, "README.md")
INDEX_DST = os.path.join(PROJECT_DIR, "docs", "pages", "index.mdx")
EXAMPLE_SRC = os.path.join(PROJECT_DIR, "example.py")
EXAMPLE_DST = os.path.join(PROJECT_DIR, "docs", "pages", "examples.mdx")
API_DST = os.path.join(PROJECT_DIR, "docs", "pages", "api-reference.mdx")


# copy index file to docs folder

with open(INDEX_SRC, "r") as f:
    index_file_content = f.read()

with open(INDEX_DST, "w") as f:
    f.write(index_file_content)


# convert example code to markdown


with open(EXAMPLE_SRC, "r") as f:
    example_file_content = f.read().strip(" \n\t").replace("# fmt: off\n", "")

example_file_blocks = example_file_content.split("\n\n\n")
markdown_blocks: typing.List[str] = ["# Example Usage"]

for block in example_file_blocks:
    is_comment_block = all([l.startswith("#") for l in block.split("\n")])
    if is_comment_block:
        markdown_blocks.append(
            "\n".join([l[1:].lstrip(" ") for l in block.split("\n")])
        )
    else:
        markdown_blocks.append(f"```python\n{block}\n```")

with open(EXAMPLE_DST, "w") as f:
    f.write("\n\n".join(markdown_blocks))


# generate automatic API reference and prettify output

# os.system call into temp file

with tempfile.NamedTemporaryFile() as f:

    def fetch(module: str) -> str:
        os.system(f"cd {PROJECT_DIR} && pydoc-markdown --module={module} > {f.name}")
        with open(f.name, "r") as f2:
            return "\n".join(
                filter(
                    lambda line: not line.startswith('<a id="'),
                    f2.read().split("\n"),
                )
            )

    raw_api_reference_content_init = fetch("tenta").replace(
        "# tenta", "# Module `tenta`"
    )
    raw_api_reference_content_types = (
        fetch("tenta.types")
        .replace("\n## ", "\n### ")
        .replace("\n# ", "\n## ")
        .replace("## tenta.types", "## Module `tenta.types`")
    )
    raw_api_reference_content_client = (
        fetch("tenta.client")
        .replace("\n## ", "\n### ")
        .replace("\n# ", "\n## ")
        .replace("## tenta.client", "## Module `tenta.client`")
    )


with open(API_DST, "w") as f:
    f.write(
        "# API Reference\n"
        + "\n".join(raw_api_reference_content_init.split("\n")[4:])
        + raw_api_reference_content_types
        + raw_api_reference_content_client,
    )
