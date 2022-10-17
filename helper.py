import argparse


def build_parser():
    """Create a parser to parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Find flight paths between two airlines")
    parser.add_argument('source', help="The source airport's IATA (3-letter) code.")
    parser.add_argument('dest', help="The destination airport's IATA (3-letter) code.")
    parser.add_argument('--max-segments', dest='max_segments', type=int, default=2,
                        help="The maximum number of segments in a valid path.")
    return parser
