import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("COMMAND:", command)
    print("OUTPUT:", result.stdout)
    print("ERROR:", result.stderr)
    print("-" * 50)

# Step 1: Add files
run_command("git add .")

# Step 2: Commit
run_command('git commit -m "Automated commit"')

#step 3: push to the repository
run_command("git push")