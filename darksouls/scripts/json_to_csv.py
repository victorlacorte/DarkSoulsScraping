import csv
import json

def main():
    with open('out.json', 'r') as fin:
        jdata = json.load(fin)
        with open('out.csv', 'w') as fout:
            writer = csv.writer(
                    fout,
                    dialect='unix')
            missing_header = True
            for d in jdata:
                if d:
                    if missing_header:
                        writer.writerow(d.keys())
                        missing_header = False
                    writer.writerow(d.values())

if __name__ == '__main__':
    main()
