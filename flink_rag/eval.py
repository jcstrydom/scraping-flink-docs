from .naive_kg_rag import run_eval

if __name__ == "__main__":
    # Keep a simple executable module entrypoint dedicated to evaluation-only runs.
    # The default build command already runs this automatically after build.
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Run evaluation over stored naive and KG artifacts")
    parser.add_argument("--naive-graph", type=str, default="data/rag/naive_rag.json")
    parser.add_argument("--kg-graph", type=str, default="data/rag/kg_rag.json")
    parser.add_argument("--eval-questions", type=str, default="documentation/evals/flink_docs_rag_eval_questions.md")
    parser.add_argument("--output", type=str, default="data/rag/evals/latest.json")
    parser.add_argument("--top-nodes", type=int, default=6)
    parser.add_argument("--top-chunks", type=int, default=6)
    parser.add_argument("--hops", type=int, default=1)
    args = parser.parse_args()

    report = run_eval(
        naive_graph_path=args.naive_graph,
        kg_graph_path=args.kg_graph,
        eval_questions_path=args.eval_questions,
        output_path=args.output,
        top_nodes=args.top_nodes,
        top_chunks=args.top_chunks,
        hops=args.hops,
    )
    print(json.dumps({"output": args.output, "summary": report["summary"]}, indent=2))
