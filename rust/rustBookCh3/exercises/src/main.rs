use std::io;

fn main() {
    // so, looping function that adds the numbers is what will end up returning it. so, main will act almost like a wrapper


    loop {
        let mut n = String::new();

        println!("Enter a number");
        io::stdin().read_line(&mut n).expect("expect....?");
        let n: u32 = match n.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        generate_fibonacci(n);
        break;
    }
}

fn generate_fibonacci(n: u32) {
    let mut f_minus_2: u32 = 0;
    let mut f_minus_1: u32 = 0;

    let mut fib: u32 = 0;
    for i in  0..n+1 {
        if i > 1 {
            f_minus_2 = f_minus_1;
            f_minus_1 = fib;
            fib = f_minus_1 + f_minus_2;
        } else {
            fib += i
        }
        println!("F{}: {}",i,fib);
    };
}
