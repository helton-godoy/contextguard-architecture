import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    activate_script = os.path.join(script_dir, "contextguard-activate.sh")
    
    # Check if shell script exists and is executable
    if not os.path.exists(activate_script):
        print(f"Error: Activation script not found at {activate_script}")
        sys.exit(1)
        
    # Execute the shell script
    try:
        subprocess.run([activate_script] + sys.argv[1:], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing activation script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
