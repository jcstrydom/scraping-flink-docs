import argparse
import ast
import dotenv
import logging

from models.processdata import ResponseProcessor
dotenv.load_dotenv(dotenv.find_dotenv("firecrawl-flink_docs/.env"))

proc = ResponseProcessor(
    root_url="https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/",
    log_level=logging.INFO
)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run ollama prompt test loop with configurable iterations and progress interval")
    parser.add_argument('--iterations', '-n', type=int, default=100, help='Number of iterations to run the loop (default: 100)')
    parser.add_argument('--progress-interval', '-p', type=int, default=10, help='How often to print progress (default: 10)')
    return parser.parse_args()

def retrieve_persisted_response():
    # Simulate retrieval of persisted response
    with open('./data/flink_firecrawl_markdown.md', 'r') as f:
        lines = f.readlines()

    md_content = '\n'.join(lines)

    with open('./data/flink_firecrawl_response_full.txt', 'r', encoding='utf-8') as f:
        full_content = f.read()

    file_response = ast.literal_eval(full_content)
    return file_response, md_content



def main(iterations=100, progress_interval=10):

    iterations = max(1, args.iterations)
    progress_interval = max(1, args.progress_interval)

    file_response, md_content = retrieve_persisted_response()

    fail_counter = 0
    for i in range(iterations):
        if i % progress_interval == 0:
            print(f"Iteration {i} ...  (fail_count={fail_counter:>3})")
        processed = proc.process_response(file_response, ask_ollama=True)
        test_dict = processed.to_dict()
        if len(test_dict.get('headings')) == 0:
            fail_counter += 1
    print(f"Failed {fail_counter} out of {iterations} attempts to extract headings.")



if __name__=="__main__":
    args = parse_arguments()
    main(**args)