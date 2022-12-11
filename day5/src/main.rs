use std::collections::VecDeque;
use std::io::BufRead;
use std::io::BufReader;
use std::fs::File;

fn main() {
    println!("Hello, world!");
    let filename = String::from("real.txt");
    let num_stacks: i32 = find_how_many_stacks(&filename);
    let mut stacks_vec: Vec<VecDeque<char>> = Vec::new();
    for _ in 0..num_stacks {
        stacks_vec.push(VecDeque::new());
    }
    println!("Found {} stacks", num_stacks);

    let file = File::open(&filename).unwrap();
    let move_cmds: _ = BufReader::new(file).lines()
          .map(|l| l.unwrap())
          .filter(|line| line.starts_with("move"))
          .map(|l| l.split_whitespace().into_iter()
                    .map(|s| String::from(s))
                    .filter(|s| is_numeric(s))
                    .map(|s| s.parse::<i32>().unwrap())
                    .collect::<Vec<i32>>())
          .collect::<Vec<Vec<i32>>>();
    let file = File::open(&filename).unwrap();
    let stacks_lines = BufReader::new(file).lines()
            .map(|l| l.unwrap())
            .filter(|l| l.contains('['))
            .collect::<Vec<String>>();
    println!("{:#?}", move_cmds);
    println!("{:#?}", stacks_lines);
    // load init data
    stacks_lines.into_iter().rev().for_each(|s| {
        for i in 0..num_stacks {
            let offset: usize = ((i)*4+1).try_into().unwrap();
            let c = s.chars().nth(offset).unwrap();
            println!("Loadind: offset[{}] - char: [{}]", offset, c);
            if c.is_alphanumeric() {
                stacks_vec[i as usize].push_back(c);
            }
        }       
    });

    // for part 2
    let mut load_q: VecDeque<char> = VecDeque::new();

    move_cmds.iter().for_each(|cmd| {
        let times_to_pop   = cmd[0];
        let target_to_pop  = cmd[1]-1; // 0 idx
        let target_to_push = cmd[2]-1; // 0 idx
        for _ in 0..times_to_pop {
            let c = stacks_vec[target_to_pop as usize].pop_back().unwrap();
            load_q.push_back(c); // part 2
        }
        for _ in 0..times_to_pop {
            stacks_vec[target_to_push as usize].push_back(load_q.pop_back().unwrap());
        }
        
    });
    
    println!("{:#?}", stacks_vec);

    println!("The final answer is:");

    stacks_vec.into_iter().for_each(|mut v| print!("{}", v.pop_back().unwrap()));


    // find out how many stacks there are
    // - instantiate a stack (or create one)
    // - store stack refs in vec or map (cmd as offset in vec or key in map)
    // - populate data
    // process commands (move 1 from 2 to 1)
    // - 1 => number of times to pop stack
    // - 2 => the id of stack to pop
    // - 1 => the id of stack to write
    // iterate through container and pop & print each top char
}

fn is_numeric(word: &str) -> bool {
    for c in word.chars() {
        if !c.is_digit(10) {
            return false;
        }
    }
    return true;
}

fn find_how_many_stacks(filename: &String) -> i32 {
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut num = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        if line.contains('1') {
            // we are on the numbers line

            line.split_whitespace().for_each(|c| { 
                let val = c.parse().unwrap();
                if  val > num {
                    num = val;
                }
            });
            return num;
        }
    }
    -1
}