use std::process::{Command, Stdio};

use execute::Execute;



fn main() {
    const TEST_PATH: &str = "~/sqlite_scraper";
    let mut command = Command::new(TEST_PATH);


    println!("Installing dependencies: ");
    command.arg("pip3");
    command.arg("install");
    command.arg("requirements.txt");
    command.stdout(Stdio::piped());
    command.stderr(Stdio::piped());

   // let output = command.execute_output().unwrap();


    println!("Executing tests: ");
    command.arg("python3");
    command.arg("sqlite_scraper.py");

   // let output = command.execute_output().unwrap();

    if let Some(exit_code) = command.execute().unwrap(){
        if exit_code == 0{
            println!("Tests Passed OK!");
        }
        else{
            eprintln!("Tests Failed!");
        }
    }
    else{
        eprintln!("Interrupted!");
    }

   // println!("{}", String::from_utf8(output.stdout).unwrap());
   // println!("{}", String::from_utf8(output.stderr).unwrap());

}
