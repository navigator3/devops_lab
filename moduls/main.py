import psutil
import argparse
import time

print(time.strftime('%x-%X'))
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval between snapshots", type=int, default=3, dest="i")
parser.add_argument("-n", help="Counts snapshots, default=0 - no limits",
                    type=int, default=3, dest="n")
parser.add_argument("-t", help="Output file type: txt or json. default is txt",
                    default="txt", dest="t")
args = parser.parse_args()


class Checker:
    def __init__(self, cpu, memory, swap):
        self.cpu = cpu
        self.memory = memory
        self.swap = swap

    def txt_report(self):
        try:
            with open("report.txt", "a") as file:
                file.write("%s: %s - %s - %s \n" % (str(time.strftime('%x-%X')), str(self.cpu),
                                                    str(self.memory), str(self.swap)))
        except BaseException:
            print("something is wrong")

    def json_report(self):
        with open("report.json", "w") as file_json:
            file_json.write("""{
"snapshot": {
    "time": "%s",
    "cpu_usage": "%s",
    "memory_usage": "%s",
    "swap_usage": "%s"
            }
}
""" % (str(time.strftime('%x-%X')), str(self.cpu), str(self.memory), str(self.swap)))


def test():
    print("Go go go")


def main():

    if args.t == "txt":
        try:
            with open("report.txt", "w") as file:
                file.write("TIME----------CPU(%)---MEMORY(%)----SWAP(%)\n")
                file.close()
        except BaseException:
            print("something is wrong")
        x = args.n
        print("snapshoer is working...-i=%s, -t=%s, -n=%s" % (args.i, args.t, args.n))
        while x >= 1 or args.n == 0:
            start = Checker(psutil.cpu_percent(interval=args.i), psutil.virtual_memory().percent,
                            psutil.swap_memory().percent)
            start.txt_report()
            x -= 1
    elif args.t == "json":
        x = args.n
        print("snapshoer is working...-i=%s, -t=%s, -n=%s" % (args.i, args.t, args.n))
        while x >= 1 or args.n == 0:
            start = Checker(psutil.cpu_percent(interval=args.i),
                            psutil.virtual_memory().percent,
                            psutil.swap_memory().percent)
            start.json_report()
            x -= 1


if __name__ == "__main__":
    main()
