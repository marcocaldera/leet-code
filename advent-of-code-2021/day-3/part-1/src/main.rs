use std::fs;

fn main() {
    let content = fs::read_to_string("input.txt").expect("Ops error");

    let mut matrix: [i32; 12] = [0; 12];

    for number in content.lines() {

        matrix = number
        .split("")
        .filter(|s| *s != "") // remove empty string
        .map(|s| s.parse::<i32>().expect("Oooops")) // convert to int
        .zip(matrix.iter()) // zip with matrix
        .map(|(b, v)| b + *v) // sum matrix with next value
        .collect::<Vec<i32>>()
        .try_into() // try to convert to matrix type [i32; 12]
        .expect("💣");

    }

    println!("{:?}", matrix);

    let count: i32 = content.lines().count().try_into().expect("💣");
    println!("{}", count);

    let mut binary_gamma = String::from("");

    for elem in matrix {

        if elem > count / 2 {
            binary_gamma.push('1');
        } else {
            binary_gamma.push('0');
        }

    }

    let decimal_gamma = usize::from_str_radix(&binary_gamma, 2).unwrap();
    let decimal_epsilon = (1 << 12) - 1 ^ decimal_gamma; // 3896

    println!("Step1: 2^12={:b} 2^12-1={:b}", 1 << 12, (1 << 12) - 1); 
    // 2^12=4096   =      1.000.000.000.000
    // 2^12-1=4095 = [0..0].111.111.111.111
    // gamma       =       .000.011.000.111
    // XOR         =       .111.100.111.000 

    println!("{}", binary_gamma);
    println!("{}", decimal_gamma);
    println!("{}", decimal_epsilon);

}
