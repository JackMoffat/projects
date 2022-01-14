use std::io;

fn main() {
    println!("guess the number!!!!!!!!!!!!!!!!!!!!!");
    println!("please input your guess");

    let mut guess = String::new(); // oh cool! so doing 

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("YOU GUEss ED: {}", guess);
}
