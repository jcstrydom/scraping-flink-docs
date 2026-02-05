import os
import json
from pathlib import Path
from firecrawl_flink_docs.models.processdata import ResponseProcessor

# Directory containing markdown files
data_dir = Path(__file__).parent.parent / "data/markdown_files"
md_files = sorted(data_dir.glob("*.md"))[:5]

processor = ResponseProcessor()
output_path = Path(__file__).parent / "ollama_headings_test_output.json"
all_results = []

for i, md_path in enumerate(md_files, 1):
    with open(md_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    result = processor.extract_summaries_with_ollama(markdown)
    all_results.append({
        "file": md_path.name,
        "ollama_response": result
    })
    print(f"Processed {md_path.name}")

# Write all results to a file for inspection
with open(output_path, "w", encoding="utf-8") as out_f:
    json.dump(all_results, out_f, indent=2, ensure_ascii=False)

print(f"\nOllama responses written to {output_path}")
