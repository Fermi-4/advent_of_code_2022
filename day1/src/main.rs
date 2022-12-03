

use std::{fs::File};
use std::io::{prelude::*, BufReader};
fn main() -> std::io::Result<()> {
    let file = File::open("real.txt")?;
    let reader = BufReader::new(file);
    let mut current_max = 0;
    let mut current_sum = 0;
    for line in reader.lines() {
        let line = line?;
        if line == "" {
            if current_sum > current_max {
                current_max = current_sum;
            }
            current_sum = 0;
        } else {
            let num: i32 = line.parse().unwrap();
            current_sum += num;
        }
    }
    println!("The max is: {}", current_max);
    Ok(())
}
