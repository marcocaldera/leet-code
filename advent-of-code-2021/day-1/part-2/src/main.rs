use std::fs;

fn main() {
    let result = fs::read_to_string("input.txt");

    let content = match result {
        Ok(content) => { content },
        Err(error) => { panic!("Can't deal with {}, just exit here", error); }
    };

    let mut sums: Vec<u32> = Vec::new();
    let mut temp: Vec<u32> = vec![0; 3];

    for (index, depth) in content.lines().into_iter().enumerate() {
        
       let depth: u32 = depth.parse().expect("This is not a number!");

        let position = index % 3;

        temp[position] = depth;

        if index >= 2 {
            sums.push(temp.iter().sum());
        }

    }

    // println!("{:?}", sums);

    let mut count: u32 = 0;
    let mut previous_value: u32 = 0;

    for (index, sum) in sums.iter().enumerate() {

        if index == 0 {
            previous_value = *sum;
            continue;
        }
        
        if *sum > previous_value {
            count += 1;
        }

        previous_value = *sum;
    }


    println!("{count}")
}
