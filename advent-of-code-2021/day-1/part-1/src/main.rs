use std::fs;

fn main() {
    let result = fs::read_to_string("input.txt");

    let content = match result {
        Ok(content) => { content },
        Err(error) => { panic!("Can't deal with {}, just exit here", error); }
    };

    let mut count: u32 = 0;
    let mut previous_value: u32 = 0;

    for (index, depth) in content.lines().into_iter().enumerate() {

        let depth: u32 = depth.parse().expect("This is not a number!");

        if index == 0 {
            previous_value = depth;
            continue;
        }
        

        if depth > previous_value {
            count += 1;
        }

        previous_value = depth;

    } 

    println!("{count}")
}
