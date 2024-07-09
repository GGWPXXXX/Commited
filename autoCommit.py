import os
import threading

def commit(start, end, ip, lock):
    for i in range(start, end):
        with lock:
            os.system(f'git commit --allow-empty -m "Commit {i+1} of {ip}"')

def main():
    ip = int(input("How many times do you want to commit? \n"))
    autoPush = input("Auto git push when committed? (y/n) \n")

    lock = threading.Lock()
    threads = []
    num_threads = 3
    commits_per_thread = ip // num_threads
    extra_commits = ip % num_threads

    start = 0
    for i in range(num_threads):
        end = start + commits_per_thread + (1 if i < extra_commits else 0)
        t = threading.Thread(target=commit, args=(start, end, ip, lock))
        threads.append(t)
        t.start()
        start = end

    for t in threads:
        t.join()

    print(f"Committed {ip} times")

    if autoPush == "y":
        os.system('git push')

if __name__ == "__main__":
    main()
import os
from time import sleep

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
	
# git commit --allow-empty -m "New Commit at: $(date)"

#  MADE BY:_            _   _____                        _ 
#  \ \    / (_)        (_) |  __ \                      (_)
#   \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _ 
#    \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
#     \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
#      \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
#                     _/ |                                 
#                    |__/                                  
