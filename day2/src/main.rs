use std::io::BufRead;
use std::io::BufReader;
use std::collections::HashMap;
use std::fs::File;

fn main() {
    
    /*

    A - ROCK
    B - PAPER
    C - SCISSORS

    X - ROCK
    Y - PAPER
    Z - SCISSORS

    ROCK     - 1
    PAPER    - 2
    SCISSORS - 3

    WIN  = 6
    DRAW = 3
    LOSE = 0


    PART 2:
    X - LOSE
    Y - DRAW
    Z - WIN
    */
    let mut lookup: HashMap<(char, char), i32> = HashMap::new();
                /*  Op   U   Score */
    // For part 2 just reorder mappings to correspond with win/lose/draw
    lookup.insert(('A', 'X'), 3);
    lookup.insert(('A', 'Y'), 4);
    lookup.insert(('A', 'Z'), 8);
    
    lookup.insert(('B', 'X'), 1);
    lookup.insert(('B', 'Y'), 5);
    lookup.insert(('B', 'Z'), 9);
    
    lookup.insert(('C', 'X'), 2);
    lookup.insert(('C', 'Y'), 6);
    lookup.insert(('C', 'Z'), 7);

    let file = File::open("real.txt").unwrap();
    let reader = BufReader::new(file);
    let mut sum = 0;
    for line in reader.lines() {
        match line {
            Ok(result) => {
                let split: Vec<char>= result.chars().collect();
                let score = (split[0], split[2]);
                let result = lookup.get(&score).unwrap();
                println!("Result is: {:?} {}", score, result);
                sum += result;
            },
            _ => println!("Oh no!")
        };
    }
    println!("The end result is: {}", sum);
}
