fn main() {

const THREE_HOURS_IN_SECONDS: u32 = 60 *  60 * 3;
println!("3 hr in sec is {}", THREE_HOURS_IN_SECONDS);

let x = 5;
let x = x + 1;

// so here we're starting a new scope

{
    let x = x * 2;
    println!("fuck fuck FUCK ME AAAAHHHHH: {}", x)
}

println!("The value x is: {}", x);


let spaces = "  "; // here, spaces is at first a string
let spaces = spaces.len(); // now, spaces is an int

let mut spaces = "  ";
// spaces = spaces.len();

let guess: u32 = "42".parse().expect("no es numero!");

let x = 2.0; // f64
let y: f32 = 3.0; // f64

// addition
let sum = 5 + 10;

// subtraction
let difference = 95.5 - 4.3;

// multiplication
let product = 4 * 30;

// division
let quotient = 56.7 / 32.2;
let floored = 2 / 3; // Results in 0

// remainder
let remainder = 43 % 5;

let tup: (i32, f64, u8) = (500,6.4,1); // explicit type annotation
let tup = (500,6.4,1); // infers type

let (x, y, z) = tup; // in this way, the three values of tuple are extracted
println!("so now I can print y: {}",y);

// tuple values can be accessed by dot annotation
let x: (i32, f64, u8) = (500, 6.4, 1);

let five_hundred = x.0;

let six_point_four = x.1;

let one = x.2;

let a = [1, 2, 3, 4, 5]; // inferred type

let first_3_months = ["jan", "feb", "march"];

// writing the type of the array and the number of elements
let a: [i32;5] = [1,2,3,4,5];

// initializing an array - concise formatting
let a = [3;5]; // the same as let a = [3,3,3,3,3]

let a = [1,2,3,4,5];

let first = a[0];
let second = a[1];

use std::io;
let a = [1, 2, 3, 4, 5];

println!("Please enter an array index.");

let mut index = String::new();

io::stdin()
    .read_line(&mut index)
    .expect("Failed to read line");

let index: usize = index
    .trim()
    .parse()
    .expect("Index entered was not a number");

let element = a[index];

println!(
    "The value of the element at index {} is: {}",
    index, element
);

}
