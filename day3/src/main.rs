
use core::iter::zip;
use itertools::Itertools;
use std::collections::HashMap;
use std::collections::HashSet;
use std::io::BufRead;
use std::io::BufReader;
use std::fs::File;
fn main() {
    // A-Z 65,90
    // a-z 97,122
    let mut priority_map: HashMap<char, i32> = HashMap::new();
    for (chr,i) in zip(97u8..=122, 1..=26) {
        priority_map.insert(chr as char, i);
    }
    for (chr,i) in zip(65u8..=90, 27..=52) { 
        priority_map.insert(chr as char, i);
    }    
    let file = File::open("real.txt").unwrap();
    let reader = BufReader::new(file);
    let mut sum = 0; 
    
    for mut line in reader.lines().chunks(3).into_iter() {
        let mut found: HashSet<char> = HashSet::new();
        let line1 = line.next().unwrap().unwrap();
        let line2 = line.next().unwrap().unwrap();
        let line3 = line.next().unwrap().unwrap();


        for c in line1.chars() {
            if line2.contains(c) && line3.contains(c) {
                found.insert(c);
            }
        }
        println!("--------");
        println!("{}", line1);
        println!("{}", line2);
        println!("{}", line3);
        found.iter().for_each(|c| print!("{} ", c));
        println!("");
        println!("--------");
        sum += found.iter().map(|c| priority_map.get(c).unwrap()).sum::<i32>();


    }
    // PART 1
    // ...
    // for line in reader.lines() {
    //     let mut found: HashSet<char> = HashSet::new();
    //     let line = line.unwrap();
    //     let size = line.len();
    //     let first_half=&line[0..size/2];
    //     let second_half=&line[size/2..size];
    //     for a in first_half.chars() {
    //         if second_half.contains(a) {
    //             found.insert(a);
    //         }
    //     }
    //     println!("----------------");
    //     println!("{}", line);
    //     println!("{}",first_half);
    //     println!("{}",second_half);
    //     found.iter().for_each(|c| print!("{} ", c));
    //     println!("");
    //     println!("----------------");
    //     sum += found.iter().map(|c| priority_map.get(c).unwrap()).sum::<i32>();
    // }
    println!("{}", sum);
}
