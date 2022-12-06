
use std::collections::HashSet;
use std::fs;

fn main() {
    let filename = "real.txt";
    let window_size = 14;
    let rx_buffer: String = get_data(&filename);
    println!("{:?}", rx_buffer);
    for i in 0..rx_buffer.len()-window_size+1 {
        let slice = &rx_buffer[i..window_size+i];
        println!("slice: {}", slice);
        let mut hash: HashSet<char> = HashSet::new();
        let is_not_signature: bool = slice.chars()
                               .map(|c| hash.insert(c))
                               .any(|r| !r);
        if !is_not_signature {
            println!("The answer is: {}", i+window_size);
            break;
        }
    };
}

fn get_data(filename: &str) -> String {
    fs::read_to_string(filename).unwrap()
}
