#!/usr/bin/env python3
"""Strip the document wrapper from index.html so it can be published as a
claude.ai Artifact (artifacts supply their own doctype/html/head/body)."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text()
head = src[: src.index("</head>")]
body = src[src.index("<body>") + len("<body>") : src.rindex("</body>")]
out = "<title>TT13 Hall of Records</title>\n" + head[head.index("<style>"):] + "\n" + body + "\n"
(root / "artifact.html").write_text(out)
print(f"wrote artifact.html ({len(out)/1024:.1f} KB)")
