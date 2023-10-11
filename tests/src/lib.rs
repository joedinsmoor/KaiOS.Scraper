#[cfg(test)]
mod tests{
    use std;
    use std::process::Command; // Run programs
    //use std::error::Error;
    use std::env;
    use std::io::ErrorKind;
    use std::path::Path;

    #[test]
    fn test_init(){
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
    #[test]
    fn test_install_python_dependencies() {
        // Create a Command to run the 'pip' command to install from requirements.txt
        let current_dir = match env::current_dir() {
            Ok(dir) => dir,
            Err(e) => panic!("Failed to get the current working directory: {}", e),
        };

        // Navigate to the parent directory
        let parent_dir = current_dir.parent().unwrap_or_else(|| {
            panic!("Failed to get the parent directory. Ensure that 'requirements.txt' is not in the root directory.");
        });

        // Change the working directory to the parent directory
        if let Err(e) = env::set_current_dir(&parent_dir) {
            panic!("Failed to change working directory to the parent directory: {}", e);
        }

        let mut cmd = Command::new("pip");

        // Specify the command arguments to install from requirements.txt
        cmd.arg("install");
        cmd.arg("-r");
        cmd.arg("requirements.txt");

        // Execute the command and check for success
        let status = match cmd.status() {
            Ok(status) => status,
            Err(e) => {
                if e.kind() == ErrorKind::NotFound {
                    panic!("'pip' command not found. Make sure it's installed on your system.");
                } else {
                    panic!("Command failed to execute: {}", e);
                }
            }
        };

        // Check if the command exited successfully (exit status code 0)
        assert!(status.success(), "Command failed with exit code: {}", status.code().unwrap_or(-1));
    }
    #[test]
    fn sms_test(){ // Run sqlite_scraper against known db
        let smsfile = "phone_numbers.csv";
        let testfile = "226660312ssm.sqlite";
        lut mut cmd = Command::new("python3");
        cmd.arg("sqlite_scraper.py");
        assert(smsfile.exists());
    }
}