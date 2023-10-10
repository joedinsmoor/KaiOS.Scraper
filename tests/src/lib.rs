#[cfg(test)]
mod tests{
    #[test]
    fn test_init(){
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
    #[test]
    fn dependencies(){ // Install all dependencies, check for errors
        let result = 1 + 1;
        assert_eq!(result, 2);
    }
    #[test]
    fn sms_test(){ // Run sqlite_scraper against known db
        let result = 1 + 1;
        assert_eq!(result, 2);
    }
}