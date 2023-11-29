# This is a sample Python script.
from datetime import datetime
from dateutil.relativedelta import relativedelta
import argparse
import sys

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

delta = relativedelta(days=1)


def process(p_command, p_business_unit, p_date_from, p_date_to, p_step, p_wait_time):

    start_date = datetime.strptime(p_date_from, "%d/%m/%Y")
    end_date = datetime.strptime(p_date_to, "%d/%m/%Y")

    # start - 1 day
    i_date = start_date - delta
    # end + 1 day
    e_date = end_date + delta

    step = relativedelta(days=int(p_step))

    while i_date < e_date:
        si_date = i_date
        i_date = i_date + step
        print(
            f'{p_command} -var /bu: {p_business_unit} -var /from: {si_date.strftime("%d/%m/%Y")} -var /to: {i_date.strftime("%d/%m/%Y")}')
        if p_wait_time:
            print(f'sleep {p_wait_time}m')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--command", help="The prefix command to launch")
    parser.add_argument("-f", "--fromdate", help="From date dd/mm/yyyy format")
    parser.add_argument("-t", "--todate", help="To date dd/mm/yyyy format")
    parser.add_argument("-b", "--bu", help="Business unit")
    parser.add_argument("-s", "--step", help="Step in days")
    parser.add_argument("-w", "--wait", help="Wait in minutes between each command")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    wait_time = 0
    if args.wait:
        wait_time = int(args.wait)

    step = 20
    if args.wait:
        step = int(args.wait)


    process(args.command, args.bu, args.fromdate, args.todate, step, wait_time)


