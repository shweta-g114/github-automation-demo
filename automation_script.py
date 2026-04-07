import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("COMMAND:", command)
    if result.stdout:
        print("OUTPUT:", result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)
    print("command executed successfully")
    print("-" * 50)

# Step 1: Add files
run_command("git add .")

# Step 2: Commit
run_command('git commit -m "Automated commit4"')

#step 3: push to the repository
run_command("git push")