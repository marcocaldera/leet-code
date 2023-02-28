use std::fs;
use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;

fn main() {
    let content = fs::read_to_string("input.txt").expect("Ops error");

    let (mut horizontal, mut depth, mut aim) = (0, 0, 0);

    for instruction in content.lines() {

       let instruction: Vec<&str> = instruction.split(" ").collect();
       let amount = instruction[1].parse::<i32>().unwrap();
       
       match instruction[0] {
        "forward" => {
            horizontal += amount;
            depth += amount * aim; 
        },
        "up" => {
            aim -= amount;
        },
        "down" => {
            aim += amount;
        }
        _ => println!("Fuck"),
       } 

    }
    
    println!("{}*{}={}", horizontal, depth, horizontal * depth); 

    let result = (horizontal * depth).to_string();
    let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
    ctx.set_contents(result).unwrap();

    
}