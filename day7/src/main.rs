use std::rc::Rc;
use core::cell::RefCell;
use regex::Regex;
use regex::RegexSet;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

trait Entry {
    fn get_name(&self) -> &str;
    fn get_size(&self) -> u32;
}

struct MyDir {
    name: String,
    files: Vec<MyFile>,
    directories: Vec<Rc<RefCell<MyDir>>>,
    parent: Option<Rc<RefCell<MyDir>>>,
}

impl MyDir {
    fn new(name: String, parent: Option<Rc<RefCell<MyDir>>>) -> Self {
        MyDir {
            name,
            directories: Vec::new(),
            files: Vec::new(),
            parent,
        }
    }

    fn add_file_entry(&mut self, name: &str, size: u32) {
        self.files.push(MyFile::new(name.to_string(), size));
    }

    fn add_dir_entry(&mut self, name: String) {
        let dir = MyDir::new(name, None);
        dir.parent = Some(Rc::new(RefCell::new(self)));
        self.directories.push(dir);
    }

    fn get_parent(&self) -> Option<Rc<RefCell<MyDir>>> {
        match &self.parent {
            Some(p) => Some(Rc::clone(&p)),
            None => None,
        }
    }

    fn get_file(&self, name: String) -> Option<MyFile> {
        for file in self.files {
            if file.get_name() == name {
                return Some(file);
            }
        }
        return None;
    }

     fn get_dir(&self, name: String) -> Option<Rc<RefCell<MyDir>>> {
        for dir in self.directories {
            if dir.borrow().get_name() == name {
                return Some(Rc::clone(&dir));
            }
        }
        return None;
    }
}

impl Entry for MyDir {
    fn get_size(&self) -> u32 {
        let mut size = 0;
        for file in self.files {
            size+=file.get_size();
        }
        for dir in self.directories {
            size+=dir.borrow().get_size();
        }
        size
    }
    fn get_name(&self) -> &str {
        &self.name
    }
}

struct MyFile {
    name: String,
    size: u32,
}

impl MyFile {
    fn new(name: String, size: u32) -> Self {
        MyFile { name, size }
    }
}

impl Entry for MyFile {
    fn get_size(&self) -> u32 {
        self.size
    }
    fn get_name(&self) -> &str {
        &self.name
    }
}

fn main() {
    // create root
    let mut root = MyDir::new("/".to_string(), None);

    let mut current_dir = Rc::new(RefCell::new(root)); 

    let cd_cmd = Regex::new(r"^\$ cd.*").unwrap();
    let _ls_cmd = Regex::new(r"$ ls").unwrap();

    let _file_desc = Regex::new(r"^\d+").unwrap();
    let _dir_desc = Regex::new(r"^dir").unwrap();

    let patterns = [r"^\d+", r"^dir"];
    let _cmd_set_re = RegexSet::new(&patterns).unwrap();

    let filename = "test.txt";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(&file);

    for line in reader.lines() {
        let line = line.unwrap();
        // ===========================
        println!("{} - {}", line, cd_cmd.is_match(&line));
        if cd_cmd.is_match(&line) {
            let target_dir: &str = line.split_whitespace().collect::<Vec<&str>>()[2];
            if current_dir.borrow().get_name() != target_dir {
                if target_dir == ".." {
                    
                } else {
                    // move to target directory
                    let dir = current_dir.borrow().get_dir(target_dir.to_string());
                    match dir {
                        Some(dir) => current_dir = dir,
                        None => create_new_dir(&current_dir, target_dir.to_string())
                    }
                }
            }
        }
        
    }
}

fn create_new_dir(directory: &Rc<RefCell<MyDir>>, name: String) {

}