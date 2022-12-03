

use std::{fs::File};
use std::io::{prelude::*, BufReader};
fn main() -> std::io::Result<()> {
    let file = File::open("real.txt")?;
    let reader = BufReader::new(file);
    let mut current_max = 0;
    let mut current_sum = 0;
    let mut sums: Vec<i32> = Vec::new();
    for line in reader.lines() {
        let line = line?;
        if line == "" {
            sums.push(current_sum);
            if current_sum > current_max {
                current_max = current_sum;
            }
            current_sum = 0;
        } else {
            let num: i32 = line.parse().unwrap();
            current_sum += num;
        }
    }
    sums.sort();
    let top_three: i32 = sums[sums.len()-3..sums.len()].iter().sum();
    println!("The top three are: {}", top_three);
    Ok(())
}
