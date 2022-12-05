use std::io::BufRead;
use std::io::BufReader;
use std::fs::File;
fn main() {
    let file = File::open("real.txt").unwrap();
    let reader = BufReader::new(file);
    let mut overlaps = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        if is_any_overlap(&line) {
            println!("{}", line);
            overlaps +=1;
        }
    }
    println!("{}", overlaps);
}

// part 2
fn is_any_overlap(line: &String) -> bool {
    // 1:(a,b); 2:(c,d)
    // assume ordering b>a and d>c
    // 1 overlaps 2 if: (a <= d && a >= c) && (b >= c && b <= d)
    //        1 **a-b****
    //          ***c-d***
    //        2 ***a-b*** 
    //          ***c-d***
    //        3 ****a-b**
    //          ***c-d***
    // 2 overlaps 1 if: c < a && d > b
    // else no overlap
    let split_elf: Vec<&str> = line.split(",").collect();
    let elf1_nums: Vec<&str> = split_elf[0].split('-').collect();
    let elf2_nums: Vec<&str> = split_elf[1].split('-').collect();
    let a: i32 = elf1_nums[0].parse().unwrap();
    let b: i32 = elf1_nums[1].parse().unwrap();
    let c: i32 = elf2_nums[0].parse().unwrap();
    let d: i32 = elf2_nums[1].parse().unwrap();
    println!("{} {} - {} {}", a,b,c,d);
    is_overlap(&line) || ((a <= d && a >= c) || (b >= c && b <= d))
}


fn is_overlap(line: &String) -> bool {
    // 1:(a,b); 2:(c,d)
    // 1 overlaps 2 if: a < c && b > d
    // 2 overlaps 1 if: c < a && d > b
    // else no overlap
    let split_elf: Vec<&str> = line.split(",").collect();
    let elf1_nums: Vec<&str> = split_elf[0].split('-').collect();
    let elf2_nums: Vec<&str> = split_elf[1].split('-').collect();
    let a: i32 = elf1_nums[0].parse().unwrap();
    let b: i32 = elf1_nums[1].parse().unwrap();
    let c: i32 = elf2_nums[0].parse().unwrap();
    let d: i32 = elf2_nums[1].parse().unwrap();
    println!("{} {} - {} {}", a,b,c,d);
    ((a <= c) && (b >= d)) || ((c <= a) && (d >= b))
}
