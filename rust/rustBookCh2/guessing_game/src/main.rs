use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("guess the number!!!!!!!!!!!!!!!!!!!!!");
    let secret_number = rand::thread_rng().gen_range(1..101);
    println!("el secreto numbero esta: {}", secret_number);

    loop {
        println!("please input your guess"); // displayed either way

        let mut guess = String::new(); // oh cool! so doing

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
        // if the... which part?...fails

        // is it important that the let guess line comes AFTER the value has been assigned?
        // what the fucK?
        // original, which would panic!!!!!!! and quit
        // let guess: u32 = guess.trim().parse().expect("please type a number!"); // expect clause here is in case you type somethin fucking stupid

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue, 
        };

        println!("YOU GUEss ED: {}", guess);

        // ok wow!! note the syntax change from a comma to a semicolon in the Equal exit clause -> because it's now in an attribute set
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("ya wee one"),
            Ordering::Greater => println!("ya huge bastard"),
            Ordering::Equal => {
                println!("right ye are!");
                break;
            }
        }}
}
