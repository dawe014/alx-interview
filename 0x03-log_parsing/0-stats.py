#!/usr/bin/python3
import sys
import re

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count_lines = 0

    log_pattern = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3} - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                count_lines += 1

                if count_lines % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")

if __name__ == "__main__":
    main()