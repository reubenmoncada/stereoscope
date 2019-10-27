#!/usr/bin/env python3

import stsc.parser as parser
from stsc.run import run
from stsc.look import look

def main():
    prs = parser.make_parser()
    args = prs.parse_args()

    if args.command == 'run':
        run(prs,args)
    elif args.command == 'look':
        look(args)
    else:
        print(' '.join(["Use the command 'steroscope run' to analyze",
                        "your data. Use 'steroescope look' to visualize",
                        "your results."]))


