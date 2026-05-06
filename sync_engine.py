import subprocess
import sys
import time

def execute_shell(command):
    """Executes a raw OS shell command and returns the process state."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def get_pending_algorithms():
    """Scans the local Git database for untracked or modified Python files."""
    status = execute_shell("git status --porcelain")
    if status.returncode != 0:
        print("[Fatal] Git repository not found or corrupted.")
        sys.exit(1)
    
    files = []
    for line in status.stdout.splitlines():
        if line:
            # Git porcelain format: status codes are in the first two characters
            filename = line[3:]
            if filename.endswith(".py") and "sync_engine" not in filename:
                files.append(filename)
    return files

def bulk_sync_pipeline():
    print(f"[{time.strftime('%H:%M:%S')}] Initiating V2 Synchronization Engine...")
    
    # Phase 1: State Reconciliation
    print("-> Reconciling local state with remote ledger...")
    pull_result = execute_shell("git pull origin main --rebase")
    if pull_result.returncode != 0:
        print(f"[Error] Reconciliation Failed. Manual intervention required.\n{pull_result.stderr}")
        sys.exit(1)

    # Phase 2: Hardware Scan
    targets = get_pending_algorithms()
    if not targets:
        print("-> State Neutral: No new algorithms detected.")
        return

    print(f"-> Detected {len(targets)} pending algorithm(s). Commencing atomic allocation.")

    # Phase 3: Atomic Commits
    for file in targets:
        # Strip extension and underscores for a clean ledger entry
        clean_name = file.replace(".py", "").replace("_", " ")
        commit_msg = f"Add {clean_name}"
        
        execute_shell(f'git add "{file}"')
        execute_shell(f'git commit -m "{commit_msg}"')
        print(f"   [Locked] {file}")

    # Phase 4: Batch Transport
    print("-> Establishing secure tunnel and broadcasting payload...")
    push_result = execute_shell("git push origin main")
    
    if push_result.returncode == 0:
        print(f"[{time.strftime('%H:%M:%S')}] Public Ledger synchronized successfully.")
    else:
        print(f"[Error] Transport Failed. Verify TUN mode routing and token scope.\n{push_result.stderr}")

if __name__ == "__main__":
    bulk_sync_pipeline()
