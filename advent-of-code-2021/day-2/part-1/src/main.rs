use std::fs;

fn main() {
    let result = fs::read_to_string("input.txt");

    let content = match result {
        Ok(content) => { content },
        Err(error) => { panic!("Can't deal with {}, just exit here", error); }
    };

    let mut direction = (0, 0);

    for instruction in content.lines() {

       let instruction: Vec<&str> = instruction.split(" ").collect();
       let amount = instruction[1].parse::<i32>().unwrap();
       
       match instruction[0] {
        "forward" => direction.0 += amount,
        "backward" => direction.0 -= amount,
        "up" => direction.1 -= amount,
        "down" => direction.1 += amount,
        _ => println!("Fuck"),

       } 

    }

    println!("{}*{}={}", direction.0, direction.1, direction.0 * direction.1);
    
}