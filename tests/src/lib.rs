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
    fn ksdependencies() {
        // Create a Command to run the 'pip' command to install from requirements.txt
        println!("Testing dependency installation, if this fails, its because it needs super user privileges on windows. Can't do much about that :)");
        let current_dir = match env::current_dir() {
            Ok(dir) => dir,
            Err(e) => panic!("Failed to get the current working directory: {}", e),
        };

        // Navigate to the parent directory
        let parent_dir = current_dir.parent().unwrap_or_else(|| {
            panic!("Failed to get the parent directory. Ensure that 'requirements.txt' is in the root directory.");
        });

        // Change the working directory to the parent directory
        if let Err(e) = env::set_current_dir(&parent_dir) {
            panic!("Failed to change working directory to the parent directory: {}", e);
        }

        let mut cmd = Command::new("pip3");

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
    #[ignore]
    fn sms_test(){ // Run sqlite_scraper against known db
        println!("testing different KS functions individually against test data found in /testData/");
        let smsfile = "phone_numbers.csv";
        //let testfile = "./testData/226660312ssm.sqlite";
        let mut cmd = Command::new("python3");
        cmd.arg("sqlite_scraper.py");
        assert!(Path::new(smsfile).exists(), "Functions did not pass testing, try again.");
    }
}