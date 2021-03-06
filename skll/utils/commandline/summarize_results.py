#!/usr/bin/env python
# License: BSD 3 clause
"""
Little helper script to create a summary file out of a list of JSON results
files.

:author: Dan Blanchard (dblanchard@ets.org)
:organization: ETS
"""

import argparse
import logging

from skll.experiments.output import _write_summary_file
from skll.version import __version__


def main(argv=None):
    """
    Handles command line arguments and gets things started.

    Parameters
    ----------
    argv : list of str
        List of arguments, as if specified on the command-line.
        If None, ``sys.argv[1:]`` is used instead.
    """

    # Get command line arguments
    parser = argparse.ArgumentParser(
        description="Creates an experiment summary TSV file from a list of JSON\
                     files generated by run_experiment.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        conflict_handler='resolve')
    parser.add_argument('summary_file',
                        help='TSV file to store summary of results.')
    parser.add_argument('json_file',
                        help='JSON results file generated by run_experiment.',
                        nargs='+')
    parser.add_argument('-a', '--ablation', action='store_true', default=False,
                        help='The results files are from an ablation run.')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {0}'.format(__version__))
    args = parser.parse_args(argv)

    # Make warnings from built-in warnings module get formatted more nicely
    logging.captureWarnings(True)
    logging.basicConfig(format=('%(asctime)s - %(name)s - %(levelname)s - ' +
                                '%(message)s'))

    with open(args.summary_file, 'w') as output_file:
        _write_summary_file(args.json_file, output_file,
                            ablation=int(args.ablation))


if __name__ == '__main__':
    main()
