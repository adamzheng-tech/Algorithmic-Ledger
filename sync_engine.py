import subprocess
import datetime
import sys

def execute_pipeline(command):
    """Executes a shell command and strictly monitors for hardware failures."""
    # shell=True is required on Windows to resolve the 'git' executable path
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Execution Failed. Hardware/Auth Error:\n{result.stderr.strip()}")
        sys.exit(1)
    
    return result.stdout.strip()

def run_sync():
    """Compiles the memory state and pushes to the public ledger."""
    # Generate deterministic timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Algorithm Sync | Compilation Checkpoint: {timestamp}"

    print("Initiating Ledger Synchronization...")

    # Step 1: Stage all new or modified algorithm files
    execute_pipeline("git add .")
    
    # Step 2: Commit the state with the timestamped payload
    # Note: We use a try-except bypass here because git throws an error if there are zero changes to commit.
    commit_result = subprocess.run(f'git commit -m "{commit_msg}"', shell=True, capture_output=True, text=True)
    if "nothing to commit" in commit_result.stdout:
        print("State Neutral: No new algorithms detected. Thread terminated.")
        sys.exit(0)

    # Step 3: Push payload to the cloud
    execute_pipeline("git push origin main")

    print(f"Sync Complete. Public Ledger Updated at: {timestamp}")

if __name__ == "__main__":
    run_sync()